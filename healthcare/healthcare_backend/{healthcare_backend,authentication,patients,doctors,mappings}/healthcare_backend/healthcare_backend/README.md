# Healthcare Backend — Django REST API

A secure backend system for managing patients, doctors, and their mappings, built with Django, DRF, JWT, and PostgreSQL.

---

## Tech Stack
- **Django 4.2** + **Django REST Framework**
- **PostgreSQL** (database)
- **djangorestframework-simplejwt** (JWT authentication)
- **django-cors-headers**
- **python-dotenv**

---

## Project Structure

```
healthcare_backend/
├── manage.py
├── requirements.txt
├── .env.example
├── healthcare_backend/       # Core config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── authentication/           # Register & Login
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── patients/                 # Patient CRUD
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── doctors/                  # Doctor CRUD
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
└── mappings/                 # Patient-Doctor assignment
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── admin.py
```

---

## Setup Instructions

### 1. Clone & create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment variables
```bash
cp .env.example .env
# Edit .env and fill in your DB credentials and SECRET_KEY
```

### 3. Create PostgreSQL database
```sql
CREATE DATABASE healthcare_db;
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional, for admin panel)
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

---

## API Reference

All protected endpoints require the header:
```
Authorization: Bearer <access_token>
```

---

### Authentication

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register/` | ❌ | Register a new user |
| POST | `/api/auth/login/` | ❌ | Login and get JWT tokens |
| POST | `/api/auth/token/refresh/` | ❌ | Refresh access token |

**Register — Request Body:**
```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "securepass123"
}
```

**Login — Request Body:**
```json
{
  "email": "john@example.com",
  "password": "securepass123"
}
```

**Login — Response:**
```json
{
  "message": "Login successful.",
  "user": { "id": 1, "username": "john", "email": "john@example.com" },
  "tokens": {
    "access": "<access_token>",
    "refresh": "<refresh_token>"
  }
}
```

---

### Patients

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/patients/` | ✅ | Create a patient |
| GET | `/api/patients/` | ✅ | List my patients |
| GET | `/api/patients/<id>/` | ✅ | Get patient details |
| PUT | `/api/patients/<id>/` | ✅ | Full update |
| PATCH | `/api/patients/<id>/` | ✅ | Partial update |
| DELETE | `/api/patients/<id>/` | ✅ | Delete patient |

**Patient fields:** `name`, `age`, `gender` (M/F/O), `contact_number`, `address`, `medical_history`

---

### Doctors

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/doctors/` | ✅ | Create a doctor |
| GET | `/api/doctors/` | ✅ | List all doctors |
| GET | `/api/doctors/<id>/` | ✅ | Get doctor details |
| PUT | `/api/doctors/<id>/` | ✅ | Full update |
| PATCH | `/api/doctors/<id>/` | ✅ | Partial update |
| DELETE | `/api/doctors/<id>/` | ✅ | Delete doctor |

**Doctor fields:** `name`, `specialization`, `contact_number`, `email`, `experience_years`

---

### Patient-Doctor Mappings

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/mappings/` | ✅ | Assign a doctor to a patient |
| GET | `/api/mappings/` | ✅ | List all mappings |
| GET | `/api/mappings/<patient_id>/` | ✅ | Get doctors for a patient |
| DELETE | `/api/mappings/delete/<id>/` | ✅ | Remove a mapping |

**Mapping — Request Body:**
```json
{
  "patient": 1,
  "doctor": 2,
  "notes": "Primary care physician"
}
```

---

## Notes
- Patients are **user-scoped** — each authenticated user only sees their own patients.
- Doctors are **global** — visible to all authenticated users.
- Duplicate patient-doctor assignments are rejected with a validation error.
- Access tokens expire in **1 hour**; refresh tokens in **7 days**.
