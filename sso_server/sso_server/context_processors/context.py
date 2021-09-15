def global_context(request):
    return {
        'CLIENT1_URL': 'http://client1.app.com:8001/client/',
        'CLIENT2_URL': 'http://client2.app.com:8002/client/'
    }