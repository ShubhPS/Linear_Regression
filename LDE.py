import numpy as np

# Load training data
X = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 4, 5, 4, 5])

# Calculate the mean of X and y
X_mean = np.mean(X)
y_mean = np.mean(y)

# Calculate the slope (m) and y-intercept (b)
m = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)
b = y_mean - m * X_mean

# Define function to make predictions
def predict(X):
    return m * X + b

# Test the algorithm
X_test = np.array([6, 7, 8]).reshape((-1, 1))
y_test = np.array([6, 8, 9])
y_pred = predict(X_test)

print("Predictions: ", y_pred)
print("True values: ", y_test)