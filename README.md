# Random Telecom Payments Generation

## Overview

Randomly simulated data is particularly useful when it's real world counterpart is hard access due to complexity, privacy and security reasons. Moreover, randomly simulated data has additional benefits including reproducibility, scalability and controllability. 

This application aims to simulate telecommunication payments using random number generation. It includes typical transaction level relationships and behaviours amongst the user, device, ip, and card entities. It can be used in place of real world telecommunication payments for prototyping solutions and as an education tool. 

## Running the Application

The following command can be used to execute the application:

     python3 RandomTelecomPayments/scripts/main.py --factor 0.5 --randomseed 1 --nitr 3

## Data Model

The underlying data model present in the simulated telecommunication payments is displayed below.

![Entity Relationship Diagram](doc/entity_relationship_diagram.jpg)

## Master File

A stable master version of the Random Telecom Payments data can be found on Kaggle here:

* https://www.kaggle.com/datasets/oislen/random-telecom-data

## Docker Image

The latests image can be found on dockerhub here:
* https://hub.docker.com/repository/docker/oislen/randomtelecompayments/general
