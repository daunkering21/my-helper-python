from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset sederhana
# Luas rumah (fitur/input)
X = np.array([[30], [50], [70], [100]])  # Harus dalam bentuk 2D array

# Harga rumah (target/output)
y = np.array([300, 500, 700, 1000])

# Buat model dan latih
model = LinearRegression()
model.fit(X, y)

# Uji prediksi: rumah seluas 85 m²
prediksi = model.predict([[85]])
print(f"Prediksi harga rumah 85 m²: {prediksi[0]:.2f} juta")
