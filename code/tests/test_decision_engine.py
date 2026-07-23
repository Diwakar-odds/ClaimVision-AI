from src.decision_engine import decide_claim


def test_supported_claim():
    decision = decide_claim(True, True)

    assert decision[0] == "supported"


def test_contradicted_claim():
    decision = decide_claim(True, False)

    assert decision[0] == "contradicted"


def test_not_enough_information():
    decision = decide_claim(False, False)

    assert decision[0] == "not_enough_information"
    