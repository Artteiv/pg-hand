from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.health import router as health_router

# Create test app without database dependencies
app = FastAPI()

# Include only the routers we need for testing
app.include_router(health_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

client = TestClient(app)


def test_read_root():
    """Test the root endpoint returns 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_health_check():
    """Test the health endpoint returns expected JSON."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "pg-hand FastAPI is up"}