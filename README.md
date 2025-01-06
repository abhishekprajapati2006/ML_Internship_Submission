# README

## Overview
This project predicts user churn for an e-commerce platform by analyzing user activity data. The goal is to identify users who are likely to churn and provide actionable insights to improve retention strategies.

## Files Included
1. **`events.csv`**: Raw dataset containing user event logs. Its a Large File ☹️☹️
2. **`churn_prediction_analysis.py`**: Python script for data preprocessing, feature engineering, and modeling.
3. **`user_features.csv`**: Processed dataset with user-level features and churn labels.
4. **`churn_prediction_overview.md`**: Summary of the approach, results, and recommendations.

## How to Run

### Prerequisites
Ensure the following packages are installed:
- Python 3.7+
- Pandas
- NumPy
- Scikit-learn

Install the required libraries using pip:
```bash
pip install pandas numpy scikit-learn
```

### Steps
1. Place the `events.csv` file in the same directory as the script.
2. Run the script `churn_prediction_analysis.py`:
   ```bash
   python churn_prediction_analysis.py
   ```
3. The processed features will be saved as `user_features.csv`.
4. The script will output the classification report and ROC AUC score for the churn prediction model.

## Project Workflow
1. **Data Cleaning**: Handled missing values and ensured correct formatting.
2. **Feature Engineering**: Created metrics like recency, frequency, and monetary value.
3. **Churn Definition**: Labeled users who had no purchases in the last 30 days as churners.
4. **Modeling**: Trained a Random Forest Classifier and evaluated its performance.

## Key Insights
- Identified behavioral patterns contributing to churn.
- Proposed business strategies to improve user retention.

## Contact
For any questions, please contact [prajapatiabhishek13988@gmail.com].
Phone No. : [7897732006].![alt text](image.png)

