import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


base_credit = pd.read_csv('C:\\Users\\User\\Downloads\\archive\\credit_risk_dataset.csv')


#print(base_credit.head(10))
#print(base_credit.describe())
print(base_credit)
#sns.countplot(x = base_credit['loan_status'])
x=np.unique(base_credit['loan_status'], return_counts=True)
print(x)
sns.countplot(c=base_credit['loan_status'])
sns.lineplot()
plt.hist(x = base_credit['person_home_ownership'])
plt.show()
grafico = px.scatter_matrix(base_credit, dimensions=['person_age', 'person_income', 'loan_intent'], color = 'person_age')
grafico.show()