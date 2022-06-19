data4 <- read.csv("data_chocolate.csv")
library(magrittr)
library(dplyr)
library(ggplot2)
png(file = "cocoa.png")
data4 %>%
  ggplot(aes(x = CocoaPercent, y = Rating)) +
  geom_jitter(alpha = .75) + 
  coord_cartesian(ylim = c(0,5)) +
  labs(x = 'Cocoa percentage', y = 'Rating') + 
  theme_minimal() + 
  geom_smooth(formula = y ~ x, method = 'lm', se = FALSE, col = 'red')
dev.off()


model <- lm(formula = Rating ~ CocoaPercent, 
            data = data4)
summary(model)
