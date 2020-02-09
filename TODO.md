# Notes and tasks

- Currently, the encoding seems to be a hash in a dictionary: converted each word into an integer. However, I think ultimately, we will want a true one hot encoding where each word becomes a vector with all zeros except a one in the corresponding entry.

- Furthermore, I think we will want to limit the dictionary size. We will already have a sparsity problem. Limiting the dictionary size should help with that. 

- I've wrapped the data parsing into a function. My original motivation was so we didn't need to make four different copies of every name. However, I believe in every iteration, we would need all four data sets simultaneously, so it probably doesn't make sense to have it in a function. We should remove this in a future iteration.

- Compute the ratio of positive to negative in the testing data set. This will serve as a baseline for any classifier. 
