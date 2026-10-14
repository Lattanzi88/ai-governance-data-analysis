# AI Governance: Recruitment Selection Analysis

## Project Overview

This project explores how Python can support the analysis of selection outcomes in an AI-assisted recruitment scenario.

Using a small synthetic dataset, the project calculates selection rates across groups defined by work experience, gender, and educational background. The results are summarized through descriptive statistics and visualized using bar charts.

The goal is to demonstrate basic data analysis skills applied to AI Governance, with a focus on identifying outcome differences that may warrant further investigation.

## Objectives

- Analyze overall candidate selection rates.
- Compare selection rates across demographic and professional groups.
- Calculate percentage-point differences between groups.
- Visualize the results using Python and Matplotlib.
- Reflect on the role and limitations of quantitative indicators in AI risk assessment.

## Tools and Technologies

- Python
- pandas
- Matplotlib

## Project Structure

```text
ai-governance-data-analysis/
├── main.py
├── README.md
└── grafici/
    ├── grafico_esperienza.png
    ├── grafico_genere.png
    └── grafico_titolo_studio.png
```

## Methodology

The analysis uses a synthetic dataset containing six fictional candidates. Each record includes work experience, selection outcome, gender, and educational background.

The script calculates overall selection rates and compares outcomes across the selected groups. It also generates three bar charts to make the differences easier to inspect.

## Limitations

The dataset is synthetic and extremely small. The results are intended solely for educational and demonstrative purposes.

Differences in selection rates do not, by themselves, establish discrimination, causation, or a violation of applicable law. A real-world assessment would require a larger and representative dataset, a justified comparison methodology, contextual analysis, and appropriate legal and governance review.

## Future Developments

Potential extensions include:

- Using a larger, documented dataset.
- Adding selection-rate ratios and further fairness indicators.
- Examining data quality, limitations, and potential sources of bias.
- Improving automated reporting and visualization.

## Author

A learning project exploring the intersection of Python, AI Governance, and responsible AI assessment.