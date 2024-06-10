### Environment 🌀 and Installation 👩🏽‍🔧👨🏽‍🔧
#### Prerequisite
+ Python 3.11.3 or above up to 3.11.6 (We will use [pyenv](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv) for Python Version Management but feel free to use any other tool)
+ Virtual environment (We will use the module venv from python but you can use any other tool)


For __MacOs__/__Linux__ users
```bash
# Sets the local Python version to 3.11.3 using pyenv
pyenv local 3.11.3 
# Create a Virtual Environment named .streamlit_env using venv
python -m venv .streamlit_env
# Activate the Virtual Environment
source .streamlit_env/bin/activate
# Install Streamlit and Additional Libraries
pip install -r requirements.txt
```

For __Windows__ users


```bash
# Sets the local Python version to 3.11.3 using pyenv
pyenv local 3.11.3 
# Create a Virtual Environment named .streamlit_env using venv
python -m venv .streamlit_env
# Activate the Virtual Environment
.streamlit_env\Scripts\Activate.ps1
# Install Streamlit and Additional Libraries
pip install -r requirements.txt
```
Feel free to play with the [Wisdom Streamlit app](https://wisdom-crowd.streamlit.app/).
