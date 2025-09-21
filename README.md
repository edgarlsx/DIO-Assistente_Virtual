# 🤖 Assistente Virtual com Python e PLN

Este projeto implementa um **Assistente Virtual** em Python utilizando técnicas de **Processamento de Linguagem Natural (PLN)** e bibliotecas de **Reconhecimento de Fala**, **Síntese de Voz** e **Integração com serviços da web**.

---

## 🎯 Objetivo

Desenvolver um sistema de assistência virtual capaz de:

- 🎙️ Ouvir comandos de voz do usuário
- 🧠 Interpretar o conteúdo usando PLN
- 🗣️ Responder com voz sintetizada (TTS)
- 🌐 Executar ações automatizadas como:
  - Pesquisar na Wikipedia
  - Abrir o YouTube
  - Localizar farmácias próximas no Google Maps

---

## 🧰 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/) – para acesso ao microfone
- [pyttsx3](https://pypi.org/project/pyttsx3/) – para Text-to-Speech offline
- [wikipedia](https://pypi.org/project/wikipedia/) – acesso à Wikipedia
- [webbrowser](https://docs.python.org/3/library/webbrowser.html) – abrir sites via navegador

---

## 🚀 Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/assistente-virtual-python.git

cd assistente-virtual-python

---

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv

source venv/bin/activate  # Linux/macOS

venv\Scripts\activate     # Windows

---

## Instale as dependências:

pip install -r requirements.txt

Ou instale manualmente:

pip install speechrecognition pyttsx3 wikipedia pyaudio

⚠️ Nota: No Windows, se pyaudio der erro, use:

pip install pipwin

pipwin install pyaudio

---

## ▶️ Como Executar

Execute o script principal:

python assistente_virtual.py

---

## Fale um comando, por exemplo:

"Wikipedia Albert Einstein"

"Abrir o YouTube"

"Onde tem farmácia próxima?"

"Encerrar"

O assistente irá interpretar seu comando e executar a ação correspondente.

## 📦 Funcionalidades

✅ Conversão de fala em texto (Speech-to-Text)

✅ Conversão de texto em fala (Text-to-Speech)

✅ Processamento de comandos com palavras-chave

✅ Integração com Wikipedia, YouTube e Google Maps

✅ Suporte à linguagem natural em português (pt-BR)
