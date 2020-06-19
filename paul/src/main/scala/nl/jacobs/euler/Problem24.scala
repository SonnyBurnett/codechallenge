package nl.jacobs.euler

import scala.collection.mutable.ArrayBuffer

object Problem24 extends App with Timer {

  def factorial(n: BigInt) = {
    if (n.toInt < 2) {
      n
    } else {
      (BigInt(1) to n) reduceLeft (_ * _)
    }
  }

  def calculate(input: ArrayBuffer[Int], remainder: Int): Int = {
    val f = factorial(input.length - 1)
    println(s"Starting met $remainder    $input $f")

    val toRemove = (for (i <- 0 until input.length; val x = input(i); val temp = (input(i) * f); if (temp < remainder)) yield (Tuple3(i, x, temp)))

    println(toRemove)
    val remove = toRemove.max
    val newRemainder = remainder - remove._3
    println(newRemainder)
    //input.remove(remove._1)
    println(input)
    println("======================")
    calculate(input, newRemainder.toInt)

    //    val newRemainder = (remainder - (input(toRemove) * f)).toInt
    //    print(input(toRemove))
    //    input.remove(toRemove)
    //    input(toRemove) + calculate(input, newRemainder)

    //    for (i <- 0 until input.length) {
    //      val temp = input(i) * f;
    //      if (temp > remainder) {
    //        print(input(i - 1))
    //        val newRemainder = remainder - (input(i - 1) * f)
    //        if (newRemainder > 0) {
    //          input.remove(i - 1)
    //          calculate(input, newRemainder.toInt)
    //        }
    //      }
    //
    //    }
    if (remainder == 0) {
      0
    } else {
      1
    }
  }

  val (result, time) = profile {
    calculate(ArrayBuffer(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 1000000)
  }
  println(s"result:[$result] took [$time] ms")
}