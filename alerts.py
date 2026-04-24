def check_alerts(data):
    print("Alert Function Running")
    recent_sales = data.sort_values('Order Date').tail(7)['Sales'].mean()
    overall_sales = data['Sales'].mean()
    if recent_sales < overall_sales * 0.5:
        return "ALERT: Sales have dropped significantly"
    elif recent_sales > overall_sales * 1.5:
        return "Sales spike"
    else:
        return "Sales are stable"
        
        