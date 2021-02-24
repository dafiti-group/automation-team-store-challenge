# Automation Team - Programming Challenge

---

## Quickstart

### Running with Docker


### Running with Anaconda Navigator

If you DON'T have Anaconda Navigator installed in your computer, go to step 2:

1. Creating a virtual environment and activating it:
  - Open Anaconda Prompt and create the virtual environment to manage versions:
    ```
    conda create --name venv
    ```
    ```
    conda activate venv
    ```

2. Setting up the application:
  - Installing necessary setup
    ```
    pip install -r requirements.txt
    ```
    - Migrating the database
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```

3. Running the application:
    ```
    python manage.py runserver
    ```

## Instructions

- Fork this repository into your personal github account. All the work must be done on your personal forked repository. We will trust you to our hearts not to take "inspiration" from other available forks. ;)

- Create a branch from `master` (e.g. `develop`) and do all of your magic on this created branch ;)

- Code (and document) up

- When finished, create a Pull Request from the created branch to master

- Send an email to us with the Pull Request link on your personal forked repository - NOT on this repository. That way we can request access to review it and provide you feedback.

---

## The Challenge

- As a business requirement, choose a fashion-related resource. E.g. shoes, pants, shirts, etc...

- Create a RESTful JSON API to expose CRUD (Create/Retrieve/Update/Delete) operations on this resource.

- Create an endpoint to populate data into the model/table using a CSV file. One of the fields of the model/table must have its' value calculated based on 1 or more of the other ones.

- Create a frontend that has a list of all resources. It must consume the backend API endpoint that lists the resources.

- Provide a way for us to run your application locally with all of its' requirements (python and infrastructure-wide)

---

## What will be taken into account

- Your understanding and conformity to the requirements (sections "Instructions" and "The Challenge" above).

- Your development workflow

- How you architecture the solution using python

- Data sanitization and validation

- API documentation

- Project documentation: the fashion-related resource you chose, how you structured the project and instructions to run your solution locally on an Ubuntu 18.04+ machine (backend and frontend). Feel free to add any other relevant information.

- Automated tests

- Code consistency (through automated formatters, linters, etc...)

---

## **You will stand out from the crowd if**:

- You handle the documentation with love and care (attention to details is a HUGE seller here)

- The frontend consumes ALL the backend API endpoints of the resource, and even more if it provides ways to search for contents.

- You use Docker - so we can run your application locally.

- If you deploy the application somewhere remotely where we can interact with it (although we will still try to run it locally ;).

---

## Frameworks, databases and other tooling

In our team we architecture applications with microservices in mind. All new applications (and nowadays the majority of them) are developed on python 3.8+, django or flask, postgres as the database, redis as cache and celery/rabbitmq when we need to deal with processing/flows too long to finish on a request-response cycle. We package our applications as docker images and deploy with kubernetes using helm charts. But feel free to use frameworks, databases and tooling your are the most familiar with.
