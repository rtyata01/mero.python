# Regularization helps when your model fits the training data too well (overfits) and performs poorly on new data. 
# It does this by shrinking or penalizing large weights in the model.
# L1 Regularization = Lasso Regression	= Adds absolute value of coefficients to the loss.
# L2 Regularization = Ridge Regression  = Adds square value of coefficients to the loss 

from sklearn.linear_model import Lasso, Ridge
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# Generate synthetic data
X, y = make_regression(n_samples=100, n_features=10, noise=10)

# Fit L1 (Lasso)
lasso = Lasso(alpha=0.1)
lasso.fit(X, y)

# Fit L2 (Ridge)
ridge = Ridge(alpha=0.1)
ridge.fit(X, y)

print("Lasso Coefficients:", lasso.coef_)
print("Ridge Coefficients:", ridge.coef_)
