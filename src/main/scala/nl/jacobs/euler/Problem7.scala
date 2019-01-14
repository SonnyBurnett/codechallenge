package nl.jacobs.euler

import scala.util.control.Breaks

object Problem7 extends App with Timer with Prime {
  def nextPrimeFrom(n: Int) = Iterator.from(n + 1).find(isPrime).get

  val (result, time) = profile {
	  val primes = Iterator.iterate(2)(nextPrimeFrom)
    primes.drop(10000).next();
  }
  println(s"result:[$result] took [$time] ms")
}