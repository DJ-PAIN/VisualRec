import json
import jwt
import hashlib

from VisualRec import accounts_API

def grantToken(grant_type, data: dict):
    with open("json\\players.json") as f:
        players = json.load(f)
    if grant_type == "create_account":
        acc = accounts_API.create(data["platform"], data["platform_id"], data["device_id"])
        role = "gameclient"
        if acc["isDeveloper"]:
            role = "developer"
        token = jwt.encode({
            "iss": "https://auth.rec.net",
            "client_id": "recnet",
            "role": role,
            "Authorization": acc["Authorization"],
            "sub": acc["accountId"],
            "auth_time": 1657773955,
            "idp": "local",
            "jti": "D9E0566B56518BCD20A64C2D6350C4E3",
            "sid": "564F9AAFC3AF41DD0A438CC19E899763",
            "iat": 1669575399,
            "scope": [],
            "amr": [
                "mfa"
            ]
        }, key="")
        return {"token": token, "key": ""}
        return {"token": token, "key": ""}
    if grant_type == "cached_login":
        for player in players:
            if int(player["accountId"]) == int(data["account_id"]):
                role = "gameclient"
                if player["isDeveloper"]:
                    role = "developer"
                token = jwt.encode({
                    "iss": "https://auth.rec.net",
                    "client_id": "recnet",
                    #"role": "gameclient",
                    "role": role,
                    "Authorization": player["Authorization"],
                    "sub": player["accountId"],
                    "auth_time": 1657773955,
                    "idp": "local",
                    "jti": "D9E0566B56518BCD20A64C2D6350C4E3",
                    "sid": "564F9AAFC3AF41DD0A438CC19E899763",
                    "iat": 1669575399,
                    "scope": [],
                    "amr": [
                        "mfa"
                    ]
                }, key="")
                return {"token": token, "key": ""}
        return {"token": None, "key": ""}
    elif grant_type == "web_login":
        for player in players:
            if int(player["accountId"]) == int(data["account_id"]):
                role = "webclient"
                #if player["isDeveloper"]:
                #    role = "developer"
                token = jwt.encode({
                    "iss": "https://auth.rec.net",
                    "client_id": "recnet",
                    "role": role,
                    "Authorization": player["Authorization"],
                    "sub": player["accountId"],
                    "auth_time": 1657773955,
                    "idp": "local",
                    "jti": "D9E0566B56518BCD20A64C2D6350C4E3",
                    "sid": "564F9AAFC3AF41DD0A438CC19E899763",
                    "iat": 1669575399,
                    "scope": [],
                    "amr": [
                        "mfa"
                    ]
                }, key="")
                return {"token": token, "key": ""}
        return {"token": None, "key": ""}
    return {"token": None, "key": ""}


def hashString(String: str):
    has = hashlib.sha256(bytes(String, "ascii")).hexdigest()
    return has


def cachedlogin(platformId: int):
    logins = []

    with open("json\\players.json") as f:
        players = json.load(f)

    for player in players:
        print(player["platformId"])
        if int(player["platformId"]) == platformId:
            logins.append({
                "platform": 0,
                "platformId": platformId,
                "accountId": player["accountId"],
                "lastLoginTime": player["lastLoginTime"]
            })
    return logins

def getPlayerByAuthorization(Authorization):
    with open("json\\players.json") as f:
        players = json.load(f)
    for player in players:
        if player["Authorization"] == Authorization:
            return player
    return None
