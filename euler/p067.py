import os


class Triangle():
  def __init__(self, filename=''):
    self._location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    if len(filename) > 0:
      self.process_data_from_file(filename)

  def calc_max_path_sum(self, data):
    # data = traingle_numbers.split('\n')
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

  def process_data_from_file(self, filename):
    if not os.path.exists(os.path.join(self._location, filename)):
      raise FileNotFoundError("File specified does not exists.")
    
    traingle_numbers = []
    with open(os.path.join(self._location, filename)) as triangle_file:
      row = triangle_file.readline()
      while row:
        if len(row) > 0:
          traingle_numbers.append(row)
        row = triangle_file.readline()

    return self.calc_max_path_sum(traingle_numbers)

  def euler_solution(self):
    return self.process_data_from_file('p067_triangle.txt')


def main():
  '''
  main function
  '''
  print('Solution for the Euler 067 problem:')
  # prints: 7273
  _triangle = Triangle()
  print(_triangle.euler_solution())


if __name__ == "__main__":
  main()
