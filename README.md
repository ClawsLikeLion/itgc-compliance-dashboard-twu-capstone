# ITGC Compliance Dashboard Capstone

This repository contains the files for my 2026 Informatics Capstone project: an ITGC Compliance Gap Analyzer Dashboard.

## Project Overview

This capstone project is a functional prototype that uses synthetic data to evaluate IT General Controls (ITGCs). The dashboard allows a user to upload a control library CSV and an evidence dataset CSV, then analyzes the evidence against each control to identify passed controls, failed controls, and controls that need further review.

The goal of this project is to show how compliance review work can be supported through a simple data-driven dashboard. Instead of reviewing control evidence only through spreadsheets or manual notes, the tool organizes results into visual summaries, priority action areas, and detailed findings.

## Features

- Uploads a control library CSV
- Uploads an evidence dataset CSV
- Compares submitted evidence against control requirements
- Classifies controls as Passed, Failed, or Needs Review
- Displays an executive compliance summary
- Shows a Compliance Risk Map using a treemap visualization
- Provides a Priority Action Plan for failed or review-needed controls
- Groups findings by company focus area
- Allows users to download the final results as a CSV file

## Files Included

- `app.py` - Streamlit dashboard application
- `CAPSTONE.ipynb` - Jupyter Notebook testing logic and analysis
- `requirements.txt` - Python packages required to run the dashboard
- CSV files - Synthetic data files used for the capstone demonstration in streamlit (3)
- Final Paper 

## How to Run the Dashboard (powershell terminal)

Install the required packages:

```bash
pip install -r requirements.txt

To Run Streamlit Application
streamlit run app.py 
