# 🎯 Your Resume Setup Guide

## ✅ Changes Made

I've customized this template for you by:

1. ✅ Removed the open source contributions section
2. ✅ Removed all related code (fetch_latest_pr.py calls)
3. ✅ Set placeholder values for your personal information
4. ✅ Updated the build process to skip GitHub API calls

## 📝 What You Need to Do Now

### 1. Update Your Personal Information

Edit these files with YOUR details:

#### **`scripts/config.py`** - Python configuration

Replace the placeholder values:

```python
PERSONAL_INFO = {
    "name": "Your Name",           # ← Your full name
    "title": "Your Job Title",     # ← e.g., "Software Engineer", "Data Scientist"
    "email": "your.email@example.com",
    "phone": "+1234567890",        # Optional
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "website": "https://yourwebsite.com",
    "location": {
        "city": "Your City",
        "country_code": "US",      # US, IN, UK, etc.
        "region": "Your State/Region"
    }
}
```

#### **`style/header.tex`** - LaTeX header (must match config.py)

```latex
{\Huge\bfseries Your Name}\\          % ← Same as config.py
\faIcon{linkedin} \href{https://linkedin.com/in/yourprofile}{LinkedIn}
\faIcon{github} \href{https://github.com/yourusername}{Github}
\faIcon{globe} \href{https://yourwebsite.com}{Portfolio}
\faIcon{envelope} \href{mailto:your.email@example.com}{Email}
```

### 2. Update Your Resume Content

Edit the LaTeX files in `sections/` folder:

#### **`sections/summary.tex`**

Replace with your professional summary:

```latex
\section{Summary}
\noindent Your professional summary here. Describe your expertise, years of experience, key skills, and what makes you unique.
```

#### **`sections/projects.tex`**

Add your projects using the `\cventry` command:

```latex
\section{Projects}

\cventry{Project Name}{Technologies Used}{\href{https://github.com/you/repo}{GitHub}}{
\begin{itemizecompact}
  \item What did you build?
  \item What technologies did you use?
  \item What was the impact? (users, performance, etc.)
  \item Key technical challenges solved
\end{itemizecompact}
}

% Add more projects...
```

#### **`sections/skills.tex`**

Update with your skills:

```latex
\section{Skills}

\noindent\textbf{Languages:} Python, JavaScript, Java, etc.\\[2pt]
\noindent\textbf{Frameworks:} React, Django, Spring Boot, etc.\\[2pt]
\noindent\textbf{Databases:} PostgreSQL, MongoDB, etc.\\[2pt]
\noindent\textbf{Tools:} Docker, Git, AWS, etc.\\[2pt]
\noindent\textbf{Concepts:} Your key competencies
```

#### **`sections/education.tex`**

Update with your education:

```latex
\section{Education}

\noindent\textbf{Your University Name} \hfill \textit{Start Year - End Year}\\
\textit{Degree Name (e.g., B.S. in Computer Science)} \hfill \textbf{GPA: X.X/4.0}
\begin{itemizecompact}
  \item Relevant coursework
  \item Achievements or honors
\end{itemizecompact}
```

### 3. Build Your Resume

#### **Option 1: Windows PowerShell** (Recommended)

```powershell
# Install dependencies (one-time)
pip install requests

# Build PDF
latexmk -pdf -interaction=nonstopmode cv.tex

# Generate JSON Resume (optional)
python scripts/generate_json.py
```

#### **Option 2: Using Make** (if you have Make installed)

```bash
make build      # Build PDF only
make all        # Build PDF + JSON
make clean      # Remove generated files
```

#### **Option 3: WSL (Windows Subsystem for Linux)**

If you have WSL installed:

```bash
make all
```

## 📦 Prerequisites

You need to install:

1. **Python 3.12+**

   - Download from: https://www.python.org/downloads/
   - Install `requests`: `pip install requests`

2. **LaTeX Distribution** (for PDF generation)

   - **Windows**: [MiKTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/)
   - **macOS**: MacTeX (via Homebrew: `brew install mactex`)
   - **Linux**: `sudo apt-get install texlive-full`

3. **Make** (Optional, for automation)
   - Windows: Install via chocolatey: `choco install make`
   - Or just use the PowerShell commands above

## 🎨 Customization Tips

### Change Colors

Edit `style/header.tex`:

```latex
\hypersetup{
    colorlinks=true,
    linkcolor=blue,    % Change to red, green, etc.
    urlcolor=blue,
}
```

### Adjust Spacing

Edit `style/macros.tex`:

```latex
\vspace{3mm}  % Change 3mm to 5mm for more space
```

### Remove/Add Sections

Edit `cv.tex`:

```latex
\input{sections/summary.tex}
\input{sections/projects.tex}
% \input{sections/certifications.tex}  % Add new sections
\input{sections/skills.tex}
\input{sections/education.tex}
```

## 🚀 Quick Start

1. **Install Python dependencies:**

   ```powershell
   pip install requests
   ```

2. **Edit your information:**

   - Update `scripts/config.py`
   - Update `style/header.tex`
   - Update all files in `sections/` folder

3. **Build your resume:**

   ```powershell
   latexmk -pdf -interaction=nonstopmode cv.tex
   ```

4. **Find your resume:**
   - PDF: `cv.pdf`
   - JSON Resume: `docs/resume.json` (after running `python scripts/generate_json.py`)

## 📄 Output Files

After building:

- **`cv.pdf`** - Your resume in PDF format (main output)
- **`docs/resume.json`** - JSON Resume format (for online profiles)
- **`docs/index.pdf`** - Copy for web deployment

## ❓ Troubleshooting

### LaTeX not found

- Make sure you installed MiKTeX or TeX Live
- Restart your terminal after installation
- Check: `latexmk --version`

### Python errors

- Make sure Python 3.12+ is installed: `python --version`
- Install dependencies: `pip install requests`

### Missing fonts/icons

- MiKTeX will auto-install missing packages (allow it when prompted)
- Or manually install: `fontawesome5` package

## 🔄 Keeping Updated

This template is now yours! The open source features have been removed, so:

- No automatic PR fetching
- No GitHub API calls
- All data is manually maintained

Edit the LaTeX files directly to keep your resume updated.

## 📞 Need Help?

Check the original README.md for more detailed information about:

- LaTeX syntax
- JSON Resume schema
- Advanced customization

Good luck with your job search! 🎉
