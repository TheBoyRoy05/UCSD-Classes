# Problem 7.2: Law of Large Numbers Simulation
# Generate 10 paths of sample means of squares from uniform distribution on [0, 2]

set.seed(123)  # For reproducibility

n_max <- 40
num_paths <- 10
theoretical_mean_squared <- 4/3  # E[X_i^2] for uniform on [0, 2] = (1/2) * (8/3) = 4/3

# Initialize matrix to store sample means of squares for each path
sample_means_squared <- matrix(0, nrow = num_paths, ncol = n_max)

# Generate 10 independent paths
for (path in 1:num_paths) {
  # Generate n_max uniform random variables from [0, 2]
  X <- runif(n_max, min = 0, max = 2)
  
  # Calculate cumulative sample means of squares
  for (n in 1:n_max) {
    sample_means_squared[path, n] <- mean(X[1:n]^2)
  }
}

# Set plot parameters for landscape orientation and larger fonts
# Open a Windows graphics device with landscape dimensions (wider than tall)
windows(width = 12, height = 7)
par(mar = c(5, 5, 4, 2), cex.axis = 1.5, cex.lab = 1.8, cex.main = 1.8, pin = c(10, 5))

# Create the plot
plot(1:n_max, sample_means_squared[1, ], type = "l", 
     ylim = c(0, 4),
     xlab = "n (sample size)",
     ylab = "Sample Mean of Squares",
     main = "Law of Large Numbers: Sample Means of Squares Converging to E[X²] = 4/3",
     col = "blue",
     lwd = 1.5)

# Add remaining 9 paths
for (path in 2:num_paths) {
  lines(1:n_max, sample_means_squared[path, ], col = path, lwd = 1.5)
}

# Add horizontal line at theoretical mean of squares
abline(h = theoretical_mean_squared, col = "red", lty = 2, lwd = 3)

# Add legend with larger font
legend("topright", 
       legend = c("10 Sample Paths", "Theoretical Mean E[X²] = 4/3"),
       col = c("blue", "red"),
       lty = c(1, 2),
       lwd = c(2, 3),
       cex = 1.5)
