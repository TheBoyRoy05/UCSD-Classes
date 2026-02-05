# Problem 7.1: Law of Large Numbers Simulation
# Generate 10 paths of sample means from uniform distribution on [0, 2]

set.seed(123)  # For reproducibility

n_max <- 40
num_paths <- 10
theoretical_mean <- 1  # E[X_i] for uniform on [0, 2]

# Initialize matrix to store sample means for each path
sample_means <- matrix(0, nrow = num_paths, ncol = n_max)

# Generate 10 independent paths
for (path in 1:num_paths) {
  # Generate n_max uniform random variables from [0, 2]
  X <- runif(n_max, min = 0, max = 2)
  
  # Calculate cumulative sample means
  for (n in 1:n_max) {
    sample_means[path, n] <- mean(X[1:n])
  }
}

# Set plot parameters for landscape orientation and larger fonts
# Open a Windows graphics device with landscape dimensions (wider than tall)
windows(width = 12, height = 7)
par(mar = c(5, 5, 4, 2), cex.axis = 1.5, cex.lab = 1.8, cex.main = 1.8, pin = c(10, 5))

# Create the plot
plot(1:n_max, sample_means[1, ], type = "l", 
     ylim = c(0, 2),
     xlab = "n (sample size)",
     ylab = "Sample Mean",
     main = "Law of Large Numbers: Sample Means Converging to E[X] = 1",
     col = "blue",
     lwd = 1.5)

# Add remaining 9 paths
for (path in 2:num_paths) {
  lines(1:n_max, sample_means[path, ], col = path, lwd = 1.5)
}

# Add horizontal line at theoretical mean
abline(h = theoretical_mean, col = "red", lty = 2, lwd = 3)

# Add legend with larger font
legend("topright", 
       legend = c("10 Sample Paths", "Theoretical Mean E[X] = 1"),
       col = c("blue", "red"),
       lty = c(1, 2),
       lwd = c(2, 3),
       cex = 1.5)
