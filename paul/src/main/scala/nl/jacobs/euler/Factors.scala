package nl.jacobs.euler

trait Factors {
  def factors(n: Long): List[Long] = (2 to math.sqrt(n).toInt)
    .find(n % _ == 0).fold(List(n))(i => i.toLong :: factors(n / i))
}