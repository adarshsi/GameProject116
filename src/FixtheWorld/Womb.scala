package FixtheWorld

import play.api.libs.json.{JsValue, Json}


class Womb {

  var players: Map[String, Sperm] = Map()


  var lastUpdateTime: Long = System.nanoTime()



  def gameState(): String = {
    val gameState: Map[String, JsValue] = Map(
      "players" -> Json.toJson(this.players.map({ case (k, v) => Json.toJson(Map(
        "sprmlft" -> Json.toJson(v.location.sprmlft),
        "sprmrgt" -> Json.toJson(v.location.sprmrght),
        "username" -> Json.toJson(k))) }))
    )

    Json.stringify(Json.toJson(gameState))
  }



}
