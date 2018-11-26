def test_app_running(host):
    socket = host.socket("tcp://80")
    assert socket.is_listening

def test_app_message(host):
    cmd = host.run("curl http://localhost/")
    assert cmd.stdout == "Hello world"
