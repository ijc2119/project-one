# Project One: Communities and Crime
#### Iris June Chang (ijc2119), Zijun Fu (zf2342), Raymond Li (jl6787), Chang Xiong (cx2335)

## Description
This project analyzes crime rates in U.S. communities by integrating multiple datasets. The objective is to identify socio-economic and law enforcement factors that influence crime patterns and provide insights to policymakers for better crime prevention and resource allocation.

## Data Sources
- [Communities and Crime Dataset](https://archive.ics.uci.edu/dataset/211/communities+and+crime+unnormalized)
- [Criminal Victimization Dataset](https://bjs.ojp.gov/library/publications/criminal-victimization-22-largest-us-states-2017-2019)
- [US Cities Database](https://simplemaps.com/data/us-cities)

## Prerequisites & Dependencies
To run this project, ensure you have the following installed:
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy
- Plotly
- Jupyter Notebook

## Installation Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/project-one.git
   ```
2. Navigate to the project directory:
   ```sh
   cd project-one
   ```
3. Install required libraries:
   ```sh
   pip install -r requirements.txt
   ```

## Usage Instructions
- Run `proj1.py` for data cleaning and preprocessing:
  ```sh
  python proj1.py
  ```
- Open `proj1_data.ipynb` to explore data processing and analysis.
- The final cleaned dataset is saved as `final_data_cleaned.csv`.

## Project Workflow
1. **Data Cleaning**: Formatting and merging datasets.
2. **Exploratory Data Analysis (EDA)**: Identifying patterns and correlations.
3. **Feature Engineering**: Standardization and PCA for dimensionality reduction.
4. **Crime Rate Insights**: Identifying key socioeconomic and law enforcement correlations.

## File Structure
- `proj1.py` → Data cleaning and preparation
- `proj1_data.ipynb` → Data analysis and report draft
- `dataset.csv` → Merged dataset
- `final_data_cleaned.csv` → Cleaned dataset after preprocessing
- `README.md` → Project documentation

## Contributors
- **Iris June Chang** - Data Acquisition & Preprocessing
- **Zijun Fu** - Report Writing & Documentation
- **Raymond Li** - Report Formatting & Refinement, ReadMe
- **Chang Xiong** - Exploratory Data Analysis & Feature Engineering

## Acknowledgments
- Inspired by research from the Bureau of Justice Statistics.
- Special thanks to our professor and teaching assistants for their guidance.