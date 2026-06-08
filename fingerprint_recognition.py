import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import time

def load_fingerprint_data():
    """
    Cette fonction simule le chargement et l'extraction de caractéristiques d'empreintes.
    Dans un vrai projet, cette fonction utiliserait OpenCV (cv2) pour lire des images,
    appliquer des filtres de Gabor, ou extraire des minuties.
    
    Ici, nous générons un jeu de données synthétique où :
    - n_samples = nombre total d'images d'empreintes
    - n_features = nombre de caractéristiques extraites par image (ex: descripteurs de texture)
    - n_classes = nombre de personnes différentes à identifier
    """
    print("Chargement et extraction des caractéristiques (Simulation)...")
    X, y = make_classification(
        n_samples=1000, 
        n_features=50,      # 50 caractéristiques extraites par empreinte
        n_informative=40,   # Caractéristiques utiles pour la classification
        n_redundant=10,
        n_classes=5,        # 5 individus différents
        random_state=42
    )
    return X, y

def plot_confusion_matrices(y_test, predictions_dict):
    """
    Affiche les matrices de confusion pour comparer visuellement les performances.
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('Matrices de Confusion des Algorithmes', fontsize=16)

    for ax, (name, y_pred) in zip(axes, predictions_dict.items()):
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax, cbar=False)
        ax.set_title(name)
        ax.set_xlabel('Prédictions')
        ax.set_ylabel('Valeurs Réelles')
    
    plt.tight_layout()
    plt.savefig('matrices_confusion.png')
    print("Graphique sauvegardé sous 'matrices_confusion.png'")
    # plt.show() # Commenté pour éviter de bloquer l'exécution en ligne de commande

def main():
    # 1. Chargement des données
    X, y = load_fingerprint_data()
    
    # 2. Séparation en données d'entraînement (80%) et de test (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Normalisation (Très important pour le SVM et le MLP)
    # Met les données à la même échelle (moyenne = 0, écart-type = 1)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 4. Définition des Modèles
    models = {
        "SVM (RBF Kernel)": SVC(kernel='rbf', C=1.0, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Réseau de Neurones (MLP)": MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
    }
    
    # Dictionnaire pour stocker les prédictions
    predictions = {}
    
    print("\n" + "="*50)
    print("ENTRAÎNEMENT ET ÉVALUATION DES MODÈLES")
    print("="*50)
    
    # 5. Entraînement et Évaluation
    for name, model in models.items():
        print(f"\nEntraînement de {name}...")
        start_time = time.time()
        
        # Le Random Forest n'a pas strictement besoin de données normalisées, 
        # mais c'est requis pour SVM et MLP. On utilise les données normalisées pour tous par souci d'équité.
        model.fit(X_train_scaled, y_train)
        
        train_time = time.time() - start_time
        
        # Prédiction sur l'ensemble de test
        y_pred = model.predict(X_test_scaled)
        predictions[name] = y_pred
        
        # Calcul des performances
        acc = accuracy_score(y_test, y_pred)
        print(f"[{name}] Précision (Accuracy) : {acc*100:.2f}%")
        print(f"[{name}] Temps d'entraînement : {train_time:.4f} secondes")
        print(f"[{name}] Rapport de classification :")
        print(classification_report(y_test, y_pred))
        print("-" * 50)
        
    # 6. Visualisation
    plot_confusion_matrices(y_test, predictions)

if __name__ == "__main__":
    main()
