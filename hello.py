def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    query = environ['QUERY_STRING']
    args = query.split('&')
    body = map(lambda s: s + '\n', args)
    start_response(status, headers )
    return body