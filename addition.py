from fastapi import APIRouter, HTTPException
from app.models.request_response import AdditionRequest, AdditionResponse
from app.controllers.addition_controller.py import process_addition

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    response_data = process_addition(request.batchid, request.payload)
    if response_data['status'] == 'error':
        raise HTTPException(status_code=500, detail="Error processing request")
    return response_data
