const apiURL = "https://8cwsd764-9873.uks1.devtunnels.ms/"
const imgURL = "https://8cwsd764-9873.uks1.devtunnels.ms/img/"

var Img
var PlayerUsername

let num = 0



function UpdateImg() {
  Imgl = document.getElementsByTagName("body")[0]
  Imgl.style.backgroundImage = "url(" + Img + ")"
}

function GetPlayer(PlayerName, RoomName) {
  div1 = document.getElementById("PlayerData")
  Text = div1.getElementsByTagName("h3")[0]

  Text.innerHTML = "This image was made by " + PlayerName + " in " + RoomName
}

function Getimg() {
  f = fetch(apiURL + "api/images/web/v1/slideshow",).then((a) => 
    {a.json().then((response) => {
      response.Images.forEach(element => {
        num = num + 1
      })
      num = Math.floor(Math.random() * num)
      PlayerUsername = response.Images[num].Username
      Img = imgURL + response.Images[num].ImageName
      UpdateImg()
      if (true == true) {
        GetPlayer(PlayerUsername, response.Images[num].RoomName)
      }
    })
  })
}

