import logging
from typing import Dict, Any
from langchain import LLMChain

class AIEngine:
    def __init__(self):
        self.llm_chain = None
        self.logger = logging.getLogger(__name__)
        
    def initialize(self):
        try:
            from langchain.agents import Agent
            from .llm_interface import get_llm
            self.llm_chain = LLMChain(llm=get_llm())
            self.logger.info("AI Engine initialized successfully.")
        except Exception as e:
            self.logger.error(f"Failed to initialize AI Engine: {str(e)}")
            raise
    
    def process_query(self, query: str) -> Dict[str, Any]:
        try:
            response = self.llm_chain.run(query)
            return {"status": "success", "response": response}
        except Exception as e:
            self.logger.error(f"AI Processing failed: {str(e)}")
            raise
    
    def start(self):
        self.initialize()