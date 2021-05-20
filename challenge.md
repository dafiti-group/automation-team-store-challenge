# Dafiti Challenge

# Automation Team - Technical Challenge

---

# Greetings

Thank you to take part on this technical challenge! We designed it to be pragmatic, convenient, low friction and to also provide useful value to you - taking into account you have given your best, we will honor your efforts and evaluate your job providing useful, respectful and meaningful feedback - using a code review to do that.

---

# Instructions

You have 2 ways you can show us the best you can do: the first is the freedom for you to choose from your github projects' portfolio. The second is a challenge that we propose, if you feel more inclined to that. Choose the one which is most convenient to you, given your time availability restrictions. No matter the one you choose, the criteria we will use to evaluate will be the same. After you decide which one is the best to you, answer the e-mail telling us what option you will choose and when you will deliver the test to our evaluation (we believe it can be delivered in less than and at maximum 7 days).

## OPTION 1: YOU CHOOSE WHAT TO SHOW US

### Steps

1) Choose an existing project from a github repository of yours. This project must use a python web framework (django, flask, etc...), and provide at least a database. The more tools it provides, e.g. Redis, Celery tasks, etc..., the better for us to evaluate what you're capable to deliver.

2) Write a great README, explaining the problem domain you're solving with the project, its' scope and any useful "business" requirement that must be taken into account.

3) Provide a way for us to run your application locally with all of its' requirements (python and infrastructure-wide). An alternative is to host it somewhere we can interact with the API and frontend. It would be great to document the steps required to that on the README. ;)

4) If you decide to make enhancements to the existing project, that will be awesome. E.g.: requirements updates, fixes to the test suite due to the updates, writing new tests, enhancing existing project documentation... all of that will raise even more our interest. To make it easy for us to track those enhancements, we ask you to open a new branch on the project and create a Pull Request, and to send us the link to it so that we can evaluate.

5) If you opt not to make any enhancement to the existing project, that is also valid - since you follow steps 1 to 3. ;)

### Tips

- Choose the repository wisely - the one you are most technically proud of is a good metric to show us your best work. ;)

- We will trust you to our hearts that the work you deliver is yours, and it reflects the best of you. =D

- You are expected to **be able to explain to us your project problem domain and its' architecture** when you go the video interview. Any code suggestions and doubts we have we will make directly into your code, in a code review format, so that we can have a practical conversation and feedback cycle. So, prepare yourself accordingly. ;)


## OPTION 2: OUR CHALLENGE TO YOU

### Specification

- As a business requirement, choose a fashion-related resource. E.g. shoes, pants, shirts, etc...

- Create a RESTful JSON API to expose CRUD (Create/Retrieve/Update/Delete) operations on this resource.

- Create a frontend to the API. You are free to do that server-side, e.g. with Django Admin, or client side with a frontend framework of your choice.

- Provide a way for us to run your application locally with all of its' requirements (python and infrastructure-wide). An alternative is to host it somewhere we can interact with the API and frontend. It would be great to document the steps required to that on the README. ;)

- Optional requirement: Create an endpoint to populate data into the model/table using a CSV file. One of the fields of the model/table must have its' value calculated based on 1 or more of the other ones.

### Steps

- Fork this repository into your personal github account. All the work must be done on your personal forked repository. We will trust you to our hearts not to take "inspiration" from other available forks. ;)

- Create a branch from `master` (e.g. `develop`) and do all of your magic on this created branch ;)

- Code (and document) up

- When finished, create a Pull Request from the created branch to master

- Send an email to us with the Pull Request link on your personal forked repository - NOT on this repository. That way we can request access to review it and provide you feedback.


---

## What will be evaluated

- Your understanding and conformity to the business specification

- Your development workflow

- How you architecture the solution using python

- Data sanitization and validation

- API documentation

- Project documentation: the business specification, the project structure/architecture, instructions to run your solution locally on an Ubuntu 18.04+ machine - or on a working remote environment it was deployed to. Feel free to add any other relevant information.

- Automated tests

- Code consistency (through automated formatters, linters, etc...)

---

## **You will stand out from the crowd if**:

- You handle the documentation with love and care (attention to details is a HUGE seller here)

- The frontend consumes ALL the backend API endpoints of the resource, and even more if it provides ways to search for contents.

- You use Docker - so we can run your application easily locally.

- If you deploy the application somewhere remotely where we can interact with it (then we won't try to run it locally and dedicate more time to the evaluation process).

---

## Frameworks, databases and other tooling

In our team we architecture applications with microservices in mind. All new applications (and nowadays the majority of them) are developed on python 3.8+, django or flask, postgres as the database, redis as cache and celery/rabbitmq when we need to deal with processing/flows too long to finish on a request-response cycle. We package our applications as docker images and deploy with kubernetes using helm charts. But feel free to use frameworks, databases and tooling you are most familiar with.


