
PARAMS = {'mkt': 'en-US', 'aspect':'Square', 'count':5,  }
# Add your Bing Search V7 subscription key and endpoint to your environment variables.
SUBSCRIPTION_KEY = "0a98f08030334a0fb14d1c6f1a957834"
ENDPOINT = "https://api.bing.microsoft.com/v7.0/images/search/"
HEADER = { 'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY }
# info about Search V7
# https://learn.microsoft.com/en-us/bing/search-apis/bing-image-search/reference/query-parameters

FILE_PATH = 'iNSPIRE tables.xlsx' 
SHEET_NAME = 'Standards' 

COLUMN_READ_SOURCE = "Standard Title"

COLUMN_START_WRITE = 17
ROW_START_WRITE = 0
BASE_NAME_NEW_COLUMN = "image link"
