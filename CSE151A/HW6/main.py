import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

# Load the heart disease dataset
data = pd.read_csv('heart.csv')

# Clean the data
data = data.dropna()
data['target'] = data['target'].apply(lambda x: 1 if x > 0 else 0)  # Binary classification

# Split the data
X = data.drop('target', axis=1).values
y = data['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the logistic regression loss function
def logistic_loss(w, X, y, return_grad=False):
    """
    Calculate the logistic regression loss and gradient if requested
    """
    n_samples = X.shape[0]
    z = X @ w
    sigmoid = 1 / (1 + np.exp(-z))
    
    # Handle numerical stability
    loss = -np.mean(y * np.log(np.maximum(sigmoid, 1e-15)) + 
                    (1 - y) * np.log(np.maximum(1 - sigmoid, 1e-15)))
    
    if return_grad:
        grad = X.T @ (sigmoid - y) / n_samples
        return loss, grad
    
    return loss

# Implementation of coordinate descent for logistic regression
def coordinate_descent(X, y, max_iter=1000, tol=1e-4, eta=0.5):
    """
    Coordinate descent algorithm for logistic regression
    
    Parameters:
    -----------
    X : array-like, shape (n_samples, n_features)
        Training data
    y : array-like, shape (n_samples,)
        Target values
    max_iter : int
        Maximum number of iterations
    tol : float
        Tolerance for stopping criterion
    eta : float
        Step size multiplier
    
    Returns:
    --------
    w : array, shape (n_features,)
        Coefficients
    loss_history : list
        Loss at each iteration
    """
    n_samples, n_features = X.shape
    w = np.zeros(n_features)
    loss_history = []
    
    for t in range(max_iter):
        # Calculate current loss and gradient
        loss, grad = logistic_loss(w, X, y, return_grad=True)
        loss_history.append(loss)
        
        # Find coordinate with largest absolute gradient value
        i = np.argmax(np.abs(grad))
        grad_max_abs = np.abs(grad[i])
        
        # Check convergence
        if grad_max_abs < tol:
            print(f"Converged after {t} iterations!")
            break
        
        # Update that coordinate
        direction = -np.sign(grad[i])
        step_size = eta * grad_max_abs
        
        # Create a one-hot update vector
        update = np.zeros(n_features)
        update[i] = direction * step_size
        
        # Apply the update
        w = w + update
        
    return w, loss_history

# Train using scikit-learn's LogisticRegression as reference
sklearn_model = LogisticRegression(penalty=None, tol=1e-5, max_iter=1000)
sklearn_model.fit(X_train, y_train)
sklearn_w = np.concatenate([sklearn_model.intercept_, sklearn_model.coef_[0]])

# Add a column of ones to X for the intercept term
X_train_with_intercept = np.column_stack([np.ones(X_train.shape[0]), X_train])
X_test_with_intercept = np.column_stack([np.ones(X_test.shape[0]), X_test])

# Calculate the optimal loss using sklearn's solution
L_star = logistic_loss(sklearn_w, X_train_with_intercept, y_train)
print(f"Optimal loss from sklearn: {L_star:.6f}")

# Run our coordinate descent implementation
cd_w, loss_history = coordinate_descent(X_train_with_intercept, y_train, max_iter=1000, tol=1e-4, eta=0.5)
final_loss = logistic_loss(cd_w, X_train_with_intercept, y_train)
print(f"Final loss from coordinate descent: {final_loss:.6f}")

# Plotting the loss convergence
plt.figure(figsize=(10, 6))
plt.plot(loss_history, label='Coordinate Descent Loss')
plt.axhline(y=L_star, color='r', linestyle='--', label=f'Optimal Loss (sklearn): {L_star:.6f}')
plt.xlabel('Iteration')
plt.ylabel('Logistic Loss')
plt.title('Convergence of Coordinate Descent')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('coordinate_descent_convergence.png')
plt.show()

# Calculate and print test accuracy
sklearn_preds = sklearn_model.predict(X_test)
sklearn_acc = np.mean(sklearn_preds == y_test)

# For our model, we need to calculate predictions manually
cd_probs = 1 / (1 + np.exp(-X_test_with_intercept @ cd_w))
cd_preds = (cd_probs >= 0.5).astype(int)
cd_acc = np.mean(cd_preds == y_test)

print(f"Test accuracy (sklearn): {sklearn_acc:.4f}")
print(f"Test accuracy (coordinate descent): {cd_acc:.4f}")

# Detailed analysis of the differences
print("\nParameter comparison:")
print("-" * 50)
print(f"{'Feature':<10} {'sklearn':<15} {'Coordinate Descent':<20} {'Diff':<10}")
print("-" * 50)
print(f"{'Intercept':<10} {sklearn_w[0]:<15.6f} {cd_w[0]:<20.6f} {abs(sklearn_w[0] - cd_w[0]):<10.6f}")

for i in range(1, len(cd_w)):
    feature_name = data.columns[i-1]
    print(f"{feature_name:<10} {sklearn_w[i]:<15.6f} {cd_w[i]:<20.6f} {abs(sklearn_w[i] - cd_w[i]):<10.6f}")

# Compare convergence rates with different step sizes
step_sizes = [0.1, 0.5, 1.0]
plt.figure(figsize=(12, 7))

for eta in step_sizes:
    _, eta_loss_history = coordinate_descent(X_train_with_intercept, y_train, max_iter=1000, tol=1e-4, eta=eta)
    plt.plot(eta_loss_history, label=f'η = {eta}')

plt.axhline(y=L_star, color='r', linestyle='--', label=f'Optimal Loss: {L_star:.6f}')
plt.xlabel('Iteration')
plt.ylabel('Logistic Loss')
plt.title('Effect of Step Size on Coordinate Descent Convergence')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('step_size_comparison.png')
plt.show()