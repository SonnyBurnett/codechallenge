import solution


def test_freq_analysis():
    assert solution.freq([]) == {}

    assert solution.freq([0]) == {0: 1}
    assert solution.freq([0, 0, 0]) == {0: 3}
