# Churn Prediction Overview

## Project Objective
The goal of this project is to predict user churn for an e-commerce platform based on user activities (e.g., views, carts, purchases). By identifying churn signals, the business can proactively engage at-risk users to improve retention.

## Steps Performed

### 1. Data Loading
- Loaded the dataset (`events.csv`) containing user events such as views, carts, and purchases.
- Parsed the event timestamps to ensure proper datetime formatting.

### 2. Feature Engineering
Aggregated user-level features to capture their behavior, including:
- **Total Views**: Number of `view` events.
- **Total Carts**: Number of `cart` events.
- **Total Purchases**: Number of `purchase` events.
- **Average Price**: Average price of products interacted with.
- **Total Spent**: Sum of prices for purchased products.
- **Sessions**: Unique number of user sessions.
- **Recency**: Days since the last user activity.
- **Conversion Rates**:
  - View-to-Cart Ratio: `total_carts / total_views`.
  - Cart-to-Purchase Ratio: `total_purchases / total_carts`.

### 3. Handling Missing and Infinite Values
- Filled missing values with `0`.
- Replaced infinite values with `0` to handle division errors.

### 4. Churn Definition
Defined churn as users who have not made a purchase in the last 30 days.
- Added a `churn` label: 1 for churned users and 0 otherwise.

### 5. Modeling
- Used a Random Forest Classifier to predict churn.
- Split the dataset into training and testing sets (80%-20%).

### 6. Evaluation
- Assessed model performance using:
  - **Classification Report**: Precision, Recall, F1-Score.
  - **ROC AUC Score**: A robust metric for evaluating binary classifiers.

## Results
- The classification metrics and ROC AUC score are printed for evaluation.
- Key features influencing churn are identified, offering insights for actionable strategies.

## Recommendations
- Use the insights to design personalized interventions, such as targeted promotions or reminders.
- Regularly update and monitor the churn model for continued effectiveness.

## How to Run
1. Ensure the dataset (`events.csv`) is in the same directory as the script.
2. Run the script `churn_prediction_analysis.py` to generate features and train the model.
3. Processed user features will be saved as `user_features.csv`.

## Files
- **`events.csv`**: Raw event dataset.
- **`churn_prediction_analysis.py`**: Python script for feature engineering and modeling.
- **`user_features.csv`**: Processed user-level features with churn labels.

