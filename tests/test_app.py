from app import app

def test_index():
    assert index() == "Hello World"