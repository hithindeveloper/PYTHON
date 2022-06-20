import json
import requests
data = {"api_key":"3Nh47mAJgycXYguXlEen9GGnYEe2vNkne2J","page":1}
request = requests.get("https://price-api.datayuge.com/api/v1/compare/list/categories",params=data)
record = json.loads(request.text)
for x in record.get("data"):
    print(x.get('category_name'))