import pytest, sys
from AbyissClient import AbyissClient
#import AbyissClient.client

#client = Client()
AbyissClient = AbyissClient.Client()

@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}
    
    def fake_write(s):
        buffer['stdout'] += s
        buffer["write_calls"] += 1
    
    monkeypatch.setattr(sys.stdout, 'write', fake_write)

def test_ping():
    ping = AbyissClient.ping()
    assert ping == {"ping": "Hello from the Abyiss"}

    #with pytest.raises(LookupError):
    #    assert client.get_exchanges(breakthis=0)

def test_exchanges():
    exchanges = AbyissClient.get_exchanges()
    assert exchanges is [4]
