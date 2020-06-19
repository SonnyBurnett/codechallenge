package nl.jacobs.euler

object Problem05 extends App with Timer {
  //2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
  //What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

  val (result, time) = profile {
    Range(20, Int.MaxValue).find(n => Range(2, 21).forall(n % _ == 0)).get
  }
  println(s"result:[$result] took [$time] ms")
}