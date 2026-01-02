# Ninjahire API

Sample FastAPI service called **Ninjahire API**, packaged for local development and Docker use.

## Local development
- Create a virtual environment (for example, `python -m venv .venv` and activate it).
- Install dependencies: `pip install -r requirements.txt`.
- Run the server: `export SECONDARY_SERVICE_BASE_URL=http://localhost:8001 && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`.
- Open `http://127.0.0.1:8000` for the welcome message, `/health` for a simple check, or `/secondary-health` to check the upstream service.

## Configuration
The application requires the following environment variables:
- `SECONDARY_SERVICE_BASE_URL`: The base URL of the secondary service (e.g., `http://secondary-service:8001`).

## Docker
- Build the image: `docker build -t ninjahire-api .`
- Run the container: `docker run --rm -p 8000:8000 -e SECONDARY_SERVICE_BASE_URL="http://host.docker.internal:8001" ninjahire-api`
- Visit `http://127.0.0.1:8000` to verify the API is running.
