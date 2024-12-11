import pandas as pd
import matplotlib.pyplot as plt

# Datos de los módulos y su peso en el desarrollo
data = {
    'Módulo': ['Caja', 'Portal de Facturas', 'Inscripciones', 'Pagos'],
    'Complejidad (%)': [30, 25, 20, 25],
    'Horas': [120, 100, 80, 100]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Crear gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(df['Complejidad (%)'], labels=df['Módulo'], autopct='%1.1f%%', startangle=140)

# Título del gráfico
plt.title('Desarrollo ágil del nuevo sistema institucional basado en una arquitectura orientada a microservicios')

# Mostrar gráfico
plt.show()

