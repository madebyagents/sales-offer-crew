from crewai.tools import BaseTool
from typing import Type, List, Optional, Dict, Any
from pydantic import BaseModel, Field
import requests
import os


class AirtableCustomerInput(BaseModel):
    """Input schema for AirtableTool."""

    base_id: Optional[str] = Field(
        None,
        description="Airtable base ID. If not provided, uses environment variable.",
    )
    table_name: Optional[str] = Field(
        None,
        description="Airtable table name. If not provided, uses environment variable.",
    )
    customer_id: Optional[str] = Field(
        None,
        description="Specific customer ID to fetch. If not provided, fetches all customers.",
    )


class AirtableTool(BaseTool):
    name: str = "Airtable Customer Data Tool"
    description: str = (
        "Fetches customer data from Airtable database. Access customer information including "
        "id, Name, Email, Age, Gender, Location, CustomerSince, TotalSpent, LastPurchaseDate, "
        "LastPurchaseAmount, PurchaseFrequency, PreferredCategory, RecentlyViewedItems, LoyaltyTier, "
        "HasSubscription, PaymentMethod, and Tags."
    )
    args_schema: Type[BaseModel] = AirtableCustomerInput

    def _run(
        self,
        base_id: Optional[str] = None,
        table_name: Optional[str] = None,
        customer_id: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Fetch customer data from Airtable.

        Args:
            base_id: Airtable base ID (optional, defaults to env var)
            table_name: Airtable table name (optional, defaults to env var)
            customer_id: Specific customer ID to fetch (optional)

        Returns:
            List of customer records as dictionaries
        """
        # Use environment variables as fallbacks
        base_id = base_id or os.environ.get("AIRTABLE_BASE_ID")
        table_name = table_name or os.environ.get("AIRTABLE_TABLE_NAME")
        api_key = os.environ.get("AIRTABLE_API_KEY")

        if not base_id or not table_name or not api_key:
            raise ValueError(
                "Airtable credentials missing. Set AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, and AIRTABLE_API_KEY environment variables."
            )

        url = f"https://api.airtable.com/v0/{base_id}/{table_name}"

        # Add filter for specific customer if provided
        params = {}
        if customer_id:
            params["filterByFormula"] = f"{{id}}='{customer_id}'"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from Airtable: {response.text}")

        data = response.json().get("records", [])

        # Transform to simplified format
        customers = []
        for record in data:
            customer_data = record.get("fields", {})
            customer_data["id"] = record.get("id")
            customers.append(customer_data)

        return customers
