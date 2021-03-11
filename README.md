# Resource Snapshot Demo

This demo contains a snapshot split into multiple JSON files that together create a query pipeline with multiple rules and Machine Learning models. The query pipeline also comes with an A/B test that is configured in a separate JSON file.

A GitHub Action is also available 

## Fork the Repo

## Create an API Key
An API key is required to communicate with the Coveo Platform and deploy your snapshots. If you need help, [this documentation](https://docs.coveo.com/en/1718/) is a good starting place. When is comes to deciding which privileges to assign to your API key, you'll need to grant the Edit All access level for every type of resource that you want to deploy with your snapshot.

> For this example, you'll need: Edit all fields, Edit all query pipelines, Edit all Machine Learning models, and View organization.

## Store the API Key as a GitHub Secret
Follow [these steps](https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository) to add a new secret named `API_KEY` and enter the API key that you created as its value. 

## Update the GitHub Action
In deploy_snapshot.yml, you'll need to update the ORG_ID variable to be the one of your own Coveo organization.
