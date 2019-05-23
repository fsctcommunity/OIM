# Forescout Palo Alto GlobalProtect & IP Stack Integration

Using the Forescout Open Integrations Module (OIM), this document will walk you through integrating Forescout with 
Palo Alto GlobalProtect running on PAN-OS (REST API) and IP Stack (ipstack.com). With this integration you will gain the following:


- Extract GlobalProtect (VPN) connected device information such as:
	- User connected
	- Device Operating System
	- Device Name
	- Time the User established connection to the GlobalProtect Gateway
	- Connecting device Public IP Address
- Disconnect users from the GlobalProtect Gateway.
- Extract Geo Location data from IP Stack using the Public IP Address of the connecting GlobalProtect device.
	- City, Zip Code, Region, Country, Continent 
	- Longitude, Latitude
	- Timezone

With the data from these integrations you will gain deeper visibility into remotely connected devices over 
the GlobalProtect VPN. This information can be used in policies (conditions) as well as {tags}. 
