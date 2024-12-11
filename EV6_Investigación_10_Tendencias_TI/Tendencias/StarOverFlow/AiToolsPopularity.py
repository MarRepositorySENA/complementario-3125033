import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame a partir de los datos
ai_tools_data = [
    ["AI Tool", "Popularity (%)"],
    ["ChatGPT", 82.1],
    ["GitHub Copilot", 41.2],
    ["Google Gemini", 23.9],
    ["Bing AI", 15.8],
    ["Visual Studio Intellicode", 13.6],
    ["Claude", 8.1],
    ["Codeium", 6.1],
    ["WolframAlpha", 5.6],
    ["Perplexity AI", 5.3],
    ["Tabnine", 5.0],
    ["Phind", 3.8],
    ["Meta AI", 3.2],
    ["Amazon Q", 2.6],
    ["You.com", 1.4],
    ["Cody", 1.3],
    ["OpenAI Codex", 1.3],
    ["Whispr AI", 1.0],
    ["Quora Poe", 0.9],
    ["Snyk Code", 0.9],
    ["Replit Ghostwriter", 0.4],
    ["Lightning AI", 0.3],
    ["AskCodi", 0.3],
    ["Andi", 0.2],
    ["Neeva AI", 0.2],
    ["Metaphor", 0.2],
]

df = pd.DataFrame(ai_tools_data[1:], columns=ai_tools_data[0])

# Convertir la columna de porcentaje a valores numéricos
df["Popularity (%)"] = pd.to_numeric(df["Popularity (%)"])

# Crear un gráfico de barras
plt.figure(figsize=(10, 8))
df.plot(x="AI Tool", y="Popularity (%)", kind="barh", color='#1f77b4', legend=False)

# Añadir título y etiquetas
plt.title("Popularity of AI Search and Developer Tools (2024 Developer Survey)")
plt.xlabel("Popularity (%)")
plt.ylabel("AI Tool")

# Mostrar el gráfico
plt.tight_layout()
plt.show()
