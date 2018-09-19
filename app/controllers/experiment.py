import os
import datetime
import json
from flask import request, jsonify
from app import app, mongo
from ..zoo import *


@app.route('/train', methods=['POST'])
def train():
  data = request.get_json()
  id = data.get('id')
  model = tips.load_model(id)
  X_train, X_test , y_train , y_test = tips.get_data_sets()
  tips.train(model, X_train, y_train)
  tips.save_model(model,id)
  return jsonify({'ok': True, 'message': 'Model trained successfully!'}), 200


@app.route('/test', methods=['GET'])
def test():
  id = request.args.get('id')
  model = tips.load_model(id)
  X_train, X_test , y_train , y_test = tips.get_data_sets()
  score = tips.test(model, X_test, y_test)
  return jsonify({'score': score}), 200

@app.route('/predict', methods=['POST'])
def predict():
  data = request.get_json()
  id = data.get('id')
  sample = data.get('sample')
  if type(sample) is str:
    sample = json.loads(sample)
  model = tips.load_model(id)
  result = tips.predict(model, sample)
  return jsonify({'result': result}), 200

@app.route('/experiment', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def experiment():
  if request.method == 'GET':
    id = request.args.get('id')
    data = mongo.db.experiments.find_one({'id': id})
    return jsonify(data), 200

  data = request.get_json()
  if request.method == 'POST':
    if data.get('name', None) is not None and data.get('id', None) is not None:
      if data.get('type') == 'tips':
        model = tips.create_model()
        tips.save_model(model,data.get('id'))
        data['start_date'] = datetime.datetime.now()
        mongo.db.experiments.insert_one(data)
        return jsonify({'ok': True, 'message': 'Model created successfully!'}), 200
    else:
      return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

  if request.method == 'DELETE':
    if data.get('id', None) is not None:
      db_response = mongo.db.experiments.delete_one({'id': data['id']})
      if db_response.deleted_count == 1:
        response = {'ok': True, 'message': 'record deleted'}
      else:
        response = {'ok': True, 'message': 'no record found'}
      return jsonify(response), 200
    else:
      return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

  if request.method == 'PATCH':
    if data.get('id', None) is not None:
      mongo.db.experiments.update_one(
        data['id'], {'$set': data.get('payload', {})})
      return jsonify({'ok': True, 'message': 'record updated'}), 200
    else:
      return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

