set.seed(42)
n_rep <- 5000

png("7b.png", width = 8, height = 5, units = "in", res = 150)  # landscape

empirical <- replicate(n_rep, {
  x <- rnorm(9, 0, 1)
  3 * mean(x) / sqrt((1 / 8) * sum((x - mean(x))^2))
})

theoretical <- rt(n_rep, df = 8)

dens_emp <- density(empirical)
dens_theo <- density(theoretical)

plot(dens_emp, type = "l", lty = 1, col = "black",
     xlab = "x", ylab = "Density",
     main = expression(3 * bar(X) / S ~ "vs" ~ t[8]))
lines(dens_theo, lty = 2, col = "gray50")
legend("topright",
       legend = c(expression(3 * bar(X) / S), expression(t[8])),
       lty = c(1, 2), col = c("black", "gray50"))

dev.off()
