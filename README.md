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

- Python 3.10+
- An Airtable account with customer data
- Airtable API key
- Brave Search API key
- OpenAI API key

### Installation

1. Clone this repository
2. Install dependencies:

```bash
crewai install
```

3. Set up environment variables:

```bash
export MODEL="openai/gpt-4o-mini"
export AIRTABLE_API_KEY="your_airtable_api_key"
export AIRTABLE_BASE_ID="your_airtable_base_id"
export AIRTABLE_TABLE_NAME="your_table_name"
export BRAVE_API_KEY="your_brave_api_key"
export OPENAI_API_KEY="your_openai_api_key"
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
crewai run
```

## Crew Structure

### Agents

1. **Data Analyst**: Extracts and organizes customer data from Airtable
2. **Customer Profiler**: Creates detailed customer profiles based on data
3. **Offer Creator**: Generates personalized offers based on customer profiles
4. **Offer Formatter**: Formats offers into structured data for API integration

### Tools

1. **Brave Search Tool**: Searches the web
2. **Airtable Tool**: Fetches customer data from Airtable

## Output Format

The system generates a structured JSON output conforming to the `SalesOfferCollection` model, which contains:

- A list of personalized sales offers
- Timestamp of generation
- Total number of customers processed
- Additional metadata

## License

MIT

## Contributors

- https://github.com/tobiaswu
