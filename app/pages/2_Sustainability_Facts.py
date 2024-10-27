import streamlit as st
import page
import env
from services import policies

FACT_SEPARATOR = '---sep---'

def sanitise_reply(text):
    return text.replace('<Response>', '').replace('</Response>', '')

class SustainabilityFacts(page.PageTemplate):
    def render(self):
        if super().render():
            policy_svc = policies.PolicyService(debug_mode=env.is_debug_mode())

            if st.session_state.get('more_details', None) == None:
                st.button(label='Refresh')

                reply = policy_svc.query_all_policies(f"""
Assuming you are a teacher familiar with all environmental-related topics. \
List down 3 facts related to all policies in an interesting manner as if you are teaching a class of students. \
Present the facts according to following JSON format enclosed in <Response> tag:

<Response>
### Title

Content about fact 1

{FACT_SEPARATOR}

### Title

Content about fact 2
</Response>

Each fact should not exceed 200 words and each header should start with an appropriate emoji. \
Each fact section should be separated by "{FACT_SEPARATOR}" \
Your reply should contain markdown text only and have 3 facts and exclude triple backticks or any enclosing <Response> tags.
""")
            
                sections = sanitise_reply(reply).split(FACT_SEPARATOR)
                
                for idx, s in enumerate(sections):
                    st.markdown(s)
                    if st.button(label='Tell Me More', key=idx):
                        st.session_state['more_details'] = s
                        st.rerun()
            else:
                # more details
                reply2 = policy_svc.query_all_policies(f"""
Assuming you are a teacher familiar with all environmental-related topics. \
Elaborate more on content enclosed in <Content> tag in an interesting manner.

<Content>
{st.session_state['more_details']}
</Content>
""")
                if st.button(label='< Back'):
                    del st.session_state['more_details']
                    st.rerun()

                st.markdown(reply2)
            
            return True
        
        return False

sustainabilityFacts = SustainabilityFacts('Sustainability Facts')
sustainabilityFacts.render()
