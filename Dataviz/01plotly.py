import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

data = {
    'Date': pd.date_range(start='2023-01-01',periods=100),
    'StockA':[100 + i for i in range(100)],
    'StockB':[120 - i for i in range(100)],
    'StockC':[90 + (i *0.5)for i in range (100)],
}

df = pd.DataFrame   (data)
print(df)