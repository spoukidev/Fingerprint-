# BioMatch Pro — Biometric Fingerprint ML Experiment

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

An interactive web application and command-line experiment for demonstrating and comparing machine-learning classifiers in a **simulated biometric fingerprint classification setting**.

> **Scope note:** This repository is an educational ML experiment using simulated fingerprint-style records. Its reported results should not be interpreted as a benchmark on a production biometric dataset or as evidence of deployment-grade biometric accuracy.

## Models

The project compares three classifiers:

- **Support Vector Machine (SVM)** with RBF and linear kernels.
- **Random Forest Classifier** with adjustable estimators.
- **Multi-Layer Perceptron (MLP)** neural network.

## Key Features

- Interactive simulation dashboard for sample volume, classes, noise, and model parameters.
- Training and validation using Python and Scikit-learn.
- Accuracy, precision, recall, and F1-score reporting.
- Confusion-matrix visualization.
- Command-line and Flask web interfaces.

## Technology Stack

- **Backend:** Python, Flask, NumPy, Scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Frontend:** HTML, JavaScript, CSS

## Installation

```bash
git clone https://github.com/spoukidev/Fingerprint-.git
cd Fingerprint-
python -m venv venv
```

Activate the environment:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

### Web dashboard

```bash
python app.py
```

Then open `http://127.0.0.1:5000`.

### Command-line experiment

```bash
python fingerprint_recognition.py
```

The script runs the configured simulation, prints classification metrics, and generates confusion-matrix output.

## Experimental Interpretation

The project is useful for studying how classifier behavior changes with:

- sample size,
- number of identity classes,
- simulated sensor noise,
- model choice,
- and hyperparameter settings.

Because the data are simulated, the most meaningful conclusions are **comparisons inside the simulator**, not claims about real-world biometric performance.

## Models in Context

### Support Vector Machine

SVMs provide a useful baseline for non-linear classification with RBF kernels and can perform well on smaller feature spaces.

### Random Forest

Random forests offer an interpretable ensemble baseline and can be useful for studying feature importance and robustness to noisy inputs.

### Multi-Layer Perceptron

The MLP provides a neural-network baseline capable of modeling non-linear relationships, with additional sensitivity to architecture and optimization choices.

## Research Extensions

- Evaluate on a documented public fingerprint dataset.
- Add repeated cross-validation and confidence intervals.
- Separate validation from final held-out test evaluation.
- Analyze class imbalance and per-class errors.
- Study robustness to controlled corruption/noise.
- Compare handcrafted features with learned representations.
- Document privacy and security considerations for biometric systems.

## Project Structure

```text
.
├── app.py
├── fingerprint_recognition.py
├── requirements.txt
├── Rapport_Projet_Empreintes.md
├── templates/
└── static/
```

## License

MIT. See [LICENSE](LICENSE).
