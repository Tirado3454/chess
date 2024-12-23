import requests
from PIL import Image
from io import BytesIO

def download_chessboard(fen):
    """
    Baixa uma imagem de tabuleiro configurada com base no FEN.
    Utiliza a API do Lichess para gerar o tabuleiro.
    """
    url = f"https://lichess.org/board/export/png/{fen}"
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception("Erro ao baixar o tabuleiro.")

# Exemplo de uso
if __name__ == "__main__":
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    board_image = download_chessboard(fen)
    board_image.save("tabuleiro_lichess.png")
    print("Tabuleiro salvo como tabuleiro_lichess.png")
