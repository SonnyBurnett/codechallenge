package nl.jacobs.euler

object Problem30 extends App with Timer {

  def compare(n: Int) = {
    n == n.toString().map(_.asDigit).map(math.pow(_, 5)).sum.toInt
  }

  val max = (math.pow(9, 5) * 5).toInt
  
  val (result, time) = profile {
    Stream.from(2).takeWhile(_ < max).filter(compare).sum
  }
  println(s"result:[$result] took [$time] ms")

}