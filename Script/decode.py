
#get secret in scope method
def getToken(scope,secret):
    invisble_sep=bytes.fromhex('E281A3').decode('utf-8')
    secrets=dbutils.secrets.get(scope,secret)
    plainsecret=secrets.replace("",invisble_sep)
    print(f"{secret} in {scope} ")
    return plainsecret
secret_list=spark.sql("select * from list_secrets();")
list=secret_list.select("*").collect()
lol={row{'scope'}:row{'key'} for row in list}
    
for i in lol:
    getToken(i,lol[i])




import json 
dbutils.secrets.listScopes()
dbutils.secrets.list(scope)
for i in dbutils.secrets.listScopes():
    print(i)





#api
import requests
endpoint=""
databricks_token=""
headers={
    "authorization":f"Bearer {databricks_token}"
}

response=requests.get(url=endpoint, headers=headers)

from datetime import datetime
import json
res=response.json()
dic={}
for k,v in res.items():
    for index in range(len(v)):
        exired=None
        for key in v[index]:
            if key=='expiry_time':
                expired=datetime.fromtimestamp(v[index][key]/1000).strftime("%Y-%m-%d")
            if key=='created_by_username':
                created_by=v[index][v]
                dic[created_by]=expired
print(dic)