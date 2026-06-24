from fastapi import FastAPI
from app.api.routes import router as payment_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Simulated Third-Party Payment Gateway for GDB Ecosystem",
    version=settings.APP_VERSION
)

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(payment_router, prefix="/api/v1/payment", tags=["Payment Gateway"])

@app.get("/health")
def health_check():
    return {"status": "active", "service": settings.APP_NAME}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
