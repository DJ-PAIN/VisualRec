from flask import Flask, request, jsonify, send_file, redirect, make_response, url_for, render_template, Response, abort, session
from flask_sock import Sock
from flask_cors import CORS
import json
import requests
import random
import colorama
from colorama import Fore
import os
import random
import base64
import sys
import random
import datetime
import jwt

from VisualRec import ProgramUtils, auth_API, accounts_API, room_API

name = f"{__name__}.py"

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
sock = Sock(app)
CORS(app)

@app.errorhandler(404)
def q405(e):
    data = ""
    return data, 404

@app.errorhandler(405)
def q405(e):
    data = ""
    return data, 405

@app.errorhandler(500)
def q405(e):
    data = {"Message":"An error has occurred."}
    return jsonify(data), 500

@app.route("/", methods=["GET"])
def index():
    url = ProgramUtils.URL()
    data = {
        "Accounts": f"https://{url}/accounts/",
        "API": f"https://{url}",
        "Auth": f"https://{url}/auth/",
        "BugReporting": f"https://{url}bugreporting/",
        "Cards": f"https://{url}/cards/",
        "CDN": f"https://8cwsd764-9873.uks1.devtunnels.ms/cdn/",
        "Chat": f"https://{url}/chat/",
        "Clubs": f"https://{url}/clubs/",
        "CMS": f"https://cms.rec.net",
        "Commerce": f"https://{url}/commerce/",
        "Data": f"https://{url}/data/",
        "DataCollection": f"https://{url}/datacollection/",
        "Discovery": f"https://{url}/discovery/",
        "Econ": f"https://{url}/econ/",
        "GameLogs": f"https://{url}/gamelogs/",
        "Geo": f"https://{url}/geo/",
        "Images": f"https://8cwsd764-9873.uks1.devtunnels.ms/img/",
        "Leaderboard": f"https://{url}/leaderboard/",
        "Link": f"https://{url}/link/",
        "Lists": f"https://{url}/lists/",
        "Matchmaking": f"https://{url}/match/",
        "Moderation": f"https://{url}/moderation/",
        "Notifications": f"https://{url}/notify/",
        "PlatformNotifications": f"https://{url}/platformnotifications/",
        "PlayerSettings": f"https://{url}/playersettings/",
        "RoomComments": f"https://{url}/roomcomments/",
        "Rooms": f"https://{url}/roomserver/",
        "Storage": f"https://{url}/storage/",
        "Strings": f"https://{url}/strings/",
        "StringsCDN": f"https://{url}/strings/",
        "Studio": f"https://{url}/studio/",
        "Thorn": f"https://{url}/thorn/",
        "Videos": f"https://{url}/videos/",
        "WWW": f"https://OldRecRoom.com/"
        }
    return jsonify(data)


@app.route("/api/versioncheck/v4", methods=["GET"])
def api_versioncheck_v4():
    v = request.args.get("v")
    if v is None:
        return jsonify({
            "Message":"The request is invalid."
        })
    if v == "20211022":
        return jsonify({
            "VersionStatus":0,
            "UpdateNotificationStage":0
        })
    return jsonify({
            "VersionStatus":0,
            "UpdateNotificationStage":0
        })

@app.route("/clubs/subscription/subscriberCount/<int:playerId>", methods=["GET"])
def clubs_subscription_subscriberCount(playerId):
    return jsonify(99999999)

@app.route("/api/gameconfigs/v1/all", methods=["GET"])
def api_gameconfigs_v1_all():
    try:
        with open("json\\GC.json") as f:
            GC = json.load(f)
    except:
        return abort(500)
    data = GC
    return jsonify(data)

@app.route("/api/PlayerReporting/v1/deviceId", methods=["POST"])
def api_PlayerReporting_v1_deviceId():
    print(dict(request.form))
    return jsonify([])

@app.route("/api/config/v2", methods=["GET"])
def api_config_v2():
    try:
        with open("json\\config.json") as f:
            GC = json.load(f)
    except:
        return abort(500)
    data = GC
    return jsonify(data)

@app.route("/roomserver/rooms/hot", methods=["GET"])
def roomserver_rooms_hot():
    data1 = room_API.getRoomsByTag(request.args["tag"])
    TotalResults = max([room["RoomId"] for room in data1])
    data = {
        "Results": data1,
        "TotalResults": TotalResults
    }
    return jsonify(data)

@app.route("/api/communityboard/v2/current", methods=["GET"])
def api_communityboard_v2_current():
    try:
        with open("json\\api\\communityboard.json") as f:
            GC = json.load(f)
    except:
        return abort(500)
    data = GC
    return jsonify(data)

@app.route("/api/announcement/v1/get", methods=["GET"])
def api_announcement_v1_get():
    try:
        with open("json\\api\\announcements.json") as f:
            GC = json.load(f)
    except:
        return abort(500)
    data = GC
    return jsonify(data)

@app.route("/api/storefronts/v3/giftdropstore/<int:id>", methods=["GET"])
def api_storefronts_v3_giftdropstore(id):
    try:
        with open("json\\storefronts-giftdropstore.json") as f:
            storefronts = json.load(f)
        for storefront in storefronts:
            if storefront["StorefrontType"] == id:
                return jsonify(storefront)
        return abort(404)
    except:
        return abort(500)

@app.route("/api/gamesight/event", methods=["POST"])
def api_gamesight_event():
    data = []
    return jsonify(data)

@app.route("/api/config/v1/amplitude", methods=["GET"])
def api_config_v1_amplitude():
    data = {
        "AmplitudeKey":"93941036bd6a7243bf5c628535f41d63",
        "UseRudderStack":True,
        "RudderStackKey":"23NiJHIgu3koaGNCZIiuYvIQNCu",
        "UseStatSig":True,
        "StatSigKey":"client-SBZkOrjD3r1Cat3f3W8K6sBd11WKlXZXIlCWj6l4Aje",
        "StatSigEnvironment":0
    }
    return jsonify(data)

@app.route("/api/avatar/v1/defaultunlocked", methods=["GET"])
def api_avatar_v1_defaultunlocked():
    try:
        with open("json\\defaultunlocked.json") as f:
            GC = json.load(f)
    except:
        return abort(500)
    data = GC
    return jsonify(data)

@app.route("/auth/cachedlogin/forplatformid/<Id1>/<int:Id2>", methods=["GET"])
def auth_cachedlogin_forplatformid(Id1, Id2):
    data = auth_API.cachedlogin(Id2)
    return jsonify(data)

@app.route("/auth/eac/challenge", methods=["GET"])
def auth_eac_challenge():
    data = "52e30238-3e90-4025-a7a9-d6cdd66002a1"
    return jsonify(data)

@app.route("/auth/connect/token", methods=["POST"])
def auth_connect_token():
    print(request.form)
    token = auth_API.grantToken(request.form.get("grant_type"), request.form)
    data = {
        "access_token": token["token"],
        "error_description":"",
        "error":"",
        "refresh_token":token["token"],
        "key":""
    }
    return jsonify(data)

@app.route("/auth/cachedlogin/forplatformids", methods=["POST"])
def auth_cachedlogin_forplatformids():
    print(dict(request.form))
    return jsonify([])


@app.route("/accounts/account/create", methods=["POST"])
def accounts_account_create():
    abort(404)
    print(dict(request.form))
    return jsonify({"success":False,"error":"Unable to create an account, steam account is not valid.","value": ""})
    data = accounts_API.create(platform=request.form["platform"], platformId=request.form["platformId"], deviceId=request.form["deviceId"])
    data = {"success":True,"error":"","value":data}
    return jsonify(data)

@app.route("/accounts/account/bulk", methods=["GET"])
def accounts_account_bulk():
    ids = request.args.getlist("id")
    accs = []
    for id in ids:
        acc = accounts_API.getPlayerById(int(id))
        if acc is None:
            continue
        accs.append(acc)
    data = accs
    return jsonify(data)

@app.route("/accounts/account/<int:playerId>", methods=["GET"])
def accounts_account_playerId(playerId):
    acc = accounts_API.getPlayerById(playerId)
    if acc is None:
        return abort(404)
    data = acc
    return jsonify(data)

@app.route("/accounts/account/<int:playerId>/bio", methods=["GET"])
def accounts_account_playerId_bio(playerId):
    acc = accounts_API.getPlayerByIdV2(playerId)
    if acc is None:
        return abort(404)
    data = {"accountId": acc["accountId"], "bio": acc["bio"]}
    return jsonify(data)

@app.route("/api/players/v2/progression/bulk", methods=["GET"])
def api_players_v2_progression_bulk():
    ids = request.args.getlist("id")
    accs = []
    for id in ids:
        acc = accounts_API.getPlayerByIdV2(int(id))
        if acc is None:
            continue
        accs.append({
            "PlayerId": acc["accountId"],
            "Level": acc["Level"],
            "XP": acc["XP"]
        })
    data = accs
    return jsonify(data)

@app.route("/api/playerReputation/v2/bulk", methods=["GET"])
def api_playerReputation_v2_bulk():
    ids = request.args.getlist("id")
    accs = []
    for id in ids:
        acc = accounts_API.getPlayerByIdV2(int(id))
        if acc is None:
            continue
        data = {
            "AccountId": acc["accountId"],
        }
        data.update(acc["Rep"])
        accs.append(data)
    data = accs
    return jsonify(data)

@app.route("/roomserver/rooms/bulk", methods=["GET"])
def roomserver_rooms_bulk():
    ids = request.args.getlist("name")
    rooms = []
    for id in ids:
        room = room_API.getRoomByName(id)
        if room is None:
            continue
        rooms.append(room)
    data = rooms
    return jsonify(data)

@app.route("/accounts/account/me", methods=["GET"])
def accounts_account_me():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerData = accounts_API.getPlayerById(playerData["accountId"])
    data = ""
    return jsonify(playerData)

@app.route("/api/settings/v2/", methods=["GET"])
def api_settings_v2():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\settings.json") as f:
        settings = json.load(f)
    for setting in settings:
        if int(setting["id"]) == int(playerId):
            return jsonify(setting["settingsData"])
    return abort(500)


@app.route("/api/avatar/v3/saved", methods=["GET"])
def api_avatar_v3_saved():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\api\\player\\saved.json") as f:
        saveds = json.load(f)
    for saved in saveds:
        if int(saved["id"]) == int(playerId):
            return jsonify(saved["avatarData"])
    return abort(500)

@app.route("/api/equipment/v2/getUnlocked", methods=["GET"])
def api_equipment_v2_getUnlocked():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\api\\player\\equipment.json") as f:
        equipments = json.load(f)
    for equipment in equipments:
        if int(equipment["id"]) == int(playerId):
            return jsonify(equipment["equipmentsData"])
    return abort(500)

@app.route("/api/consumables/v2/getUnlocked", methods=["GET"])
def api_consumables_v2_getUnlocked():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\api\\player\\consumables.json") as f:
        consumables = json.load(f)
    for consumable in consumables:
        if int(consumable["id"]) == int(playerId):
            return jsonify(consumable["consumablesData"])
    return abort(500)

@app.route("/api/avatar/v2/gifts", methods=["GET"])
def api_avatar_v2_gifts():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\api\\player\\gifts.json") as f:
        gifts = json.load(f)
    for gift in gifts:
        if int(gift["id"]) == int(playerId):
            return jsonify(gift["giftsData"])
    return abort(500)

@app.route("/match/player/heartbeat", methods=["POST"])
def match_player_heartbeat():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\heartbeat.json") as f:
        heartbeats = json.load(f)
    for heartbeat in heartbeats:
        if int(heartbeat["playerId"]) == int(playerId):
            return jsonify(heartbeat)
    return abort(500)

@app.route("/api/avatar/v4/items", methods=["GET"])
def api_avatar_v4_items():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\avatar_items.json") as f:
        avatar_items = json.load(f)
    for avatar_item in avatar_items:
        if int(avatar_item["id"]) == int(playerId):
            with open("json\\defaultunlocked.json") as f:
                defaultunlocked = json.load(f)
            for x in defaultunlocked:
                avatar_item["itemsData"].append(x)
            return jsonify(avatar_item["itemsData"])
    return abort(500)

@app.route("/clubs/club/home/me", methods=["GET"])
def clubs_clube_home_me():
    return jsonify([])

@app.route("/api/avatar/v2", methods=["GET"])
def api_avatar_v2():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\players.json") as f:
        players = json.load(f)
    for player in players:
        if int(player["accountId"]) == int(playerId):
            return jsonify(player["avatarData"])
    return abort(500)

@app.route("/auth/account/me/haspassword", methods=["GET"])
def auth_account_me_haspassword():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\players.json") as f:
        players = json.load(f)
    for player in players:
        if int(player["accountId"]) == int(playerId):
            if player["password"] is None:
                return jsonify(False)
            return jsonify(True)
    return jsonify(), 200

@app.route("/api/avatar/v2/set", methods=["POST"])
def api_avatar_v2_set():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\players.json") as f:
        players = json.load(f)
    for player in players:
        if int(player["accountId"]) == int(playerId):
            player["avatarData"] = request.get_json()
            with open("json\\players.json", "w") as f:
                json.dump(players, f, indent=2)
            return "", 200
    return abort(500)

@app.route("/accounts/account/me/username", methods=["PUT"])
def accounts_account_me_username():
    return jsonify({"success":True,"error":"","value":None}), 200

@app.route("/accounts/account/me/profileimage", methods=["PUT"])
def accounts_account_me_profileimage():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\players.json") as f:
        players = json.load(f)
    for player in players:
        if int(player["accountId"]) == int(playerId):
            player["profileImage"] = request.form["imageName"]
            with open("json\\players.json", "w") as f:
                json.dump(players, f, indent=2)
            return jsonify({"success":True,"error":"","value":None}), 200
    return jsonify({"success":False,"error":"","value":None}), 200

@app.route("/auth/account/me/changepassword", methods=["POST"])
def auth_account_me_changepassword():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    password = request.form["newPassword"]
    password = auth_API.hashString(password)
    with open("json\\players.json") as f:
        players = json.load(f)
    for player in players:
        if int(player["accountId"]) == int(playerId):
            player["password"] = password
            with open("json\\players.json", "w") as f:
                json.dump(players, f, indent=2)
            return jsonify({"success":True,"error":"","value":None}), 200
    return jsonify({"success":False,"error":"","value":None}), 200

@app.route("/api/PlayerReporting/v1/moderationBlockDetails", methods=["GET"])
def api_PlayerReporting_v1_moderationBlockDetails():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    with open("json\\moderationBlockDetails.json") as f:
        moderationBlockDetails = json.load(f)
    for moderationBlockDetail in moderationBlockDetails:
        if int(moderationBlockDetail["playerId"]) == int(playerId):
            return jsonify(moderationBlockDetail)
    return jsonify({"ReportCategory":0,"Duration":0,"GameSessionId":0,"Message":""}), 200

@app.route("/match/player/login", methods=["POST"])
def match_player_login():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    data2 = {
        "content": None,
        "embeds": [
            {
                "title": "Login",
                "description": f"@{playerData['username']} [{playerData['displayName']}] ({playerData['accountId']}) is logging in!",
                "color": 5898927,
                "thumbnail": {
                    "url": f"https://{ProgramUtils.DataURL()}/img/{playerData['profileImage']}?width=256&cropSquare=1"
                }
            }
        ],
        "attachments": []
    }

    requests.post(ProgramUtils.discordWenhook, json=data2)

    data = {
        "access_token": Authorization,
        "error_description":"",
        "error":"",
        "refresh_token":Authorization,
        "key":""
    }
    return jsonify(data)

@app.route("/match/goto/none", methods=["POST"])
def match_goto_none():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    
    with open("json\\heartbeat.json") as f:
        heartbeats = json.load(f)

    for heartbeat in heartbeats:
        if heartbeat["playerId"] == int(playerData["accountId"]):
            heartbeat.update({
                "roomInstance": None,
                "isOnline": True
            })

            with open("json\\heartbeat.json", "w") as f:
                json.dump(heartbeats, f, indent=2)

    data = {
        "access_token": Authorization,
        "error_description":"",
        "error":"",
        "refresh_token":Authorization,
        "key":""
    }
    return jsonify(data)

@app.route("/notify/hub/v1/negotiate", methods=["POST"])
def notify_hub_v1_negotiate():
    url = ProgramUtils.URL()
    url2 = f"https://{url}/notify"
    data = {
        "ConnectionId":"skull",
        "negotiateVersion":0,
        "SupportedTransports":[],
        "url":url2
    }
    return jsonify(data)

@app.route("/notify/negotiate", methods=["POST"])
def notify_negotiate():
    data = {
        "negotiateVersion": 0,
        "connectionId": "notif",
        "availableTransports": [
            {
                "transport": "WebSockets",
                "transferFormats": [
                    "Text",
                    "Binary"
                ]
            }
        ]
    }
    return jsonify(data)

@app.route("/api/relationships/v2/get", methods=["GET"])
def api_relationships_v2_get():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    data = []
    return jsonify(data)

@app.route("/api/messages/v2/get", methods=["GET"])
def api_messages_v2_get():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    data = []
    return jsonify(data)


@app.route("/api/settings/v2/set", methods=["POST"])
def api_settings_v2_set():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    Json = request.get_json()
    key = Json["Key"]
    Value = Json["Value"]
    with open("json\\settings.json", "r") as f:
      PlayerSettings = json.load(f)
    for x in PlayerSettings:
      if x["id"] == playerData["accountId"]:
        for y in x["settingsData"]:
          if y["Key"] == key:
            y["Value"] = Value
            with open("json\\settings.json", "w") as f:
              json.dump(PlayerSettings, f, indent=2)
            return jsonify(PlayerSettings), 200
        x["settingsData"].append({"Key":key,"Value":Value})
        with open("json\\settings.json", "w") as f:
          json.dump(PlayerSettings, f, indent=2)
        return jsonify(PlayerSettings), 200
    return abort(401)


@app.route("/api/PlayerReporting/v1/hile", methods=["POST"])
def api_PlayerReporting_v1_hile():
    return jsonify(False)

@app.route("/roomserver/rooms", methods=["GET"])
def roomserver_rooms():
    Name = request.args["name"]
    room = room_API.getRoomByName(Name)
    print(room)
    if room is None:
        return abort(404)
    return jsonify(room)

@app.route("/roomserver/rooms/<int:roomId>", methods=["GET"])
def roomserver_rooms1(roomId):
    room = room_API.getRoomById(roomId)
    print(room)
    if room is None:
        return abort(404)
    return jsonify(room)

@app.route("/api/objectives/v1/myprogress", methods=["GET"])
def api_objectives_v1_myprogress():
    data = {
        "Objectives": [],
        "ObjectiveGroups": []
    }
    return jsonify(data)

@app.route("/clubs/subscription/mine/member", methods=["GET"])
def clubs_subscription_mine_member():
    data = []
    return jsonify(data)

@app.route("/api/playerevents/v1/all", methods=["GET"])
def api_playerevents_v1_all():
    data = {"Created": [], "Responses": []}
    return jsonify(data)

@app.route("/api/CampusCard/v1/UpdateAndGetSubscription", methods=["POST"])
def api_CampusCard_v1_UpdateAndGetSubscription():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    data = {
        "Subscription":{
            "SubscriptionId": 0,
			"RecNetPlayerId": playerId,
			"PlatformType": 0,
			"PlatformId": 1,
			"PlatformPurchaseId": "0",
			"Level": "Platinum",
			"Period": "Year",
			"ExpirationDate": datetime.datetime.strptime("9999-12-30T23:37:28.553Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
			"IsAutoRenewing": True,
			"CreatedAt": ProgramUtils.getCurrentTime(),
			"ModifiedAt": ProgramUtils.getCurrentTime(),
			"IsActive": True
        },
        "CanBuySubscription": True,
        "PlatformAccountSubscribedPlayerId": playerId
    }
    return jsonify(data)

@app.route("/api/roomkeys/<path:path>", methods=["GET"])
def api_roomkeys(path):
    return jsonify([])

@app.route("/match/goto/room/<RoomName>", methods=["POST"])
def match_goto_room(RoomName):
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    room = room_API.getRoomByName(RoomName, playerId=playerData["accountId"])
    if room is None:
        return abort(404)
    roomInstanceId = random.randint(100000000, 999999999)
    if str(room["Name"]).lower() == "dormroom":
        name = f"@{playerData['username']}'s DormRoom"
    else:
        name = room["Name"]
    localRoomInstance = {
        "roomInstanceId":roomInstanceId,
        "roomId":room["RoomId"],
        "subRoomId":room["SubRooms"][0]["SubRoomId"],
        "location":room["SubRooms"][0]["UnitySceneId"],
        "roomInstanceType":0,
        "photonRegionId":"us",
        "photonRegion":"us",
        "photonRoomId":"OldRecRoom2022-" + room["Name"] + str(room["SubRooms"][0]["SubRoomId"]) + str(room["RoomId"]),
        "name":name,
        "maxCapacity":4,
        "isFull":False,
        "isPrivate":False,
        "isInProgress":False,
        "matchmakingPolicy":0
    }

    with open("json\\heartbeat.json") as f:
        heartbeats = json.load(f)

    for heartbeat in heartbeats:
        if heartbeat["playerId"] == int(playerData["accountId"]):
            heartbeat.update({
                "roomInstance": localRoomInstance,
                "isOnline": True
            })

            with open("json\\heartbeat.json", "w") as f:
                json.dump(heartbeats, f, indent=2)

    data2 = {
        "content": None,
        "embeds": [
            {
                "title": "Matchmaking",
                "description": f"@{playerData['username']} [{playerData['displayName']}] ({playerData['accountId']}) is joining the room \"{localRoomInstance['name']}\"",
                "color": 5898927,
                "thumbnail": {
                    "url": f"https://{ProgramUtils.DataURL()}/img/{room['ImageName']}?width=256&cropSquare=1"
                }
            }
        ]
    }
    requests.post(ProgramUtils.discordWenhook, json=data2)
    return jsonify({
        "errorCode": 0,
        "roomInstance": localRoomInstance
    })

@app.route("/auth/role/developer/<int:playerId>", methods=["GET"])
def auth_role_developer(playerId):
    player = accounts_API.getPlayerById(playerId)
    if player is None:
        return abort(404)
    return jsonify(player["isDeveloper"])
    
@app.route("/api/sanitize/v1/isPure", methods=["POST"])
def api_sanitize_v1_isPure():
    return jsonify({"IsPure":True})

@app.route("/roomserver/rooms/3/tags", methods=["PUT"])
def api_sanitize_v1_isPure1():
    print(request.form)
    return jsonify([])

@app.route("/storage/upload", methods=["POST"])
def storage_upload():
    FileType = request.form["FileType"]
    print(FileType)
    if int(FileType) == 6:
        name = f"cdn\\room\\{ProgramUtils.randomString(70)}.room"
        request.files["File"].save(name)
        return jsonify({"FileName": name})
    return abort(404)

@app.route("/api/storefronts/v4/balance/<Id>", methods=["GET"])
def api_storefronts_v4_balance(Id):
    return jsonify({
        "Balance": 999999,
        "CurrencyType": int(Id)
    })
    return abort(404)

@app.route("/api/images/v4/uploadsaved", methods=["POST"])
def api_images_v4_uploadsaved():
    Authorization = request.headers.get("Authorization")
    token = jwt.decode(Authorization.split("Bearer ")[1], algorithms=["HS256"])
    playerData = auth_API.getPlayerByAuthorization(token["Authorization"])
    if playerData is None:
        return abort(401)
    playerId = playerData["accountId"]
    nameStr = ProgramUtils.randomString(25)
    name = f"{playerId}\\{nameStr}.png"
    name2 = f"{playerId}/{nameStr}.png"
    request.files["image"].save(f"img\\player\\{name}")
    data2 = {
        "content": None,
        "embeds": [
            {
                "title": "Images",
                "description": f"@{playerData['username']} [{playerData['displayName']}] ({playerData['accountId']}) has shared an image!",
                "color": 5898927,
                "image": {
                    "url": f"https://{ProgramUtils.DataURL()}/img/player/{name2}?width=256&cropSquare=1"
                }
            }
        ]
    }
    requests.post(ProgramUtils.discordWenhook, json=data2, verify=False)

    return jsonify({
        "ImageName": f"player\\{name}"
    })

@app.route("/api/sanitize/v1", methods=["POST"])
def api_sanitize_v1():
    return jsonify(request.get_json()["Value"])



@sock.route("/notify")
def notify(ws):
    while True:
        data = ws.receive()
        print("received data: " + str(data))
        ws.send(data)
    


def run():
    Port = 27614
    Ip = "0.0.0.0"
    app.run(str(Ip), int(Port))