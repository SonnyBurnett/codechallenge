package nl.jacobs.euler

import scala.BigInt

object Problem16 extends App with Timer {
  val (result, time) = profile {
	  BigInt(2).pow(1000).toString().map(_.asDigit).sum
  }
  println(s"result:[$result] took [$time] ms")
}