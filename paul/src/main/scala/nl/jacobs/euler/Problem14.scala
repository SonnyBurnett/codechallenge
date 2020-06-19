package nl.jacobs.euler

object Problem14 extends App with Timer {

  def calculate(n: Long): Long = {
    if (n % 2 == 0) return (n / 2)
    else return (3 * n + 1)
  }

  def test(n: Long, x: Long): Long = {
    val xx = calculate(n)
    if (xx == 1) {
      return x + 1
    }
    test(xx, x + 1)
  }

  val (result, time) = profile {
    var y = Array(0, 1L)
    (for (i <- 1 to 999999) yield {val r = test(i,1); if(r > y(1)) {y = Array(i,r)}})
    y(0)
  }
  println(s"result:[$result] took [$time] ms")

}