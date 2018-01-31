import hug


@hug.get('/')
def raiz():
    return{ "status":"OK" } 
