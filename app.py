import streamlit as st
import requests

# Função para obter a previsão do tempo
def get_weather(city, month):
    # Substitua pela sua chave de API do OpenWeatherMap
    api_key = 'SUA_API_KEY'
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    # Extrair dados de temperatura
    temp_min = min([item['main']['temp_min'] for item in data['list']])
    temp_max = max([item['main']['temp_max'] for item in data['list']])
    temp_avg = sum([item['main']['temp'] for item in data['list']]) / len(data['list'])
    
    return temp_max, temp_avg, temp_min

# Função para obter informações do aeroporto
def get_airport_info(city):
    # Substitua pela sua chave de API do AeroDataBox
    api_key = 'SUA_API_KEY'
    url = f"https://api.aerodatabox.com/v1/airports/search/term?q={city}"
    headers = {'x-apikey': api_key}
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Extrair nome do aeroporto e verificação de sala VIP
    airports = []
    for airport in data['items']:
        airport_info = {
            "name": airport['name'],
            "vip_lounge": 'Sim' if 'vipLounge' in airport and airport['vipLounge'] else 'Não'
        }
        airports.append(airport_info)
        
    return airports

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
    # Obter dados de clima
    temp_max, temp_avg, temp_min = get_weather(city, month)
    st.write(f"Temperatura máxima: {temp_max}°C")
    st.write(f"Temperatura média: {temp_avg}°C")
    st.write(f"Temperatura mínima: {temp_min}°C")

    # Obter dados de aeroporto
    airports = get_airport_info(city)
    st.write("Aeroportos e Salas VIP:")
    for airport in airports:
        st.write(f"Aeroporto: {airport['name']}, Sala VIP: {airport['vip_lounge']}")

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
