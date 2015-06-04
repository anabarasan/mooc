best <- function(state, outcome) {
  ## Read outcome data
  ip <- read.csv('outcome-of-care-measures.csv', colClasses = 'character', na.strings = "Not Available")
  ## Check that state and outcome are valid
  valid.states <- unique(ip$State)
  valid.outcomes <- c("heart attack", "heart failure", "pneumonia")
  if (!state %in% valid.states) { stop("invalid state") }
  if (!outcome %in% valid.outcomes) { stop("invalid outcome") }
  
  # get the outcome column name
  valid.colName <- c("Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack", "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure", "Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia")
  colName <- valid.colName[match(outcome, valid.outcomes)]
  
  ## Return hospital name in that state with lowest 30-day death rate
  # Get the state related records alone
  ip.state <- subset(ip, ip$State == state)
  
  # get required columns alone
  # the hospital names in the state
  # the morality value for the provided outcome
  state.hospitals <- ip.state$Hospital.Name
  state.outcome   <- ip.state[,colName]
  
  # clean the filtered data
  state.outcome <- as.numeric(state.outcome)
  bad <- is.na(state.outcome)
  state.outcome.good <- ip.state[!bad,]
  
  # get hospitals with min value for outcome
  outcome.numeric <- as.numeric(state.outcome.good[, colName])
  desired_rows <- which(outcome.numeric == min(outcome.numeric))
  best_hospitals <- state.outcome.good[desired_rows, 2]
  best_hospitals_sorted <- sort(best_hospitals)
  best_hospitals_sorted[1]
}

#source("http://d396qusza40orc.cloudfront.net/rprog%2Fscripts%2Fsubmitscript3.R")