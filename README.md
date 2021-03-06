# Luki API :purple_square:
<img width="374" alt="luki" src="https://user-images.githubusercontent.com/65993425/112252659-881cc000-8c2b-11eb-9bb0-b2a266e5dac0.png" style="border-radius: 15%;"/>  

[Link to Luki front-end repository :link:](https://github.com/I7RANK/Luki)

##### _goes were you go_
This repo contains the main code for the Luki API ready to run in localhost and you can test the API in the section **Endpoints**
​
## How to run in localhost :computer:
##### Please see the **requirements.txt** file and install the necessary dependencies
First before to clone go to the API folder and export the application using:
```
export FLASK_APP=application
```
​
Before you can run the API you would create a database and set to **RDS_DB_NAME** variable:
​
Run the next command changing the varible values:
```
RDS_USERNAME=<your_mysql_username> RDS_PASSWORD=<your_mysql_password> RDS_HOSTNAME=localhost RDS_PORT=5000 RDS_DB_NAME=<your_mysql_DB_NAME> flask run
```
​
## Endpoints :dart:
Here is all the end points that you can use with the luki app:
this is the API deployed URL:
```
http://luki-env-1.eba-2zc72njp.us-east-2.elasticbeanstalk.com
```
​
| HTTP Method | Endpoint | Description |
| ------ | ------ | ------ |
| GET | /api/v1.0/ | Return the status of the API to check that it works. |
| GET | /api/v1.0/rents/ | Returns the apartments’ available for rent, based on the current location, a format is made to filter the closest places. |
| GET | /api/v1.0/landlord/[id] | Returns the landlord’s information by its ID, in case that a rent is clicked. |
| GET | /api/v1.0/rents/ | Create a new apartment for rent. |
| GET | /api/v1.0/landlord/ | Create a new landlord to post a new offer. |
​
## Colaborators :busts_in_silhouette:
Lilibeth Tabares - [Github](https://github.com/LiliTa1762) / [Twitter](https://twitter.com/LilibethTabares)  / [Linkedin](https://www.linkedin.com/in/lilibeth-tabares/)  
Mauricio Contreras - [Github](https://github.com/mauroxcf) / [Twitter](https://twitter.com/MauroJCF)  / [Linkedin](https://www.linkedin.com/in/mauricio-contrerasf/)  
Francisco Guzmán - [Github](https://github.com/I7RANK) / [Twitter](https://twitter.com/I7RANKI)  / [Linkedin](https://www.linkedin.com/in/francisco-guzman-herrera/)  
Jose Parrales - [Github](https://github.com/JParrales) / [Twitter](https://twitter.com/JParrales7)  / [Linkedin](https://www.linkedin.com/in/jparrales/) 
