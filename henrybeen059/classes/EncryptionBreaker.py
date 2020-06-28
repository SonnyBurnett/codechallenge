from classes.Solution import Solution


class EncryptionBreaker:
    __solutions = []
    __cypher_text = ''

    def __init__(self, file_name):
        self.__candidate_key_parts = range(ord('a'), ord('z'))
        self.__file_name = file_name

    def run(self):
        self.__read_cypher_text()
        self.__find_candidate_solutions()

        return self.__pick_solution()

    def __read_cypher_text(self):
        with open(self.__file_name, 'r') as input_file:
            self.__cypher_text = list(map(int, input_file.readlines()[0].split(',')))

    def __find_candidate_solutions(self):
        candidate_keys = [(a, b, c)
                          for a in self.__candidate_key_parts
                          for b in self.__candidate_key_parts
                          for c in self.__candidate_key_parts]

        self.__solutions = map(lambda candidate_key: Solution(candidate_key, self.__cypher_text), candidate_keys)

    def __pick_solution(self):
        return sorted(self.__solutions, reverse=True, key=lambda solution: solution.get_letter_count())[0]
