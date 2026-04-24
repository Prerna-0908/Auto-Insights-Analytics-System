def generate_kpis(data):
    total_sales = data['Sales'].sum()
    monthly_sales = data.groupby(data['Order Date'].dt.to_period('M'))['Sales'].sum()
    category_sales = data.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    region_sales = data.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    return total_sales, monthly_sales, category_sales, region_sales 