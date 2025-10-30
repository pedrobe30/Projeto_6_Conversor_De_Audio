def tranforma_audio():
    try:
        with open('audio_TOP_SECRET.txt', 'rb') as arquive:
            conteudo = arquive.read()
            print(type(conteudo))
        with open('conteudo.mp3', 'wb') as audio:
            audio.write(conteudo)
    except FileNotFoundError as e:
        print("Arquivo não existe", e)
        arquive = open("audio_TOP_SECRET.txt", 'wb')
        arquive.close()
    except IOError as e:
        print ('Erro')

tranforma_audio()

