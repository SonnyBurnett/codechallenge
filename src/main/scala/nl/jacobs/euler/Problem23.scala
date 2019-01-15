package nl.jacobs.euler

object Problem23 extends App with Timer {
  def divisor(n: Int) = {
    (1 to n / 2).filter(n % _ == 0).sum
  }

  val (result, time) = profile {
    val abundant = (0 to 28123).map(divisor).zipWithIndex.filter(p => p._1 > p._2).map(_._2)
    val exclude = {
      (for (i <- 0 until abundant.size; j <- 0 until abundant.size; val sum = abundant(i) + abundant(j)) yield (sum))
    }
    (1 to 28123 diff exclude).sum
  }
  println(s"result:[$result] took [$time] ms")
}
