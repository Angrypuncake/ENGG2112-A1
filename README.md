# ENGG2112-A1

Q/A Cheatsheet

1. Why did clinical data perform better than lifestyle data?
Answer: Clinical data is more specific and numerical, like cholesterol and blood pressure, which are direct health indicators. These features make it easier for models to find patterns, unlike the more general and categorical lifestyle data.

2. What preprocessing steps did you apply to the data?
Answer: For the clinical data, we removed missing values and scaled the data. For lifestyle data, we did more: filling in missing values, scaling, encoding categorical variables, and using PCA to reduce complexity.

3. Why did you use PCA, and what is it?
Answer: PCA (Principal Component Analysis) reduces data complexity by transforming it into fewer dimensions. We used it on lifestyle data to help the model handle the large number of variables, though it didn’t fully improve prediction accuracy.

4. What are ROC curves, and why did you use them?
Answer: ROC (Receiver Operating Characteristic) curves show how well the model distinguishes between high and low risk. A curve closer to the top-left corner means better accuracy. We used them to compare model performance visually.

5. Why did you choose K-Nearest Neighbors and Logistic Regression?
Answer: Both are simple, reliable models. They performed well with clinical data due to its clear, numerical patterns, which these models handle well.

6. What limitations did you face with the lifestyle data?
Answer: Lifestyle data had mostly categorical values, like exercise level and diet. These are less precise than numerical data, making it harder for the model to identify strong risk patterns.

7. What is the significance of your findings?
Answer: Our findings show that clinical data can be used to make accurate early predictions, helping doctors recommend preventive actions. Lifestyle data, while less precise, may still help as extra context.

8. How could lifestyle data still be useful?
Answer: Even though it’s not as precise, lifestyle data can add context to clinical data, giving a fuller picture of a patient’s risk factors.

9. What improvements would you make in future work?
Answer: We would gather more detailed and consistent lifestyle data, explore combining more clinical factors, and try more advanced models to see if they handle categorical data better.

10. Did you encounter any ethical considerations in this project?
Answer: Yes, mainly privacy concerns. Handling health data requires strict data protection, and model recommendations should be used carefully to avoid misleading patients.

11. How could this project be applied in real-world settings?
Answer: It could be used in healthcare to create risk assessment tools, integrate with hospital systems, or even in wearable devices for tracking heart health.

12. Why is accuracy important in this project?
Answer: High accuracy reduces the chance of false negatives (missed risks) and false positives (unnecessary warnings), ensuring that only high-risk patients get flagged for preventive measures.

13. Why did lifestyle data models perform close to random?
Answer: Lifestyle data may be too generalized and lacks the precision of clinical readings, making it hard for models to identify specific risk patterns.

14. What metrics did you use to evaluate model performance?
Answer: We used accuracy, ROC-AUC, and precision-recall metrics. ROC-AUC was especially useful because it shows how well the model distinguishes risk levels.

15. How would you handle missing data differently if you had more time?
Answer: We could try more advanced imputation methods, like predictive modeling to fill gaps more accurately, especially for lifestyle data.

16. What is recall, and why is it important in your project?
Answer: Recall measures how well the model identifies actual heart attack risks among all those at risk. High recall is crucial here because it means the model successfully flags most high-risk individuals, reducing missed cases.

17. How did the recall scores differ between clinical and lifestyle models?
Answer: Clinical models had higher recall, meaning they were better at detecting high-risk cases. Lifestyle models, however, had low recall, indicating they missed many actual risks, likely due to the general nature of lifestyle data.

18. What is the F1 score, and why did you use it?
Answer: The F1 score is the balance between precision and recall, giving a single measure of a model’s accuracy, especially with imbalanced data. It’s useful in our project because it shows how well the model balances identifying risks accurately without too many false positives.

19. How did the F1 scores compare between clinical and lifestyle models?
Answer: The F1 score was higher for clinical models, showing they could balance identifying risks while minimizing false positives. For lifestyle models, the F1 score was low, indicating they struggled to make accurate predictions consistently.

20. What is specificity, and why does it matter for this project?
Answer: Specificity measures the model’s ability to correctly identify low-risk cases, or true negatives. High specificity reduces false alarms, so only actual high-risk patients get flagged. This is essential to avoid overloading healthcare resources with unnecessary alerts.

21. How did specificity scores compare across the datasets?
Answer: Clinical data models had higher specificity, meaning they accurately identified low-risk patients, reducing false positives. The lifestyle models had low specificity, which means they often flagged low-risk individuals as high-risk due to the general nature of lifestyle data.

22. Why is balancing recall and specificity important in healthcare predictions?
Answer: Balancing recall and specificity ensures the model doesn’t miss high-risk patients (high recall) while also avoiding unnecessary warnings (high specificity). This balance helps make predictions both reliable and practical for real-world healthcare.

23. What insights did you gain from using F1 score over accuracy alone?
Answer: The F1 score helped us understand how well the model balanced detecting true risks and avoiding false alarms, which accuracy alone doesn’t show. This was particularly useful for evaluating lifestyle models, which had lower F1 scores despite decent accuracy.
