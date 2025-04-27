from fastapi import APIRouter, HTTPException

from app.crud import get_address, write_data
from app.logger import logger
from app.schemas import WriteDataRequest

router = APIRouter()


@router.post("/write_data", status_code=201)
async def write_data_endpoint(data: WriteDataRequest):
    """
    Save or update phone and address in Redis.
    """
    try:
        operation = await write_data(data.phone, data.address)
    except Exception as e:
        logger.error(f"Error writing data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    if operation == "created":
        return {"message": "Data created successfully"}
    elif operation == "updated":
        return {"message": "Data updated successfully"}


@router.get("/check_data")
async def check_data(phone: str):
    """
    Retrieve address by phone number.
    """
    try:
        address = await get_address(phone)
        if address is None:
            raise HTTPException(status_code=404, detail="Phone number not found")
    except Exception as e:
        logger.error(f"Error getting data for phone: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return {"phone": phone, "address": address}
