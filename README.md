# FICO Credit Scoring ML Model

This project demonstrates a machine learning workflow for predicting FICO credit scores using synthetic data and various features relevant to creditworthiness. The notebook walks through data exploration, feature engineering, model training, and evaluation. The notebook and dataset are tailored for the Mongolian situation, reflecting local demographics, financial behaviors, and credit factors. Both the notebook and dataset are in Mongolian language.

## Live Demo
-> https://credit-scoring-fico.streamlit.app

## Dataset
- **Source:** `fico_mn2.csv` (synthetic data)
- **Rows:** 1000
- **Columns:** 17
- **Features:**
  - Demographics: Age, Experience, Marital Status, Housing, Car Ownership, Profession, City
  - Financial: Income, Years at Work, Years at Residence
  - Credit Factors: New Credit Inquiry (%), Credit History (%), Credit Portfolio (%), Credit Balance (%), Repayment (%)
  - Target: FICO Score (300–850)

## Workflow
1. **Data Loading & Exploration:**
   - Loads the dataset and explores distributions, missing values, and feature statistics.
   - Visualizes FICO score distribution and relationships with key features.
2. **Feature Engineering:**
   - Creates new features (e.g., experience ratio).
   - Encodes categorical variables.
   - Scales numerical features.
3. **Modeling:**
   - Trains multiple regression models: Linear, Ridge, Lasso, Random Forest, Gradient Boosting, SVR.
   - Performs cross-validation and hyperparameter tuning.
   - Selects the best model based on CV R2 score.
4. **Evaluation:**
   - Reports accuracy, mean absolute error, and feature importance.
   - Compares actual vs. predicted FICO scores for test samples.

## Results
- **Best Model:** Ridge Regression (with hyperparameter tuning)
- **Accuracy:** Reported as R2 score and mean absolute error
- **Feature Importance:** Repayment, Credit History, Experience, Age, Portfolio, New Credit Inquiry, Profession

## Requirements
- Python 3.8+
- pandas, numpy, matplotlib, seaborn, scikit-learn

## Usage
1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
2. Open `fico_scoring.ipynb` in Jupyter or VS Code.
3. Run all cells to reproduce the analysis and results.

# FICO Credit Scoring Streamlit App

In addition to the ML notebook, this project includes a Streamlit application for interactively calculating FICO scores. The app simulates a real-world credit scoring process and provides personalized recommendations.

## Live Demo
https://credit-scoring-fico.streamlit.app

## Features
- Calculate FICO score (350–800 range) based on 5 major factors:
  - Payment History (35%)
  - Amounts Owed (30%)
  - Credit History Length (15%)
  - New Credit Inquiries (10%)
  - Credit Mix (10%)
- Detailed breakdown of each factor’s contribution.
- Classification into categories:
  - Маш муу, Боломжийн, Сайн, Маш сайн, Онцгой сайн
- Personalized recommendations for score improvement.

## Run Locally
1. Install dependencies:
   pip install streamlit pandas

2. Run the app:
   streamlit run app.py

3. Open browser at:
   http://localhost:8501

Author: Bayarmaa T.
