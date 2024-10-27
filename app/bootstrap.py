import os
import certifi
import env
from services import documents
from services import policies

# all code that should be run when app is first started
# should be stored in this function
def initialise_app():
    # add path to certifi pem file to avoid SSL verification errors
    # when making HTTP requests to external sources
    os.environ['REQUESTS_CA_BUNDLE'] = str(certifi.where())
    print(os.environ['REQUESTS_CA_BUNDLE'])

    print('load all policies')
    policyService = policies.PolicyService(debug_mode=env.is_debug_mode())
    policyService.load_all_policies()