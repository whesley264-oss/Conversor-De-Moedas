import requests
import os

# --- CONFIGURAÇÃO ---
# Sua chave de API, já inserida no código.
API_KEY = "63844d0e45a0baf3184c26e1"

# Lista de moedas com os nomes mais comuns para facilitar a seleção
CURRENCIES = {
    "1": {"code": "USD", "name": "Dólar Americano"},
    "2": {"code": "EUR", "name": "Euro"},
    "3": {"code": "GBP", "name": "Libra Esterlina"},
    "4": {"code": "JPY", "name": "Iene Japonês"},
    "5": {"code": "CAD", "name": "Dólar Canadense"},
    "6": {"code": "AUD", "name": "Dólar Australiano"},
    "7": {"code": "BRL", "name": "Real Brasileiro"},
    "8": {"code": "CNY", "name": "Yuan Chinês"},
    "9": {"code": "ARS", "name": "Peso Argentino"}
}

# --- LÓGICA DO SCRIPT ---

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_exchange_rate(from_currency, to_currency):
    """Busca a taxa de conversão da API."""
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    
    try:
        response = requests.get(url, timeout=10) # Adiciona um timeout para evitar travamentos
        response.raise_for_status() # Lança um erro para códigos de status HTTP ruins
        data = response.json()

        if data["result"] == "success":
            rate = data["conversion_rates"][to_currency]
            return rate
        else:
            print("Erro na API. Verifique a chave ou o tipo de moeda.")
            print(f"Mensagem da API: {data.get('error-type', 'Não especificado')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: Verifique sua internet ou o URL da API.")
        return None
    except KeyError:
        print(f"Erro: A moeda de destino '{to_currency}' não foi encontrada nos dados da API.")
        return None

def display_currencies():
    """Exibe as moedas disponíveis para o usuário."""
    print("Moedas disponíveis para conversão:")
    for key, value in CURRENCIES.items():
        print(f"  {key} - {value['name']} ({value['code']})")

def get_currency_choice(prompt):
    """Obtém a escolha de moeda do usuário e valida."""
    while True:
        choice = input(prompt)
        if choice in CURRENCIES:
            return CURRENCIES[choice]
        else:
            print("Opção inválida. Por favor, digite o número da moeda.")

def get_amount():
    """Obtém a quantidade e valida."""
    while True:
        try:
            amount = float(input("Digite a quantidade que deseja converter: "))
            return amount
        except ValueError:
            print("Quantidade inválida. Por favor, digite um número.")

# --- FLUXO DO PROGRAMA ---

def main():
    clear_screen()
    print("--- Conversor de Moedas ---")

    display_currencies()
    from_currency_info = get_currency_choice("\nSelecione a moeda de origem (digite o número): ")
    
    clear_screen()
    display_currencies()
    to_currency_info = get_currency_choice("\nSelecione a moeda de destino (digite o número): ")

    clear_screen()
    amount_to_convert = get_amount()

    print("\nCalculando...\n")
    rate = get_exchange_rate(from_currency_info["code"], to_currency_info["code"])

    if rate is not None:
        result = amount_to_convert * rate
        print(f"--- Resultado da Conversão ---")
        print(f"{from_currency_info['name']} ({from_currency_info['code']}) {amount_to_convert:.2f} --> {to_currency_info['name']} ({to_currency_info['code']}) {result:.2f}")
    
    print("\nConversão concluída. Fim do programa.")

if __name__ == "__main__":
    main()
#qualquer um que queira usar ou modificar qualquer coisa va no site ExchangeRate-API e gere sua API gratuita pra conseguir usar