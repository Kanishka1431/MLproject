import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data = {
    'size': [1500, 1800, 2400, 3000, 3500],  # square footage
    'price': [400000, 500000, 600000, 650000, 700000]  # house price
}

df = pd.DataFrame(data)

X = df[['size']]  
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

with open('house_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
