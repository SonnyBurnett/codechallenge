package nl.jacobs.euler

object Problem21 extends App with Timer {

  def divisor(n: Int) = {
    (1 to n / 2).filter(n % _ == 0).sum
  }

  val (result, time) = profile {
    (for (
      i <- 1 to 10000;
      val x = divisor(i) if (divisor(x) == i && i != x)
    ) yield (i))sum
  }
  println(s"result:[$result] took [$time] ms")
}