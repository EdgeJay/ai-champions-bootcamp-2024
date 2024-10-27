from services import documents
from services import openai
import env
import policy
import utils

# Service for loading policies and provide methods to "interact" with policy doucments
class PolicyService:
    debug_mode: bool

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def load_all_policies(self):
        for p in policy.all_policies:
            self.load_policy(p)

    def load_selected_policy(self):
        # get policy
        policy = utils.get_selected_policy()
        if policy == None:
            return False

        return self.load_policy(policy)
    
    def load_policy(self, policy):
        openai_service = openai.OpenAIService(api_key=env.get_openai_key())
        # check if policy is loaded
        doc_service = documents.DocumentStorageService(openai_service.get_embeddings(), debug_mode=self.debug_mode)
        return doc_service.load_and_store_html_document(
            id=policy.nav_id,
            url=policy.policy_url,
            force_reload=env.force_reload_documents()
        )

    def query_selected_policy(self, query):
        openai_service = openai.OpenAIService(api_key=env.get_openai_key())
        policy = utils.get_selected_policy()
        if policy != None:
            doc_service = documents.DocumentStorageService(openai_service.get_embeddings(), debug_mode=self.debug_mode)
            output = doc_service.query_document(policy.nav_id, query)
            return output['result']
        return None