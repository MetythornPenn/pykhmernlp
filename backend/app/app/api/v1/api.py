from fastapi import APIRouter
from app.api.v1.endpoints import (
    address
)

api_router = APIRouter()
api_router.include_router(address.router, prefix="/address", tags=["address"])
