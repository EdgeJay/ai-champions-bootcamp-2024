import const

class Policy:
    nav_id: str
    button_label: str
    policy_url: str

    def __init__(self, nav_id, button_label, policy_url):
        self.nav_id = nav_id
        self.button_label = button_label
        self.policy_url = policy_url

all_policies = [
    Policy(const.NAV_POLICY_CLIMATE, 'Climate Change', 'https://www.mse.gov.sg/policies/climate-change'),
    Policy(const.NAV_POLICY_ENERGY, 'Energy', 'https://www.mse.gov.sg/policies/energy'),
    Policy(const.NAV_POLICY_AIR, 'Clean Air', 'https://www.mse.gov.sg/policies/clean-air'),
    Policy(const.NAV_POLICY_WATER, 'Water', 'https://www.mse.gov.sg/policies/water'),
    Policy(const.NAV_POLICY_FOOD, 'Food Security', 'https://www.mse.gov.sg/policies/food/'),
]
