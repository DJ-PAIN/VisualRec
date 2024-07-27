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
import cv2

from VisualRec import ProgramUtils, auth_API, accounts_API, room_API, image_API

time = ProgramUtils.getCurrentTime()

name = f"{__name__}.py"

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
sock = Sock(app)
CORS(app)

@app.errorhandler(404)
def q405(e):
    return render_template("404.html"), 404

@app.errorhandler(405)
def q405(e):
    data = ""
    return data, 405

@app.errorhandler(500)
def q405(e):
    data = {"Message":"An error has occurred."}
    return jsonify(data), 500

@app.route("/img/<path:img>", methods=["GET"])
def img(img):
    if os.path.exists(f"img\\{img}"):
        try:
            img__ = cv2.imread(f"img\\{img}")

            #if request.args.get("cropSquare") == "1":
            #   pass
            return Response(cv2.imencode(".png", img__)[1].tobytes(), 200, content_type="image/png", headers={"content-signature": "key-id=KEY:RSA:p1.rec.net; data=IWwe/pZ5vWWqNSkSM/54isgDxlZkdrP0sUrppKCbNktO2yCOTjq746xWiiLsueGuVcAGQqkjeRTimxolHckS/YXSYkEJxtiCXbLlsRia2DyAqtWVkGWsfczzFhp/56U66FVzolTspPCvjScOVlGO7dDIK7sJ+ndcRauWjsQsC6g3e7rUc6uwY099a6gy7sw6xr5BFZQSz8wg+fqyHYD/Sc4nQQVOTFZNNASqbJYhpNhEMXRnafCMuLl8a3mkGwvy3t4q2D/7SM48xrGZjEV47qNx1A91KCe28XVToFh4BzwEUU8nZ0d+KwV79MGarLo1cY8igc8FcoThKcovI4ClOg=="})
        except:
            return abort(500)
    else:
        return "", 404

        

@app.route("/css/<cssName>", methods=["GET"])
def css(cssName):
  cssName = cssName + ".css"
  if not os.path.exists(f"web\\css\\/{cssName}"):
    return "", 404
  with open(f"web\\css\\{cssName}", "rb") as f:
    return Response(f.read(), mimetype='text/css')


@app.route("/js/<path:jsName>", methods=["GET"])
def js(jsName):
  jsName = jsName + ".js"
  if os.path.exists(F"web\\js\\{jsName}"):
    with open(F"web\\js\\{jsName}", "rb") as f:
      return Response(f.read(), 200, content_type="text/javascript")
    
@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/admin/login", methods=["GET"])
def admin_login():
    return render_template("admin/login.html")

@app.route("/", methods=["GET"])
def index():
    return render_template("home.html")
        

@app.route("/api/images/web/v1/slideshow", methods=["GET"])
def api_images_web_v1_slideshow():
    return jsonify(image_API.getSlideshow())
    

@app.route("/cdn/room/<DataBlob>", methods=["GET"])
def cdn_room(DataBlob):
    if os.path.exists(f"cdn\\room\\{DataBlob}"):
        try:
            with open(f"cdn\\room\\{DataBlob}", "rb") as f:
                return Response(f.read(), 200, content_type="application/octet-stream")
        except:
            return abort(500)
    else:
        return "", 404
    
@app.route("/cdn/video/<DataBlob>", methods=["GET"])
def cdn_video(DataBlob):
    if os.path.exists(f"cdn\\video\\{DataBlob}"):
        try:
            with open(f"cdn\\video\\{DataBlob}", "rb") as f:
                return Response(f.read(), 200, content_type="video/mp4")
        except:
            return abort(500)
    else:
        return "", 404
    
@app.route("/api/web/v1/login", methods=["POST"])
def api_web_v1_login():
    json1 = request.get_json()
    password_hash = auth_API.hashString(json1["password"])
    username = json1["username"]

    with open("json\\players.json") as f:
        players = json.load(f)
    
    for player in players:
        if player["username"] == username:
            if player["password"] == password_hash:
                data = {"account_id": player["accountId"]}
                session["token"] = auth_API.grantToken("web_login", data)["token"]
                return jsonify({"success":True,"error":""}), 200
    return jsonify({"success":False,"error":"Login failed. Please check your credentials."}), 401

@app.route("/api/admin/v1/login", methods=["POST"])
def api_admin_v1_login():
    json1 = request.get_json()
    password_hash = auth_API.hashString(json1["password"])
    username = json1["username"]

    with open("json\\players.json") as f:
        players = json.load(f)
    
    for player in players:
        if player["username"] == username:
            if player["password"] == password_hash:
                data = {"account_id": player["accountId"]}
                session["token"] = auth_API.grantToken("web_login", data)["token"]
                return jsonify({"success":True,"error":""}), 200
    return jsonify({"success":False,"error":"Login failed. Please check your credentials."}), 401


    
@app.route("/cdn/config/LoadingScreenTipData", methods=["GET"])
def cdn_config_LoadingScreenTipData():
    data = [
        {
            "Name":"a21b995fcddf4edc8b1ab5ec79474e49",
            "Title":"Welcome to your Dorm Room!",
            "Message":"Check out your own personal space!",
            "RoomNames":["dormroom"],
            "Context":3,
            "InputType":0,
            "Visibility":1,
            "AllowCycling":False,
            "RestrictToNewUsers":False,
            "ImageName":"lob2a1gpoxeyo68lz97c7hacj.png",
            "PlatformMask":239,
            "CreatedAt":time
        },
        {
            "Name":"86752231820d457c8814e1be5556a04b",
            "Title": "Welcome to Rec Room",
            "Message": "Let's see what Rec Room is all about. Head inside to start playing!",
            "RoomNames":["orientation"],
            "Context":3,
            "InputType":0,
            "Visibility":1,
            "AllowCycling":False,
            "RestrictToNewUsers":False,
            "ImageName":"4w0178z2j8fadgpr1gkph0hw0.png",
            "PlatformMask":239,
            "CreatedAt":time
        },
        {
            "Name":"20d32b1739c44f5d94d32ab2daaf0304",
            "Title":"OldRecRoom for 2021",
            "Message":"",
            "RoomNames":[],
            "Context":3,
            "InputType":0,
            "Visibility":1,
            "AllowCycling":False,
            "RestrictToNewUsers":False,
            "ImageName":"player\\2\\bmew46v5siafo222xspw7npzq.png",
            "PlatformMask":239,
            "CreatedAt":time
        }
    ]
    return jsonify(data)


def run():
    Port = 9873
    Ip = "0.0.0.0"
    app.run(str(Ip), int(Port))