package nl.jacobs.euler

import java.util.Date
import java.util.Calendar
import java.util.GregorianCalendar

object Problem19 extends App with Timer {
  val date = new GregorianCalendar(1901, 1, 1)
  
  def isSunday(months: Int) = {
    date.set(Calendar.YEAR, 1901)
    date.set(Calendar.MONTH, 1)

    date.add(Calendar.MONTH, months)
    date.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY
  }
  val (result, time) = profile {
    Stream.from(1).takeWhile(_ < 1200).filter(isSunday).size
  }
  println(s"result:[$result] took [$time] ms")
}