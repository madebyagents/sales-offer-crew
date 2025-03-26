#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from sales_offer_crew.crew import SalesOfferCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    # Default inputs for testing
    inputs = {
        "current_year": str(datetime.now().year),
        "offer_expiration_days": 30,
        "default_discount": 15,
    }

    try:
        # Run the crew
        result = SalesOfferCrew().crew().kickoff(inputs=inputs)

        # Show where the output file is saved
        print(f"\nSales offers generated successfully!")
        print(f"Output saved to: sales_offers.json")

        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "current_year": str(datetime.now().year),
        "offer_expiration_days": 30,
        "default_discount": 15,
    }

    try:
        SalesOfferCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SalesOfferCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "current_year": str(datetime.now().year),
        "offer_expiration_days": 30,
        "default_discount": 15,
    }

    try:
        SalesOfferCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
