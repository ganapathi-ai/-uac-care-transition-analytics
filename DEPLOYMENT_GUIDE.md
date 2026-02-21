# Deploy to Streamlit Community Cloud

## 1. Push this project to GitHub

From the project root:

```bash
git init
git add .
git commit -m "Prepare Streamlit Cloud deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/uac-care-transition-analytics.git
git push -u origin main
```

## 2. Deploy in Streamlit Cloud

1. Open https://share.streamlit.io/
2. Click `New app`
3. Select repository: `YOUR_USERNAME/uac-care-transition-analytics`
4. Select branch: `main`
5. Main file path: `app.py`
6. Click `Deploy`

## 3. Expected public URL

After deployment completes, Streamlit provides a permanent HTTPS URL like:

```text
https://yourusername-uac-care-transition-analytics.streamlit.app
```

## Required files in repo

- `app.py`
- `requirements.txt`
- `runtime.txt`
- `.streamlit/config.toml`
- `data/uac_metrics_processed.csv`

## Troubleshooting

- If deployment says module missing, verify `requirements.txt`.
- If deployment says file not found, confirm `data/uac_metrics_processed.csv` exists in GitHub.
- If app fails at startup, check Streamlit logs for stack trace and line number.
