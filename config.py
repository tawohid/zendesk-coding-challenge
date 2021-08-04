import os

bearer_token = os.environ.get('BEARER_TOKEN')
header = {'Authorization': 'Bearer ' + bearer_token}
api = 'https://zccsupport.zendesk.com/api/v2/'
