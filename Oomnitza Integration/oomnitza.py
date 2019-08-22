import requests
import sys

def main():
	if (len(sys.argv) <= 1):
		print("ERROR --- You did not specify asset ID in program argument!")
	else:
		head = {"Authorization2": "INSERT_API_KEY_HERE"}
		url = "https://OOMNITZA_URL_HERE/api/v3/assets/{}".format(sys.argv[1])
		payload = {"status": "Inventory"}
		r = requests.patch(url, json=payload, headers=head)
		print("Done! Status code: {}".format(str(r.status_code)))

if __name__ == '__main__':
	main()