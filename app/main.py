from fastapi import FastAPI


app = FastAPI(title="Ninjahire API")


@app.get("/", summary="Welcome message")
async def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Ninjahire API"}


@app.get("/health", summary="Health check")
async def health() -> dict[str, str]:
    return {"status": "ok"}

