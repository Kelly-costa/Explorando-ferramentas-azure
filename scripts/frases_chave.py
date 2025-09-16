# Exemplo de extração de frases-chave usando Azure Language Studio

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "SUA_CHAVE_AQUI"
endpoint = "SEU_ENDPOINT_AQUI"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Texto de exemplo
document = ["Clean rooms, good service, great location near Buckingham Palace and Westminster Abbey."]

response = client.extract_key_phrases(documents=document)[0]

print("Texto:", document[0])
print("Frases-chave extraídas:", response.key_phrases)
