import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.utils import resample
import matplotlib.pyplot as plt

# Assuming datasets are available at the specified path
file_path = 'datasets/'

# Load lifestyle and clinical datasets
lifestyle_dataset = pd.read_csv(file_path + 'lifestyle_dataset.csv')
clinical_dataset = pd.read_csv(file_path + 'clinical_dataset.csv')

# Step 2: Split the 'Blood Pressure' column into 'Systolic_BP' and 'Diastolic_BP'
blood_pressure_split = lifestyle_dataset['Blood Pressure'].str.split('/', expand=True)
lifestyle_dataset['Systolic_BP'] = pd.to_numeric(blood_pressure_split[0], errors='coerce')
lifestyle_dataset['Diastolic_BP'] = pd.to_numeric(blood_pressure_split[1], errors='coerce')

# Drop the original 'Blood Pressure' column
lifestyle_dataset = lifestyle_dataset.drop(columns=['Blood Pressure'])

# Step 3: Separate numeric and categorical columns
numeric_columns_lifestyle = ['Age', 'Cholesterol', 'Systolic_BP', 'Diastolic_BP', 'Heart Rate', 'Exercise Hours Per Week', 
                   'Stress Level', 'Sedentary Hours Per Day', 'Income', 'BMI', 'Triglycerides', 
                   'Physical Activity Days Per Week', 'Sleep Hours Per Day']
categorical_columns_lifestyle = ['Sex', 'Diabetes', 'Smoking', 'Obesity', 'Alcohol Consumption', 'Diet', 
                       'Country', 'Continent', 'Hemisphere']

# Step 4: Handle missing values for numeric and categorical data
imputer_numeric = SimpleImputer(strategy='mean')
lifestyle_dataset[numeric_columns_lifestyle] = imputer_numeric.fit_transform(lifestyle_dataset[numeric_columns_lifestyle])

imputer_categorical = SimpleImputer(strategy='most_frequent')
lifestyle_dataset[categorical_columns_lifestyle] = imputer_categorical.fit_transform(lifestyle_dataset[categorical_columns_lifestyle])

# Step 5: Convert categorical features using get_dummies
lifestyle_dataset_encoded = pd.get_dummies(lifestyle_dataset, columns=categorical_columns_lifestyle, drop_first=True)

# Step 6: Feature scaling for numeric columns
scaler = StandardScaler()
lifestyle_dataset_encoded[numeric_columns_lifestyle] = scaler.fit_transform(lifestyle_dataset_encoded[numeric_columns_lifestyle])

# Step 7: Clean the clinical dataset
clinical_dataset_cleaned = clinical_dataset.dropna()

# Step 8: Combine the two datasets
combined_dataset = pd.concat([clinical_dataset_cleaned.reset_index(drop=True), lifestyle_dataset_encoded.reset_index(drop=True)], axis=1)

# Step 9: Define X (features) and y (target)
X_combined = combined_dataset.drop(columns=['Heart Attack Risk', 'output'], errors='ignore')  # Drop target columns
y_combined = combined_dataset['Heart Attack Risk'].fillna(combined_dataset['output'])  # Fill target using either column

# Step 10: Balance the data by upsampling the minority class
X_upsampled, y_upsampled = resample(X_combined[y_combined == 1], y_combined[y_combined == 1], replace=True, n_samples=len(y_combined[y_combined == 0]), random_state=42)
X_balanced = pd.concat([X_combined[y_combined == 0], X_upsampled])
y_balanced = pd.concat([y_combined[y_combined == 0], y_upsampled])

# Step 11: Split the data into training and testing sets
X_train_combined, X_test_combined, y_train_combined, y_test_combined = train_test_split(X_balanced, y_balanced, test_size=0.2, random_state=42)

# Step 12: Hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

rf_model_combined = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(estimator=rf_model_combined, param_grid=param_grid, cv=3, scoring='roc_auc', n_jobs=-1)
grid_search.fit(X_train_combined, y_train_combined)

# Best model from grid search
best_rf_model = grid_search.best_estimator_

# Step 13: Make predictions and evaluate the model
y_pred_proba = best_rf_model.predict_proba(X_test_combined)[:, 1]
roc_auc = roc_auc_score(y_test_combined, y_pred_proba)

# Step 14: Plot the ROC curve
fpr, tpr, thresholds = roc_curve(y_test_combined, y_pred_proba)

plt.figure()
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='grey', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.show()

# Return the best parameters and ROC AUC score
grid_search.best_params_, roc_auc
