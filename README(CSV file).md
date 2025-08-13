Objective

Analyze sales data using Python and Pandas, and visualize the results using charts.

 Tools Used
	•	Python 3
	•	Pandas (for data analysis)
	•	Matplotlib (for charts)
	•	Jupyter Notebook / Google Colab

Project Structure

├── sales_data.csv           # Sample sales dataset
├── task5_sales_analysis.ipynb # Jupyter Notebook with analysis code
└── README.md                # Project documentation

Steps Performed
	1.	Load CSV File
Used pandas.read_csv() to load the sales data from sales_data.csv.
	2.	Analyze Sales
	•	Grouped data by Product and calculated total sales using groupby() and sum().
	•	Grouped data by Date to observe daily sales trends.
	3.	Visualize Data
	•	Created bar charts to compare product-wise sales.
	•	Created line charts to show sales trends over time.

 Sample Results
	•	Product B had the highest total sales.
	•	Sales peaked on 2025-08-03 for Product B.

 How to Run
	1.	Install dependencies:
    pip install pandas matplotlib
  2.	Run the Jupyter Notebook:
    jupyter notebook task5_sales_analysis.ipynb
