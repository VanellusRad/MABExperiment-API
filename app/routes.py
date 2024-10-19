from flask import Blueprint, request, jsonify
from .models import ExperimentData  # Importação relativa do modelo
from .app import db  # Importação relativa do objeto db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "API is running!"

@main.route('/experiment', methods=['POST'])
def add_experiment_data():
    data = request.get_json()

    if not all(k in data for k in ("timestamp", "page_variant", "impressions", "clicks")):
        return jsonify({"error": "Missing data"}), 400

    timestamp = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S')

    new_data = ExperimentData(
        timestamp=timestamp,
        page_variant=data['page_variant'],
        impressions=data['impressions'],
        clicks=data['clicks']
    )

    db.session.add(new_data)
    db.session.commit()

    return jsonify({"message": "Data added successfully"}), 201
