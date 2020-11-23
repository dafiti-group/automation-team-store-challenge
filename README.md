## Sumary
- [About](https://github.com/MartinsBruno/automation-team-store-challenge/blob/main/README.md#about) 
  - [Overview](https://github.com/MartinsBruno/automation-team-store-challenge/blob/main/README.md#overview)
  - [Description](https://github.com/MartinsBruno/automation-team-store-challenge/blob/main/README.md#description)
- [Requirements](https://github.com/MartinsBruno/automation-team-store-challenge/blob/main/README.md#requirements)

## About
### Overview 
This project aims to participate in the selection process of the company Dafiti

### Description
The design goal is to have a backend with tools to help deliver an API and a frontend that consumes this API.

## Requirements
- Python 3.8.x installed.
- Pip3 20.x installed.

---

## Installation
- Clone this repository:
```bash
$ git clone https://github.com/dafiti-group/automation-team-store-challenge
```
- Use the main directory:
```bash
$ cd automation-team-store-challenge/
```
- Install all requirements to this project
```bash
$ pip install -r requirements.txt
```
- Export the flask variable to use the main app.py file of the project
```bash
$ export FLASK_APP=store/app.py
```
- Create the database using a command created internally in flask
```bash
$ flask create-database
```
- Run the application! (Specify the door if necessary. The default will be :5000)
```bash
$ flask run --port 8000
```
- Access the application in localhost:()