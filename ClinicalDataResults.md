Clinical Model Training Results Summary
The clinical dataset used in this analysis contained 303 rows and 14 columns. All columns were numerical, and no preprocessing was required as the dataset had no null or invalid values.

Model Performance Analysis
Each model's performance was evaluated based on ROC-AUC scores and Test Accuracy. Models were tested with various scalers (e.g., StandardScaler, RobustScaler) to observe the impact of scaling on performance. Notably, scaling generally reduced performance, indicating that the dataset's feature distribution did not significantly benefit from normalization or standardization.

ROC Curve Rankings
The ROC-AUC score evaluates each model's ability to distinguish between classes, with higher values indicating better performance.

Model	ROC-AUC Score (No Scaling)	ROC-AUC Score (StandardScaler)	Notes
KNN	0.91	0.89	Slight drop with StandardScaler
WNN	0.91	0.89	Slight drop with StandardScaler
Logistic Regression	0.90	0.90	Slight drop with RobustScaler
Random Forest	0.90	Not Applicable	Drops with any scaler
MLP	0.89	Not Applicable	No scaling used
SVC	Not Applicable	0.88	Only evaluated with StandardScaler
Key Observations:

KNN and WNN achieved the highest ROC-AUC scores of 0.91 without scaling, slightly decreasing to 0.89 with scaling.
Logistic Regression and Random Forest also performed well but showed sensitivity to scaling.
SVC and MLP had slightly lower ROC-AUC scores, with SVC evaluated only with StandardScaler.
Test Accuracy Rankings
The Test Accuracy measures the proportion of correctly predicted instances in the test set. Scaling had a mixed impact, with some models showing a drop in accuracy.

Model	Test Accuracy (No Scaling)	Test Accuracy (StandardScaler)	Notes
KNN	0.89	0.84	Drops with StandardScaler
WNN	0.89	0.84	Drops with StandardScaler
Logistic Regression	0.89	0.89	Drops with RobustScaler
SVC	Not Applicable	0.87	Only evaluated with StandardScaler
Random Forest	0.85	Not Applicable	Drops with any scaler
MLP	0.85	Not Applicable	No scaling used
Key Observations:

KNN, WNN, and Logistic Regression achieved the highest Test Accuracy (0.89) when scaling was limited or excluded.
SVC and Random Forest had slightly lower test accuracy, with Random Forest particularly sensitive to any form of scaling.
MLP had comparable performance (0.85 Test Accuracy) without scaling.
Overall Model Performance
The overall performance of each model suggests that KNN and WNN are the most effective algorithms for this dataset, achieving high scores in both ROC-AUC and Test Accuracy without the need for scaling.

Summary of Key Findings
Top Performing Models:

KNN and WNN models achieved the best performance in both ROC-AUC (0.91) and Test Accuracy (0.89), with minimal impact from scaling.
Logistic Regression also performed well with 0.90 ROC-AUC and 0.89 Test Accuracy, though it showed sensitivity to certain scalers.
Impact of Scaling:

Scaling generally resulted in a slight drop in performance across most models, indicating that feature distribution was already suitable for training.
Random Forest was particularly sensitive to scaling, with a noticeable drop in both ROC-AUC and Test Accuracy when scaled.
Recommended Models:

KNN and WNN are recommended as the top models based on their balanced ROC-AUC and Test Accuracy performance without scaling.
