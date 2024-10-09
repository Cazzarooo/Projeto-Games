import streamlit as st
import requests

# Função para buscar jogos da API Zelda
def get_zelda_games(limit=5):
    url = f"https://zelda.fanapis.com/api/games?limit={limit}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        st.error("Falha ao buscar dados da API Zelda.")
        return []

# Função para exibir detalhes do jogo
def show_game_details(game):
    st.subheader(game['name'])
    st.write(f"**Descrição**: {game['description']}")
    st.write(f"**Desenvolvedor**: {game['developer']}")
    st.write(f"**Publicador**: {game['publisher']}")
    st.write(f"**Data de Lançamento**: {game['released_date']}")

# Interface principal
def main():
    st.title("Biblioteca de Jogos Zelda")

    # Número de jogos a serem mostrados
    limit = st.sidebar.slider("Número de jogos a exibir", 1, 10, 2)
    
    # Obter dados da API
    games = get_zelda_games(limit)

    if games:
        game_names = [game['name'] for game in games]
        selected_game = st.selectbox("Selecione um jogo para ver mais detalhes:", game_names)

        for game in games:
            if game['name'] == selected_game:
                show_game_details(game)
                break
    else:
        st.write("Nenhum dado disponível no momento.")

if __name__ == "__main__":
    main()
