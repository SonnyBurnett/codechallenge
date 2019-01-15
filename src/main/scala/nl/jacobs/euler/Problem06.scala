package nl.jacobs.euler

import java.util.stream.IntStream

object Problem06 extends App with Timer {
  val numbers = 1 to 100
  def square(n: Int) = n * n

  val (result, time) = profile(square(numbers.sum) - numbers.map(square).sum)

  println(s"result:[$result] took [$time] ms")
}