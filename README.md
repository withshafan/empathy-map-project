# Empathy Map Project

A comprehensive project combining UX research visualization and order data analysis tools.

## 📋 Project Overview

This project contains two main components:

1. **Empathy Map Visualization** - An interactive HTML-based empathy map for a fitness app targeting busy professionals
2. **Order Analysis Tool** - A Python-based analysis system for e-commerce order data

## 📁 Project Structure

```
empathy-map-project/
├── index.html                          # Interactive empathy map visualization
├── order-analysis/
│   ├── analyze_orders.py              # Python script for order analysis
│   └── analysis_report.txt            # Generated analysis report
└── README.md                           # This file
```

## 🎯 Features

### Empathy Map Visualization
- Interactive persona-based empathy map for fitness app users
- User-friendly interface with gradient design
- Responsive layout optimized for desktop and mobile viewing
- Explores customer pain points, goals, and expectations

### Order Analysis Tool
- Comprehensive e-commerce order analysis
- Supports Excel file input (Online-Store-Orders.xlsx)
- Generates detailed analysis reports including:
  - Total orders and revenue metrics
  - Order status breakdown
  - Top/bottom selling products
  - Cancelled product analysis
  - Additional insights and trends

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pandas library
- matplotlib library
- Modern web browser (for HTML visualization)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/withshafan/empathy-map-project.git
cd empathy-map-project
```

2. Install Python dependencies:
```bash
pip install pandas matplotlib openpyxl
```

### Usage

#### Empathy Map
Open `index.html` in your web browser to view the interactive empathy map visualization.

#### Order Analysis
1. Place your `Online-Store-Orders.xlsx` file in the `order-analysis` directory
2. Run the analysis script:
```bash
cd order-analysis
python analyze_orders.py
```
3. Check the generated `analysis_report.txt` for results

## 📊 Analysis Report Output

The order analysis generates a detailed report containing:
- **Total Orders**: Overall order count
- **Total Revenue**: Aggregated revenue from all orders
- **Order Status Breakdown**: Distribution across Cancelled, Returned, Pending, Shipped, and Delivered statuses
- **Top Products**: Best and worst selling products by quantity
- **Cancelled Orders**: Analysis of products with highest cancellation rates

## 🛠️ Technologies Used

- **Frontend**: HTML, CSS (modern design with gradients and responsive layout)
- **Backend**: Python
- **Data Processing**: pandas, matplotlib
- **Data Format**: Excel (.xlsx)

## 📝 Notes

- The empathy map is designed specifically for a fitness app targeting busy professionals
- Order analysis supports various product categories and order statuses
- All generated reports include timestamps for tracking

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

withshafan

## 📧 Support

For issues or questions, please open an issue on the GitHub repository.
