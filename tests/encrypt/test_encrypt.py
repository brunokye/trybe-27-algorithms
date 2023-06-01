import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('Teste', 2.5)

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(1, 2)

    assert encrypt_message('Teste', 10) == 'etseT'

    assert encrypt_message('Teste', 2) == 'ets_eT'
