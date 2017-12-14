import flask

from account import command, api, repo

from contact_manager.account import exception


def start_app(host, port, api_:api.Api, debug=False):
    app = flask.Flask(__name__)

    @app.route('/api/account/register_user', methods=['POST'])
    def register_user():
        command_ = command.RegisterAccount(
            id=flask.request.json['id'],
            email_address=flask.request.json['email_address'],
            password=flask.request.json['password'],
        )
        api_.register_account(command_)
        return flask.jsonify('OK'), 201


    @app.route('/admin/shutdown', methods=['POST'])
    def shutdown():
        shutdown = flask.request.environ.get('werkzeug.server.shutdown')
        shutdown()
        return 'OK'


    @app.route('/api/auth/login', methods=['POST'])
    def login():
        command_ = command.Login(flask.request.json['email_address'], flask.request.json['password'])
        session = api_.login(command_)
        return flask.jsonify(dict(session_token=session))


    @app.errorhandler(exception.InvalidCredentials)
    def invalid_creds(error):
        return flask.jsonify('Not Found'), 404

    app.run(host, port, debug=debug)
    app.logger.info('app started')



if __name__ == '__main__':
    api_ = api.Api(repo.InMemoryAccountRepository(), 'dkajf;lkajflk')
    start_app('localhost', 5000, api_, debug=True)
