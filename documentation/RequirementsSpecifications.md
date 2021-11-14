# Requirements specification

## Application purpose

The application is a tool for butgeting, where the users can track montly spendigs. The user can set a monthly budget, add expences as different categories (e.g. groceries, clothes etc.) and track their monthly spendings.

## User interface draft

![](./Images/)

## Basic functionality

### Before logging in

A user can:
- Create a new account by choosing a 
  - User name (any string)
  - Password (must include 4 letters and one number)
- Log in
  - The user is informed if the username does not exist or the password is incorrect
  
### After logging in

Landing page displays:
- Current month
- Total spendings
- Total left 
- Spendings per category
- Settings icon
- Option to add new spendings
  - User chooses a category from a dropdown list and inserts amount in euros

Settings page displays:
- Option to change montly budget
- Option to delete existing categories
- Option to add new category
- Option to delete account

## Additional ideas

Additional ideas include
- Option to request new password
- Visualisation of spendings on landing page
