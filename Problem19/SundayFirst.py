from datetime import date

def __isSunday(day: date):
  if day.strftime('%A')=='Sunday':
    return True
  return False

def countSundays(start: int, end: int):
  if start>end or (not 0<start<2021) or (not 0<end<2021):
    raise ValueError("Input should be a start and an end year (both integers) between 0 and 2020")
  count=0
  for year in range(start,end):
    for month in range(1,13):
      if __isSunday(date(year, month, 1)):
        count+=1
  return count

def main():
  print("The number of Sundays being the first day of the month in the 20th century is: " +
    str(countSundays(1901,2001)))

if __name__ == '__main__':
    main()
