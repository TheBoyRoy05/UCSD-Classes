# Theoretical values (for comparison)
alpha <- c(0.01, 0.05, 0.1)
theoretical <- qnorm(1 - alpha / 2)  # upper critical values
names(theoretical) <- paste0("alpha=", alpha)
print("Theoretical z_{alpha/2}:")
print(round(theoretical, 4))

set.seed(42)
n1 <- 1000
sample1 <- rnorm(n1, mean = 0, sd = 1)
approx1 <- quantile(sample1, probs = 1 - alpha / 2)
names(approx1) <- paste0("alpha=", alpha)
print("Approximation (n = 1000):")
print(round(approx1, 4))
print("Difference from theoretical:")
print(round(approx1 - theoretical, 4))

# n = 10000 (better approximation)
n2 <- 10000
sample2 <- rnorm(n2, mean = 0, sd = 1)
approx2 <- quantile(sample2, probs = 1 - alpha / 2)
names(approx2) <- paste0("alpha=", alpha)
print("Approximation (n = 10000):")
print(round(approx2, 4))
print("Difference from theoretical:")
print(round(approx2 - theoretical, 4))