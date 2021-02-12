# Microservices-Web-App

## Basic idea of the project
The basic idea of this project is to show how various microservices, each independent of each other, communicate among themselves. There are three microservices: User, Product and Like. These microservices are independent of each other, are built on different frameworks and yet are still able to communicate with each other using the messaging service - RabbitMQ.

## Requirements
Python == 3.9.1
Django == 3.1.4
Flask == 1.1.2
MySQL == 5.7.32
Postman == 7.36.1
Docker

## Details about the microservices
It is a backend web application which consists of three microservices.

#### User microservice
This microservice is built on the Django framework. It is concerned with storing, processing and retrieving information related to users. To store the information of the users, it uses a MySQL database called User. All the CRUD operations related to the users are performed by this microservice. 

#### Product microservice
This microservice is built on the Django framework. It is concerned with storing, processing and retrieving information related to products. To store the information of the products, it uses a MySQL database called Product. All the CRUD operations related to the products are performed by this microservice.

#### Likes microservice
This microservice is built on the Flask framework and is concerned with incrementing the likes on a product by a user. This microservice communicates with the Product and the User app to update the information in their respective databases.

## API Description

#### User microservice
There are 6 APIs made in this app:
Get list: It lists all the users available in the database.
Create a user: It creates a new user and feeds this information to the database.
Retrieve user using id: It fetches the user corresponding to the given user id
Update user: It updates the information of the user corresponding to the given user id.
Delete user: It deletes the specified user id from the database.
Get random user: It generates the user id of any random user.

#### Product microservice
There are 6 APIs made in this app:
Get list: It lists all the products available in the database.
Create a product: It creates a new product and feeds this information to the database.
Retrieve product using id: It fetches the product corresponding to the given product id.
Update product: It updates the information of the product corresponding to the given product id.
Delete product: It deletes the specified product id from the database.
Get random product: It generates the product id of any random product.

#### Likes microservice
This app has one API called - create likes. This generates a random user id and random product id and increases the likes count corresponding to this user and product. This API communicates with the user and product microservice via RabbitMQ.

## Screenshots

#### 1. Create user API
  ![Create User](https://github.com/jainkashish/Microservices-Web-App/blob/main/screenshots/Image%20create%20user.jpeg)
  
#### 2. Create product API
  ![Create Product](https://github.com/jainkashish/Microservices-Web-App/blob/main/screenshots/Image%20create%20product.jpeg)

#### 3. Create likes API
  ![Create Likes](https://github.com/jainkashish/Microservices-Web-App/blob/main/screenshots/Image%20create%20likes.jpeg)

#### 4. Retrieve product using id API
Increased likes count on product id 9
  ![Retrive Product](https://github.com/jainkashish/Microservices-Web-App/blob/main/screenshots/Image%20retrive%20product.jpeg)



#### 5. Retrieve user id API
Increased likes count on user id 6
  ![Retrive User](https://github.com/jainkashish/Microservices-Web-App/blob/main/screenshots/Image%20retrieve%20user.jpeg)


