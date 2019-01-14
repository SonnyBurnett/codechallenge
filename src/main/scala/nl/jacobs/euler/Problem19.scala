package nl.jacobs.euler

import java.util.Date
import java.util.Calendar

object Problem19 extends App with Timer {
  val (result, time) = profile {
    val date = Calendar.getInstance;
    date.set(1901, 1, 1);
    var sunday = 0;
    while (date.get(Calendar.YEAR) < 2001) {
      if (date.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
        sunday += 1;
      }
      date.add(Calendar.MONTH, 1);
    }
    sunday
  }
  println(s"result:[$result] took [$time] ms")

}