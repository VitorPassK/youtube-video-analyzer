# 🎥 YouTube Video Analyzer — Analisador de Vídeos do YouTube com Python

Projeto pessoal para analisar vídeos do YouTube automaticamente com Python, transcrevendo o áudio e gerando um resumo do conteúdo.  
Ideal para estudantes, produtores de conteúdo ou qualquer pessoa que deseje extrair informações rápidas de vídeos.

---

## ⚙️ Funcionalidades

✔️ Download do áudio de vídeos do YouTube  
✔️ Conversão do áudio para `.mp3` com FFmpeg  
✔️ Transcrição usando o modelo **Whisper** da OpenAI (API) ou local (offline)  
✔️ Geração automática de resumo com **ChatGPT (GPT-4)** na versão com API  
✔️ Opção totalmente gratuita com transcrição local

---

## 🧠 Versões Disponíveis

### 🔹 `api_analisador.py`
> Usa a API da OpenAI para transcrição (`whisper-1`) e resumo (GPT-4 ou GPT-3.5).
- Requer chave de API da OpenAI
- Transcrição precisa e automatizada
- Resumo gerado automaticamente
- Ideal para uso em produção

### 🔹 `local_analisador.py`
> Usa o modelo **Whisper localmente**, sem precisar de internet ou chave de API.
- 100% gratuito
- Requer instalação do Whisper e PyTorch
- Transcrição gerada localmente
- Resumo precisa ser feito manualmente (Claude, Bard, etc.)

---

## 📂 Estrutura do Projeto
youtube-analisador/
├── .venv/ ← Ambiente virtual (não vai para o GitHub)
├── downloads/ ← Áudios baixados (.mp3)
├── api_analisador.py ← Versão com OpenAI API
├── local_analisador.py ← Versão com Whisper local
├── requirements.txt ← Lista de bibliotecas necessárias
├── README.md ← Este documento
├── .gitignore ← Arquivo para ignorar env, áudios etc.


---

## ▶️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/youtube-analisador.git
cd youtube-analisador
```


### 2. Crie o ambiente virtual (opcional, mas recomendado)

python -m venv .venv
source .venv/Scripts/activate  # No Windows
ou
source .venv/bin/activate      # No Linux/macOS


### 3. Instale as dependências

pip install -r requirements.txt


### 4. Execute a versão desejada

#### Com API (transcrição + resumo):
python api_analisador.py

#### Local (somente transcrição):

python local_analisador.py


## 🧪 Teste Gratuito
Se não quiser usar a API da OpenAI:

Use local_analisador.py para transcrever sem custo.

Copie a transcrição e cole em modelos gratuitos como:

Claude (Anthropic)
Gemini (Google)
ChatGPT Free (GPT-3.5)

## 🔐 OpenAI API Key
Para usar a versão api_analisador.py, você precisará de uma chave da OpenAI:

1. Crie uma conta em https://platform.openai.com/

2. Vá em API Keys

3. Copie sua chave e cole no código:

openai.api_key = "sk-..."

📄 Licença
Este projeto está sob a licença MIT.
Sinta-se à vontade para usar, modificar e compartilhar!

Desenvolvido por Vítor Passeri de Souza Kaluf


