import urllib
import urlparse
import pprint
import datetime
import SocketServer
import BaseHTTPServer
import select

from django.http import QueryDict
from django.db import DatabaseError

from rapidsms.backends.base import BackendBase
from rapidsms.log.mixin import LoggerMixin


class TwilioHandler(BaseHTTPServer.BaseHTTPRequestHandler, LoggerMixin):
    '''An HTTP server that handles messages to and from Twilio '''

    def _logger_name(self):
        return 'handler/twilio'

    def do_POST(self):
        self.debug('POST')
        content_length = self.headers['Content-Length']
        data = self.rfile.read(int(content_length))
        data = self.server.backend.parse_POST(data)
        message = self.server.backend.message(data)
        self.server.backend.route(message)
        # immediately respond with OK message
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('OK')
        return


class HttpServer (BaseHTTPServer.HTTPServer, SocketServer.ThreadingMixIn):

    def handle_request (self, timeout=1.0):
        # don't block on handle_request
        reads, writes, errors = (self,), (), ()
        reads, writes, errors = select.select(reads, writes, errors, timeout)
        if reads:
            BaseHTTPServer.HTTPServer.handle_request(self)


class TwilioBackend(BackendBase):
    '''A RapidSMS backend for Twilio (http://www.twilio.com/)'''

    def configure(self, host="localhost", port=8080, **kwargs):
        self.handler = TwilioHandler
        self.debug('Starting Twilio HTTP server on {0}:{1}'.format(host, port))
        self.server = HttpServer((host, int(port)), self.handler)
        # set this backend in the server instance so it
        # can callback when a message is received
        self.server.backend = self
        # also set it in the handler class so we can callback
        self.handler.backend = self

    def run(self):
        self.debug('run')
        while self.running:
            msg = self.next_message()
            if msg:
                if handlers.msg_store.has_key(msg.connection.identity):
                        handlers.msg_store[msg.connection.identity].append(msg.text)
                else:
                        handlers.msg_store[msg.connection.identity] = []
                        handlers.msg_store[msg.connection.identity].append(msg.text)
            self.server.handle_request()

    def send(self, message):
        self.debug('send: %s' % message)

    def parse_POST(self, data):
        data = QueryDict(data)
        self.debug(pprint.pformat(data, indent=4))
        return data

    def message(self, data):
        self.debug('message')
        now = datetime.datetime.utcnow()
        sms = data['Body']
        sender = data['From']
        self.debug('{0} {1} {2}'.format(sender, sms, now))
        try:
            msg = super(TwilioBackend, self).message(sender, sms, now)
        except DatabaseError, e:
            self.exception(e)
            raise
        self.debug(msg)
        return msg
