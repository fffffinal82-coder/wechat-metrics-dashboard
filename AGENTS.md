# AGENTS.md

## Cursor Cloud specific instructions

This is a minimal Python Streamlit dashboard app for HUME marketing data analysis. No database, Docker, or external services required — all data is embedded directly in `app.py`.

### Running the app

```
streamlit run app.py --server.port 8501 --server.headless true
```

The app will be available at `http://localhost:8501`.

### Dependencies

Dependencies are listed in `requirements.txt` and installed via `pip install -r requirements.txt`. The three packages are: `streamlit`, `pandas`, `plotly`.

### Notes

- There are no automated tests, linters, or build steps in this repository.
- The codebase has no `Makefile`, no CI config, and no pre-commit hooks.
- `HUME_Marketing_Report.html` is a standalone static HTML report that can be opened directly in a browser; it does not depend on the Python app.
