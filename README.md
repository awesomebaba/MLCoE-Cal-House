# California Housing Price Prediction (Using Linear Regression)

This project predicts housing prices in California based on several housing-related features using a **Linear Regression** model. The model helps estimate house prices based on user inputs. The web app is built with **Streamlit**, providing a user-friendly interface for predictions.

## Features

The following features are used to predict house prices:

1. **Name**: Enter your name.
2. **Longitude**: Longitude of the house's location.
3. **Latitude**: Latitude of the house's location.
4. **Housing Median Age**: The median age of houses in the area.
5. **Total Rooms**: Total number of rooms in the house.
6. **Total Bedrooms**: Total number of bedrooms in the house.
7. **Population**: Population in the area.
8. **Households**: Total number of households in the area.
9. **Median Income**: The median income of households in the area.
10. **Ocean Proximity**: The house's proximity to the ocean (options: '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND').

## How to Use

You can try the deployed app by following these steps:

1. Input your personal information and the details about the house (longitude, latitude, etc.).
2. Submit the form, and the app will provide an estimated house price based on your inputs.

## Technical Details

### Algorithm: **Linear Regression**

- **Linear Regression** is used to predict the house price based on a linear relationship between the target variable (house price) and the input features.
- The model was trained on the **California Housing Dataset**, which contains a variety of features like geographical location, housing age, and socio-economic factors that influence house prices.

### Key Features:
- **Geographical location (Longitude & Latitude)**: Important in determining house value, as different areas in California have varying real estate prices.
- **Ocean Proximity**: The model takes into account whether the house is near the ocean, which can significantly impact its price.
- **Socio-economic factors**: Variables such as population and median income also play a crucial role in the prediction.

## Deployed Link

#### Access the California Housing Price Prediction app here:  [https://mlcoe-cal-house.streamlit.app/](https://mlcoe-cal-house.streamlit.app/)

## Future Enhancements

- Incorporate other regression techniques such as Ridge and Lasso to improve accuracy.
- Include additional features like distance to schools, crime rates, and neighborhood amenities.
- Add visual analytics to show trends and correlations between features and house prices.

