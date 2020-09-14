# gitlab-check-public-assets
A python script that searchs for public repos, groups and snippets in a given Gitlab server


## Usage

### From console

You may run the following command:

``` 
python gitlab-check-public-assets.py 
```

### Prerequisites

* Should work with python 3.x.
* An access token with `read_repository` scope is required in order to access your Gitlab project.
* You need to provide a Gitlab API endpoint and Gitlab Token API as follows: 

````
export GITLAB_API_ENDPOINT=https://<your gitlab server url>/api/v4  
export GITLAB_API_PRIVATE_TOKEN=<your token>
