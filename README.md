# Web Programming with Python - a Tutor Company Project

### Demo of application working:
 https://youtu.be/6mLSpm-u69c

 ![Title](./planning/LOVE%20LEARNING%20PRESENTATION/1.jpg)

This project is designed to consolidate learning from weeks 1 - 4 on the CodeClan Software Development Course. It involves designing and building an app that focuses on the following objectives:

* Object oriented programming with Python
* Test Driven Development
* Web Programming (REST, MVC)
* Interacting with a PostgreSQL database (CRUD)

## The technologies used

The app is built using the following technologies (as per the brief): 

* HTML / CSS - for front-end design and styling
* Python - for back-end development
* Flask - a Python web framework
* PostgreSQL and the psycopg - for interacting with a PostgreSQL database

## Setting Up the Project

To set up the project on your local machine, follow these steps:

1. Create a new PostgreSQL database by running the following command in your terminal:
```bash
createdb love_learning
```

2. Run the SQL file db/love_learning.sql to set up the necessary tables in the database. You can do this by running the following command:
```bash
psql -d love_learning -f db/love_learning.sql
```

3. Run the console.py file to execute the console program. Use the following command:
```bash
python3 console.py
```

## Running the App

To run the web application, execute the following command in your terminal:
```bash
flask run 
```

After running the command, open your Chrome browser and navigate to http://localhost:4999/ to view the app.

![homepage](/planning/homepage_screenshot.png)

## Sitemap

![sitemap](/Planning/user_sitemap_tutor_company.png)






