import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the Excel file
df = pd.read_excel('Online-Store-Orders.xlsx')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create output file
with open('analysis_report.txt', 'w', encoding='utf-8') as report:
    report.write("=" * 60 + "\n")
    report.write("📊 ONLINE STORE ORDERS ANALYSIS REPORT\n")
    report.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.write("=" * 60 + "\n\n")

    # 1. Basic stats
    total_orders = len(df)
    total_revenue = df['TotalPrice'].sum()
    report.write(f"📦 Total Orders: {total_orders}\n")
    report.write(f"💰 Total Revenue: ${total_revenue:,.2f}\n\n")

    # 2. Order status breakdown
    report.write("📋 Order Status Breakdown:\n")
    status_counts = df['OrderStatus'].value_counts()
    for status, count in status_counts.items():
        report.write(f"   {status}: {count} orders\n")
    report.write("\n")

    # 3. Best selling products
    product_qty = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
    report.write("🏆 Top 5 Best Selling Products (by quantity):\n")
    for product, qty in product_qty.head(5).items():
        report.write(f"   {product}: {qty} units\n")
    report.write("\n")

    # 4. Worst selling products
    report.write("📉 Bottom 5 Worst Selling Products (by quantity):\n")
    for product, qty in product_qty.tail(5).items():
        report.write(f"   {product}: {qty} units\n")
    report.write("\n")

    # 5. Most cancelled products
    cancelled = df[df['OrderStatus'] == 'Cancelled']
    if len(cancelled) > 0:
        cancelled_counts = cancelled.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
        report.write("❌ Top 5 Most Cancelled Products:\n")
        for product, qty in cancelled_counts.head(5).items():
            report.write(f"   {product}: {qty} units cancelled\n")
        report.write("\n")

    # 6. Payment method popularity
    report.write("💳 Payment Method Usage:\n")
    payment_counts = df['PaymentMethod'].value_counts()
    for method, count in payment_counts.items():
        report.write(f"   {method}: {count} orders\n")
    report.write("\n")

    # 7. Referral source
    report.write("📢 Top Referral Source:\n")
    referral_counts = df['ReferralSource'].value_counts()
    for source, count in referral_counts.head(5).items():
        report.write(f"   {source}: {count} orders\n")
    report.write("\n")

    # 8. Coupon usage analysis
    coupon_used = df[df['CouponCode'].notna() & (df['CouponCode'] != '')]
    coupon_revenue = coupon_used['TotalPrice'].sum()
    report.write("🎟️ Coupon Usage:\n")
    report.write(f"   Orders with coupon: {len(coupon_used)} ({len(coupon_used)/total_orders*100:.1f}%)\n")
    report.write(f"   Revenue from coupon orders: ${coupon_revenue:,.2f}\n")
    report.write(f"   Most used coupon: {df['CouponCode'].mode()[0] if not df['CouponCode'].mode().empty else 'None'}\n\n")

    # 9. Monthly revenue trend
    df['YearMonth'] = df['Date'].dt.to_period('M')
    monthly_revenue = df.groupby('YearMonth')['TotalPrice'].sum().sort_index()
    report.write("📅 Monthly Revenue Trend:\n")
    for period, revenue in monthly_revenue.items():
        report.write(f"   {period}: ${revenue:,.2f}\n")
    report.write("\n")

    # 10. Insight summary
    report.write("💡 KEY INSIGHTS:\n")
    report.write(f"   - Best selling product: {product_qty.index[0]} ({product_qty.iloc[0]} units)\n")
    report.write(f"   - Worst selling product: {product_qty.index[-1]} ({product_qty.iloc[-1]} units)\n")
    report.write(f"   - Most common order status: {status_counts.index[0]} ({status_counts.iloc[0]} orders)\n")
    report.write(f"   - Highest revenue month: {monthly_revenue.idxmax()} (${monthly_revenue.max():,.2f})\n")
    report.write("=" * 60 + "\n")
    report.write("✅ Analysis complete. Report saved as 'analysis_report.txt'\n")

print("✅ Analysis complete! Check 'analysis_report.txt' for full report.")

# ----- CHARTS (optional, will show pop-up windows) -----
try:
    # Bar chart: Top 10 best selling products
    plt.figure(figsize=(10, 5))
    product_qty.head(10).plot(kind='bar', color='skyblue')
    plt.title('Top 10 Best Selling Products (by quantity)')
    plt.xlabel('Product')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('top_products_chart.png')
    plt.show()

    # Pie chart: Order status distribution
    plt.figure(figsize=(8, 8))
    status_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Order Status Distribution')
    plt.ylabel('')
    plt.savefig('order_status_pie.png')
    plt.show()

    # Line chart: Monthly revenue trend
    plt.figure(figsize=(12, 5))
    monthly_revenue.plot(kind='line', marker='o', color='green')
    plt.title('Monthly Revenue Trend')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('monthly_revenue_trend.png')
    plt.show()

    print("📊 Charts saved as: top_products_chart.png, order_status_pie.png, monthly_revenue_trend.png")
except Exception as e:
    print(f"Note: Charts could not be generated. If you want charts, run: pip install matplotlib")