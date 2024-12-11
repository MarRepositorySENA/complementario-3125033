import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    "Library": ["Lodash", "date-fns", "Zod", "Moment", "Day.js", "RxJS", "jQuery", "Yup", "core-js", "Immer"],
    "Usage (%)": [50, 36, 35, 33, 27, 24, 22, 16, 14, 12],
    "Respondents": [8633, 6281, 5809, 5680, 4611, 4125, 3864, 2836, 2474, 2156]
}

df = pd.DataFrame(data)

# Plot the data
plt.figure(figsize=(10, 6))
plt.barh(df["Library"], df["Usage (%)"], color="mediumpurple")
plt.xlabel("Usage (%)")
plt.ylabel("Library")
plt.title("JavaScript Libraries Usage (%)")
plt.gca().invert_yaxis()  # Invert the y-axis to have the highest rank on top
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.show()
