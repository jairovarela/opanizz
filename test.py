# test.py
def application(opanizenv, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    #return [b"Hello World"] # python3
    return ["Hello World"] # python2