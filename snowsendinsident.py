# ./snowsendinsident.py "$sysparm_action" "$category" "$impact" "$urgency" "$caller_id" "$cmdb_ci" "$short_description"  << usage
# Edite URL paramater, UserName and Password below
import sys
import urllib2
import json
from requests.auth import HTTPBasicAuth
import requests
# This py file is a stand-alone integration, it directly works with SHH or BASH CALLS
payload = {
   "sysparm_action":sys.argv[1],
   "category":sys.argv[2],
   "impact":sys.argv[3],
   "urgency":sys.argv[4],
   "caller_id":sys.argv[5],
   "cmdb_ci":sys.argv[6],
   "short_description":sys.argv[7]
   "work_notes":sys.argv[7]
}


auth = HTTPBasicAuth("admin", "admin")
uri = "https://demo002.service-now.com/incident.do?JSONv2"

# http headers for request
headers = {
    "Accept": "application/json;charset=utf-8",
    "Content-Type": "application/json"
}

#we insert a insident
r = requests.post(url=uri, data=json.dumps(payload), auth=auth, verify=False, headers=headers)

content = r.json()
assert (r.status_code == 200)
print "Response Status Code: " + str(r.status_code)
print "Response JSON Content: " + str(content)
