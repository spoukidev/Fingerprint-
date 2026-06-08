# Rapport de Projet : Reconnaissance d'Empreintes Digitales par Algorithmes d'Apprentissage Automatique

## 1. Introduction

La biométrie est la science de l'analyse des caractéristiques physiques ou comportementales spécifiques à chaque individu dans le but d'authentifier son identité. Parmi les modalités biométriques, la **reconnaissance d'empreintes digitales** est l'une des plus déployées et fiables. Les empreintes sont caractérisées par des motifs globaux (arches, boucles, tourbillons) et des caractéristiques locales appelées **minuties** (terminaisons de crêtes, bifurcations).

Ce rapport détaille la recherche théorique sur trois algorithmes d'apprentissage automatique appliqués à cette problématique : **SVM (Support Vector Machine)**, **Random Forest**, et **MLP (Multi-Layer Perceptron)**. Il documente également l'implémentation pratique "BioMatch Pro", une plateforme de démonstration web interactive permettant de comparer ces modèles.

---

## 2. Recherche et Fondements Théoriques

Avant la classification, une image d'empreinte digitale brute doit être prétraitée. Des algorithmes (comme les filtres de Gabor) sont appliqués pour améliorer l'image, puis des vecteurs de caractéristiques numériques (représentant les minuties ou la texture) sont extraits. Ce sont ces vecteurs numériques qui sont fournis aux algorithmes d'apprentissage.

### 2.1. Support Vector Machine (SVM)
Le SVM est un algorithme d'apprentissage supervisé qui cherche à trouver un hyperplan optimal séparant les données en différentes classes avec la marge la plus large possible (distance entre la frontière de décision et les points de données les plus proches, appelés *vecteurs de support*).

*   **Application aux empreintes :** Les données biométriques étant complexes, elles sont rarement séparables par une simple ligne (linéairement séparables). Le SVM utilise donc l'**astuce du noyau (Kernel Trick)**, particulièrement le noyau RBF (Radial Basis Function), pour projeter les données dans un espace de dimension supérieure où une séparation linéaire devient possible.
*   **Avantages :** Très performant dans les espaces de grande dimension ; efficace même avec un nombre de données d'entraînement modéré.
*   **Inconvénients :** Le temps d'entraînement augmente drastiquement (quadratiquement) avec le nombre d'échantillons. Le choix des hyperparamètres (C, Gamma) nécessite une optimisation méticuleuse.

### 2.2. Random Forest (Forêts Aléatoires)
Le Random Forest est une méthode d'apprentissage d'ensemble (Ensemble Learning). Il combine les prédictions de multiples **arbres de décision** indépendants pour produire un résultat plus robuste.

*   **Application aux empreintes :** Chaque arbre est entraîné sur un sous-échantillon aléatoire des empreintes et n'utilise qu'un sous-ensemble aléatoire des caractéristiques extraites (ex: seulement la position de certaines minuties). Pour identifier une nouvelle empreinte, chaque arbre vote pour une identité, et la classe majoritaire l'emporte.
*   **Avantages :** Excellente robustesse au bruit et aux données manquantes ou abîmées (fréquent avec des empreintes sales). Moins sujet au surapprentissage que les arbres de décision individuels.
*   **Inconvénients :** Modèle très lourd en mémoire spatiale si le nombre d'arbres est élevé.

### 2.3. Réseaux de Neurones (Multi-Layer Perceptron - MLP)
Le MLP est l'architecture classique des réseaux de neurones artificiels "Feed-Forward". Il se compose d'une couche d'entrée, de plusieurs couches cachées composées de neurones avec des fonctions d'activation non linéaires, et d'une couche de sortie.

*   **Application aux empreintes :** Le réseau reçoit le vecteur de l'empreinte en entrée. Par rétropropagation de l'erreur (Backpropagation), il ajuste les poids de ses milliards de connexions lors de l'entraînement pour modéliser les relations mathématiques extrêmement complexes liant le vecteur de caractéristiques à l'identité de l'individu.
*   **Avantages :** Capacité inégalée à approximer des fonctions non linéaires hautement complexes. Performances exceptionnelles si la base de données est immense.
*   **Inconvénients :** Phénomène de "Boîte noire" (difficile de comprendre *pourquoi* le modèle a pris une décision). Nécessite une grande puissance de calcul et un temps de convergence élevé.

---

## 3. Implémentation Pratique : Simulateur "BioMatch Pro"

Pour illustrer et comparer ces théories, nous avons développé **BioMatch Pro**, une application web interactive complète reposant sur une architecture moderne.

### 3.1. Architecture du Système
L'application est structurée en deux tiers :
1.  **Backend (Python & Flask) :** Exécute le moteur de Machine Learning via la librairie `scikit-learn`. Il expose une API REST (`/api/run-simulation`) capable de recevoir des paramètres dynamiques et de retourner des métriques et des graphiques générés à la volée.
2.  **Frontend (Vanilla Web) :** Une interface utilisateur "Premium" utilisant HTML5, du CSS moderne (Glassmorphism, animations) et du JavaScript asynchrone (`fetch`). L'UI n'utilise aucun framework lourd, garantissant une exécution instantanée.

### 3.2. Simulation des Données et Prétraitement
Pour que la démo soit exécutable sans base de données lourde (comme FVC2002), le backend simule l'étape d'extraction des caractéristiques en utilisant `make_classification`.
*   **Normalisation :** Avant d'être passées aux modèles, les données sont normalisées avec `StandardScaler` (mise à l'échelle pour avoir une moyenne de 0 et un écart-type de 1). *Cette étape de notre implémentation est critique pour que le SVM et le MLP convergent correctement et rapidement.*

### 3.3. Interactivité et Paramétrage en Temps Réel
L'interface web permet à l'utilisateur de modifier en temps réel les contraintes du problème :
*   **Volume de données (100 à 5000) :** Démontre l'évolution quadratique du temps d'entraînement du SVM par rapport au Random Forest.
*   **Classes (2 à 20 individus) :** Illustre la chute de précision lorsque le problème de multi-classification se complexifie.
*   **Niveau de Bruit :** Permet de prouver expérimentalement la robustesse théorique du Random Forest face aux données imparfaites par rapport au MLP.
*   **Noyau SVM :** En permettant de passer du noyau RBF au noyau Linéaire, l'utilisateur constate visuellement que les données d'empreintes nécessitent une projection dans un espace non linéaire pour être classifiées correctement.

---

## 4. Résultats Typiques et Observations

Lors de l'utilisation du simulateur avec des paramètres standards (1000 empreintes, 5 classes, Bruit faible), voici les observations typiques :

| Modèle | Précision Moyenne | Temps d'exécution | Comportement observé dans la démo |
| :--- | :--- | :--- | :--- |
| **SVM (RBF)** | ~70% - 85% | Très Rapide (< 0.1s) | Excellent compromis pour des données limitées. S'effondre totalement (précision < 60%) si on passe en noyau Linéaire. |
| **MLP** | ~65% - 80% | Lent (~0.6s) | Modèle le plus gourmand en ressources informatiques, mais maintient de bonnes performances générales. |
| **Random Forest** | ~55% - 65% | Moyen (~0.4s) | Précision de base parfois plus faible sur ces données simulées spécifiques, mais la précision reste stable même si l'on augmente drastiquement le paramètre de "Bruit". |

*(Note : Le simulateur génère graphiquement des Matrices de Confusion pour analyser où les modèles se trompent spécifiquement entre deux individus.)*

## 5. Conclusion

La reconnaissance d'empreintes digitales repose autant sur la qualité de l'extraction des caractéristiques (traitement d'image) que sur la puissance de l'algorithme de classification en aval. 
Comme l'illustre notre simulateur BioMatch Pro, **il n'existe pas d'algorithme parfait** : le SVM est idéal pour des systèmes avec des ressources limitées, le Random Forest excelle face aux capteurs de mauvaise qualité (bruit), tandis que les réseaux de neurones sont incontournables pour les systèmes d'identification biométrique de très grande envergure (bases de données nationales) disposant de moyens de calculs considérables.
