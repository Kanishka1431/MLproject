from django.shortcuts import render
from .models import HousePriceHistory
from decimal import Decimal

def predict(request):
    prediction = None
    inputs = None

    if request.method == "POST":
        # Extract data from the form
        size = float(request.POST['size'])
        bedrooms = int(request.POST['bedrooms'])
        bathrooms = int(request.POST['bathrooms'])
        location = request.POST['location']
        age = int(request.POST['age'])
        garage = int(request.POST['garage'])

        # Example prediction model (you can replace with your own logic)
        prediction = Decimal(size * 100 + bedrooms * 5000 + bathrooms * 3000)  # Simple formula for demo

        # Save prediction to the database
        history_entry = HousePriceHistory(
            size=size,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            location=location,
            age=age,
            garage=garage,
            predicted_price=prediction
        )
        history_entry.save()

        # Return the data to the template
        inputs = {
            'size': size,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'location': location,
            'age': age,
            'garage': garage
        }

    # Fetch the last 5 predictions from the database to show history
    history = HousePriceHistory.objects.all().order_by('-timestamp')[:5]

    return render(request, 'predict.html', {'prediction': prediction, 'inputs': inputs, 'history': history})