# Problem 7.2: Sample mean consistency - compare histograms for n=10 vs n=1000

mu <- 1
sigma2 <- 2
sigma <- sqrt(sigma2)
n_sims <- 500

set.seed(42)
means_n10 <- replicate(n_sims, mean(rnorm(10, mean = mu, sd = sigma)))
means_n1000 <- replicate(n_sims, mean(rnorm(1000, mean = mu, sd = sigma)))

# Side-by-side histograms
png("7.2.png", width = 1200, height = 500)
par(mfrow = c(1, 2))

hist(means_n10, breaks = 20, main = "n = 10", xlab = "Sample mean",
     xlim = range(c(means_n10, means_n1000)), col = "lightblue")
abline(v = mu, col = "red", lwd = 2)

hist(means_n1000, breaks = 20, main = "n = 1000", xlab = "Sample mean",
     xlim = range(c(means_n10, means_n1000)), col = "lightgreen")
abline(v = mu, col = "red", lwd = 2)

par(mfrow = c(1, 1))

# Summary statistics
cat("n = 10:  mean =", mean(means_n10), ", sd =", sd(means_n10),
    "(theoretical sd =", sigma / sqrt(10), ")\n")
cat("n = 1000: mean =", mean(means_n1000), ", sd =", sd(means_n1000),
    "(theoretical sd =", sigma / sqrt(1000), ")\n")

dev.off()