from typing import Any
import os
import httpx
from fastapi import FastAPI, HTTPException, status


app = FastAPI(title="Ninjahire API")


SECONDARY_SERVICE_BASE_URL = os.getenv("SECONDARY_SERVICE_BASE_URL")


@app.get("/", summary="Welcome message")
async def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Ninjahire API"}


@app.get("/health", summary="Health check")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/secondary-health", summary="Secondary service health check")
async def secondary_health() -> dict[str, Any]:
    if not SECONDARY_SERVICE_BASE_URL:
        # If the URL is not configured, we consider it a server configuration error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="SECONDARY_SERVICE_BASE_URL environment variable not set"
        )
    
    target_url = f"{SECONDARY_SERVICE_BASE_URL.strip('/')}/health"
    
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(target_url)  
            
        if response.status_code == 200:
            return {"status": "secondary service ok", "secondary_response": response.json() if response.headers.get("content-type") == "application/json" else response.text}
        else:
             raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=f"Secondary service returned status {response.status_code}"
            )

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Secondary service unreachable: {str(exc)}"
        )

