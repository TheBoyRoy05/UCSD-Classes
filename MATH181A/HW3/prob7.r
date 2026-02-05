# Problem 7: Likelihood and Log-Likelihood Functions for Normal Distribution

set.seed(123)  # For reproducibility

# Parameters
n <- 20
mu_true <- 1
sigma <- 2
sigma_sq <- sigma^2

# Generate random sample from N(mu=1, sigma^2=4)
y <- rnorm(n, mean = mu_true, sd = sigma)

# Compute MLE (sample mean)
mu_mle <- mean(y)
cat("MLE of mu:", mu_mle, "\n")

# Create range of mu values for plotting
mu_range <- seq(mu_mle - 2, mu_mle + 2, length.out = 1000)

# Likelihood function
likelihood <- function(mu, y, sigma_sq) {
  n <- length(y)
  constant <- (2 * pi * sigma_sq)^(-n/2)
  sum_sq <- sum((y - mu)^2)
  return(constant * exp(-sum_sq / (2 * sigma_sq)))
}

# Log-likelihood function
log_likelihood <- function(mu, y, sigma_sq) {
  n <- length(y)
  constant <- -n/2 * log(2 * pi * sigma_sq)
  sum_sq <- sum((y - mu)^2)
  return(constant - sum_sq / (2 * sigma_sq))
}

# Compute likelihood and log-likelihood values
L_values <- sapply(mu_range, function(mu) likelihood(mu, y, sigma_sq))
logL_values <- sapply(mu_range, function(mu) log_likelihood(mu, y, sigma_sq))

# Plot 1: Likelihood function
windows(width = 12, height = 7)
par(mar = c(5, 5, 4, 2), cex.axis = 1.5, cex.lab = 1.8, cex.main = 1.8)
plot(mu_range, L_values, type = "l", lwd = 2,
     xlab = expression(mu), ylab = "Likelihood",
     main = "Likelihood Function")
abline(v = mu_mle, col = "red", lty = 2, lwd = 2)
points(mu_mle, likelihood(mu_mle, y, sigma_sq), 
       col = "red", pch = 19, cex = 1.5)
legend("topright", legend = paste("MLE =", round(mu_mle, 3)),
       col = "red", lty = 2, lwd = 2, cex = 1.5)

# Plot 2: Log-likelihood function
windows(width = 12, height = 7)
par(mar = c(5, 5, 4, 2), cex.axis = 1.5, cex.lab = 1.8, cex.main = 1.8)
plot(mu_range, logL_values, type = "l", lwd = 2,
     xlab = expression(mu), ylab = "Log-Likelihood",
     main = "Log-Likelihood Function")
abline(v = mu_mle, col = "red", lty = 2, lwd = 2)
points(mu_mle, log_likelihood(mu_mle, y, sigma_sq), 
       col = "red", pch = 19, cex = 1.5)
legend("topright", legend = paste("MLE =", round(mu_mle, 3)),
       col = "red", lty = 2, lwd = 2, cex = 1.5)
