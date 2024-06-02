# vk_EY_assessment

1. Project Setup
First, create a directory structure for the project:

fastapi_mvc_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── request_response.py
│   ├── views/
│   │   ├── __init__.py
│   │   └── addition.py
│   └── controllers/
│       ├── __init__.py
│       └── addition_controller.py
├── tests/
│   ├── __init__.py
│   ├── test_addition.py
├── requirements.txt
└── README.md

2. Install Dependencies
Create a requirements.txt file with the following content:
fastapi
uvicorn
pydantic
pytest

Install the dependencies: ’pip install -r requirements.txt’ in bash

3. Create Pydantic Models
Create app/models/request_response.py

4. Implement the Controller Logic
Create app/controllers/addition_controller.py

5. Create the FastAPI View
Create app/views/addition.py

6. Setup the Main Application
Create app/main.py

7. Running the Application
Create an entry point to run the server run the below command in bash:
>uvicorn app.main:app –reload

8. Writing Unit Tests
Create tests/test_addition.py

9. Running the Tests
Run the tests using pytest, run this command in bash
>pytest tests/

10. Logging Setup
Add logging configuration in app/main.py
