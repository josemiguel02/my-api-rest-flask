# API REST with Flask, SQLAlchemy and SQLite <img src='https://emojis.slackmojis.com/emojis/images/1643514075/314/flask.png?1643514075' height='30'>

## Table of Content

- [About The Project](#about-the-project)
  - [Description](#description)
  - [Built With](#built-with)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contact](#contact)

## About The Project

![Demo](demo/api-demo.jpg)

## Description

This basic project is a Rest API developed with the Python Flask framework, which also uses an SQLite database that stores tasks and uses the SQLAlchemy ORM.

## Built With

[![flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)

[![sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org)

<a href='https://www.sqlalchemy.org'>
  <img src='https://hakin9.org/wp-content/uploads/2019/08/connect-a-flask-app-to-a-mysql-database-with-sqlalchemy-and-pymysql.jpg' height='37'>
</a>

## Installation

1. Clone the repo and change "my-project" to your project name.

```sh
  git clone https://github.com/josemiguel02/my-api-rest-flask.git ./my-project
```

2. Go to the project directory

```sh
  cd my-project
```

3. Install dependencies

```sh
  pip install -r requirements.txt
```

## Usage

Start the server

```sh
  python app.py
```

Running on: http://localhost:5000

# API Reference

### Get all tasks

```http
  GET /todos
```

### Create task

```http
  POST /create
```

### Get single task

```http
  GET /todo/<id>
```

| Parameter | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `id`      | `string` | **Required**. ID of task |

### Edit task

```http
  PUT /edit/<id>
```

| Parameter | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `id`      | `string` | **Required**. ID of task |

### Delete task

```http
  DELETE /delete/<id>
```

| Parameter | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `id`      | `string` | **Required**. ID of task |

## Contact

- Gmail - [josemidev24@gmail.com](mailto:josemidev24@gmail.com)
- Instagram - [@jmdp.02](https://www.instagram.com/jmdp.02)
