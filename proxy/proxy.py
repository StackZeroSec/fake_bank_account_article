import mitmproxy.http
import re
from mitmproxy.tools.main import mitmdump

def response(flow: mitmproxy.http.HTTPFlow):
    
    if '<span class="balance">$1.00</span>' in flow.response.text:
        flow.response.text = flow.response.text.replace('<span class="balance">$1.00</span>', '<span class="balance">$10,000,000.00</span>')
        print('Replacement made!')


if __name__ == "__main__":
    mitmdump(['-s', __file__, '-p', '8888', '--certs', '*=mitmproxy-ca-cert.pem'])
