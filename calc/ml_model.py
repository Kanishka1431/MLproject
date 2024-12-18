import numpy as np
from sklearn.linear_model import LinearRegression  # Use a model (e.g., linear regression)

# Example dummy model for the sake of illustration
def predict_house_price(size, bedrooms, bathrooms, location, age, garage):
    # Example encoding for location
    locations = {'downtown': 1, 'suburb': 2, 'rural': 3}
    location_value = locations.get(location.lower(), 0)  # Default to 0 if location is invalid

    # Dummy coefficients (replace this with your actual model)
    model = LinearRegression()
    model.coef_ = np.array([100, 5000, 3000, 10000, -200, 2000])  # Example coefficients
    model.intercept_ = 50000  # Example intercept

    # Create feature array (size, bedrooms, bathrooms, location, age, garage)
    features = np.array([[size, bedrooms, bathrooms, location_value, age, garage]])

    # Make the prediction
    price = model.predict(features)
    return price[0]  # Return predicted price
