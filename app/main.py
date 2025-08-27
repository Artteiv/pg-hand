from fastapi import FastAPI
from app.api.endpoints import example
from app.api.v1.health import router as health_router
from app.database.db import Base, engine

app = FastAPI()

# Include routers
app.include_router(example.router, prefix="/api/v1")
app.include_router(health_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Create database tables
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
