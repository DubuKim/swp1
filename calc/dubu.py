from cgi import parse_qs
from dubuTemplate import html

def application(environ, start_response):
		d = parse_qs(environ['QUERY_STRING'])
		a = d.get('a', [''])[0]
		b = d.get('b', [''])[0]
		
		if '' in [a, b]:
			response_body = html % {
				'sum' : "No Input",
				'product' : "No Input"
			}
		else:
			try:
				a, b = int(a), int(b)
				response_body = html % {
					'sum' : str(a + b),
					'product' : str(a * b)
				}
			except ValueError:
				response_body = html % {
					'sum' : "Wrong Input",
					'product' : "Wrong Input" 
				}
		start_response('200 OK', [
		  ('Content-Type', 'text/html'),
		  ('Content-Length', str(len(response_body)))
		])
		return [response_body]
