# Evaluation Report

## Project Overview

This project verifies damage claims using:

* Claim conversation
* Submitted images
* User history
* Evidence requirements

The system supports:

* Car claims
* Laptop claims
* Package claims

The final decision is generated using image evidence, claim context, and user risk history.

---

## Evaluation Strategy

The following workflow was used:

1. Extract damage claim from conversation
2. Analyze submitted image using Gemini Vision
3. Detect visible issue type and object part
4. Validate evidence quality
5. Check user history for risk indicators
6. Generate claim decision

Possible decisions:

* supported
* contradicted
* not_enough_information

---

## Models and Tools Used

* Gemini 2.5 Flash
* Python 3.10
* Pandas
* Pillow
* dotenv

---

## Operational Analysis

### Approximate Model Calls

* One Gemini Vision call per image
* One claim extraction call per claim

### Images Processed

* Multiple images supported per claim
* First image evaluated during development

### Runtime

* Approximately 10–15 seconds per claim
* Additional delay added to respect Gemini free-tier limits

### Rate Limiting

Gemini API free tier limits were handled using:

* Request throttling
* time.sleep() between requests

### Token Usage

Estimated:

* Input: 300–800 tokens per claim
* Output: 50–150 tokens per claim

### Cost Estimate

Development was performed using the Gemini free tier.

Approximate production cost depends on:

* Number of images
* Number of claims
* Selected Gemini model

---

## Strengths

* Multimodal claim verification
* Image-grounded decisions
* User history risk detection
* Structured CSV output
* Modular architecture

---

## Limitations

* Currently processes one image as primary evidence
* Basic rule-based decision logic
* Free-tier API rate limits increase runtime

---

## Future Improvements

* Multi-image evidence aggregation
* Confidence scoring
* Improved contradiction detection
* Enhanced fraud detection
* Parallel batch processing

---

## Final Result

The system successfully generates output.csv with the required schema and produces structured claim review decisions using image evidence and claim context.
