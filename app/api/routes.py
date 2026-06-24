from fastapi import APIRouter, HTTPException, Depends
from app.models.payment import PaymentRequest, PaymentResponse
from app.services.payment_gateway_service import PaymentGatewayService
from app.dependencies.providers import get_payment_gateway_service

router = APIRouter()

@router.post("/process", response_model=PaymentResponse)
async def process_payment(
    request: PaymentRequest,
    service: PaymentGatewayService = Depends(get_payment_gateway_service)
):
    """
    Process a payment through the Central Payment Gateway.
    Acts as a 2nd level validation for reliability.
    """
    try:
        response = await service.process_payment(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
