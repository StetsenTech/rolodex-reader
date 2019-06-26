# GETTING STARTED

## Requirements

- [Python 2.7](https://www.python.org/download/releases/2.7/)
- [Virtualenv](https://virtualenv.pypa.io/)

## Setup Environment

1. Create a new virtual environment
   - `virtualenv {env_path}`
2. Activate the virtual environment
   - `source {env_path}/bin/activate`
3. Verify that project is using Python 2.7
   - `python --version`
4. Install package requirements for project
   - `pip install -r requirements.txt`
   - *OPTIONAL* for tests and python notebook
     - `pip install -r requirements-dev.txt`