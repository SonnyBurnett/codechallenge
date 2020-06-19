package nl.jacobs.euler

object Problem22 extends App with Timer {

  def calculate(name: String): Long = {
    name.toCharArray().map(_ - 64).sum
  }

  val (result, time) = profile {
    io.Source.fromResource("nl/jacobs/euler/p022_names.txt").mkString.replaceAll("\"","").split(",").sorted.map(calculate).
      zipWithIndex.map(x => x._1 * (1 + x._2)).sum

  }
  println(s"result:[$result] took [$time] ms")
}