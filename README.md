# Django + Vue Demo

This project separates a Vue-based front end from a Django back end.
The back end exposes API endpoints that serve profile and blog data
stored in a SQLite database. The front end fetches this data and
renders the Home and Blog pages using Vue Router.

## Database Structure

| Table       | Fields                                                     |
|-------------|-------------------------------------------------------------|
| `Profile`   | `name`, `introduction`, `contact`, `work_experience`        |
| `BlogPost`  | `title`, `body`, `created_at`                               |

Run `python backend/manage.py makemigrations` and `python backend/manage.py migrate`
to create the database.

## Running

1. Start the Django development server:
   `python backend/manage.py runserver`
2. Open `frontend/index.html` in a browser to load the Vue app.
   The app calls `/api/profile/` and `/api/blog/` to retrieve data.

## Formatting

`npx prettier --check frontend/index.html frontend/app.js frontend/style.css`
