#from request.auth import HTTPBasicAuth
import os
import requests


token = os.environ['GITLAB_API_PRIVATE_TOKEN']
urlGitlab = os.environ['GITLAB_API_ENDPOINT']


def get_snippets():
    """
    Return json with all public snippets
    """

    url = urlGitlab+"api/v4/snippets/public"
    headers = {"Accept": "application/json","PRIVATE-TOKEN": token}
    req = requests.get(url, headers=headers)
    if req.status_code != 200:
    # if fail
        raise ApiError('GET '.format(req.status_code))
    return req.json()

def get_projects():
    """
    Return json with public projets
    """
    url = urlGitlab+"api/v4/projects?visibility=public"
    headers = {"Accept": "application/json","PRIVATE-TOKEN": token}
    req = requests.get(url, headers=headers)
    if req.status_code != 200:
    # if fail
        raise ApiError('GET '.format(req.status_code))
    return req.json()

def get_groups():
    """
    Return json with public projects
    """
    url = urlGitlab+"api/v4/groups"
    headers = {"Accept": "application/json"}
    req = requests.get(url, headers=headers)
    if req.status_code != 200:
    # if fail
        raise ApiError('GET '.format(req.status_code))
    return req.json()


print('Public Snnipets')
for snippet in get_snippets():
    print ('{} {} {} '.format(snippet['id'],snippet['title'],snippet['raw_url']))

print ('Public Projects')
for project in get_projects():
    print ('{} {} {} '.format(project['id'],project['name'],project['web_url']))

print('Public Groups')
for group in get_groups():
    print ('{} {} {} '.format(group['id'],group['name'],group['web_url']))


