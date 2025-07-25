from um import count


def test_single_um():
    assert count("um") == 1


def test_question_um():
    assert count("um?") == 1


def test_case_insensitive_um():
    assert count("Um, thanks for the album.") == 1


def test_multiple_um():
    assert count("Um, thanks, um...") == 2


def test_no_um():
    assert count("yummy") == 0
