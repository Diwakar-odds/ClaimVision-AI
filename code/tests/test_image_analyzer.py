from unittest.mock import patch, MagicMock
from PIL import Image
import tempfile
import os

from src.image_analyzer import (
    analyze_image,
    validate_image_file,
    _estimate_repair_cost,
    _confidence_score,
)


def create_temp_image():
    temp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    img = Image.new("RGB", (100, 100), color="white")
    img.save(temp.name)
    temp.close()
    return temp.name


# -----------------------------
# validate_image_file
# -----------------------------

def test_validate_image_file_success():
    path = create_temp_image()

    ok, error = validate_image_file(path)

    assert ok is True
    assert error is None

    os.remove(path)


def test_validate_image_file_missing():
    ok, error = validate_image_file("does_not_exist.jpg")

    assert ok is False
    assert error is not None


# -----------------------------
# helper functions
# -----------------------------

def test_estimate_repair_cost():
    cost = _estimate_repair_cost("car", "high")
    assert "INR" in cost


def test_confidence_score():
    result = {
        "damage_visible": True,
        "valid_image": True,
        "severity": "high",
        "quality_flags": []
    }

    score = _confidence_score(result)

    assert score > 0
    assert score <= 100


# -----------------------------
# analyze_image success
# -----------------------------

@patch("src.image_analyzer.model.generate_content")
def test_analyze_image_success(mock_generate):

    fake_response = MagicMock()

    fake_response.text = """
    {
        "object_type":"car",
        "issue_type":"dent",
        "object_part":"front_bumper",
        "damage_visible":true,
        "severity":"high",
        "valid_image":true,
        "quality_flags":[]
    }
    """

    mock_generate.return_value = fake_response

    path = create_temp_image()

    result = analyze_image(path, "car")

    assert result["object_type"] == "car"
    assert result["issue_type"] == "dent"
    assert result["damage_visible"] is True
    assert result["severity"] == "high"

    os.remove(path)


# -----------------------------
# analyze_image exception
# -----------------------------

@patch("src.image_analyzer.model.generate_content")
def test_analyze_image_exception(mock_generate):

    mock_generate.side_effect = Exception("Gemini API failed")

    path = create_temp_image()

    result = analyze_image(path, "car")

    assert result["valid_image"] is False
    assert result["issue_type"] == "unknown"
    assert "manual_review_required" in result["quality_flags"]

    os.remove(path)


# -----------------------------
# invalid image path
# -----------------------------

def test_analyze_image_invalid_path():

    result = analyze_image("invalid.jpg", "car")

    assert result["valid_image"] is False
    assert result["damage_visible"] is False