complete <- function(directory, id=1:332) {
  file_list <- list.files(path = directory, full.names = TRUE)
  df <- data.frame()
  for (i in id) {
    data <- read.csv(file_list[i])
    filter <- complete.cases(data)
    good <- data[filter,]
    nobs <- nrow(good)
    df <- rbind(df, c(i, nobs))
  }
  colnames(df) <- c("id","nobs")
  df
}
