import pandas as pd
import matplotlib.pyplot as plt

# Datos
data = {
    'Technology': [
        'JavaScript (JS)', 'HTML/CSS', 'Python (PY)', 'SQL', 'TypeScript (TS)', 'Bash/Shell', 'Java',
        'C#', 'C++', 'C', 'PHP', 'PowerShell', 'Go', 'Rust', 'Kotlin', 'Lua', 'Dart', 'Assembly', 'Ruby',
        'Swift', 'R', 'Visual Basic', 'MATLAB', 'VBA', 'Groovy', 'Scala', 'Perl', 'GDScript', 'Objective-C',
        'Elixir', 'Haskell', 'Delphi', 'MicroPython', 'Lisp', 'Clojure', 'Julia', 'Zig', 'Fortran', 'Solidity',
        'Ada', 'Erlang', 'F#', 'Apex', 'Prolog', 'OCaml', 'Cobol', 'Crystal', 'Nim', 'Zephyr'
    ],
    'Popularity (%)': [
        62.3, 52.9, 51, 51, 38.5, 33.9, 30.3, 27.1, 23, 20.3, 18.2, 13.8, 13.5, 12.6, 9.4, 6.2, 6, 5.4, 5.2,
        4.7, 4.3, 4.2, 4, 3.7, 3.3, 2.6, 2.5, 2.3, 2.1, 2.1, 2, 1.8, 1.6, 1.5, 1.2, 1.1, 1.1, 1.1, 1.1, 0.9,
        0.9, 0.9, 0.8, 0.8, 0.8, 0.7, 0.4, 0.4, 0.3
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Graficar
plt.figure(figsize=(10, 8))
df_sorted = df.sort_values('Popularity (%)', ascending=False)
plt.barh(df_sorted['Technology'], df_sorted['Popularity (%)'], color='skyblue')
plt.xlabel('Popularity (%)')
plt.ylabel('Technology')
plt.title('Most Popular Programming, Scripting, and Markup Languages (2024)')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar los porcentajes más altos arriba
plt.tight_layout()

# Mostrar el gráfico
plt.show()
