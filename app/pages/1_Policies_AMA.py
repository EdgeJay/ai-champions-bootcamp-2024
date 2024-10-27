import streamlit as st
import policy
import page
import utils
import env
from components import chat
from services import policies

def on_selector_click(selected):
    utils.set_selected_policy_nav(selected)

def render_policy_selector(selected_nav):
    cols = st.columns(len(policy.all_policies))

    for index, col in enumerate(cols):
        with col:
            icon = '✅' if selected_nav == policy.all_policies[index].nav_id else None
            st.button(
                policy.all_policies[index].button_label,
                icon=icon,
                use_container_width=True,
                on_click=on_selector_click,
                args=[policy.all_policies[index].nav_id],
                disabled=selected_nav == policy.all_policies[index].nav_id)

def user_input_from_chat(role, message):
    policy_svc = policies.PolicyService(debug_mode=env.is_debug_mode())
    reply = policy_svc.query_selected_policy(message)
    chat.ChatContainer.add_assistant_chat_message(reply)

class PoliciesAMA(page.PageTemplate):
    def render(self):
        super().render()
        st.text('Hi, what would you like to learn about today?')
        
        # policy selector buttons
        render_policy_selector(utils.get_selected_policy_nav())
        
        # container for chat
        container = chat.ChatContainer(
            f'Ask me anything about policies related to {utils.get_selected_policy().button_label}',
            user_input_from_chat
        )
        container.render()

policiesAMA = PoliciesAMA('Policies AMA')
policiesAMA.render()
