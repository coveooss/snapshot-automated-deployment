import json
import requests
import sys

"""
This script expects the following command line parameters:
  - Coveo organization ID
  - API key
  - GitHub repository name
"""
org_id = sys.argv[1]
api_key = sys.argv[2]
repo_name = sys.argv[3]

print(f"Running deployment script with org ID: {org_id} and repo name: {repo_name}.")

headers = {'Authorization': f"Bearer {api_key}", 'accept': 'application/json'}
fileobj = open('./Snapshot.zip', 'rb')

url = f'https://platformdev.cloud.coveo.com/rest/organizations/{org_id}/snapshots/file?developerNotes=New%20merge%20in%20{repo_name}&snapshotFileType=ZIP'

r = requests.post(url, headers=headers, files={"file": fileobj})

print(f"Coveo platform replied with status code: {r.status_code} and body: {r.content}.")

r.raise_for_status()

print(f"The following snapshot was created: {json.loads(r.content)['id']}")