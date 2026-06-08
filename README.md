# BioMatch Pro: Biometric Fingerprint Recognition Platform

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

An interactive, premium-quality web application and command-line tool designed to demonstrate, evaluate, and compare machine learning algorithms for **biometric fingerprint recognition**. 

This platform evaluates three primary classifiers:
*   **Support Vector Machine (SVM)** with RBF and Linear Kernels.
*   **Random Forest Classifier** with adjustable estimators.
*   **Multi-Layer Perceptron (MLP)** Artificial Neural Network.

---

## 🚀 Key Features

*   **Interactive Simulation Dashboard:** Adjust sample volume, individual classes (identities), noise level, and hyperparameters in real-time.
*   **Real-time Machine Learning Inference:** Runs training and validation cycles on the backend using Python & Scikit-Learn.
*   **Beautiful Glassmorphism Interface:** A dark-themed, responsive web GUI with interactive form controls and dynamic charts.
*   **Comprehensive Performance Metrics:** Evaluates and compares **Accuracy**, **Precision**, **Recall**, and **F1-Score**.
*   **Visual Analysis:** Generates dynamic **confusion matrices** to analyze classifications and error patterns.
*   **Dual Mode:** Includes both a lightweight command-line simulator (`fingerprint_recognition.py`) and a Flask-based web server (`app.py`).

---

## 🛠️ Technology Stack

*   **Backend:** Python 3, Flask, NumPy, Scikit-Learn
*   **Visualizations:** Matplotlib, Seaborn
*   **Frontend:** HTML5, Vanilla JavaScript (ES6 Fetch API), Vanilla CSS (Custom Glassmorphism Design System)

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/biomt.git
cd biomt
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 How to Run

### Option A: Launch the Web Dashboard (Recommended)
Launch the Flask development server and open the web dashboard:
```bash
python app.py
```
Open your browser and navigate to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### Option B: Run the Command Line Tool
Execute the raw Python training script directly in your terminal:
```bash
python fingerprint_recognition.py
```
This runs the simulation with standard settings, prints a detailed classification report for each model, and saves the confusion matrices to `matrices_confusion.png`.

---

## 📊 Algorithmic Comparison & Theory

### 1. Support Vector Machine (SVM)
*   **Concept:** Finds the optimal separating hyperplane with the maximum margin between classes. Projects non-linear data into higher-dimensional spaces using the **Kernel Trick** (specifically Radial Basis Function - RBF).
*   **Biometric Fit:** Exceptional for small-to-medium datasets. However, training time scales quadratically, making it less suitable for national-scale databases.

### 2. Random Forest
*   **Concept:** An ensemble method that constructs multiple decision trees during training. Predictions are made via majority voting across trees.
*   **Biometric Fit:** Robust against sensor noise, dust, and partial prints. Resilient to overfitting, but can be memory-heavy when trees are large.

### 3. Multi-Layer Perceptron (MLP)
*   **Concept:** A Feed-Forward artificial neural network consisting of input, hidden, and output layers, optimized via backpropagation.
*   **Biometric Fit:** Models highly complex, non-linear biometric features. Excels with large volumes of training data but requires substantial compute power.

---

## 📈 Performance Summary (Typical Results)

Below is a typical comparison with $1000$ simulated fingerprint records, $5$ distinct classes, and low sensor noise:

| Algorithm | Avg. Accuracy | Training Speed | Observed Behavior in Simulator |
| :--- | :--- | :--- | :--- |
| **SVM (RBF)** | **~70% - 85%** | **Instant (< 0.1s)** | Highest performance with small datasets. Dropping the RBF kernel for a Linear kernel collapses accuracy to < 60%. |
| **MLP (Neural Network)** | **~65% - 80%** | **Slow (~0.6s)** | Computationally heavy, but retains good general classification bounds. |
| **Random Forest** | **~55% - 65%** | **Moderate (~0.4s)** | Slightly lower accuracy on synthetic lines, but highly resilient and stable even under extreme noise settings. |

---

## 📁 Project Structure

```text
biomt/
│
├── app.py                     # Flask backend with API endpoints
├── fingerprint_recognition.py # Standalone CLI simulation script
├── requirements.txt           # Python dependencies
├── Rapport_Projet_Empreintes.md # Academic report detailing mathematical foundations (in French)
│
├── templates/
│   └── index.html             # Premium glassmorphism user interface
│
└── static/
    ├── styles.css             # Custom styling rules and layout
    └── script.js              # Asynchronous dashboard request & update logic
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
