# RiwiSport Data Analysis Project

## Overview
This project analyzes sales data from RiwiSport, a retail store, using Python, SQL, and visualization libraries. The goal is to extract insights from customer orders, products, and categories to support business decisions.

## Project Structure
- `RiwiSport.sql`: SQL script to create and populate the database.
- `analisis_RIWI_Sport_Alberto-Jimenez.ipynb`: Python notebook to extract, process, and visualize sales data.
- `requirements.txt`: Contains all Python dependencies.
- `README.md`: Project documentation.
- `sqlLoader.py`: A python script to execute sql files

## Dependencies
The project uses the following Python libraries:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `sqlalchemy`
- `psycopg2`
- `scipy`

Install dependencies using:

```bash
pip install -r requirements.txt
````

## Database

The `RiwiSport.sql` file contains the database schema and initial data. Make sure it is located in the same folder as the project scripts. The project connects to a PostgreSQL database:

```python
host="localhost"
dbname="riwisport"
user="user with permissions"
password="password of the user"
port=5432
```

## Usage

### Step 1: Execute SQL Script

Create the database and then run the Python script to execute `RiwiSport.sql`:

```bash
python sqlLoader.py
```

### Step 2: Run Analysis

Use the `analisis_RIWI_Sport_Alberto-Jimenez.ipynb` script to:

* Load data from PostgreSQL.
* Compute aggregates and KPIs:

  * Total sales by category, product, customer, and city.
  * Measures of central tendency (mean, median, mode) per order and per customer.
  * Dispersion metrics (variance, standard deviation) per order and per customer.
  * Average order and customer ticket.
* Identify top 5 categories/products by sales and quantity.
* Identify product with highest price variability.
* Generate visualizations:

  * Histogram of total spending per customer.
  * Boxplot of sales by category.
  * Bar charts for top 5 categories and products by sales.

Run the script:

```bash
python analisis_RIWI_Sport_Alberto-Jimenez.ipynb
```

All outputs are printed to the console and visualizations are displayed using Matplotlib and Seaborn.