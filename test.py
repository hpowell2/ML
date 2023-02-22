# import the necessary libraries

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np
class LinearRegression:
	
	def __init__(self):
		self.slope = None
		self.intercept = None

	def bestfit(self, x, y):
		x_avg = np.mean(x)
		y_avg = np.mean(y)
		x_dev  = x - x_avg #this is still an array/list 
		y_dev = y - y_avg	#dev stands for deviation away from the mean of the list

		slope = np.sum(x_dev*y_dev) / np.sum(x_dev**2)
		intercept = y_avg - slope * x_avg

		self.slopeintercept = (slope, intercept)

	def predict(self, x):
		slope, intercept  = self.slopeintercept 
		return slope * x + intercept

	def display(self):
		slope, intercept  = self.slopeintercept 
		return f"y = {slope:.2f}x + {intercept:.2f}"

	print("Welcome to my simple linear regression model.")

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create a linear regression model
model = LinearRegression()

# fit the model to the training data
model.bestfit(X_train, y_train)

# make predictions on the test data
y_pred = model.predict(X_test)

# evaluate the model using mean squared error, R-squared score, root mean squared error, and mean absolute error
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)

# print the evaluation metrics for the model
print("Evaluation Metrics:")
print("MSE:", mse)
print("R2:", r2)
print("RMSE:", rmse)
print("MAE:", mae)
