package nl.jacobs.euler

object Problem04 extends App with Timer {

  val (result, time) = profile {
    (for (
      i <- 100 to 999;
      j <- 100 to 999;
      val x = (i * j);
      if (x.toString == x.toString.reverse)
    ) yield (x)).max
  }
  println(s"result:[$result] took [$time] ms")
}