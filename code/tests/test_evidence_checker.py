from src.evidence_checker import check_evidence


def test_valid_evidence():
    result = check_evidence(True, True)

    assert result[0] is True


def test_invalid_image():
    result = check_evidence(True, False)

    assert result[0] is False


def test_damage_not_visible():
    result = check_evidence(False, True)

    assert result[0] is False