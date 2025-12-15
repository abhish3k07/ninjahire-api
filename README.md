# Ninjahire API

Sample FastAPI service called **Ninjahire API**, packaged for local development and Docker use.

## Local development
- Create a virtual environment (for example, `python -m venv .venv` and activate it).
- Install dependencies: `pip install -r requirements.txt`.
- Run the server: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`.
- Open `http://127.0.0.1:8000` for the welcome message and `/health` for a simple check.

## Docker
- Build the image: `docker build -t ninjahire-api .`
- Run the container: `docker run --rm -p 8000:8000 ninjahire-api`
- Visit `http://127.0.0.1:8000` to verify the API is running.
