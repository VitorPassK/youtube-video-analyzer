import os
from pytubefix import YouTube
import ffmpeg
import whisper
from datetime import datetime

def baixar_audio(url, pasta_destino="downloads"):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    caminho_download = audio_stream.download(output_path=pasta_destino)
    caminho_mp3 = os.path.splitext(caminho_download)[0] + ".mp3"

    ffmpeg.input(caminho_download).output(caminho_mp3).run(overwrite_output=True)
    os.remove(caminho_download)

    return caminho_mp3

def transcrever_com_whisper_local(caminho_mp3):
    model = whisper.load_model("base")  # ou "small", "medium", "large"
    resultado = model.transcribe(caminho_mp3)
    return resultado["text"]

def salvar_transcricao(texto, nome_base="transcricao"):
    nome_arquivo = f"{nome_base}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(texto)
    print(f" Transcrição salva em: {nome_arquivo}")
    return nome_arquivo

def analisar_video_local(url):
    print("1. Baixando áudio...")
    mp3_path = baixar_audio(url)

    print("2. Transcrevendo localmente com Whisper...")
    texto = transcrever_com_whisper_local(mp3_path)

    salvar_transcricao(texto)

    print("\n Essa versão local não gera o resumo automaticamente.")
    print("Copie a transcrição e use um modelo gratuito (Claude, Bard, etc) para resumir.")

# Execução
if __name__ == "__main__":
    url = input("URL do vídeo do YouTube: ").strip()
    analisar_video_local(url)
