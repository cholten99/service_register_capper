import json
import urllib

url = "https://government-service.alpha.openregister.org/records.json?page-size=200"
url_handle = urllib.urlopen(url)
service_json = url_handle.read()
service_dom = json.loads(service_json)

for service in service_dom:
  print "https://www.gov.uk/" + service_dom[service]["hostname"]

