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

# Convertir los valores de desarrolladores y crecimiento a un formato adecuado
df['# de desarrolladores (millones)'] = df['# de desarrolladores'].str.extract(r'(\d+[\.,]?\d*)').replace({',': '.'}, regex=True).astype(float)
df['Crecimiento interanual (%)'] = df['Crecimiento interanual'].str.replace('%', '').astype(float)

# Crear el gráfico de burbujas
plt.figure(figsize=(10,6))

# Trazar las burbujas
plt.scatter(
    df['Crecimiento interanual (%)'],  # Eje X
    df['País'],                        # Eje Y
    s=df['# de desarrolladores (millones)']*100,  # Tamaño de las burbujas
    alpha=0.6, color='skyblue', edgecolor='black'
)

# Etiquetas y título
plt.xlabel('Crecimiento Interanual (%)')
plt.ylabel('País')
plt.title('Crecimiento Interanual y Número de Desarrolladores por País (Gráfico de Burbujas)')

# Mostrar la gráfica
plt.show()
