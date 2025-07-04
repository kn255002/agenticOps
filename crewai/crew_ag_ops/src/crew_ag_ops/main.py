#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from crew_ag_ops.crew import CrewAgOps

# Load environment variables from .env file
# This is useful for loading API keys and other configurations
# without hardcoding them into the source code.
# Make sure to create a .env file in the root directory with the necessary variables.
#
#from dotenv import load_dotenv
#load_dotenv()
#

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs Framework prepared by CrewAI',
        'current_year': str(datetime.now().year)
    }
    
    try:
        CrewAgOps().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception("An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        CrewAgOps().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception("An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewAgOps().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception("An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        CrewAgOps().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception("An error occurred while testing the crew: {e}")
