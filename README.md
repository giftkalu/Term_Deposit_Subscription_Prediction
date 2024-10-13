# Term Deposit Subscription
Building a Decision Tree classifier to predict if the client will subscribe to a Term Deposit based on their demographic and behavioural data. This dataset has 11162 entries.
#### Variables
1. age: Age of the client
2. job: Occupation of the client
3. marital: Whether the client is married or not
4. education: The highest level of Education attained(ordinal)
5. default: If the customer has a previous loan default
6. balance: Current balance in the account
7. housing: If the customer had a housing loan
8. loan: If they have obtained a previous loan
9. contact: Mode of contact with customer
10. day: The day of the month contacted
11. month: The month contact was made
12. duration: The duration of the most recent contact with the client in seconds.
13. campaign:The number of contacts performed during the current marketing campaign.
14. pdays:The number of days that passed since the client was last contacted, or -1 if not contacted previously.
15. previous:The number of times the client was contacted before during previous campaigns.
16. poutcome:The outcome of the previous marketing campaign with the client (e.g., success, failure).
#### Target Variable
17. deposit: subscribed to the deposit (yes or no)
#### Model Used
- Decision Trees
#### Techniques Used
- Exploratory Data Analysis
- Diverse Data Visualisations
- Handling Categorical columns using label encoders
- Hyper Parameter Tuning using Grid Search
- Tree pruning
- Overview of Insights
#### Evaluation Metrics
- Accuracy
- Cross Validation score
- Precision
- Recall
- F-1 score
