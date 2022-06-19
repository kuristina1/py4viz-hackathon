data5 <- read.csv("data_chocolate.csv")
library(magrittr)
library(dplyr)
library(ggplot2)
png(file = "ratings for countries.png")
data2 %>%
  group_by(CompanyLocation) %>% 
  filter(n() > 10) %>% 
  mutate(avg = mean(Rating)) %>%
  ggplot() + 
  geom_boxplot(aes(reorder(CompanyLocation, avg), Rating, fill = avg)) + 
  scale_fill_continuous(low = '#00bfff', high = '#00008b', name = "Average rating") + 
  coord_flip() + 
  theme_minimal() + 
  labs(x = 'Countries', y = 'Rating') +
  expand_limits(y = c(0,5))
dev.off()

