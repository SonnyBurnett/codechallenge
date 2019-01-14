package nl.jacobs.euler

object Problem3 extends App with Timer with Factors {
  //The prime factors of 13195 are 5, 7, 13 and 29.
  //What is the largest prime factor of the number 600851475143 ?

  val (result, time) = profile(factors(600851475143l).last)
  println(s"result:[$result] took [$time] ms")
}