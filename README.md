# RandomDataGeneration

## TODO:
1. code underlying relationships between transaction status and user behaviour for non-zero transactions
   1. Inconsistent country codes indicate higher risk
   2. Excess number of devices, ips, cards
   4. Shared devices, ips and cards
2. add command line interface
3. add documentation
4. containerise
5. add multiprocessing through dask to scale performance up with dataset size
6. add new hire tasks

gen_user_data execution times
factor,n_users,pandas,dask
1,1372,11.75,18.44
2,2744,35.69,41.23
3,4116,69.84,78.91