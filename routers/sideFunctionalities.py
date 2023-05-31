from fastapi import APIRouter
import requests


router = APIRouter(
    prefix = '/sideFunctionalities',
    tags = ['sideFunctionalities']
)


@router.get('/currencyRate')
def currencyRate():
   print('fee')
   #URL OF CURRENCY WEBSITE
   #https://www.xe.com/currencyconverter/
   url = 'https://www.xe.com/api/protected/midmarket-converter/'
   headers = {
      'authorization': 'Basic bG9kZXN0YXI6WWJndkQ0ZGpRcFNKalI0S2d1Q0RIMlRnYXBsN2VzVzQ='
   }

   response = requests.get(url, headers=headers)

   if response.status_code == 200:
      data = response.json()
      # Process the response data as needed
      # print(data)
      return data
   else:
      return print('Request failed with status code', response.status_code)
   