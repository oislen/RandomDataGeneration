# RandomDataGeneration

## TODO:
1. code underlying relationships between transaction status and user behaviour for non-zero transactions (possibly wrap within a single function call applied over lambda)
   1. Users with excess number of devices, ips, cards
   2. Users with shared devices, ips and cards
   3. Infrequent domain names
2. add input parameter error handling
3. expand to include other countries and continents (possibly combine all country information into a single file)
4. add unittests
5. containerise application
6. deploy on aws ec2 instance
7. add documentation to repo and code
8. add new hire tasks
   1. network analysis
   2. cluster
   3. feature engineering
   4. predictive modelling

gen_user_data execution times
factor,n_users,pandas,dask
1,1372,11.75,18.44
2,2744,35.69,41.23
3,4116,69.84,78.91