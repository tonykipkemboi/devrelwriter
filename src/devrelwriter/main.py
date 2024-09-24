#!/usr/bin/env python
import sys
from devrelwriter.crew import DevrelwriterCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': "A Simple RAG CrewAI Agent app with MongoDB",
        "tech_stack": "crewai.com, Python, MongoDB",
        "github_repo_name": "https://github.com/crewAIInc/crewAI",
    }
    results = DevrelwriterCrew().crew().kickoff(inputs=inputs)

    print(results)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Simple RAG app with Haystack",
        "tech_stack": "Python, Haystack, Langchain",
    }
    try:
        DevrelwriterCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        DevrelwriterCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Simple RAG app with Haystack",
        "tech_stack": "Python, Haystack, Langchain",
    }
    try:
        DevrelwriterCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

# if __name__ == "__main__":
#     run()