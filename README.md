# YouTube Video Analyzer (Analisador de Vídeos do YouTube)

Projeto em Python que analisa vídeos do YouTube para transcrição e resumo automático.

## Funcionalidades
- Baixa o áudio de vídeos do YouTube
- Converte para MP3 com ffmpeg
- Transcreve o conteúdo com o modelo Whisper (API ou local)
- Gera um resumo com GPT (na versão com API)

## Versões disponíveis

### `api_analisador.py`
- Usa OpenAI Whisper e ChatGPT
- Requer chave da OpenAI
- Ideal para automação

### `local_analisador.py`
- Usa Whisper localmente (gratuito)
- Transcrição offline
- O resumo deve ser feito manualmente com Claude, Bard ou similares

## Como usar
```bash
pip install -r requirements.txt
python api_analisador.py   # ou
python local_analisador.py
