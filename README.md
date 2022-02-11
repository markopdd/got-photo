Test Automation Framework based on pytest and selenium.
To run tests from a framework you should have a testing set up. 

Install python on your machine according to your OS system.

Install Google Chrome browser any version.

Install python environment from console command: 
`python -m venv venv`

Install dependencies: 
`pip install -r requirements.txt`

Open test_data/data.py and fill USER_TEST_DATA dict example ('firstname': "TestJohn")

To run tests: `pytest -v tests`