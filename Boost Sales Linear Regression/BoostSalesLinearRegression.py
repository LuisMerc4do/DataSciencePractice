### LUIS MERCADO ### 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

# Data
months = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
ai_spending = np.array([3.2, 7.5, 9.9, 10.2, 12.4, 15.7, 20.0, 23.3, 26.6, 30.9, 34.2, 44.5]).reshape(-1, 1)  # Reshape for sklearn
# Reshape for sklearn
revenue = np.array([44, 32, 27, 22, 17, 16, 12, 10, 8, 4, 2, 0])

# Scatter plot
plt.figure(figsize=(10,6))
plt.scatter(ai_spending, revenue, color="blue", label="Data")
plt.xlabel("Money Spent in AI ($K)")
plt.ylabel("Revenue (K Units)")
plt.title("Money Spending vs Revenue")
plt.grid(True)

#Linear Regression
regressor = LinearRegression()
regressor.fit(ai_spending, revenue)
predicted_sales = regressor.predict(ai_spending)

# Plotting the regression Line
plt.plot(ai_spending, predicted_sales, color="red", label="Regression Line")
plt.legend()
# Show Plot
plt.show()

# Coefficients
print("Intercept:", regressor.intercept_)
print("Coefficient: ", regressor.coef_[0])
