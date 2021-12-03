# Budget app

The application is a tool for butgeting, where the users can track montly spendigs. The user can set a monthly budget, add expences as different categories (e.g. groceries, clothes etc.) and track their monthly spendings.

## Documentation

- [Requirements specifiction](documentation/RequirementsSpecifications.md)
- [Hours worked](documentation/tuntikirjanpito.md)
- [Architecture](documentation/architecture.md)

## Installation

1. Install dependencies:

```bash
poetry install
```

2. Start application:

```bash
poetry run invoke start
```

## Testing

Run tests:

```bash
poetry run invoke test
```

### Test coverage

Generate test coverage report:

```bash
poetry run invoke coverage-report
```



