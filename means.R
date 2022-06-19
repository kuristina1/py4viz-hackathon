dataset <- read.csv("flavors_of_cacao.csv")
dataset
png(file = "boxplot for rating.png")
boxplot(dataset$Rating, ylab = "Rating from 1 to 5", main = "Ratings")
dev.off()
dataset2 <- read.csv("data.csv")
png(file = "boxplot for cocoa percentage.png")
boxplot(dataset2$CocoaPercent, ylab = "Cocoa percentage", main = "Cocoa content")
dev.off()
