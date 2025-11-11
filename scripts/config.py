#!/usr/bin/env python3
"""
Centralized configuration for resume generation scripts.
Update this file to change personal information across all formats.
"""

# Personal Information (used by all generators)
PERSONAL_INFO = {
    "name": "Sumit Ranjan Jha",
    "title": "DevOps Engineer",
    "email": "sumitjhawiki@gmail.com",
    "phone": "+916200129832",
    "linkedin": "https://www.linkedin.com/in/sumitranjanjha7/",
    "github": "https://github.com/SumitWiki",
    "website": "https://github.com/SumitWiki",  # Optional: Your portfolio/website or leave empty
    "location": {
        "city": "",
        "country_code": "IN",
        "region": ""
    }
}

# GitHub Configuration (Not needed if you removed open source section)
GITHUB_USERNAME = "SumitWiki"

# File Paths
SECTIONS_DIR = "sections"
STYLE_DIR = "style"
DOCS_DIR = "docs"

# Output Files
OUTPUT_FILES = {
    "json": "docs/resume.json",
    "latest_pr": "sections/latest_pr.tex"
}

# Resume Content Summary - parsed from sections/summary.tex by utils.get_summary_text()
# Fallback if parsing fails:
SUMMARY_TEXT = "Your professional summary goes here. Describe your expertise, skills, and what you bring to the table."

# Fallback text for latest PR (NOT USED - Open source section removed)
FALLBACK_PR_TEXT = r"\item \textbf{Active Contributor:} Ongoing contributions to open-source projects."

# Open Source Contributions - NOT USED (Open source section removed)
OPEN_SOURCE_CONTRIBUTIONS = []

# API Configuration
GITHUB_API_TIMEOUT = 10  # seconds
GITHUB_API_BASE = "https://api.github.com"
