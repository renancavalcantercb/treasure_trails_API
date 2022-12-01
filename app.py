from flask import Flask
from flask_restx import Api, Resource, fields, marshal, abort

from api import get_treasures_trails_data

app = Flask(__name__)

app.config['ERROR_404_HELP'] = False

api = Api(app, version='1.0', title='Runescape Treasure Trails API',
          description='A simple treasure trails API',
          )

ns = api.namespace('treasure_trails', description='Treasure Trails values per tier')

treasure_trails = api.model('Model', {
    'tier': fields.String(required=True),
    'quantity': fields.String(required=True),
    'rank': fields.String(required=True),
})


@ns.route('/<string:nickname>')
@api.doc(params={'nickname': 'The player nickname'})
class TreasureTrails(Resource):
    @api.marshal_with(treasure_trails)
    def get(self, nickname):
        try:
            return marshal(get_treasures_trails_data(nickname).to_dict(orient='records'), treasure_trails,
                           skip_none=True)
        except Exception as e:
            abort(404, e)


if __name__ == '__main__':
    app.run()
