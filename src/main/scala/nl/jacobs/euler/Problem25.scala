package nl.jacobs.euler

object Problem25 extends App with Timer {
  lazy val stream: Stream[BigInt] = BigInt(0) #:: stream.scanLeft(BigInt(1))(_ + _)

  val (result, time) = profile {
    stream.indexOf(stream.filter(_.toString().length() > 999).head)
  }

  println(s"result:[$result] took [$time] ms")
}