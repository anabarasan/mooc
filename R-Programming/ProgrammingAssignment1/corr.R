source('complete.R')
corr <- function(directory, threshold = 0) {
  file_list = list.files(path = directory, full.names = TRUE)
  correlation <- numeric()#data.frame()
  for (i in 1:332) {
    comp.case <- complete(directory, i)
    if (comp.case$nobs > threshold) {
      dat <- read.csv(file_list[i])
      good <- complete.cases(dat)
      dat <- dat[good,]
      sulphate <- dat$sulfate
      nitrate <- dat$nitrate
      correlation <- c(correlation, cor(sulphate, nitrate))
    }
  }
  correlation
}
