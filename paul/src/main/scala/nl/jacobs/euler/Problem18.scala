package nl.jacobs.euler

object Problem18 extends App with Timer {
  val input = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

  val grid = {
    val rows = input.split("\n").map(_.trim)
    rows.map(_.split(" ").map(_.toInt))
  }

  def getValue(x: Int, y: Int): Int = {
    if (grid.isDefinedAt(y) && grid(y).isDefinedAt(x)) grid(y)(x)
    else 0
  }

  def getMax(x: Int, y: Int) = {
    getValue(x, y) + (getValue(x, y + 1) max getValue(x + 1, y + 1))
  }

  val (result, time) = profile {
    for (y <- grid.length - 2 to 0 by -1) {
      val row = grid(y)
      for (x <- 0 until row.length) {
        grid(y)(x) = getMax(x, y)
      }
    }
    grid(0)(0)
  }

  println(s"result:[$result] took [$time] ms")
}