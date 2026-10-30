# Mental Health Insights: Physical Challenges and General Population

**MindScope** is an educational Flask dashboard comparing illustrative wellbeing indicators for a group labelled “Physical challenges” and a “General population” group across age bands.

## Important data note
All included data is **synthetic demonstration data**. It was created only to demonstrate the dashboard and does not represent real people, clinical research or any actual population. Do not present these values as research findings or use them for decisions about people.

## Features
- Interactive Plotly comparison chart
- Selectable indicators: wellbeing score, stress level, sleep hours, social support and physical activity
- Group-average summary cards and a simple difference calculation
- CSV download of illustrative data
- Responsive interface for desktop and mobile
- About and ethics page with limitations and privacy guidance
- No login, personal health data collection or API key required

## Technology
Python 3, Flask, Pandas, Plotly, HTML and CSS.

## Run locally
1. Install Python 3.10 or later.
2. Open a terminal in this project folder.
3. Optional: create a virtual environment with `python -m venv .venv`, then activate it.
4. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000`.

## Deploy
The included `Procfile` uses Gunicorn. On a compatible host, use build command `pip install -r requirements.txt` and start command `gunicorn app:app`.

## Structure
- `app.py` — Flask routes, calculations and chart generation
- `templates/index.html` — dashboard page
- `templates/about.html` — project and ethics information
- `static/style.css` — responsive styling
- `data/illustrative_mental_health_data.csv` — synthetic demo dataset

## Responsible use
This is an educational visualization project, not a diagnostic or treatment tool and not medical advice. Before replacing sample values with real data, verify its provenance, license, consent and privacy protections. Do not commit identifiable or confidential health information to GitHub.

## License
MIT. See `LICENSE`.
