# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Run Application**: `python app.py` (starts the Flask server on port 5001)
- **Install Dependencies**: `pip install -r requirements.txt`
- **Run Tests**: `pytest`
- **Run a Single Test**: `pytest path/to/test_file.py`

## Architecture Overview

This is a Flask-based web application for an Expense Tracker, currently structured as a project skeleton.

### Project Structure
- `app.py`: Main entry point. Contains application configuration and route definitions.
- `database/`: Handles data persistence.
    - `db.py`: Intended for database connection logic (`get_db`), schema initialization (`init_db`), and seeding (`seed_db`).
- `static/`: Stores frontend assets.
    - `css/`: Stylesheets.
    - `js/`: Client-side JavaScript.
- `templates/`: Contains Jinja2 HTML templates for the user interface.

### Key Design Patterns
- **Routing**: Centralized in `app.py` using Flask decorators.
- **Templates**: Uses a base template (`base.html`) and specific page templates for consistent layout.
- **Database**: Designed to use SQLite for simplicity in a student project context.
