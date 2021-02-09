# enrollment-processor
[![<Enrollment Processor>](https://circleci.com/gh/circleci/circleci-docs.svg?style=shield)](https://app.circleci.com/pipelines/github/Silvian/enrollment-processor)

Processes member data from Google Sheets into Samaritan using webhook api.

### Installation Guide

1. Clone the project.
2. Create a python3 virtual environment: `python3 -m venv venv`
3. Install all requirements: `pip install -r requirements.txt`
4. Configure cron job to run: `python processor.py`

### Tests

To run tests: `pytest`
