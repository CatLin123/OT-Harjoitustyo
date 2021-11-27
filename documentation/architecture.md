# Architecture description

## Structure

The application architechture follows this structure:

INSERT

UI: Handles user interface
Services: Handles application logic
Respositories: Handles data
Entities: Classes managing information used in the application.

## User interface

The user interface will consist of three views:

- Login view
- User creation view
- Spendings/budget management view

## Application logic

The logical data models consist of the classes User, Category and CategoryList

INSERT


## Main functionalities

The main application functionalities are illustrated below.

### User login

When the user inserts their username and a password to the displayed text fields and clicks _Log in_, the application proceeds as follows:

INSERT

### User creation

When the user inserts a username that is not yet in use and a valid password and clicks "Create", the application runs as follows:

INSERT

### Managing and creating spendings

When the user chooses a category and inserts a decimal number representing a spending (e.g. 4.5 euros spent on the category groceries) the application runs as follows:

INSERT
