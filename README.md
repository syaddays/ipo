# IPO Web Application

A Django-based web application for tracking and managing Initial Public Offerings (IPOs).

## Features

- Track upcoming, open, closed, and listed IPOs
- Detailed IPO information including price bands, issue sizes, and important dates
- RESTful API for programmatic access
- Admin interface for managing IPO data
- Responsive Bootstrap-based UI

## Tech Stack

- Backend: Django 5.0.6
- API: Django REST Framework 3.16.0
- Frontend: Bootstrap 5
- Database: SQLite

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ipo-web-app.git
cd ipo-web-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
python -m pip install django==5.0.6 djangorestframework==3.16.0 django-cleanup==9.0.0
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Load sample data:
```bash
python manage.py load_sample_ipos
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

- `/api/ipos/` - List all IPOs (GET) or create new IPO (POST)
- `/api/ipos/{id}/` - Retrieve, update, or delete specific IPO
- `/admin/` - Admin interface
- `/` - Main web interface

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 