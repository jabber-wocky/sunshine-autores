Remove-Item .venv -Recurse -ErrorAction Ignore
python -m venv .venv
.\.venv\Scripts\activate.ps1
pip install -r requirements.txt
