import requests
from typing import Tuple

CLIENT_ID = "c128fe76-dc54-4daa-993c-1a13c1e82080"
REDIRECT_URI = "TODO"

def azure_refresh_token(refresh_token: str) -> Tuple[str, str]:
    """
    Refreshes a given refresh token and returns the
    new access token and refresh token
    """
    url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"

    payload = f'client_id={CLIENT_ID}&scope=https://graph.microsoft.com/User.Read&redirect_uri={REDIRECT_URI}&grant_type=refresh_token&refresh_token={refresh_token}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    rjson = response.json()

    if response.status_code != 200:
        return ("", "")

    return (rjson['access_token'], rjson['refresh_token'])