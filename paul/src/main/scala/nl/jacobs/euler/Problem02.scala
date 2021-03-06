package nl.jacobs.euler

object Problem02 extends App with Timer {
  lazy val stream: Stream[Int] = 0 #:: stream.scanLeft(1)(_ + _)
  val (result, time) = profile { 
    stream.takeWhile(_ <= 4000000).filter(_ % 2 == 0).sum 
    }
  println(s"result:[$result] took [$time] ms")
}