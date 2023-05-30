# RandomDataGeneration

## TODO:
1. revise lambda parameters for poisson distributions and relationship with number of hashed entities
2. code underlying relationships between transaction status and user behaviour for non-zero transactions
   1. Country codes / email domains (different levels of risk across different values)
   2. Inconsistent country codes indicate higher risk
   3. Excess number of devices, ips, cards
   4. Shared devices, ips and cards
3. incorporate multiprocessing / dask for parallel processing across cores for scaling random dataset size