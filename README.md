
# How to Publish to CaptionPartnersDev Private PyPi Repo
--------------------
## Setup uv

Create an venv and have the following two enviromental variables:

```
UV_EXTRA_INDEX_URL=https://pypi.org/simple
UV_INDEX_URL=*******************
```


## Setup with pip
Edit your local pip.conf located at `$HOME/.config/pip/pip.conf`
Grab a token from jfrog and replace the pip.conf with the text below:

```
[global]
index-url = https://<jfrog_username>:<jfrog_token>@captionpartnersllc.jfrog.io/artifactory/api/pypi/pypi/simple
```

## Upload from local build
```bash
twine upload --repository-url https://captionpartnersllc.jfrog.io/artifactory/api/pypi/pypi dist/* -u <jfrog_username> -p <jfrog_token>
```
