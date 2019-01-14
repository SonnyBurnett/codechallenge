package nl.jacobs.euler

trait Timer {
  import System.currentTimeMillis
  def profile[R](code: => R, t: Long = currentTimeMillis) = (code, currentTimeMillis - t)
}