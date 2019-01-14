package nl.jacobs.euler

object Problem12 extends App with Timer {
  def count(num: Int) = {
    2 + ((for (i <- 2 to math.sqrt(num).toInt if num % i == 0) yield (i)).size * 2)
  }

  lazy val triangular: Stream[Int] = Stream.from(2).scanLeft(1)(_ + _)

  val (result, time) = profile {
    triangular.filter(i => count(i) > 500).head
  }
  println(s"result:[$result] took [$time] ms")

}