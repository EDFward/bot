"""Scheduled jobs to fetch Steam deals."""

import lxml
import requests

# TODO: set up as Celery jobs.

DEAL_SOURCE_URL = 'https://www.steamgifts.com/sales/recommended'

def fetch_deals():
    r = requests.get(DEAL_SOURCE_URL)
    # TODO: parse HTML and extract deal information.
    print(r.text)
    

if __name__ == '__main__':
    fetch_deals()