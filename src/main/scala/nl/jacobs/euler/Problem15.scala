package nl.jacobs.euler

object Problem15 extends App with Timer {
  val (result, time) = profile {
    val faculty20 = (BigInt(1) to BigInt(20)) reduceLeft (_ * _)
    val faculty40 = (BigInt(1) to BigInt(40)) reduceLeft (_ * _)
     faculty40 / faculty20.pow(2)
  }
  println(s"result:[$result] took [$time] ms")
}