package FixtheWorld

// Received by Multiple Types
case object SendGameState
case class GameState(gameState: String)


case object UpdateGame
case class newsprm(username: String)
case class movesprm(username: String, sprmleft: Double, sprmrigt:Double)
case class removesprm(username:String)



