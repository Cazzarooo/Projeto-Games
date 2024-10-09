# Zelda Games Dashboard

Este projeto é um **Dashboard Interativo** que permite explorar e visualizar informações sobre jogos da série **The Legend of Zelda** usando a [Zelda API](https://zelda.fanapis.com/). Ele é construído em **Python** usando a biblioteca **Streamlit** para a interface interativa e a biblioteca **Requests** para fazer chamadas à API.

## 📋 Funcionalidades

- Exibe uma lista de jogos da série **The Legend of Zelda**.
- Permite selecionar um jogo específico para visualizar detalhes, como descrição, desenvolvedor, publicador e data de lançamento.
- Interface simples e interativa com suporte a filtro de número de jogos a serem exibidos.

## 🚀 Requisitos

- Python 3.7+
- Bibliotecas:
  - Streamlit
  - Requests

## 🔧 Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/zelda-games-dashboard.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd zelda-games-dashboard
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Executando o Projeto

Após instalar as dependências, você pode iniciar o aplicativo com o seguinte comando:

```bash
streamlit run app.py
```

Isso abrirá o aplicativo no seu navegador padrão. Use o **slider** na barra lateral para selecionar quantos jogos deseja exibir e clique no nome do jogo para ver mais detalhes.

## 💻 Exemplo de Uso

### Tela Inicial
- A tela inicial apresenta uma lista de jogos da série **Zelda**, que pode ser filtrada pelo número de jogos exibidos.

### Detalhes do Jogo
- Ao selecionar um jogo da lista, o dashboard exibe detalhes sobre o jogo, incluindo sua descrição, desenvolvedor, publicador e data de lançamento.

## 📂 Estrutura do Projeto

```plaintext
├── app.py                 # Arquivo principal da aplicação
├── README.md              # Instruções e informações do projeto
├── requirements.txt       # Arquivo de dependências
```

## 🌐 API Utilizada

Este projeto utiliza a [Zelda API](https://zelda.fanapis.com/) para buscar dados sobre os jogos da série. Nenhuma chave de API é necessária, o que torna o uso extremamente simples.

---

### **requirements.txt**

```plaintext
streamlit
requests
```
