from flask import (Flask, request, jsonify, abort)
from .models import db, setup_db, Convocatoria
from flask_cors import CORS
from config.local import config
from .utilities import allowed_file

import os
import sys


def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins=['http://localhost:8080'])

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Max-Age', '10')
        return response


    @app.route('/convocatorias', methods=['POST'])
    def create_convocatorias():
        returned_code = 201
        list_errors = []
        try:
            body = request.get_json()

            if "jugador" not in body:
                list_errors.append("jugador is required")
            else:
                jugador = body.get('jugador')

            if "equipo" not in body:
                list_errors.append("equipo is required")
            else:
                equipo = body.get('equipo')
            
            if "torneo" not in body:
                list_errors.append("torneo is required")
            else:
                torneo = body.get('torneo')
            
            if len(list_errors) > 0:
                returned_code = 400
            else:
                convocatoria = Convocatoria(jugador, equipo, torneo)
                db.session.add(convocatoria)
                db.session.commit()

                convocatoria_id = convocatoria.id
            
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500

        finally:
            db.session.close()
        
        if returned_code == 400:
            return jsonify({'success': False, 'message': 'Error creando convocatoria', 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({'id': convocatoria_id, 'success': True, 'message': 'Convocatoria creada!'}), returned_code

    @app.route('/convocatorias', methods=['GET'])
    def get_convocatorias():
        returned_code = 200
        list_errors = []
        try:
            convocatorias = Convocatoria.query.all()
            convocatorias = [convocatoria.__serialize__() for convocatoria in convocatorias]
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        
        if returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({'success': True, 'convocatorias': convocatorias}), returned_code

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'message': 'Internal Server error'
        }), 500

    return app
