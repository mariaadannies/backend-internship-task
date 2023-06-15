# Setup Instructions

1. Clone the repository:
```
git clone https://github.com/mariaadannies/backend-internship-task.git  

cd backend-internship-task
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

# Test Suite

To run the test suite, use the following command:
```
python manage.py test
```

# API Server

To start the API server, follow these steps:

1. Apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```


2. Run the development server:
```
python manage.py runserver
```
The API server will now be accessible at `http://localhost:8000`.

## API Documentation

The API documentation and endpoints are as follows:

- Register a new user:  
Endpoint: `POST /api/register/`

- Obtain an access token:  
Endpoint: `POST /api/token/`

- Refresh an access token:  
Endpoint: `POST /api/token/refresh/`

- Retrieve a list of entries for the authenticated user:  
Endpoint: `GET /api/entries/`

- Create a new entry for the authenticated user:
- Endpoint: `POST /api/entries/`

- Retrieve details of a specific entry:  
Endpoint: `GET /api/entries/<id>/`

- Update details of a specific entry:  
Endpoint: `PUT /api/entries/<id>/`

- Delete a specific entry:  
Endpoint: `DELETE /api/entries/<id>/`