class Triangle():
  def __init__(self):
    pass

  def calc_max_path_sum(self, traingle_numbers):
    data = traingle_numbers.split('\n')
    curent_row = []
    for i in range(len(data) - 1):
      row_i = [int(x) for x in data[i].split()] if i == 0 else curent_row
      row_i_1 = [int(x) for x in data[i + 1].split()]
      curent_row = []
      for j in range(len(row_i_1)):
        sum_1 = 0 if j == 0 else row_i[j - 1] + row_i_1[j]
        sum_2 = row_i[j] + row_i_1[j] if j < len(row_i) else 0
        curent_row.append(max(sum_1, sum_2))

    max_path = max(curent_row)
    return max_path

  def euler_solution(self):
    traingle_numbers = '''75
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
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
    return self.calc_max_path_sum(traingle_numbers)


def main():
  '''
  main function
  '''
  print('Solution for the Euler 018 problem:')
  # prints: 171
  _triangle = Triangle()
  print(_triangle.euler_solution())


if __name__ == "__main__":
  main()
