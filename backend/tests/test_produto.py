from backend.entity.produto import Produto
import pytest
from backend.exceptions.excecoes import NomeInvalidoError

def test_criar_produto_com_sucesso():
    """Garante que o Produto seja criado com dados válidos."""
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)
    assert  cafe._nome == "cafe" and cafe._preco == 18 and \
            cafe._quant_estoque == 50 and cafe._validade == 3 and \
            cafe._codigo_barras == 1234567890 and \
            cafe._categoria == "alimenticio" and cafe._peso == 250

def test_criar_produto_sem_nome():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(NomeInvalidoError):
        Produto(None,
                18,
                50,
                3,
                1234567890,
                "alimenticio",
                250)

def test_criar_produto_nome_vazio():
    with pytest.raises(NomeInvalidoError) as exc_info:
        Produto("",
                18,
                50,
                3,
                1234567890,
                "alimenticio",
                250)
    assert str(exc_info.value) == "Nome não pode ser vazio"

def test_criar_produto_sem_quantidade():
    with pytest.raises(ValueError):
        Produto("cafezes",
                None,
                50,
                3,
                1234567890,
                "alimenticio",
                250)

def test_criar_produto_sem_estoque():
    with pytest.raises(ValueError):
        Produto("cafezes",
                18,
                None,
                3,
                1234567890,
                "alimenticio",
                250)

def test_criar_produto_sem_valodade():
    with pytest.raises(ValueError):
        Produto("cafezes",
                18,
                50,
                None,
                1234567890,
                "alimenticio",
                250)

def test_criar_produto_sem_codigo_barra():
    with pytest.raises(ValueError):
        Produto("cafezes",
                18,
                50,
                3,
                None,
                "alimenticio",
                250)

def test_criar_produto_sem_categoria():
    with pytest.raises(ValueError):
        Produto("cafezes",
                18,
                50,
                3,
                1234567890,
                None,
                250)

def test_criar_produto_sem_peso():
    with pytest.raises(ValueError):
        Produto("cafezes",
                18,
                50,
                3,
                1234567890,
                "alimenticio",
                None)

def test_acessar_nome_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)
    assert cafe.nome == "cafe"

def test_acessar_preco_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)
    assert cafe.preco == 18

def test_acessar_quant_estoque_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)
    assert cafe.quant_estoque == 50

def test_acessar_validade_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)
    assert cafe.validade == 3

def test_acessar_codigo_barras_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)
    assert cafe.codigo_barras == 1234567890

def test_acessar_categoria_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)
    assert cafe.categoria == "alimenticio"

def test_acessar_peso_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)
    assert cafe.peso == 250

def test_atualizar_nome_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)

    cafe.nome = "cafezes"

    assert cafe._nome == "cafezes"
    assert cafe.nome == "cafezes"

def test_atualizar_preco_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)

    cafe.preco = 22

    assert cafe._preco == 22
    assert cafe.preco == 22

def test_atualizar_quant_estoque_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)

    cafe.quant_estoque = 1914

    assert cafe.quant_estoque == 1914
    assert cafe._quant_estoque == 1914

def test_atualizar_validade_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)

    cafe.validade = 12

    assert cafe.validade == 12
    assert cafe._validade == 12

def test_atualizar_codigo_barras_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)

    cafe.codigo_barras = 987654321

    assert cafe.codigo_barras == 987654321
    assert cafe._codigo_barras == 987654321

def test_atualizar_categoria_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)

    cafe.categoria = "Pneu"

    assert cafe.categoria == "Pneu"
    assert cafe._categoria == "Pneu"

def test_atualizar_peso_produto():
    cafe = Produto("cafe",
                   18,
                   50,
                   3,
                   1234567890,
                   "alimenticio",
                   250)

    cafe.peso = 2000

    assert cafe.peso == 2000
    assert cafe._peso == 2000