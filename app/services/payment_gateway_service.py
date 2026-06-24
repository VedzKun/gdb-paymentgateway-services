import asyncio
import uuid
import random
from app.models.payment import PaymentRequest, PaymentResponse

class PaymentGatewayService:
    
    async def process_payment(self, request: PaymentRequest) -> PaymentResponse:
        # Simulate network latency (100ms - 500ms)
        await asyncio.sleep(random.uniform(0.1, 0.5))
        
        # 1. Basic Validation Logic
        if request.amount <= 0:
             return PaymentResponse(
                success=False,
                transaction_id=request.reference_id or str(uuid.uuid4()),
                message="Invalid Amount: Must be greater than zero",
                gateway_ref_id=str(uuid.uuid4())
            )
            
        if request.source_account_id == request.destination_account_id:
             return PaymentResponse(
                success=False,
                transaction_id=request.reference_id or str(uuid.uuid4()),
                message="Invalid Transaction: Source and Destination cannot be same",
                gateway_ref_id=str(uuid.uuid4())
            )

        # 2. Simulate Random Network Failures (1% chance)
        # In a real scenario, this would check against blacklists, fraud detection, etc.
        if random.random() < 0.01:
             return PaymentResponse(
                success=False,
                transaction_id=request.reference_id or str(uuid.uuid4()),
                message="Gateway Error: Network Timeout",
                gateway_ref_id=str(uuid.uuid4())
            )
            
        # 3. Success
        return PaymentResponse(
            success=True,
            transaction_id=request.reference_id or str(uuid.uuid4()),
            message="Payment Processed Successfully",
            gateway_ref_id=str(uuid.uuid4())
        )

payment_service = PaymentGatewayService()
