package nl.jacobs.euler

object Problem1 extends App with Timer {
  val (result, time) = profile {
    (1 until 1000).filter(n => n % 3 == 0 || n % 5 == 0).sum
  }
  println(s"result:[$result] took [$time] ms")
}