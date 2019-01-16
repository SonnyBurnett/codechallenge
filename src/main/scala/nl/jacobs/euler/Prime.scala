package nl.jacobs.euler
//t
trait Prime {
  def isPrime(n: Int) = !(2 to math.sqrt(n).toInt).exists(n % _ == 0)
}
