set.seed(42)
n_rep <- 5000

png("7a.png", width = 8, height = 5, units = "in", res = 150)  # landscape

empirical <- replicate(n_rep, sum(rnorm(9, 0, 1)^2))

theoretical <- rchisq(n_rep, df = 9)

dens_emp <- density(empirical)
dens_theo <- density(theoretical)

plot(dens_emp, type = "l", lty = 1, col = "black",
     xlab = "x", ylab = "Density",
     main = expression(sum(X[i]^2, i = 1, 9) ~ "vs" ~ chi[9]^2))
lines(dens_theo, lty = 2, col = "gray50")
legend("topright",
       legend = c(expression(sum(X[i]^2, i = 1, 9)), expression(chi[9]^2)),
       lty = c(1, 2), col = c("black", "gray50"))

dev.off()
