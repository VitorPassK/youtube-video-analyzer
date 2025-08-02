import os
from pytubefix import YouTube
import ffmpeg
import openai
from datetime import datetime

# Insira entre as aspas sua chave da OpenAI
openai.api_key = ""

def baixar_audio_do_youtube(url, pasta_destino="downloads"):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    caminho_download = audio_stream.download(output_path=pasta_destino)
    caminho_mp3 = os.path.splitext(caminho_download)[0] + ".mp3"

    # Converte para mp3 usando ffmpeg
    ffmpeg.input(caminho_download).output(caminho_mp3).run(overwrite_output=True)
    os.remove(caminho_download)  # remove .webm ou .mp4 original

    return caminho_mp3

def transcrever_audio_whisper(caminho_mp3):
    with open(caminho_mp3, "rb") as arquivo_audio:
        resposta = openai.Audio.transcribe(
            model="whisper-1",
            file=arquivo_audio
        )
    return resposta["text"]

def gerar_resumo_com_gpt(transcricao):
    prompt = f"Resuma o seguinte conteúdo extraído de um vídeo do YouTube:\n\n{transcricao}"

    resposta = openai.ChatCompletion.create(
        model="gpt-4",  # ou gpt-3.5-turbo se quiser economizar
        messages=[
            {"role": "system", "content": "Você é um assistente especialista em criar resumos."},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta['choices'][0]['message']['content']

def analisar_video(url):
    print("1. Baixando e convertendo áudio...")
    caminho_mp3 = baixar_audio_do_youtube(url)

    print("2. Transcrevendo com Whisper...")
    texto_transcrito = transcrever_audio_whisper(caminho_mp3)

    print("3. Resumindo com ChatGPT...")
    resumo = gerar_resumo_com_gpt(texto_transcrito)

    # Salva o resumo em um arquivo
    nome_arquivo = f"resumo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(resumo)

    print(f"\n Resumo salvo em: {nome_arquivo}")
    return resumo

# EXEMPLO DE USO:
if __name__ == "__main__":
    url_do_video = input("Digite a URL do vídeo do YouTube: ").strip()
    resultado = analisar_video(url_do_video)
    print("\nResumo final:\n", resultado)
