document.addEventListener('DOMContentLoaded', () => {
    const runBtn = document.getElementById('runBtn');
    const spinner = document.getElementById('spinner');
    const btnText = document.querySelector('.btn-text');
    const dashboard = document.getElementById('dashboard');

    // UI Updates for Sliders
    const inputs = {
        n_samples: document.getElementById('n_samples'),
        n_classes: document.getElementById('n_classes'),
        noise_level: document.getElementById('noise_level'),
        rf_trees: document.getElementById('rf_trees'),
        svm_kernel: document.getElementById('svm_kernel')
    };

    const noiseLabels = { 1: "Faible", 2: "Moyen", 3: "Élevé" };

    inputs.n_samples.addEventListener('input', (e) => document.getElementById('n_samples_val').textContent = e.target.value);
    inputs.n_classes.addEventListener('input', (e) => document.getElementById('n_classes_val').textContent = e.target.value);
    inputs.rf_trees.addEventListener('input', (e) => document.getElementById('rf_trees_val').textContent = e.target.value);
    inputs.noise_level.addEventListener('input', (e) => {
        document.getElementById('noise_level_val').textContent = noiseLabels[e.target.value];
    });

    runBtn.addEventListener('click', async () => {
        // UI Loading State
        runBtn.disabled = true;
        spinner.classList.remove('hidden');
        btnText.textContent = 'Calculs en cours...';
        
        dashboard.classList.remove('visible');
        setTimeout(() => dashboard.classList.add('hidden'), 300);

        // Gather Data
        const payload = {
            n_samples: parseInt(inputs.n_samples.value),
            n_classes: parseInt(inputs.n_classes.value),
            noise_level: parseInt(inputs.noise_level.value),
            rf_trees: parseInt(inputs.rf_trees.value),
            svm_kernel: inputs.svm_kernel.value
        };

        try {
            const response = await fetch('/api/run-simulation', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });
            
            if (!response.ok) throw new Error('Erreur réseau');
            const data = await response.json();

            updateCard('SVM', data.SVM);
            updateCard('RandomForest', data.RandomForest);
            updateCard('MLP', data.MLP);

            setTimeout(() => {
                dashboard.classList.remove('hidden');
                setTimeout(() => dashboard.classList.add('visible'), 50);
            }, 300);

        } catch (error) {
            console.error('Erreur:', error);
            alert('Une erreur est survenue lors de la simulation.');
        } finally {
            runBtn.disabled = false;
            spinner.classList.add('hidden');
            btnText.textContent = 'Relancer Simulation';
        }
    });

    function updateCard(modelId, data) {
        document.getElementById(`acc-${modelId}`).textContent = `${data.accuracy}%`;
        document.getElementById(`prec-${modelId}`).textContent = `${data.precision}%`;
        document.getElementById(`rec-${modelId}`).textContent = `${data.recall}%`;
        document.getElementById(`f1-${modelId}`).textContent = `${data.f1}%`;
        document.getElementById(`time-${modelId}`).textContent = `${data.time} s`;
        document.getElementById(`cm-${modelId}`).src = `data:image/png;base64,${data.cm_image}`;
    }
});
