import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


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

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
