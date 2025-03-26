from pydantic import BaseModel, Field
from typing import List, Dict, Any
from datetime import datetime


class SalesOffer(BaseModel):
    """Individual sales offer for a customer"""

    customer_id: str = Field(..., description="Customer ID from Airtable")
    customer_name: str = Field(..., description="Customer name")
    customer_email: str = Field(..., description="Customer email address")
    offer_title: str = Field(..., description="Title of the personalized offer")
    offer_description: str = Field(..., description="Detailed description of the offer")
    discount_percentage: float = Field(..., description="Discount percentage (0-100)")
    recommended_products: List[str] = Field(
        ..., description="List of recommended product names"
    )
    valid_until: datetime = Field(..., description="Offer expiration date")
    personal_message: str = Field(
        ..., description="Personalized message for the customer"
    )
    offer_code: str = Field(..., description="Unique code for this offer")
    reason: str = Field(..., description="Reasoning behind this offer selection")


class SalesOfferCollection(BaseModel):
    """Collection of sales offers for multiple customers"""

    offers: List[SalesOffer] = Field(
        ..., description="List of personalized sales offers"
    )
    generated_at: datetime = Field(
        default_factory=datetime.now, description="When these offers were generated"
    )
    total_customers: int = Field(..., description="Total number of customers processed")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata about this batch of offers",
    )
