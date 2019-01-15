package nl.jacobs.euler

object Problem09 extends App with Timer {
  //There exists exactly one Pythagorean triplet for which a + b + c = 1000.
  //Find the product abc.

  val (result, time) = profile {
    (for (
      a <- 1 to 1000;
      b <- 1 to (1000 - a);
      c = 1000 - a - b if (a + b + c == 1000);
      if ((a * a + b * b) == c * c)
    ) yield (a * b * c)).head
  }

  println(s"result:[$result] took [$time] ms")
}