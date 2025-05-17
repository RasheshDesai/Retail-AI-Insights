
# 📊 Sales Analytics Dashboard

This is a **Sales Analytics Dashboard** built using **Plotly Dash** to visualize product sales across different cities in Canada. It enables users to explore data interactively via dropdowns, graphs, and tables.

![Example Output](images/App.png) 

## 🚀 Features

- Dark themed UI using `Dash Bootstrap Components (DARKLY theme)`
- Filter sales data by:
  - City
  - Product
  - Category
  - Month
- Interactive visualizations:
  - Top Products in City
  - Top Categories in City
  - Top Retailers by Sales
  - Postal Code level comparison
  - Sales Distribution Map
- Summary text and total sales information
- Dynamic product distribution table

## 🛠️ Tech Stack

- **Python**
- **Dash & Plotly**
- **Dash Bootstrap Components**
- **Pandas**
- **Custom Data Analysis Functions** (e.g. `TopProductCitySalesDollars`, `TotalCategoryCitySales`, etc.)

## 📂 Folder Structure

```
project/
├── app.py
├── data/
│   └── sales_data.csv
├── assets/
│   └── Example-Images
├── functions/
│   ├── charts.py
│   ├── maps.py
│   └── tables.py
├── README.md
```

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/sales-dashboard.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Visit [http://localhost:5000](http://localhost:5000) in your browser.

## 📊 Example Visuals

- Top Products by Sales in a Selected City

![Example Output](images/TopProductsSales.png) 

- Geographical Map Visualization of Retailers and Postal Code performance for selling the selected product (strong vs weak)

![Example Output](images/MapAndPostal.png)

- Category-wise Summary Stats

![Example Output](images/TableStat.png)



## 📦 Requirements

Include the following in `requirements.txt`:
```
dash
dash-bootstrap-components
pandas
plotly
```

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

Built with ❤️ using [Dash](https://dash.plotly.com/)
