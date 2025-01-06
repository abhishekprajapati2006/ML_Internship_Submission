import pandas as pd
import numpy as np

# Load the cleaned dataset
file_path = "events.csv"
events_data = pd.read_csv(file_path, parse_dates=['event_time'])

# Feature Engineering
# Step 1:Aggregating user-level features
user_features = events_data.groupby('user_id').agg(
    total_views=('event_type', lambda x: (x == 'view').sum()),
    total_carts=('event_type', lambda x: (x == 'cart').sum()),
    total_purchases=('event_type', lambda x: (x == 'purchase').sum()),
    avg_price=('price', 'mean'),
    total_spent=('price', lambda x: x[elements.event_type == 'purchase'].sum()),
    sessions=('user_session', 'nunique'),
    last_event_time=('event_time', 'max')
).reset_index()

# Step 2: Calculating derived metrics
user_features['view_to_cart_ratio'] = user_features['total_carts'] / user_features['total_views']
user_features['cart_to_purchase_ratio'] = user_features['total_purchases'] / user_features['total_carts']
user_features['recency'] = (events_data['event_time'].max() - user_features['last_event_time']).dt.days

# Step 3: Handling infinities and NaNs in derived metrics
user_features = user_features.fillna(0)  # Replace NaNs with 0
user_features = user_features.replace([np.inf, -np.inf], 0)  # Replace infinities with 0

# Save the processed features for modeling
user_features.to_csv("user_features.csv", index=False)

# Next steps: Modeling
# Import machine learning libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

# Example target definition: Users with no purchases in the last 30 days are churners
user_features['churn'] = (user_features['recency'] > 30).astype(int)

# Splitting data into features and target
X = user_features.drop(columns=['user_id', 'last_event_time', 'churn'])
y = user_features['churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("Classification Report:\n", classification_report(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_prob))
