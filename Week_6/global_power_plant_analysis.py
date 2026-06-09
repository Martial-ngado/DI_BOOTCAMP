"""
Global Power Plant Database — Analysis script
Performs download, cleaning, EDA, statistical tests, time-series analysis,
matrix operations (covariance + eigendecomposition), and visualizations.
"""

import os
import zipfile
import requests
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

DATA_URL = "https://github.com/devtlv/Datasets-DA-Bootcamp-2-/raw/refs/heads/main/Week%206%20-%20Applications%20for%20Data%20Analysis/W6D2%20-%20Advanced%20Numpy/globalpowerplantdatabasev130.zip"
DATA_DIR = os.path.join("data", "global_power")
PLOTS_DIR = os.path.join("outputs", "plots")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)


def download_and_extract_zip(url, dest_dir):
    print("Downloading dataset...")
    r = requests.get(url, stream=True)
    r.raise_for_status()
    z = zipfile.ZipFile(io.BytesIO(r.content))
    # find CSV inside zip
    csv_names = [n for n in z.namelist() if n.lower().endswith('.csv')]
    if not csv_names:
        raise RuntimeError("No CSV found inside downloaded zip")
    csv_name = csv_names[0]
    print(f"Extracting {csv_name} to {dest_dir}")
    z.extract(csv_name, path=dest_dir)
    return os.path.join(dest_dir, csv_name)


def load_dataframe(csv_path):
    print(f"Loading CSV from {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"Loaded dataframe with {df.shape[0]} rows and {df.shape[1]} columns")
    return df


def clean_dataframe(df):
    # Typical useful columns in the Global Power Plant Database
    # We'll standardize column names just in case
    df = df.rename(columns=lambda s: s.strip())

    # Convert capacity to numeric
    if 'capacity_mw' in df.columns:
        df['capacity_mw'] = pd.to_numeric(df['capacity_mw'], errors='coerce')
    else:
        print("Warning: 'capacity_mw' not found in columns")

    # primary_fuel
    if 'primary_fuel' not in df.columns and 'fuel1' in df.columns:
        df = df.rename(columns={'fuel1': 'primary_fuel'})

    # commissioning_year -> numeric
    if 'commissioning_year' in df.columns:
        df['commissioning_year'] = pd.to_numeric(df['commissioning_year'], errors='coerce')

    # Fill missing capacity by median per fuel type
    if 'capacity_mw' in df.columns and 'primary_fuel' in df.columns:
        med_by_fuel = df.groupby('primary_fuel')['capacity_mw'].median()
        def fill_capacity(row):
            if np.isnan(row['capacity_mw']):
                fuel = row['primary_fuel']
                if pd.notna(fuel) and fuel in med_by_fuel and not np.isnan(med_by_fuel[fuel]):
                    return med_by_fuel[fuel]
                return np.nan
            return row['capacity_mw']
        df['capacity_mw'] = df.apply(fill_capacity, axis=1)
        # fallback global median
        global_med = df['capacity_mw'].median()
        df['capacity_mw'] = df['capacity_mw'].fillna(global_med)

    # Drop rows with no location or no fuel type
    if 'latitude' in df.columns and 'longitude' in df.columns:
        df = df.dropna(subset=['latitude', 'longitude'])

    if 'primary_fuel' in df.columns:
        df = df[df['primary_fuel'].notna()]

    return df


def eda_stats(df):
    print("\nOverall numeric summary:")
    print(df.describe(include=[np.number]).T[['count','mean','50%','std']].rename(columns={'50%':'median'}))

    if 'capacity_mw' in df.columns:
        arr = df['capacity_mw'].to_numpy()
        print('\nUsing NumPy: mean, median, std for capacity_mw')
        print(np.nanmean(arr), np.nanmedian(arr), np.nanstd(arr))

    # Distribution by country
    if 'country' in df.columns:
        top_countries = df['country'].value_counts().head(10)
        print('\nTop 10 countries by plant count:')
        print(top_countries)

    # Distribution by fuel
    if 'primary_fuel' in df.columns:
        fuel_counts = df['primary_fuel'].value_counts()
        print('\nPlant counts by fuel type:')
        print(fuel_counts)

    # Save simple plots
    if 'primary_fuel' in df.columns:
        plt.figure(figsize=(10,6))
        sns.boxplot(x='primary_fuel', y='capacity_mw', data=df[df['capacity_mw']>0])
        plt.xticks(rotation=45)
        plt.title('Capacity distribution by fuel type (MW)')
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, 'capacity_by_fuel_boxplot.png'))
        plt.close()

    if 'country' in df.columns:
        plt.figure(figsize=(10,6))
        sns.barplot(x=top_countries.index, y=top_countries.values)
        plt.xticks(rotation=45)
        plt.title('Top 10 countries by number of plants')
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, 'top_countries.png'))
        plt.close()


def statistical_analysis(df):
    # Compare mean capacity between two fuels: Coal vs Gas (if available)
    fuels = df['primary_fuel'].unique()
    print('\nAvailable fuels:', fuels[:10])
    # pick two common fuels
    candidates = ['Coal', 'Gas']
    present = [f for f in candidates if f in fuels]
    if len(present) == 2:
        a = df.loc[df['primary_fuel']=='Coal', 'capacity_mw'].dropna()
        b = df.loc[df['primary_fuel']=='Gas', 'capacity_mw'].dropna()
        print(f"\nComparing Coal (n={len(a)}) vs Gas (n={len(b)}) mean capacities")
        tstat, pval = stats.ttest_ind(a, b, equal_var=False, nan_policy='omit')
        print('t-statistic:', tstat, 'p-value:', pval)
        # If non-normal or very different distributions, do Mann-Whitney
        u_stat, u_p = stats.mannwhitneyu(a, b, alternative='two-sided')
        print('Mann-Whitney U p-value:', u_p)
    else:
        print('Coal and Gas not both present; skipping t-test')

    # Statistical summary per fuel using numpy
    by_fuel = {}
    for fuel, g in df.groupby('primary_fuel'):
        arr = g['capacity_mw'].to_numpy()
        by_fuel[fuel] = {
            'count': len(arr),
            'mean': np.nanmean(arr),
            'median': np.nanmedian(arr),
            'std': np.nanstd(arr)
        }
    fuel_stats = pd.DataFrame(by_fuel).T.sort_values('mean', ascending=False)
    print('\nFuel statistics (capacity_mw):')
    print(fuel_stats.head(20))
    fuel_stats.to_csv(os.path.join(PLOTS_DIR, 'fuel_capacity_stats.csv'))


def time_series_analysis(df):
    if 'commissioning_year' not in df.columns:
        print('No commissioning_year column; skipping time series analysis')
        return
    ts = df.groupby('commissioning_year')['capacity_mw'].sum().sort_index()
    ts = ts[ts.index.notna()]
    plt.figure(figsize=(12,5))
    ts.plot()
    plt.title('Total capacity commissioned per year')
    plt.xlabel('Year')
    plt.ylabel('Capacity (MW)')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'capacity_by_year.png'))
    plt.close()

    # fuel mix over time (top fuels)
    pivot = df.pivot_table(index='commissioning_year', columns='primary_fuel', values='capacity_mw', aggfunc='sum', fill_value=0)
    top_fuels = pivot.sum(axis=0).sort_values(ascending=False).head(6).index
    pivot[top_fuels].plot(figsize=(12,6))
    plt.title('Top fuel types capacity commissioned over time')
    plt.xlabel('Year')
    plt.ylabel('Capacity (MW)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'fuel_mix_over_time.png'))
    plt.close()


def geographic_plots(df):
    # Scatter of plants colored by fuel
    if not {'latitude','longitude','primary_fuel'}.issubset(df.columns):
        print('Missing geographic columns; skipping geographic plots')
        return
    sample = df.sample(min(20000, len(df)))
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='longitude', y='latitude', hue='primary_fuel', data=sample, legend=False, s=10, alpha=0.6)
    plt.title('Geographic scatter of sampled power plants')
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'geo_scatter.png'))
    plt.close()


def matrix_operations_and_eig(df):
    # Use capacity, latitude, longitude for matrix ops
    cols = [c for c in ['capacity_mw','latitude','longitude'] if c in df.columns]
    X = df[cols].dropna()
    Xn = X.to_numpy()
    print(f"Performing matrix operations on array shape {Xn.shape}")
    # covariance
    cov = np.cov(Xn, rowvar=False)
    print('\nCovariance matrix:\n', cov)
    # eigen decomposition
    vals, vecs = np.linalg.eig(cov)
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]
    print('\nTop eigenvalues:', vals[:3])
    print('\nCorresponding eigenvectors:\n', vecs[:, :3])
    # Save to file
    np.savetxt(os.path.join(PLOTS_DIR, 'cov_matrix.csv'), cov, delimiter=',')
    np.savetxt(os.path.join(PLOTS_DIR, 'eigenvalues.csv'), vals, delimiter=',')
    np.savetxt(os.path.join(PLOTS_DIR, 'eigenvectors.csv'), vecs, delimiter=',')

    # Short discussion printed
    print('\nInterpretation: eigenvectors of covariance show principal directions of variability.\nFor example, a large eigenvalue direction might indicate that capacity covaries with geographic coordinates,\nsuggesting regional differences in typical plant capacities.')


def main():
    csv_path = download_and_extract_zip(DATA_URL, DATA_DIR)
    df = load_dataframe(csv_path)
    df = clean_dataframe(df)
    eda_stats(df)
    statistical_analysis(df)
    time_series_analysis(df)
    geographic_plots(df)
    matrix_operations_and_eig(df)
    print('\nAnalysis complete. Plots and outputs saved to', PLOTS_DIR)


if __name__ == '__main__':
    main()
