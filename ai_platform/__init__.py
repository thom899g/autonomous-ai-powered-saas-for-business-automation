"""
The __init__.py file initializes the AI Platform module and provides entry points for various components.
"""

from .ai_engine import AIEngine
from .messaging import MessagingHandler
from .crm_integration import CRMManager
from .rules_engine import RulesEngine
from .monitoring import Monitor
from .config_manager import ConfigLoader

# Initialize core components
AI_ENGINE = AIEngine()
MESSAGING_HANDLER = MessagingHandler()
CRM_MANAGER = CRMManager()
RULES_ENGINE = RulesEngine()
MONITOR = Monitor()
CONFIG_LOADER = ConfigLoader()

def start_platform():
    """
    Starts the AI Platform by initializing all core components and beginning the listening process.
    """
    AI_ENGINE.start()
    MESSAGING_HANDLER.listen()
    CRM_MANAGER.connect()
    RULES_ENGINE.load_rules()
    MONITOR.start_monitoring()