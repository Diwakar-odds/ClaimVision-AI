from src.history_checker import get_history_flags


def test_none_history():
    row = {"history_flags": "none"}

    assert get_history_flags(row) == ["none"]


def test_multiple_flags():
    row = {"history_flags": "fraud;suspicious"}

    result = get_history_flags(row)

    assert "fraud" in result
    assert "suspicious" in result