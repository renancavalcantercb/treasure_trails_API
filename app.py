from flask import Flask, jsonify
from api import get_treasures_trails_data, UserNotFound
from flask_restx import Api, Resource, abort

app = Flask(__name__)
app.config['ERROR_404_HELP'] = False

api = Api(app, version='1.0', title='Runescape Treasure Trails API',
          description='A simple treasure trails API',
          )

ns = api.namespace('treasure_trails', description='Treasure Trails values per tier')


@app.errorhandler(UserNotFound)
def handle_user_not_found(error):
    return jsonify(error=str(error)), 404


@ns.route('/<string:nickname>')
@api.doc(params={'nickname': 'The player nickname'})
class TreasureTrails(Resource):
    def get(self, nickname):
        try:
            return get_treasures_trails_data(nickname).to_dict(orient='records')
        except Exception as e:
            abort(404, e)


if __name__ == '__main__':
    app.run()
