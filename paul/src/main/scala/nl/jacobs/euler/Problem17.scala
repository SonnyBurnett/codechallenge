package nl.jacobs.euler

object Problem17 extends App with Timer {
  val zeroToTwenty = Array(0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7,
    7, 9, 8, 8)

  val tens = Array(0, 0, 6, 6, 5, 5, 5, 7, 6, 6)

  val hundred = 7

  val and = 3

  val thousand = 11

  def number(num: Int): Int = {
    if (num == 1000) thousand
    else if (num < 20) zeroToTwenty(num)
    else if (num < 100) tens(num / 10) + (if (num % 10 > 0) zeroToTwenty(num % 10) else 0)
    else if (num < 1000) zeroToTwenty(num / 100) + hundred + (if (num % 100 > 0) and + number(num % 100) else 0)
    else 0
  }

  val (result, time) = profile((1 to 1000).map(number).sum)
  println(s"result:[$result] took [$time] ms")

}