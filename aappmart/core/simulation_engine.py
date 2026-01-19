import logging
from core.pipeline import Pipeline
from agents.dummy_agent import DummyAgent

class SimulationEngine:

    def __init__(self):
        self.agents = [DummyAgent("Agent1"), DummyAgent("Agent2")]
        self.pipeline = Pipeline(steps=5)

    def run(self):
        logging.info("Simulation Engine started")
        self.pipeline.execute(self.agents)
        logging.info("Simulation Engine finished")
