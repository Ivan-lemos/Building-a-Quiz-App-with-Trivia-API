import requests

def get_trivia_questions(amount: int = 10, question_type: str = "boolean") -> list[dict]:
    """Busca perguntas de trivia da Open Trivia Database API.

    Args:
        amount (int): O número de perguntas a serem buscadas (padrão: 10).
        question_type (str): O tipo de pergunta (e.g., "boolean" para verdadeiro/falso, padrão: "boolean").

    Returns:
        list[dict]: Uma lista de dicionários, onde cada dicionário representa uma pergunta.

    Raises:
        requests.exceptions.RequestException: Se a requisição à API falhar.
    """
    parameters = {
        "amount": amount,
        "type": question_type,
    }
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()  # Levanta uma exceção para erros de status HTTP
    data = response.json()
    return data["results"]


# Exemplo de uso (pode ser removido se este arquivo for apenas um módulo de dados)
if __name__ == "__main__":
    try:
        question_data = get_trivia_questions()
        print(f"Total de perguntas buscadas: {len(question_data)}")
        # print(question_data[0]) # Para ver a estrutura de uma pergunta
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar perguntas da API: {e}")


