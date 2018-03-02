import hug
import API_web


def test_raiz():
    datos = hug.test.get(API_web, '/')
    assert datos.status == "200 OK"
    assert datos.data['status']=="OK"

def test_npartidas():
    datos = hug.test.get(API_web, '/')
    assert datos.status == "200 OK"
    assert datos.data['status']=="OK"
