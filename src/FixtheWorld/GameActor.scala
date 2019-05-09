package FixtheWorld

import akka.actor.{Actor, ActorRef}


class GameActor extends Actor {

  var players: Map[String, ActorRef] = Map()
  val wmb: Womb = new Womb


  override def receive: Receive = {
    case message: newsprm => wmb.players += (message.username -> new Sperm(loc = new sprmlocation(0, 0)))
    case message: removesprm => wmb.players -= message.username
    case message: movesprm => wmb.players(message.username).location.sprmrght = this.wmb.players(message.username).location.sprmrght
      wmb.players(message.username).location.sprmlft = this.wmb.players(message.username).location.sprmlft

  }
}
