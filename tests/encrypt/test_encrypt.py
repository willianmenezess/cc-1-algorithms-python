from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("palmeiras", 3) == "lap_sariem"
    assert encrypt_message("palmeiras", 4) == "sarie_mlap"
    assert encrypt_message("palmeiras", 10) == "sariemlap"
    with pytest.raises(TypeError):
        encrypt_message('palmeiras', 'p')

    with pytest.raises(TypeError):
        encrypt_message(1, 1)
