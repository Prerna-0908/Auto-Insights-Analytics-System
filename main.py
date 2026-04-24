print(">>> THIS IS THE MAIN FILE RUNNING")
from data_cleaning import clean_data
from analysis import generate_kpis
from visualization import plot_monthly_sales
from alerts import check_alerts
from forecast import forecast_sales
from email_alert import send_email

file_path = "train.csv"

data = clean_data(file_path)

total_sales, monthly_sales, category_sales, region_sales = generate_kpis(data)

print("\nTotal Sales:", total_sales)
print("\nCategory Sales:\n", category_sales)
print("\nRegion Sales:\n", region_sales)

plot_monthly_sales(monthly_sales)

print("About to call alert function")
alert_msg = check_alerts(data)
print(">>> Function returned:", alert_msg)

predictions = forecast_sales(data)
print("\n Next 7 Days Sales Prediction:\n", predictions)

alert_msg = check_alerts(data)
print("\nALERT STATUS:", alert_msg)
send_email(alert_msg)