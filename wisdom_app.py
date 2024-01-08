import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.graph_objects as go

def simulate_collective_accuracy(num_learners, num_simulations, individual_accuracy, correlation_strength):
    """
    Simulate collective accuracy based on correlated individual estimates.

    Parameters:
    - num_learners (int): Number of learners in the simulation.
    - num_simulations (int): Number of simulation runs.
    - individual_accuracy (float): Probability of an individual learner making a correct estimate.
    - correlation_strength (float): Strength of correlation among individual estimates.

    Returns:
    - float: Mean collective accuracy across all simulations.

    Description:
    The function simulates a scenario where multiple learners provide individual estimates,
    and there is a correlation among these estimates. The correlation is introduced using
    a simple autoregressive model. The first individual estimate for each simulation is
    initialized randomly, and subsequent estimates are correlated with the previous ones.
    The final collective accuracy is calculated based on the majority decision for each simulation.
    
    The code uses vectorized operations to optimize performance, making use of NumPy's
    capabilities for efficient array computations.

    Correlation Scenarios:
    - When correlation_strength is 0, there is no correlation among individual estimates.
      Each learner's estimate is independent of others.
      Expectation: Collective accuracy may vary and could be influenced by the diversity of independent predictions among learners.

    - When correlation_strength is 1, there is perfect positive correlation among individual estimates.
      If one learner makes a correct estimate, all others will make correct estimates, and vice versa.
      Expectation: Collective accuracy will be close to the accuracy of a single learner.
      Note: With perfect correlation (correlation = 1), the collective accuracy should be the same as the individual accuracy.

    - When correlation_strength is -1, there is perfect negative correlation among individual estimates.
      If one learner makes a correct estimate, all others will make incorrect estimates, and vice versa.
    """

    # Initialize arrays for individual estimates and collective accuracies
    individual_estimates = np.zeros((num_simulations, num_learners), dtype=bool)
    collective_accuracies = np.zeros(num_simulations, dtype=int)

    # Initialize the first individual estimate randomly for each simulation
    individual_estimates[:, 0] = np.random.choice([1, 0], size=num_simulations, p=[individual_accuracy, 1 - individual_accuracy])

    # Simulate individual estimates for the remaining learners and all simulations
    for i in range(1, num_learners):
        correlated_values = (
            correlation_strength * (2*individual_estimates[:, i-1].astype(int) -1 )
            + np.sqrt(1 - correlation_strength**2) * np.random.choice([1, 0], size=num_simulations, p=[individual_accuracy, 1 - individual_accuracy])
        )
        individual_estimates[:, i] = np.clip(correlated_values, 0, 1) >= np.array(individual_accuracy)

    # Check collective accuracy for all simulations
    collective_accuracies = np.sum(individual_estimates, axis=1) >= num_learners // 2 + 1

    # Calculate the mean collective accuracy
    mean_collective = np.mean(collective_accuracies)

    return mean_collective, collective_accuracies

# Streamlit App
def main():
    st.markdown("<h1 style='text-align: center; color: #1f4d7a;'>🌟 Ensemble Simulation App 🌟</h1>", unsafe_allow_html=True)

    # Brief description
    st.write(
        "This app simulates the collective accuracy of an ensemble of learners with varying individual accuracies "
        "and correlation among their estimates. Adjust the simulation settings in the sidebar to observe how the "
        "collective accuracy evolves over multiple simulations"
    )

    # Sidebar
    st.sidebar.header("Simulation Settings")
    num_learners = st.sidebar.slider("Number of Learners", min_value=1, max_value=5000, value=100)
    num_simulations = st.sidebar.slider("Number of Simulations", min_value=1, max_value=50000, value=25000)
    individual_accuracy = st.sidebar.slider("Individual Accuracy", min_value=0.1, max_value=1.0, value=0.51, step=0.01)
    correlation_strength = st.sidebar.slider("Correlation Strength", min_value=-1.0, max_value=1.0, value=0.0, step=1.0, format="%d")

    # Simulation
    mean_collective, collective_accuracies= simulate_collective_accuracy(num_learners, num_simulations, individual_accuracy, correlation_strength)
    cumulative_accuracies = np.cumsum(collective_accuracies) / np.arange(1, num_simulations + 1)

    # Individual Estimates
    individual_estimates = np.zeros((num_simulations, num_learners), dtype=bool)
    for i in range(num_learners):
        individual_estimates[:, i] = np.random.choice([1, 0], size=num_simulations, p=[individual_accuracy, 1 - individual_accuracy])

    

  
   
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(1, num_simulations + 1), y=cumulative_accuracies,
                             mode='lines', name='Collective Accuracy',
                             line=dict(color='#4a7c59', dash='dash', width=2)))
    fig.update_layout(
        xaxis=dict(title='Number of Simulations'),
        yaxis=dict(title='Collective Accuracy'),
        title='Collective Accuracy Convergence',
        template='plotly_dark'
    )
    st.plotly_chart(fig)
    st.write(
        "The line chart above illustrates how the collective accuracy evolves over "
        "multiple simulation runs."
    )
    # Display results
    collective_accuracy_percentage = mean_collective * 100
    st.markdown(
    f"<div style='text-align: center; padding: 5px; background-color: white; border-radius: 15px;'>"
    f"<h5 style='color: #1f4d7a;'>Collective Accuracy:</h3>"
    f"<p style='font-size: 18px; color: {'green' if collective_accuracy_percentage >= 50 else 'red'};'>"
    f"{collective_accuracy_percentage:.2f}%"
    f"</p></div>",
    unsafe_allow_html=True
)
   

if __name__ == '__main__':
    main()
