import pandas as pd
from ydata_profiling import ProfileReport

# Load your dataset
df = pd.read_csv("your_dataset.csv")

profile = ProfileReport(df, title="Profiling Report")
profile.to_file("output.html")  # Saves the report as an HTML file

# Once generated, open output.html in your browser to explore insights like:
# - Data types (categorical, numerical, etc.)
# - Missing values
# - Correlations
# - Distributions
# - Duplicate rows
# - Time-series and text analysis
# This package is great for Exploratory Data Analysis (EDA), helping you understand your dataset before diving into modeling.
