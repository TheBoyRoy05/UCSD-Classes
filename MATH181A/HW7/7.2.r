# Problem 7(b): Power vs effect size delta for two-sided z-test
# H0: mu = mu0 vs H1: mu != mu0, sigma^2 = 1, alpha = 0.05
# Power(delta, n) = Phi(-1.96 - sqrt(n)*delta) + 1 - Phi(1.96 - sqrt(n)*delta)

delta <- seq(-2, 2, length.out = 200)
power_n10 <- pnorm(-1.96 - sqrt(10) * delta) + 1 - pnorm(1.96 - sqrt(10) * delta)
power_n40 <- pnorm(-1.96 - sqrt(40) * delta) + 1 - pnorm(1.96 - sqrt(40) * delta)

par(pin = c(8, 5))
plot(delta, power_n10, type = "l", col = "blue", lwd = 2,
     xlab = expression(delta), ylab = "Power",
     main = "Power vs Effect Size (two-sided test, alpha = 0.05)",
     ylim = c(0, 1))
lines(delta, power_n40, col = "red", lwd = 2)
legend("bottomright", legend = c("n = 10", "n = 40"),
       col = c("blue", "red"), lty = 1, lwd = 2)
abline(h = 0.05, lty = 2, col = "gray")  # alpha at delta = 0
