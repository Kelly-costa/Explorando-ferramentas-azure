# Exemplo de análise de sentimento de texto usando Azure Language Studio

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "SUA_CHAVE_AQUI"
endpoint = "SEU_ENDPOINT_AQUI"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Texto de exemplo
document = ["The hotel was very clean and the staff was friendly."]

response = client.analyze_sentiment(documents=document)[0]

print("Texto:", document[0])
print("Sentimento geral:", response.sentiment)
print("Pontuações:", response.confidence_scores)
