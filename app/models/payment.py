from pydantic.dataclasses import dataclass
from pydantic import Field
from typing import Optional

@dataclass
class PaymentRequest:
    source_account_id: int = Field(..., description="ID of the source account")
    destination_account_id: int = Field(..., description="ID of the destination account")
    amount: float = Field(..., gt=0, description="Amount to transfer")
    mode: str = Field(..., description="Payment mode (NEFT/RTGS/IMPS/UPI)")
    reference_id: Optional[str] = None

@dataclass
class PaymentResponse:
    success: bool
    transaction_id: str
    message: str
    gateway_ref_id: str
