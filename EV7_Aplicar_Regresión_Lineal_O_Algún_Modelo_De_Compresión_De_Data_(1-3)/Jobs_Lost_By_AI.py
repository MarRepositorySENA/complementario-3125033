import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el CSV
df = pd.read_csv('Hostinger/Jobs_Lost_by_AI.csv')

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Crear el gráfico de barras apiladas
df.set_index('Country')[['Definitely', 'Probably']].plot(kind='bar', stacked=True, color=['#FF4B4B', '#FF8C8C'], ax=ax)

# Añadir título y etiquetas
ax.set_title('Percepción del impacto de los robots en los trabajos en los próximos 50 años', fontsize=14)
ax.set_xlabel('Países', fontsize=12)
ax.set_ylabel('Porcentaje de Respuestas', fontsize=12)

# Mostrar leyenda y ajustar
ax.legend(title='Respuestas')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
