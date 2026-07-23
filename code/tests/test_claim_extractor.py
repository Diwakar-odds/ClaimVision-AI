from src.claim_extractor import extract_claim


def test_extract_dent():
    result = extract_claim("Front bumper has a dent")

    assert result["issue_type"] == "dent"
    assert result["object_part"] == "front_bumper"


def test_extract_scratch():
    result = extract_claim("Door is scratched")

    assert result["issue_type"] == "scratch"
    assert result["object_part"] == "door"


def test_unknown_issue():
    result = extract_claim("Vehicle looks fine")

    assert result["issue_type"] == "unknown"
    assert result["object_part"] == "unknown"