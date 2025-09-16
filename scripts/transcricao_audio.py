# Exemplo de transcrição de áudio usando Azure Speech-to-Text

from azure.ai.speech import SpeechConfig, SpeechRecognizer, AudioConfig

# Configurações do serviço
speech_key = "SUA_CHAVE_AQUI"
service_region = "REGIAO_DO_SERVICO"

speech_config = SpeechConfig(subscription=speech_key, region=service_region)
audio_config = AudioConfig(filename="WhatAICanDo.m4a")  # seu arquivo de áudio
speech_recognizer = SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Reconhecimento
result = speech_recognizer.recognize_once()
print("Transcrição do áudio:")
print(result.text)
