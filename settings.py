import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SCRAPING_PAGE_DMAIN = os.environ.get('SCRAPING_PAGE_DMAIN')
SCRAPING_PAGE_URL = os.environ.get('SCRAPING_PAGE_URL')
LINE_GROUP_ID = os.environ.get('LINE_GROUP_ID')