import csv

# Datos extraídos de la imagen
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

# Guardar datos en un archivo CSV
file_path_ai = 'ai_tools_popularity.csv'
with open(file_path_ai, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(ai_tools_data)

print(f"Archivo CSV guardado en {file_path_ai}")
