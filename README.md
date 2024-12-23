# Simplified Airline Booking System API

This project is a Django REST Framework-based API for managing flights and passengers in a simplified airline booking system.

---

## Features

- Manage **Flights**: Create, Retrieve, Update, and Delete flights.
- Manage **Passengers**: Perform CRUD operations for passengers and associate them with flights.
- Filtering capabilities:
  - Filter flights by `origin` and `destination`.
  - Filter passengers by `flight_number`.
- Pagination for efficient data handling in APIs.

---

## Prerequisites

1. **Python 3.8+** installed.
2. **pip**, Python's package manager.
3. A virtual environment tool like `venv` (recommended).

---

## Installation Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/BenjaminMbuthi/Group-7-AirlineBookingSystem.git
```

### Step 2: Set Up the Virtual Environment

Create and activate a virtual environment to isolate the project dependencies:

```bash
# Create virtual environment
python -m venv env

# Activate the virtual environment
# On Windows:
.\env\Scripts\Activate


### Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations

Set up the database by applying migrations:

```bash
python manage.py migrate
```

### Step 5: Start the Development Server

Run the local development server:

```bash
python manage.py runserver
```

### Step 6: Access the API

- API Base URL: `http://127.0.0.1:8000/api/`
- Django Admin: `http://127.0.0.1:8000/admin/`

---

## API Endpoints

### Flights

- **List all flights**: `GET /api/flights/`
- **Retrieve a single flight**: `GET /api/flights/<id>/`
- **Create a new flight**: `POST /api/flights/`
- **Update a flight**: `PUT /api/flights/<id>/`
- **Delete a flight**: `DELETE /api/flights/<id>/`

### Passengers

- **List all passengers**: `GET /api/passengers/`
- **Retrieve a single passenger**: `GET /api/passengers/<id>/`
- **Create a new passenger**: `POST /api/passengers/`
- **Update a passenger**: `PUT /api/passengers/<id>/`
- **Delete a passenger**: `DELETE /api/passengers/<id>/`

### Filtering

- **Filter flights**: Search by `origin` or `destination`:
  ```
  GET /api/flights/?search=<query>
  ```
- **Filter passengers**: Search by `flight_number`:
  ```
  GET /api/passengers/?search=<flight_number>
  ```

---

## Project Structure

```
project/
├── bookings/
│   ├── migrations/         # Database migrations
│   ├── models.py           # Flight and Passenger models
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API views and viewsets
│   ├── urls.py             # API routing
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── settings.py             # Project settings
```

---

## Future Enhancements

- Add user authentication and permissions.
- Implement advanced filtering (e.g., by flight date).
- Improve test coverage with unit tests for all endpoints.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Contributors
151664 Mbuthi Benjamin
150344 Naibei Timothy
152439 Kaguai Daniel
151115 Odhiambo Tyrone

---

For any questions or suggestions, please feel free to create an issue or contact the repository owner.

