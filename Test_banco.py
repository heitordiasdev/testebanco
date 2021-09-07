#Código de testes

import pytest
from Banco import banco

@pytest.fixture
def exemplo_test():
    return banco(1001, 'Heitor', 100, 500)

def test_se_o_valor_maior_que_zero_depositar(exemplo_test):
    assert exemplo_test.deposita(1001, 100) > 0
    #esse teste irá dá certo, pois estou depositado um valor maior que zero
    #no caso, 100 reais

def test_se_tem_saldo_depositar(exemplo_test):
    assert exemplo_test.deposita(1001, 0) > 0
    #esse teste não estou depositando nada, para verificar
    #se há saldo

def test_se_o_saque_vai_ser_positivo(exemplo_test):
    assert exemplo_test.saca(1001, 200) > 0
    #esse teste está dando certo, pois estou sacando 200 reais
    #um valor positivo

def test_se_tem_saldo_para_fazer_o_saque(exemplo_test):
    assert exemplo_test.saca(1001, 0) > 0
    #nesse teste não estou depositando nada, para verificar
    #se há saldo

def test_se_tem_saldo_para_fazer_a_transferencia(exemplo_test):
    assert exemplo_test.transfere(1001, 0) > 0
    #já nesse teste, estou novamente sem transferir valor
    #para primeiro saber se há saldo.

def test_se_a_conta_para_transferir_é_valida(exemplo_test):
    assert exemplo_test.transfere(1001, 100, 1003) == 1002
    #esse teste irá dá erro, pois não existe esse conta "1003"
    #para depositar.

def test_se_tem_valor_positivo_em_extrato(exemplo_test):
    assert exemplo_test.extrato(1001, -1) > 0
    #esse teste irá verificar se o extrato é positivo.
    #nesse caso "-1" não é positivo.






