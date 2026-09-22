# Program 1: Salary Prediction using Linear Regression

from sklearn.linear_model import LinearRegression

# Training data
X = [[1], [2], [3], [4], [5]]
y = [25000, 30000, 35000, 40000, 45000]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])

print("Predicted Salary:", prediction[0])