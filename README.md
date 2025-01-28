# Contract Sign Gateway

https://www.conventionalcommits.org/en/v1.0.0/

## Description

This project was developed as a microservice for signature management,
supporting multiple signature providers. Initially, it uses **Clicksign**
as the primary gateway (the only one implemented so far),
but the architecture allows for the quick integration of additional gateways.

---

## Preparing the Environment

1. Navigate to the `main.py` file.
2. Uncomment the section responsible for database creation.
3. Run the project to create the database tables.
4. After the database is created, comment the section again.

- `pre-commit install`
- `pre-commit install --hook-type pre-push`
- `pre-commit install --hook-type commit-msg`

---

## Starting the Project

1. In your terminal, build the project with the following command:
    make build
2. Before following command:
    make up

---

## Swagger Documentation
To access the API documentation via Swagger, open your browser and go to:
- URL: http://localhost:8000/docs

---

## Commit Guidelines

Before committing changes, follow these steps to ensure the code adheres to the project standards:

1. List files that do not follow PEP8 standards:
    flake8 .
2. Format files automatically:
    black .
3. After ensuring all files comply with the standards, proceed with your commit:
    git add .
    git commit -m "Your commit message here"

---
