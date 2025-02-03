# Marketing Mix Modeling for L'Oreal

## Create environment

Run the following in your terminal:
- `uv venv .venv`
- source .venv/bin/activate
- uv pip install -e . # Use the pyproject.toml to install dependencies

## Download and extract data

- Create a data folder and put the Excel file with the data in that folder.

- Then run `python3 scripts/split_excel_to_csv.py` in your terminal.