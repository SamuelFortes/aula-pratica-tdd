import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno, contar_aprovados


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

def test_calcular_media():
    alunoTeste = Aluno("aluno teste", [10, 9, 7, 7, 6], 3)
    somatorioNotasALuno = sum(alunoTeste.notas)
    quantNotasAluno = len(alunoTeste.notas)
    CalculoDaMediaDoTeste = somatorioNotasALuno /quantNotasAluno
    CalculoDaMediaAtual = alunoTeste.calcular_media()

    assert CalculoDaMediaAtual == CalculoDaMediaDoTeste

def test_situacao():
    alunoTeste = Aluno("aluno teste", [6, 6, 6, 6], 3)
    alunoComMediaSeis = alunoTeste.situacao()

    assert alunoComMediaSeis == "Aprovado"

def test_menor_nota():
    alunoTeste = Aluno("aluno teste", [6, 6, 6, 7], 3)
    menorNotaAlunoTeste = min(alunoTeste.notas)
    menorNotaAlunoAtual = alunoTeste.menor_nota()

    assert menorNotaAlunoTeste == menorNotaAlunoAtual

def test_calcular_media_arredondada():
    alunoTeste = Aluno("aluno teste", [7, 8, 8], 0)
    mediaArredondada = alunoTeste.calcular_media_arredondada()

    assert mediaArredondada == 8

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função

def test_contar_aprovados_todos_aprovados():
    alunos = [Aluno("A", [8, 9, 7, 8]), Aluno("B", [7, 7, 7, 7])]
    assert contar_aprovados(alunos) == 2

def test_contar_aprovados_todos_reprovados():
    alunos = [Aluno("A", [4, 3, 5, 4]), Aluno("B", [2, 3, 2, 3])]
    assert contar_aprovados(alunos) == 0

def test_contar_aprovados_lista_mista():
    alunos = [Aluno("A", [8, 9, 7, 8]), Aluno("B", [4, 3, 5, 4]), Aluno("C", [6, 6, 6, 6])]
    assert contar_aprovados(alunos) == 2

def test_contar_aprovados_lista_vazia():
    assert contar_aprovados([]) == 0

# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
