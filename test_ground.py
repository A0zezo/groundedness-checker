from ground import check, words


def test_words_drop_stopwords():
    assert words("The cat is on the mat") == {"cat", "mat"}


def test_grounded_sentence():
    assert check("FastAPI uses type hints.", "FastAPI uses type hints and Pydantic.")[0][2]


def test_unsupported_sentence():
    assert not check("It was created by Google in 2010.", "FastAPI uses type hints.")[0][2]


def test_empty_content_words_counts_as_grounded():
    assert check("It is the.", "anything")[0][2]


def test_one_result_per_sentence():
    assert len(check("A b. C d. E f.", "a b c d e f")) == 3
