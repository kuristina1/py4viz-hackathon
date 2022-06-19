data3 <- read.csv("data_chocolate.csv")
library(magrittr)
library(dplyr)
library(ggplot2)
png(file = "ratings for companies.png")
data2 %>%
  group_by(Company) %>% 
  filter(n() > 10) %>% 
  mutate(avg = mean(Rating)) %>%
  ggplot() + 
  geom_boxplot(aes(reorder(Company, avg), Rating, fill = avg)) + 
  scale_fill_continuous(low = '#00bfff', high = '#00008b', name = "Average rating") + 
  coord_flip() + 
  theme_minimal() + 
  labs(x = 'Companies', y = 'Rating') +
  expand_limits(y = c(0,5))
dev.off()
