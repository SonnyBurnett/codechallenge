package nl.jacobs.euler

object Problem20 extends App with Timer {
  val (result, time) = profile {
    ((BigInt(1) to BigInt(100)) reduceLeft (_ * _)).toString.map(_.asDigit).sum
  }
  println(s"result:[$result] took [$time] ms")
}