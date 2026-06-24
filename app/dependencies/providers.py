from fastapi import Depends
from app.services.payment_gateway_service import PaymentGatewayService

def get_payment_gateway_service() -> PaymentGatewayService:
    """Provider for PaymentGatewayService."""
    return PaymentGatewayService()
