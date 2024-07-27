import json
from VisualRec import ProgramUtils, room_API, accounts_API

def getSlideshow(web=True):
    with open("json\\api\\images\\images.json") as f:
        images = json.load(f)
    slideshow = {
        "Images": [

        ]
    }
    for image in images:
        if not web:
            ImageName = str(image["ImageName"])
            ImageName = ImageName.replace("/", "\\")
            image["ImageName"] = ImageName

        playerdata = accounts_API.getPlayerById(int(image["PlayerId"]))
        roomdata = room_API.getRoomById(image["RoomId"])

        slideshow["Images"].append({
            "SavedImageId": image["Id"],
            "ImageName": image["ImageName"],
            "Username": playerdata["username"],
            "RoomName": roomdata["Name"]
        })
    return slideshow

def getImageById(id: int, web=True):
    with open("json\\api\\images\\images.json") as f:
        images = json.load(f)
    
    for image in images:
        if image["Id"] == id:
            if not web:
                ImageName = str(image["ImageName"])
                ImageName = ImageName.replace("/", "\\")
                image["ImageName"] = ImageName
            return image
    return None

#/api/images/v1/slideshow