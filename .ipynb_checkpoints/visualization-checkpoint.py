import matplotlib.pyplot as plt
def plot_monthly_sales(monthly_sales):
    monthly_sales.plot()
    plt.title("Monthly Sales trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("monthly_sales.png")
    plt.close()