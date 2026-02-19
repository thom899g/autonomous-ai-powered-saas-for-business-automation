import logging
from typing import Dict, Any
from .config_manager import ConfigLoader

class CRMManager:
    def __init__(self):
        self.config = None
        self.logger = logging.getLogger(__name__)
        
    def connect(self):
        try:
            self.config = ConfigLoader().load_config('crm')
            # Initialize CRM client based on configuration
            if self.config['provider'] == 'salesforce':
                from .crm_clients.salesforce import SalesforceClient
                self.client = SalesforceClient()
            elif self.config['provider'] == 'hubspot':
                from .crm_clients.hubspot import HubSpotClient
                self.client = HubSpotClient()
            else:
                raise ValueError("Unsupported CRM provider")
            self.logger.info(f"Connected to {self.config['provider']} CRM.")
        except Exception as e:
            self.logger.error(f"Failed to connect to CRM: {str(e)}")
            raise
    
    def update_customer(self, customer_id: str, data: Dict[str, Any]):
        try:
            response = self.client.update(customer_id, data)
            return {"status": "success", "response": response}
        except Exception as e:
            self.logger.error(f"Failed to update customer {customer_id}: {str(e)}")
            raise
    
    def get_customer(self, customer_id: str) -> Dict[str, Any]:
        try:
            return self.client.get(customer_id)
        except Exception as e:
            self.logger.error(f"Failed to retrieve customer {customer_id}: {str(e)}")
            raise