#Page configuration
st.set_page_config(page_title='AQI & AQI Bucket Predictor', layout='wide')

image = Image.open("images.jpeg")
st.image("images.jpeg", width=500)

# set title
st.title("AQI and AQI Bucket Prediction App")

# Sidebar and Main columns
col1 = st.sidebar
col2, col3 = st.columns((2, 1))

#Load models
@st.cache_resource
def load_models():

    model_paths = {
        "aqi_model": "aqi_regressor.pkl",
        "bucket_model": "aqib_classifier.pkl",
        "bucket_encoder": "bucket_encoder.pkl"}

    # Validate files exist before loading
    for name, path in model_paths.items():
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing model file: {path}")

    aqi_model = joblib.load(model_paths["aqi_model"])
    bucket_model = joblib.load(model_paths["bucket_model"])
    bucket_encoder = joblib.load(model_paths["bucket_encoder"])

    return aqi_model, bucket_model, bucket_encoder


aqi_model, bucket_model, bucket_encoder = load_models()

# Sidebar About Section
col1.header("About this App")
col1.write("""
This app predicts:
- AQI (Air Quality Index)
- AQI Bucket (Good, Moderate, Poor, etc.)
""")

# Input Section
col2.subheader("Input Parameters")

city = col2.selectbox(
    "Select City",
    ['Ahmedabad', 'Aizawl', 'Amaravati', 'Amritsar', 'Bengaluru',
     'Bhopal', 'Brajrajnagar', 'Chandigarh', 'Chennai', 'Coimbatore',
     'Delhi', 'Ernakulam', 'Gurugram', 'Guwahati', 'Hyderabad',
     'Jaipur', 'Jorapokhar', 'Kochi', 'Kolkata', 'Lucknow', 'Mumbai',
     'Patna', 'Shillong', 'Talcher', 'Thiruvananthapuram', 'Visakhapatnam'])

date = col2.date_input("Select Date")

pollutants = [
    'PM2.5', 'PM10', 'NO', 'NO2', 'NOx',
    'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']

pollutant_values = {p: col2.number_input(f"{p}", min_value=0.0) for p in pollutants}

# Prediction logic
if col2.button("Predict"):

    year = date.year
    month = date.month
    day = date.day

    month_sin = np.sin(2 * np.pi * month / 12)
    month_cos = np.cos(2 * np.pi * month / 12)
    day_sin = np.sin(2 * np.pi * day / 7)
    day_cos = np.cos(2 * np.pi * day / 7)

    expected_columns = [
        "City", "year", "month_sin", "month_cos", "day_sin", "day_cos",
        'PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2',
        'O3', 'Benzene', 'Toluene', 'Xylene']

    data_dict = {
        "City": city,
        "year": year,
        "month_sin": month_sin,
        "month_cos": month_cos,
        "day_sin": day_sin,
        "day_cos": day_cos,
        **pollutant_values}

    input_data = pd.DataFrame([[data_dict[c] for c in expected_columns]], columns=expected_columns)

    predicted_aqi = aqi_model.predict(input_data)[0]

    input_data["AQI"] = predicted_aqi
    predicted_bucket = bucket_model.predict(input_data)[0]
    predicted_bucket_label = bucket_encoder.inverse_transform([predicted_bucket])[0]

    col2.success(f"Predicted AQI: {predicted_aqi:.2f}")
    col2.info(f"AQI Bucket: {predicted_bucket_label}")


# Pollutant Bar Chart

col3.subheader("Pollutant Levels Chart")

pollutant_df = pd.DataFrame({
    "Pollutant": pollutant_values.keys(),
    "Value": pollutant_values.values()
})

fig = px.bar(pollutant_df, x="Pollutant", y="Value", title="Input Pollutant Levels", text="Value")
fig.update_layout(xaxis_tickangle=-90, height=450)

col3.plotly_chart(fig, use_container_width=True)
