# FastAPI Pokemon Project

## Project Structure

```
.
├── app
│   ├── db
│   └── main.py
├── tests
├── requirements.txt
└── run.py
```

## Setup Instructions

1. **Environment Setup**:

   - Create a `.env` file in the root directory with the following content:
     ```
     DATABASE_URL=postgresql+asyncpg://user:password@localhost:port/dbname
     ```
     Replace `user`, `password`, `localhost`, `port`, and `dbname` with your PostgreSQL database credentials.

2. **Python Environment**:
   - Create a Python virtual environment:
     ```
     python3 -m venv env
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       .\env\Scripts\activate
       ```
     - On macOS and Linux:
       ```
       source env/bin/activate
       ```
3. **Install Requirements**:
   - Install project dependencies using pip:
     ```
     pip install -r requirements.txt
     ```

## Running the FastAPI Server

To start the FastAPI server, run:

```
python3 run.py
```

The server will start running locally.

## Running Tests

To run tests using pytest, use the following command:

```
pytest tests/{Test File}
```

Replace `{Test File}` with the name of the specific test file you want to run.

---
