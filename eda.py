import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("Telco_customer_churn.xlsx")

print("Shape:", df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Churn Distribution
plt.figure(figsize=(6,4))
sns.countplot(x="Churn Label", data=df)
plt.title("Customer Churn Distribution")
plt.show()

# Contract Type vs Churn   <-- ADD THIS BELOW THE FIRST GRAPH
plt.figure(figsize=(7,5))
sns.countplot(x="Contract", hue="Churn Label", data=df)
plt.title("Contract Type vs Churn")
# Monthly Charges vs Churn
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn Label", y="Monthly Charges", data=df)
plt.title("Monthly Charges vs Churn")
plt.show()
plt.figure(figsize=(7,5))
sns.countplot(x="Internet Service", hue="Churn Label", data=df)
plt.title("Internet Service vs Churn")
plt.show()
# Payment Method vs Churn
plt.figure(figsize=(8,5))
sns.countplot(x="Payment Method", hue="Churn Label", data=df)
plt.title("Payment Method vs Churn")
plt.xticks(rotation=20)
plt.show()
# Tenure Months vs Churn
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn Label", y="Tenure Months", data=df)
plt.title("Tenure Months vs Churn")
plt.show()
# Senior Citizen vs Churn
plt.figure(figsize=(6,4))
sns.countplot(x="Senior Citizen", hue="Churn Label", data=df)
plt.title("Senior Citizen vs Churn")
plt.show()
plt.figure(figsize=(6,4))
sns.countplot(x="Paperless Billing", hue="Churn Label", data=df)
plt.title("Paperless Billing vs Churn")
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(x="Gender", hue="Churn Label", data=df)
plt.title("Gender vs Churn")
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(x="Dependents", hue="Churn Label", data=df)
plt.title("Dependents vs Churn")
plt.show()