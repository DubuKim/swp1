from cgi import parse_qs
from dubuTemplate import html

def application(environ, start_response):
		d = parse_qs(environ['QUERY_STRING'])
		a = d.get('a', [''])[0]
		b = d.get('b', [''])[0]
		if '' not in [a, b]:
			a, b = int(a), int(b)
			response_body = html % {
				'sum' : str(a + b),
				'product' : str(a * b)
			}
		else:
			response_body = html % {
				'sum' : "No Input",
				'product' : "No Input" 
			}
		start_response('200 OK', [
		  ('Content-Type', 'text/html'),
		  ('Content-Length', str(len(response_body)))
		])
		return [response_body]
