import streamlit as st

# Função para obter endereço da embaixada do Brasil
def get_embassy_address(city, country):
    # Aqui você pode usar uma lista pré-definida com endereços ou uma API de embaixadas
    embassy_data = {
        "Londres": "14-16 Cockspur St, St. James's, London SW1Y 5BL, UK",
        "Paris": "34 cours Albert 1er, 75008 Paris, France",
        # Adicione mais endereços conforme necessário
    }
    return embassy_data.get(city, "Endereço não disponível")

# Função para verificar hotéis da Accor
def check_accor_hotels(city):
    # Simular uma pesquisa de hotel. Na prática, você usaria uma API de hotéis.
    accor_hotels = ["Londres", "Paris", "São Paulo"]
    return "Sim" if city in accor_hotels else "Não"

# Função para recomendações turísticas
def get_tourist_recommendations(city):
    recommendations = {
        "Londres": ["Museu Britânico", "Big Ben", "London Eye"],
        "Paris": ["Torre Eiffel", "Museu do Louvre", "Catedral de Notre-Dame"],
        # Adicione mais recomendações conforme necessário
    }
    return recommendations.get(city, ["Recomendações não disponíveis"])

# Interface Streamlit
st.title("Informações para Turistas")

city = st.text_input("Digite a cidade que vai visitar")
month = st.selectbox("Selecione o mês da viagem", 
                     ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                      "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])

if city:
    # Endereço da embaixada
    embassy_address = get_embassy_address(city, "country")
    st.write(f"Endereço da Embaixada do Brasil: {embassy_address}")

    # Recomendações turísticas
    recommendations = get_tourist_recommendations(city)
    st.write("Sugestões de lugares para visitar:")
    for place in recommendations:
        st.write(f"- {place}")

    # Verificação de hotéis Accor
    has_accor = check_accor_hotels(city)
    st.write(f"Existem hotéis da rede Accor? {has_accor}")
