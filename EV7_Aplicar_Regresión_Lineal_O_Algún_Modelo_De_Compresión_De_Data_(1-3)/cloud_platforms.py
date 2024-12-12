import pandas as pd
import matplotlib.pyplot as plt

# Define los datos extraídos
data = [
    ["Cloud Platform", "Desired (%)", "Admired (%)"],
    ["Amazon Web Services", 43.4, 63.3],
    ["Microsoft Azure", 24.9, 59.9],
    ["Google Cloud", 23.4, 55.6],
    ["Cloudflare", 15.8, 68.2],
    ["Firebase", 11.8, 54.8],
    ["Vercel", 10.6, 59.4],
    ["Digital Ocean", 10.4, 56.6],
    ["Hetzner", 5.6, 74.6],
    ["Supabase", 5.3, 62.8],
    ["Netlify", 5.2, 49.4],
    ["Heroku", 4.0, 25.8],
    ["Fly.io", 3.9, 61.7],
    ["VMware", 3.8, 39.1],
    ["Linode", 3.5, 55.2],
    ["Oracle Cloud Infra", 2.9, 56.3],
    ["Databricks", 2.7, 54.9],
    ["OpenShift", 2.5, 52.0],
    ["Managed Hosting", 2.4, 62.6],
    ["OVH", 2.4, 55.1],
    ["Render", 2.2, 50.2],
    ["OpenStack", 2.1, 49.0],
    ["PythonAnywhere", 2.1, 41.6],
    ["Vultr", 1.5, 51.1],
    ["Alibaba Cloud", 1.4, 40.9],
    ["IBM Cloud Or Watson", 1.4, 40.3],
    ["Scaleway", 0.9, 55.6],
    ["Colocation", 0.8, 62.5],
]

# Crea un DataFrame a partir de los datos
df = pd.DataFrame(data[1:], columns=data[0])

# Convierte las columnas de porcentaje a valores numéricos
df["Desired (%)"] = pd.to_numeric(df["Desired (%)"])
df["Admired (%)"] = pd.to_numeric(df["Admired (%)"])

# Gráfico de líneas para comparar Desired (%) y Admired (%)
plt.figure(figsize=(10, 8))
plt.plot(df["Cloud Platform"], df["Desired (%)"], marker='o', linestyle='-', color='#1f77b4', label='Desired (%)')
plt.plot(df["Cloud Platform"], df["Admired (%)"], marker='o', linestyle='-', color='#ff7f0e', label='Admired (%)')

# Títulos y etiquetas
plt.title("Comparison of Desired and Admired Cloud Platforms (2024 Developer Survey)", fontsize=14)
plt.xlabel("Cloud Platform", fontsize=12)
plt.ylabel("Percentage", fontsize=12)

# Rotar etiquetas del eje x
plt.xticks(rotation=90)

# Añadir leyenda
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
