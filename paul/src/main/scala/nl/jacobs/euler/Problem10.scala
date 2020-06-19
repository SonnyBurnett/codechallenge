package nl.jacobs.euler

object Problem10 extends App with Timer with Prime {
  lazy val stream: Stream[Int] = 2 #:: Stream.from(3).filter(i => isPrime(i))
  val (result, time) = profile {
    stream.takeWhile(_ < 2000000).foldLeft(0L)(_ + _)
  }
  println(s"result:[$result] took [$time] ms")
}