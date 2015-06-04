pollutantmean <- function (directory, pollutant, id = 1:332){
  file_list <- list.files(path = directory, full.names = TRUE)
  df <- data.frame()
  for (i in id) {
    df <- rbind(df, read.csv(file_list[i]))
  }
  mean(df[,pollutant], na.rm=TRUE)
}