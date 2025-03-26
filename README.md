# Sales Offer Crew

A CrewAI-powered system that generates personalized sales offers for customers based on Airtable data.

## Overview

This project uses CrewAI to create a team of AI agents that work together to:

1. Fetch customer data from Airtable
2. Analyze customer profiles
3. Generate personalized sales offers
4. Format offers for API integration

## Setup

### Prerequisites

- Python 3.8+
- An Airtable account with customer data
- Airtable API key

### Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
export AIRTABLE_API_KEY="your_airtable_api_key"
export AIRTABLE_BASE_ID="your_airtable_base_id"
export AIRTABLE_TABLE_NAME="your_table_name"  # defaults to "Customers"
```

### Expected Airtable Structure

Your Airtable should have the following fields:

```
id, Name, Email, Age, Gender, Location, CustomerSince, TotalSpent, 
LastPurchaseDate, LastPurchaseAmount, PurchaseFrequency, PreferredCategory, 
RecentlyViewedItems, LoyaltyTier, HasSubscription, PaymentMethod, Tags
```

## Usage

Run the crew to generate personalized offers:

```bash
python -m src.sales_offer_crew.main
```

The output will be saved to `sales_offers.json` in the project directory.

## Crew Structure

### Agents

1. **Data Analyst**: Extracts and organizes customer data from Airtable
2. **Customer Profiler**: Creates detailed customer profiles based on data
3. **Offer Creator**: Generates personalized offers based on customer profiles
4. **Offer Formatter**: Formats offers into structured data for API integration

### Tools

1. **Airtable Tool**: Fetches customer data from Airtable
2. **Product Recommender**: Suggests relevant products based on customer preferences
3. **Offer Code Generator**: Creates unique offer codes for each customer

## Output Format

The system generates a structured JSON output conforming to the `SalesOfferCollection` model, which contains:

- A list of personalized sales offers
- Timestamp of generation
- Total number of customers processed
- Additional metadata

## License

MIT

## Contributors

- Your Name
