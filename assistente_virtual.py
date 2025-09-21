import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import time

# Inicializa o mecanismo de fala (TTS)
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Velocidade da fala

# Função para falar
def speak(text):
    print(f"Assistente: {text}")
    engine.say(text)
    engine.runAndWait()

# Função para ouvir comandos do usuário
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Ouvindo...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Desculpe, não entendi.")
            return ""
        except sr.RequestError:
            speak("Erro na conexão com o serviço de reconhecimento.")
            return ""

# Ações por comando de voz
def process_command(command):
    if "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        if topic:
            try:
                summary = wikipedia.summary(topic, sentences=2, lang='pt')
                speak(f"Segundo a Wikipedia: {summary}")
            except wikipedia.exceptions.DisambiguationError:
                speak("O termo é muito genérico, seja mais específico.")
            except wikipedia.exceptions.PageError:
                speak("Não encontrei nada sobre isso.")
        else:
            speak("Sobre o que você quer saber na Wikipedia?")

    elif "youtube" in command:
        speak("Abrindo o YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "farmácia" in command:
        speak("Buscando farmácias próximas.")
        webbrowser.open("https://www.google.com/maps/search/farmácia+próxima")

    elif "sair" in command or "encerrar" in command:
        speak("Encerrando o assistente. Até logo!")
        exit()

    else:
        speak("Comando não reconhecido. Tente novamente.")

# Loop principal
def main():
    speak("Olá! Eu sou seu assistente virtual. Como posso ajudar?")
    while True:
        command = listen()
        if command:
            process_command(command)
        time.sleep(1)

if __name__ == "__main__":
    main()
