import http.client
conn = http.client.HTTPSConnection("webservices.nextbus.com/service/publicXMLFeed?command=agencyList")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()  # This will return entire content.
print(data1)
# The following example demonstrates reading data in chunks.
conn.close()
