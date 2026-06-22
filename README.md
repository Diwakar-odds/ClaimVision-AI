# ClaimVision AI

AI-powered damage claim verification system for automated insurance evidence review, fraud risk assessment, and claim validation.

## Overview

ClaimVision AI is an intelligent damage claim verification platform built using Python, Streamlit, Computer Vision, and Google Gemini AI.

The system helps automate the insurance claim review process by analyzing uploaded damage images, extracting claim information, validating evidence quality, detecting visible damage, assessing fraud risk, generating AI-driven insights, and producing professional claim reports.

The platform is designed to reduce manual verification effort while improving claim processing efficiency and consistency.

---

## Key Features

### Evidence Review Workspace

* Upload claim images
* Image preview and validation
* Claim object selection
* Claim description input
* Real-time evidence review workflow

### AI Damage Analysis

* Damage visibility detection
* Severity assessment
* Object identification
* Image quality validation
* AI-generated claim reasoning

### Fraud Risk Assessment

* Historical risk evaluation
* Evidence consistency checks
* Manual review recommendations
* Risk categorization

### Analytics Dashboard

* Claim statistics
* Approval and rejection trends
* Severity distribution
* Business insights
* Performance visualization

### Automated Report Generation

* Professional PDF reports
* Claim summaries
* AI findings
* Decision recommendations
* Evidence snapshots

### Explainable AI Insights

* Confidence scoring
* Decision transparency
* Evidence-based recommendations
* Repair guidance

---

## Tech Stack

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* Python

### AI & Machine Learning

* Google Gemini AI
* Computer Vision
* OpenCV
* Scikit-Learn

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Reporting

* ReportLab

---

## Project Structure

```text
code/
│
├── app.py
├── main.py
├── report_generator.py
│
├── src/
│   ├── claim_extractor.py
│   ├── image_analyzer.py
│   ├── evidence_checker.py
│   ├── history_checker.py
│   └── decision_engine.py
│
├── models/
├── notebooks/
├── utils/
├── evaluation/
└── reports/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Komal2008/ClaimVision-AI.git
cd ClaimVision-AI
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Enhancements

* Multi-image claim verification
* Advanced fraud detection models
* Explainable AI dashboards
* Historical claim matching
* RAG-based claim knowledge assistant
* REST API integration
* Cloud deployment
* Real-time claim monitoring

---

## Use Cases

* Insurance claim verification
* Vehicle damage assessment
* Property damage inspection
* Evidence validation workflows
* AI-assisted claim processing

---

## Author

Komal Pandey

Engineering Student | AI & Machine Learning Enthusiast

GitHub: https://github.com/Komal2008

---

## License

This project is licensed under the MIT License.
