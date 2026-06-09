Global Power Plant Database — Analysis

Files:
- global_power_plant_analysis.py — main analysis script
- requirements.txt — Python dependencies

How to run:
1. Create and activate a virtual environment (recommended):

   python -m venv .venv
   .\.venv\Scripts\activate

2. Install dependencies:

   pip install -r Week_6/requirements.txt

3. Run the analysis script (it will download the dataset automatically):

   python Week_6/global_power_plant_analysis.py

Outputs:
- Generated plots and CSV outputs will be saved under `outputs/plots`.

Notes:
- The script uses NumPy for array-level statistics, SciPy for hypothesis testing, and Matplotlib/Seaborn for plots.
- If you prefer a notebook, open the script and adapt cells into a Jupyter notebook.
