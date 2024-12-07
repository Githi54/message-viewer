import pytest
from bcrypt import hashpw, gensalt, checkpw
from api.utils import hash_password, verify_password

def test_hash_password():
    password = "mysecretpassword"
    hashed_password = hash_password(password)

    assert hashed_password != password

    assert verify_password(password, hashed_password)

def test_wrong_password():
    password = "mysecretpassword"
    wrong_password = "wrongpassword"
    hashed_password = hash_password(password)

    assert not verify_password(wrong_password, hashed_password)
