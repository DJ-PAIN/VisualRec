import json
import os
from VisualRec import ProgramUtils, room_API

def create(platform, platformId: int, deviceId):
    name = ProgramUtils.randomString(15)
    with open("json\\players.json") as f:
        players = json.load(f)

    for player in players:
        if player["platformId"] == int(platformId):
            return "err1"
        
    nextAvailableId = max([player["accountId"] for player in players]) + 1
    
    newPlayer = {
        "platformId": int(platformId),
        "deviceId": deviceId,
        "accountId": nextAvailableId,
        "username": name,
        "displayName": name,
        "Level": 1,
        "XP": 0,
        "bannerImage": None,
        "personalPronouns": 0,
        "identityFlags": 0,
        "createdAt": ProgramUtils.getCurrentTime(),
        "isDeveloper": False,
        "password": None,
        "isJunior": False,
        "bio": None,
        "platforms":1,
        "profileImage": "DefaultProfileImage",
        "lastLoginTime": ProgramUtils.getCurrentTime(),
        "Rep": {
            "IsCheerful": True,
            "Noteriety": 0.0,
            "SelectedCheer": 0,
            "CheerCredit": 0,
            "CheerGeneral": 0,
            "CheerHelpful": 0,
            "CheerCreative": 0,
            "CheerGreatHost": 0,
            "CheerSportsman": 0
        },
        "Authorization": ProgramUtils.randomString(800),
        "avatarData": {
            "OutfitSelections": "21599b51-c50f-43d8-ac5f-62c30cd02ca5,,,,0;21caa68e-c3fa-474c-af5e-af1e742b7a60,,,,1",
            "FaceFeatures": "{\"ver\":5,\"eyeId\":\"7szdCr_Q00-c50QJ1rLvxg\",\"eyePos\":{\"x\":0.003236842341721058,\"y\":0.006024859845638275},\"eyeScl\":-0.0020316801965236665,\"mouthId\":\"pc1z8k98X0ae0Nab-IKhfA\",\"mouthPos\":{\"x\":0.019394949078559877,\"y\":0.018625065684318544},\"mouthScl\":-0.0012852326035499573,\"hairPrimaryColorId\":\"befcc00a-a2e6-48e4-864c-593d57bbbb5b\",\"hairSecondaryColorId\":\"f9a50d3d-a6e0-42a4-a4e3-42dc89f84a2e\",\"hairPatternId\":\"OigHQzfNaUao_EhQTNQbfg\",\"beardColorId\":\"f9a50d3d-a6e0-42a4-a4e3-42dc89f84a2e\",\"beardSecondaryColorId\":\"befcc00a-a2e6-48e4-864c-593d57bbbb5b\",\"faceShapeId\":\"yR4oYZr_AUSynXCgwS2lGw\",\"bodyShapeId\":\"5QIIhNQVwE-E_cxtXSKCfw\",\"useHatAnchorParams\":true,\"hideEars\":true,\"hatAnchorParams\":{\"NormalizedPosition\":{\"x\":0.5,\"y\":0.5},\"HemisphereOffsets\":{\"x\":0.0,\"y\":0.0,\"z\":0.0},\"HemisphereRotations\":{\"x\":0.0,\"y\":0.0,\"z\":0.0}}}",
            "SkinColor": "Xac-W_R330KfOz-pQla9qg",
            "HairColor": "3Q8U6E5pV0uzK141ut2WBg"
        }
    }

    newSettings = {
        "id": nextAvailableId,
        "settingsData": [
            {
                "Key": "Recroom.AccountCreation.HasStarted",
                "Value": "True"
            },
            {
                "Key": "Recroom.AccountCreation.HasFinished",
                "Value": "False"
            },
            {
                "Key": "Recroom.AccountCreation.HasChosenUsername",
                "Value": "False"
            },
            {
                "Key": "Recroom.AccountCreation.HasCreatedPassword",
                "Value": "False"
            },
            {
                "Key": "USE_NEW_HOME_SCREEN",
                "Value": "True"
            },
            {
                "Key": "TUTORIAL_COMPLETE_MASK",
                "Value": "57"
            },
            {
                "Key": "RRUI_THEME",
                "Value": "1"
            },
            {
                "Key": "HAS_SEEN_HOME_SCREEN_CHOICE",
                "Value": "True"
            },
            {
                "Key": "SplitTestAssignedSegments",
                "Value": "1|{\"SplitTesting+RudderStackAnalyticsDestinations_2022_02_10\":\"Disabled\",\"SplitTesting+Consolidated_Info_Account_Creation_NonJr_2022_01_10\":\"Phone\",\"SplitTesting+ParallelNetworkingInitialRoomLoad_2021_06_28\":\"ParallelLoad\",\"SplitTesting+ProfileOnClick_2021_04_30\":\"Off\",\"SplitTesting+DefaultNewPlayersToPlayMenu_2021_05_24\":\"On\",\"SplitTesting+RoomJackpot_2021_11_16\":\"ChanceThenHighlightDefault5Min\",\"SplitTesting+RoomJackpot_V2_E1_2021_12_01\":\"DynamicPlaylists\",\"SplitTesting+UseSets_2021_08_06\":\"UseSets\",\"SplitTesting+RoomSimilarities_2021_10_29\":\"Off\"}"
            }
        ]
    }

    newHeartbeat = {
        "playerId":nextAvailableId,
        "statusVisibility":3,
        "platform":-1,
        "deviceClass":0,
        "vrMovementMode":0,
        "roomInstance":None,
        "lastOnline":ProgramUtils.getCurrentTime(),
        "isOnline":True,
        "appVersion":20210804
    }

    newAvatar_items = {
        "id": nextAvailableId,
        "itemsData": []
    }

    newSaved = {
      "id": nextAvailableId,
      "avatarData": []
    }

    newGifts =  {
      "id": nextAvailableId,
      "giftsData": []
    }

    newEquipment = {
      "id": nextAvailableId,
      "equipmentsData": []
    }

    newConsumable = {
      "id": nextAvailableId,
      "consumablesData": []
    }

    os.mkdir(f"img\\player\\{nextAvailableId}")
    
    if room_API.ClonDormRoom(nextAvailableId):
        pass
    else:
        return "err500"
    
    try:
        with open("json\\settings.json") as f:
            settings = json.load(f)
        with open("json\\heartbeat.json") as f:
            heartbeat = json.load(f)
        with open("json\\Avatar_items.json") as f:
            Avatar_items = json.load(f)
        with open("json\\api\\player\\saved.json") as f:
            saved = json.load(f)
        with open("json\\api\\player\\gifts.json") as f:
            gifts = json.load(f)
        with open("json\\api\\player\\equipment.json") as f:
            equipment = json.load(f)
        with open("json\\api\\player\\consumables.json") as f:
            consumables = json.load(f)
        players.append(newPlayer)
        settings.append(newSettings)
        heartbeat.append(newHeartbeat)
        Avatar_items.append(newAvatar_items)
        saved.append(newSaved)
        gifts.append(newGifts)
        equipment.append(newEquipment)
        consumables.append(newConsumable)
    except:
        return "err500"
    try:
        with open("json\\players.json", "w") as f:
            json.dump(players, f, indent=2)
        with open("json\\settings.json", "w") as f:
            json.dump(settings, f, indent=2)
        with open("json\\heartbeat.json", "w") as f:
            json.dump(heartbeat, f, indent=2)
        with open("json\\Avatar_items.json", "w") as f:
            json.dump(Avatar_items, f, indent=2)
        with open("json\\api\\player\\saved.json", "w") as f:
            json.dump(saved, f, indent=2)
        with open("json\\api\\player\\gifts.json", "w") as f:
            json.dump(gifts, f, indent=2)
        with open("json\\api\\player\\equipment.json", "w") as f:
            json.dump(equipment, f, indent=2)
        with open("json\\api\\player\\consumables.json", "w") as f:
            json.dump(consumables, f, indent=2)
    except:
        return "err500"
    return newPlayer

def getPlayerById(Id: int):
    with open("json\\players.json") as f:
        players = json.load(f)

    for player in players:
        del player["deviceId"]
        del player["platformId"]
        del player["Level"]
        del player["XP"]
        del player["lastLoginTime"]
        del player["Rep"]
        del player["Authorization"]
        del player["bio"]
        del player["password"]
        del player["avatarData"]
        if player["accountId"] == Id:
            return player
    return None

def getPlayerByIdV2(Id: int):
    with open("json\\players.json") as f:
        players = json.load(f)

    for player in players:
        if player["accountId"] == Id:
            return player
    return None