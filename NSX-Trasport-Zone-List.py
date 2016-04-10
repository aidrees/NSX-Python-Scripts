import requests
from xml.etree import ElementTree
requests.packages.urllib3.disable_warnings()
print 'Getting Transport Zones from NSX...'
response = requests.get('https://10.10.11.8/api/2.0/vdn/scopes',verify=False,auth=('admin','VMware1!'),stream=True)
tree = ElementTree.parse(response.raw)


for vdnScope in tree.iter('vdnScope'):
	print 'Name: ' + vdnScope.find ('name').text
	print 'ID: ' + vdnScope.find('objectId').text
