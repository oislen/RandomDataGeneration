# Random Telecom Data Generation

Randomly simulated data is particularly useful when it's real world counterpart is hard to come by due to complexity, privacy and security reasons. This application aims to simulate telecommunication payments using random number generation. It includes typical transaction level relationships and behaviours amongst user, device, ip, and card entities. It can be used inplace of real world telecommunication payments for prototyping solutions and as an education tool.

The following command can be used to execute the application:

     python3 RandomTeleComData/scripts/main.py --factor 0.5 --randomseed 1 --nitr 3

The underlying data model present in the simulated telecommunication payments is displayed below.

![Entity Relationship Diagram](doc/entity_relationship_diagram.jpg)
