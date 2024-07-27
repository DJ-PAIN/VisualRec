import json
from VisualRec import ProgramUtils

def getRoomByName(Name: str, playerId=0):
    with open("json\\Room\\Rooms.json") as f:
        Rooms = json.load(f)
    for x in Rooms:
        if x["Name"].lower() == "dormroom":
            if not x["CreatorAccountId"] == int(playerId):
                continue
            if x["Name"].lower() == Name.lower():
                SubRooms = []
                with open("json\\Room\\SubRooms.json") as f:
                    SubRooms1 = json.load(f)
                for y in SubRooms1:
                    if y["RoomId"] == x["RoomId"]:
                        SubRooms.append(y)
                x.update({"SubRooms": SubRooms})
                return x
        if x["Name"].lower() == Name.lower():
            SubRooms = []
            with open("json\\Room\\SubRooms.json") as f:
                SubRooms1 = json.load(f)
            for y in SubRooms1:
                if y["RoomId"] == x["RoomId"]:
                    SubRooms.append(y)
            x.update({"SubRooms": SubRooms})
            return x
    return None

def getRoomsByTag(tag: str):
    Rooms2 = []
    with open("json\\Room\\Rooms.json") as f:
        Rooms = json.load(f)
    for x in Rooms:
        for tag1 in x["Tags"]:
            if tag1["Tag"] == tag:
                SubRooms = []
                with open("json\\Room\\SubRooms.json") as f:
                    SubRooms1 = json.load(f)
                for y in SubRooms1:
                    if y["RoomId"] == x["RoomId"]:
                        SubRooms.append(y)
                x.update({"SubRooms": SubRooms})
                Rooms2.append(x)
    return Rooms2

def getRoomById(Id: int):
    with open("json\\Room\\Rooms.json") as f:
        Rooms = json.load(f)
    for x in Rooms:
        if x["RoomId"] == Id:
            SubRooms = []
            with open("json\\Room\\SubRooms.json") as f:
                SubRooms1 = json.load(f)
            for y in SubRooms1:
                if y["RoomId"] == x["RoomId"]:
                    SubRooms.append(y)
            x.update({"SubRooms": SubRooms})
            return x
    return None

def ClonDormRoomOLD(playerId: int):
    with open("json\\Room\\Rooms.json") as f:
        Rooms = json.load(f)

    nextAvailableId = max([room["RoomId"] for room in Rooms]) + 1

    for x in Rooms:
        if x["RoomId"] == 1:
            x.update({
                "RoomId": nextAvailableId,
                "CreatorAccountId": playerId,
                "CreatedAt": ProgramUtils.getCurrentTime()
            })
            x["Roles"][0].update({
                "AccountId": playerId
            })
            with open("json\\Room\\SubRooms.json") as f:
                SubRooms = json.load(f)
            nextAvailableId1 = max([SubRoom["RoomId"] for SubRoom in SubRooms]) + 1

            for y in SubRooms:
                if y["SubRoomId"] == 1:
                    y.update({
                        "SubRoomId": nextAvailableId1,
                        "RoomId": nextAvailableId
                    })

            
            SubRooms.append(y)
            Rooms.append(x)

            #with open("json\\Room\\Rooms.json", "w") as f:
            #    json.dump(Rooms, f, indent=2)

            #with open("json\\Room\\SubRooms.json", "w") as f:
            #    json.dump(SubRooms, f, indent=2)


            return [SubRooms, Rooms]
    return False

    print(DormRoom)

def ClonDormRoom(playerId: int):
    with open("json\\Room\\Rooms.json") as f:
        Rooms = json.load(f)

    with open("json\\Room\\SubRooms.json") as f:
        SubRooms = json.load(f)

    nextAvailableId = max([room["RoomId"] for room in Rooms]) + 1
    nextAvailableId1 = max([SubRoom["SubRoomId"] for SubRoom in SubRooms]) + 1

    newRoom ={
        "Accessibility": 2,
        "CloningAllowed": False,
        "CreatedAt": ProgramUtils.getCurrentTime(),
        "CreatorAccountId": playerId,
        "CustomWarning": "",
        "DataBlob": None,
        "Description": "Your private room",
        "DisableMicAutoMute": False,
        "DisableRoomComments": False,
        "EncryptVoiceChat": False,
        "ImageName": "lob2a1gpoxeyo68lz97c7hacj.png",
        "IsDorm": True,
        "IsRRO": False,
        "LoadScreenLocked": False,
        "LoadScreens": [],
        "MaxPlayerCalculationMode": 1,
        "MaxPlayers": 4,
        "MinLevel": 0,
        "Name": "DormRoom",
        "PromoExternalContent": [],
        "PromoImages": [],
        "Roles": [
        {
            "AccountId": playerId,
            "Role": 255,
            "InvitedRole": 0
        }
        ],
        "RoomId": nextAvailableId,
        "State": 0,
        "Stats": {
            "CheerCount": 0,
            "FavoriteCount": 0,
            "VisitorCount": 0,
            "VisitCount": 0
        },
        "SupportsJuniors": True,
        "SupportsLevelVoting": False,
        "SupportsMobile": True,
        "SupportsQuest2": True,
        "SupportsScreens": True,
        "SupportsTeleportVR": True,
        "SupportsVRLow": True,
        "SupportsWalkVR": True,
        "Tags": [],
        "Version": 0,
        "WarningMask": 0
    }

    newSubRoom = {
        "SubRoomId": nextAvailableId1,
        "RoomId": nextAvailableId,
        "Name": "Home",
        "DataBlob": "",
        "IsSandbox": True,
        "MaxPlayers": 4,
        "Accessibility": 1,
        "UnitySceneId": "76d98498-60a1-430c-ab76-b54a29b7a163",
        "SavedByAccountId": -1
  }
    
    Rooms.append(newRoom)
    SubRooms.append(newSubRoom)

    with open("json\\Room\\Rooms.json", "w") as f:
        json.dump(Rooms, f, indent=2)

    with open("json\\Room\\SubRooms.json", "w") as f:
       json.dump(SubRooms, f, indent=2)

    return True
