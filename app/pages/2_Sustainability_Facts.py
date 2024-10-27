import streamlit as st
import page
import env
from services import policies

class SustainabilityFacts(page.PageTemplate):
    def render(self):
        if super().render():
            st.button(label='Refresh')

            policy_svc = policies.PolicyService(debug_mode=env.is_debug_mode())
            reply = policy_svc.query_selected_policy("""
Assuming you are a teacher familiar with all environmental-related topics. \
List down 3 facts related to all policies in an interesting manner as if you are teaching a class of students. \
Present the facts according to following markdown text enclosed in <Facts> tag:

<Facts>
### Title

Content about fact 1

### Title

Content about fact 2
</Facts>

Each fact should not exceed 200 words and each header should start with an appropriate emoji. Your reply should contain markdown text only and have 3 facts and exclude triple backticks or any enclosing <Facts> tags.
""")
            st.markdown(reply)
            return True
        return False

sustainabilityFacts = SustainabilityFacts('Sustainability Facts')
sustainabilityFacts.render()
