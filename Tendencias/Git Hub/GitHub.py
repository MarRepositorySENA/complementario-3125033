import pandas as pd
import matplotlib.pyplot as plt

# Definir los datos
data = {
    'País': [
        'Singapur', 'India', 'Hong Kong (RAE)', 'Vietnam', 'Indonesia', 'Japón', 
        'Filipinas', 'Tailandia', 'Corea del Sur', 'Australia'
    ],
    '# de desarrolladores': [
        '>1 millón de desarrolladores', '>13,2 millones de desarrolladores', '>1,6 millones de desarrolladores', 
        '>1,5 millones de desarrolladores', '>2,9 millones de desarrolladores', '>2,8 millones de desarrolladores', 
        '>1,3 millones de desarrolladores', '>857K desarrolladores', '>1,9 millones de desarrolladores', 
        '>1,4 millones de desarrolladores'
    ],
    'Crecimiento interanual': [
        '39%', '36%', '35%', '34%', '31%', '31%', '31%', '25%', '22%', '21%'
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Convertir los valores de desarrolladores y crecimiento a un formato adecuado para la gráfica
df['# de desarrolladores (millones)'] = df['# de desarrolladores'].str.extract(r'(\d+[\.,]?\d*)').replace({',': '.'}, regex=True).astype(float)
df['Crecimiento interanual (%)'] = df['Crecimiento interanual'].str.replace('%', '').astype(float)

# Crear la figura y los ejes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Graficar el número de desarrolladores como un gráfico de barras
ax1.barh(df['País'], df['# de desarrolladores (millones)'], color='skyblue')
ax1.set_xlabel('Millones de Desarrolladores')
ax1.set_ylabel('País')
ax1.set_title('Número de Desarrolladores y Crecimiento Interanual por País')

# Crear un segundo eje para el crecimiento interanual
ax2 = ax1.twinx()
ax2.plot(df['Crecimiento interanual (%)'], df['País'], color='orange', marker='o', linestyle='--', label='Crecimiento Interanual (%)')
ax2.set_ylabel('Crecimiento Interanual (%)')

# Añadir leyendas y mostrar la gráfica
ax1.legend(['Desarrolladores'], loc='lower right')
ax2.legend(['Crecimiento Interanual'], loc='upper right')

plt.tight_layout()
plt.show()
