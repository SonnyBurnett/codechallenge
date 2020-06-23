import solution


def test_freq_analysis():
    assert solution.freq([]) == {}

    assert solution.freq([0]) == {0: 1}
    assert solution.freq([0, 0, 0]) == {0: 3}

    assert solution.freq([0, 3, 7]) == {0: 1, 3: 1, 7: 1}
    assert solution.freq([0, 7, 7, 3, 3, 3, 0, 3, 7, 0]) == {0: 3, 3: 4, 7: 3}
