# Machine learning

## Simple regression

### Steps to find a linear regression line:

1. input x and y values in an array
2. find mean of those arrays
3. on a graph, plot the x mean and the y mean
4. calculate the distance of the x values from the x mean line, and the y values from the y mean line. these values go in the x-x_mean and y-y_mean columns
5. now square the values in the x-x_mean column
6. and multiply the x-x_mean column. by the y-y_mean column.

| x | y | x-x_mean | y-y_mean | (x-x_mean)^2 | (x-x_mean)*(y-y_mean) | 
|---|---|--------|--------|------------|----------------------| 
1 | 2 | -2 | -1 | 4 | 2 |
| 2 | 4 | -1 | 1 | 1 | 1 |
| 3 | 5 | 0 | 2 | 0 | 0 | 
| 4 | 4 | 1 | 1 | 1 | 1 | 
| 5 | 5 | 2 | 2 | 4 | 2 |
	

Now that we have our values, we can find the slope of the regression line, by this formula:
> m =  sum of(x-x_mean)(y-y_mean)/sum of(x-x_mean)^2
where the sum is calculated by adding the column of values,
which means the slope of the regression line of our values is 6/10 = .6

Now we want to find the y-intercept, or c, by subbing in and rearranging the formula:
> y = mx + c, becomes
> 4 = .6(3) + c, which means
> c = 2.2

So, after our calculations we can write the simple regression line as:
> y = 0.6x + 2.2

## My python implementation
```
import numpy as np
class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None
    def bestfit(self, x, y):
        x_avg = np.mean(x)
        y_avg = np.mean(y)
        
        x_dev  = x - x_avg #remember this is still an array so we use sum() later.
        y_dev = y - y_avg  #where dev stands for deviation

        slope = np.sum(x_dev*y_dev) / np.sum(x_dev**2)
        intercept = y_avg - slope * x_avg
        self.slopeintercept = (slope, intercept)

    def predict(self, x):
        slope, intercept  = self.slopeintercept
        return slope * x + intercept
```



