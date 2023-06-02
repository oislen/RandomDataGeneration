# Random Telecom Data Generation

This application simulates telecommunication payments using random number generation. 


     python3 RandomTeleComData/scripts/main.py --factor 0.5 --randomseed 1 --nitr 3

![Entity Relationship Diagram](./doc/entity_relationship_diagram.png)

## TODO:
1. revise underlying relationships between transaction status and user behaviour for non-zero transactions 
   1. wrap all logic within a single function and call over .apply with lambda
2. expand to include other countries and continents (possibly combine all country information into a single file)
3. add unittests
4. add documentation to repo and code
5. add new hire tasks
   1. network analysis
   2. cluster
   3. feature engineering
   4. predictive modelling