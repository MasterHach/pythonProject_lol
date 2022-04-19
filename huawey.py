import numpy as np
import pandas as pd
import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.linear_model import LinearRegression, LassoCV, Lasso, RidgeCV, Ridge
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Some nice default configuration for plots
plt.rcParams['figure.figsize'] = 10, 7.5
plt.rcParams['axes.grid'] = True
plt.pink()

df = datasets.fetch_openml(name="house_prices", as_frame=True)
dataframe = df['frame']
print(dataframe.head())
print(dataframe.dtypes)

# Определим имена столбцов, тип данных которых object
objects_names = dataframe.axes[1][dataframe.dtypes == object]
print(objects_names)
# Приведем столбцы (переменные) на позициях к типу данных категорий
dataframe[objects_names] = dataframe[objects_names].astype('category')

print(dataframe.dtypes)
print(dataframe)