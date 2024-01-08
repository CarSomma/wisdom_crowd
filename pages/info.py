import streamlit as st
def explanation_page():
    st.markdown("<h2 style='text-align: center; color: #1f4d7a;'>Simulation Process Explanation</h2>", unsafe_allow_html=True)
    st.write(
        "The simulation involves generating individual estimates for each learner in each simulation run. "
        "The initial individual estimate for each learner is randomly selected based on the given individual accuracy."
        " Subsequent estimates for each learner are influenced by the correlation strength, which introduces a correlation"
        " among the estimates. The collective accuracy is then calculated based on the majority decision across all learners"
        " for each simulation run."
    )

    st.subheader("Correlation Strength Scenarios:")
    st.markdown(
        "1. **Correlation Strength = -1:**\n"
        "   - Inversely correlated predictions.\n"
        "   - If one learner predicts correctly, others predict incorrectly, and vice versa.\n"
        "   - Collective accuracy may be substantially lower than individual accuracy."
    )
    st.markdown(
        "2. **Correlation Strength = 0:**\n"
        "   - No correlation among weak learners.\n"
        "   - Predictions are independent.\n"
        "   - Collective accuracy may be substatially better than individual accuracy."
    )
    st.markdown(
        "3. **Correlation Strength = 1:**\n"
        "   - Perfectly correlated predictions.\n"
        "   - If one learner predicts correctly, all others predict correctly, and vice versa.\n"
        "   - Collective accuracy is the same as the accuracy of an individual learner.\n"
        "   - Presence of correlation doesn't change collective accuracy; it remains around individual accuracy."
    )

    st.write(
        "The app displays the collective accuracy and a line chart showing how the collective accuracy evolves over "
        "multiple simulation runs."
    )
if __name__ == '__main__':
    explanation_page()
