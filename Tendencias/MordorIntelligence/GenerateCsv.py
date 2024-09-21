import pandas as pd

# Data from the image to be converted into a CSV file
data = {
    'Category': ['Periodo de Estudio', 'Año Base Para Estimación', 'CAGR', 'Mercado de Crecimiento Más Rápido', 
                 'Mercado Más Grande', 'Concentración del Mercado', 'Jugadores Principales'],
    'Details': ['2019 - 2029', '2023', '24.30%', 'Asia Pacífico', 'América del Norte', 'Medio', 
                'Wolters Kluwer, CropX, General Electric, Microsoft, IBM']
}

# Create DataFrame
df = pd.DataFrame(data)

# Define the path for the CSV file
csv_path = "C:/Users/Maryu/Desktop/2024/Investigacion/Tendencias/MordorIntelligence/Green_Technology_Market.csv"

# Save DataFrame to CSV
df.to_csv(csv_path, index=False)

csv_path
