# Luki API
##### _goes were you go_
This repo contains the main code for the Luki API ready to run in localhost and you can test the API in the section **Endpoints**
​
## How to run in localhost ��
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
## Endpoints ��
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
## Colaborators ��
[Lilibeth Tabares](https://github.com/LiliTa1762)
[Mauricio Contreras](https://github.com/mauroxcf)
[Jose Parrales](https://github.com/JParrales)

