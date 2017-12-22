import multiprocessing

import pytest
import zmq


def test_can_send_and_receive():
    def run_command(command):
        return {'hi': 'there'}

    def start_server():
        ctx = zmq.Context()
        rep = ctx.socket(zmq.REP)
        rep.bind('tcp://*:5555')
        command = rep.recv_json()
        rep.send_json(run_command(command))

    server = multiprocessing.Process(target=start_server)
    server.start()

    ctx = zmq.Context()
    req = ctx.socket(zmq.REQ)
    req.connect('tcp://localhost:5555')
    req.send_json({'name': 'RunHello'})
    data = req.recv_json()
    assert data == {'hi': 'there'}
