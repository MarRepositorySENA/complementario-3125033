import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
csv_path = "C:/Users/Maryu/Desktop/2024/Investigacion/Tendencias/MordorIntelligence/Green_Technology_Market.csv"
df = pd.read_csv(csv_path)

# Datos para el gráfico (solo tomaremos algunas columnas para ilustrar)
labels = df['Category'][:6]  # Las categorías importantes
sizes = [24.30, 20, 15, 18, 10, 12]  # Asignamos algunos valores ilustrativos (puedes modificar según el análisis)

# Crear un gráfico circular
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

# Asegurar que el gráfico sea un círculo
plt.axis('equal')

# Título del gráfico
plt.title('Distribución de Categorías del Mercado de Tecnología Verde')

# Mostrar el gráfico
plt.show()
