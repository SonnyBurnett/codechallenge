from classes.Solution import Solution


class EncryptionBreaker:
    def __init__(self, file_name):
        self.candidate_key_parts = range(ord('a'), ord('z'))
        self.file_name = file_name
        self.solutions = []

    def run(self):
        self.__read_cypher_text()
        self.__find_candidate_solutions()
        solution = self.__pick_solution()

        return solution

    def __read_cypher_text(self):
        with open(self.file_name, 'r') as input_file:
            self.cypher_text = list(map(int, input_file.readlines()[0].split(',')))

    def __find_candidate_solutions(self):
        candidate_keys = [(a, b, c)
                          for a in self.candidate_key_parts
                          for b in self.candidate_key_parts
                          for c in self.candidate_key_parts]

        for candidate_key in candidate_keys:
            self.solutions.append(Solution(candidate_key, self.cypher_text))

    def __pick_solution(self):
        return sorted(self.solutions, reverse=True, key=lambda solution: solution.get_letter_count())[0]
