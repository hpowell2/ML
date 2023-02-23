#linear regression  
#practice with np and linear statistics
#quick note so i don't forget: 
#the slope tells us how much y is expected to change for every unit change in x,
#while taking into account the average deviation of x and y from their means.


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


def main():
	print("This model finds a line of best fit in equation y = mx + c and can then make predictions.")
	x_input = input("Enter a list of x values separated by spaces: ")
	y_input = input("Enter a list of y values separated by spaces: ")
	x_predict_input = input("Enter a value of x to predict: ")

	try:
		x = np.array(x_input.split(), dtype=float)
		y = np.array(y_input.split(), dtype=float)
		x_predict = float(x_predict_input)
		if len(x) == 0 or len(y) == 0:
			raise ValueError("Input lists cannot be empty.")
		if len(x) != len(y):
			raise ValueError("The length of x and y must be the same.")
	except ValueError as x:
		print(f"Error: {x}")
	
	
	model = LinearRegression()#initialize instance
	model.bestfit(x, y)#find bestfit
	y_predict = model.predict(x_predict)#calculate y
	
	line_equation = model.display()#find eq
	print(f'Predicted value of y for x = {x_predict:.2f}: {y_predict:.2f}')#display predict
	print(f'Equation of the line: {line_equation}')#display eq
	
	again = input("Do you want to try again? (y/n)")
	if again == "y":
		main()

if __name__ == "__main__":
	main()
