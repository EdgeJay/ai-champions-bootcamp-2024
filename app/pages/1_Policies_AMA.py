import streamlit as st
import policy
import page
import utils

def on_selector_click(selected):
    utils.set_selected_policy(selected)

def renderPolicySelector(selected_nav):
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

class PoliciesAMA(page.PageTemplate):
    def render(self):
        super().render()
        st.text('Hi, what would you like to learn about today?')
        renderPolicySelector(utils.get_selected_policy())
        st.write(utils.get_selected_policy())

policiesAMA = PoliciesAMA('Policies AMA')
policiesAMA.render()
