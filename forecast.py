import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
def forecast_sales(data):
    data = data.copy()
    data = data.sort_values('Order Date')
    data['Day'] = (data['Order Date'] - data['Order Date'].min()).dt.days
    x = data[['Day']]
    y = data['Sales']
    model = LinearRegression()
    model.fit(x,y)
    #Making Predictions
    future_days = np.array(range(x['Day'].max()+1, x['Day'].max()+8)).reshape(-1,1)
    predictions = model.predict(future_days)
    return predictions