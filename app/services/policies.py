from services import documents
import utils

# Service for loading policies and provide methods to "interact" with policy doucments
class PolicyService:
    debug_mode: bool

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def load_selected_policy(self):
        # get policy
        p = utils.get_selected_policy()
        if p == None:
            return False

        # check if policy is loaded
        doc_service = documents.DocumentStorageService(self.debug_mode)
        return doc_service.load_and_store_html_document(p.nav_id, p.policy_url)