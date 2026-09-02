# Python Engineering Lab

A foundational Python project demonstrating core software engineering practices: modular architecture, validation, error handling, type hints, and unit testing.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the CLI tool on the sample data:

```bash
python -m src.main --file examples/sample_data.json
```

Options:
- `--sort`: Sort users alphabetically by name.
- `--summary`: Display total count, average age, and city distribution.

## Testing

Run the unit tests:

```bash
python -m unittest discover tests
```

## Architecture

- `models.py`: Defines the User dataclass.
- `validators.py`: Contains email/age/user validation logic.
- `processors.py`: Handles JSON loading, filtering, sorting, and summarization.
- `main.py`: CLI entry point with argument parsing.
