import pandas as pd

# Data based on the provided information about AI trends and predictions for 2024
data = [
    {
        "Tendencia": "Personalización de la IA empresarial",
        "Descripción": "La personalización de la IA empresarial está en aumento, con aplicaciones de IA generativas personalizadas que satisfacen necesidades comerciales específicas. Esto transforma la IA en un activo estratégico vital para la interacción con los clientes, la eficiencia operativa y la competitividad del mercado.",
        "Ejemplo": "En Japón, la IA prioriza la eficiencia y precisión, mientras que en Brasil enfatiza la calidez y el compromiso, reflejando valores culturales en interacciones con clientes."
    },
    {
        "Tendencia": "Modelos de IA de código abierto",
        "Descripción": "Los modelos de IA preentrenados de código abierto ganan tracción, permitiendo a las empresas combinar estos modelos con datos privados para mejorar la productividad y rentabilidad.",
        "Ejemplo": "IBM y NASA crearon un modelo de IA geoespacial de código abierto que mejora la investigación relacionada con el clima y la inteligencia geoespacial."
    },
    {
        "Tendencia": "IA basada en API y microservicios",
        "Descripción": "La proliferación de API simplifica la creación de aplicaciones complejas impulsadas por IA, aumentando la productividad en diversos sectores.",
        "Ejemplo": "IBM desarrolló microservicios de IA para un minorista que mejoraron la eficiencia del servicio al cliente y la toma de decisiones basadas en datos."
    },
    {
        "Tendencia": "La IA como prioridad nacional",
        "Descripción": "Naciones de todo el mundo priorizan el desarrollo de la IA, impulsando avances significativos en investigación, ciencia y crecimiento económico.",
        "Ejemplo": "La Unión Europea trabaja en la Ley de IA de la UE, el primer marco legal integral que regula la implementación de la IA en diferentes niveles de riesgo."
    },
    {
        "Tendencia": "IA generativa multimodal",
        "Descripción": "La integración de texto, voz e imágenes en la IA generativa promete respuestas contextualmente relevantes y fomenta la innovación en diversos sectores.",
        "Ejemplo": "Durante una llamada de servicio al cliente, la IA puede analizar solicitudes habladas, documentos financieros y expresiones faciales para brindar asesoramiento más personalizado."
    },
    {
        "Tendencia": "Seguridad y ética de la IA",
        "Descripción": "El enfoque en la seguridad y la ética de la IA se intensifica, con esfuerzos para desarrollar sistemas de IA robustos y éticos.",
        "Ejemplo": "IBM y Meta fundaron la AI Safety Alliance para promover la innovación responsable y el desarrollo de tecnología de IA abierta con protocolos de seguridad y ética."
    }
]

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_file_path = '/mnt/data/tendencias_ia_2024.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8')

csv_file_path
