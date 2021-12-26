# Testing document

The application has been tested both through automatic unitest testing and manual tests.

The manual tests include testing all functionalities mentioned in the Requirements Specifications document, both with valid and invalid inputs.

### Test coverage

The coverage (excluding the UI) is above 90%.

## Error messages

The application displays an error message when:
- Inserted user credentials are invalid because user already exists
- Inserted user credentials are invalid because username or password is incorrect
- Inserted sum is not an integer or decimal

The application does not show error messages when:
- SQLite database has not been created because the command "run invoke build" has not been run
