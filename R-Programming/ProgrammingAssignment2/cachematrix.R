## Cache Inverse of Matrix
## Matrix Inversion in a costly computation.  
## Caching the result may have some benefits rather than repeatedly calculating.

makeCacheMatrix <- function(x = matrix()) {
    ## Creates a special matrix object which can cache its inverse 
    ##
    ## Args:
    ##    x: the matrix whose inverse is to be calculated / cached
    ##
    ## Returns:
    ##    The special matrix object which can cache its inverse
    
    # initialize inverse to NULL
    inverse <- NULL
    
    set <- function(y) {
        # set the matrix object in x which is to be enhanced with caching.
        # clear the INVERSE value
        x <<- y
        inverse <<- NULL
    }
    get <- function () {
        # Returns:
        #    the stored value of matrix
        x
    }
    
    setInverse <- function (inv) {
        # store the inverse value of the matrix
        # Args:
        #    The inverse value of the matrix to be stored
        inverse <<- inv
    }
    
    getInverse <- function () {
        # Returns:
        #    The inverse value of the matrix
        inverse
    }
    
    # create a list with properties which will be returned
    list(set = set, get = get, setInverse = setInverse, getInverse = getInverse)
}


cacheSolve <- function(x, ...) {
    ## Calculate the inverse for makeCacheMatrix Object
    ## Args:
    ##    x: The CacheMatrix Object
    ## Returns:
    ##    The inverse Matrix
    
    inverse <- x$getInverse()               # get the Inverse value from the cache.
    
    if (is.null(inverse)) {                 # check if cache value exists.
        message('calculating inverse')      # cache value does not exist
        mtrix <- x$get()                    # get the matrix from CacheMatrix Object
        inverse <- solve(mtrix, ...)        # calculate the inverse
        x$setInverse(inverse)               # store the inverse in cache
        inverse                             # return the calculated inverse
    } else {
        message('retrieving from cache')    # cache value exists
        return (inverse)                    # return the inverse from cache
    }
}
