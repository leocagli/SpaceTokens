from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pickle
import numpy as np
import random

app = Flask(__name__)
CORS(app)

# Simulated AI model (replace with real trained model)
class ExoplanetClassifier:
    def predict(self, features):
        # Simulate prediction based on features
        score = random.uniform(0.7, 0.99)
        return score > 0.85, score

model = ExoplanetClassifier()

# Token rarity calculation
def calculate_rarity(radius, period, temp):
    if radius < 1.5 and 200 < period < 400 and 4000 < temp < 6000:
        return "Ultra Rare"
    elif radius < 2.0 and 100 < period < 500:
        return "Rare"
    elif radius < 3.0:
        return "Uncommon"
    return "Common"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/classify', methods=['POST'])
def classify():
    data = request.json
    
    # Extract features
    period = float(data.get('period', 365))
    radius = float(data.get('radius', 1.0))
    temp = float(data.get('temp', 5778))
    
    # Predict
    is_candidate, confidence = model.predict([period, radius, temp])
    
    if is_candidate:
        # Generate token metadata
        token = {
            'id': f'EXO-{random.randint(1000, 9999)}',
            'name': f'Exoplanet {random.choice(["Alpha", "Beta", "Gamma", "Delta"])} {random.randint(1, 999)}',
            'rarity': calculate_rarity(radius, period, temp),
            'confidence': round(confidence * 100, 2),
            'period': period,
            'radius': radius,
            'temp': temp,
            'fundingGoal': random.randint(5000, 50000),
            'currentFunding': 0
        }
        return jsonify({'success': True, 'token': token})
    
    return jsonify({'success': False, 'message': 'Not a strong candidate'})

@app.route('/api/tokens')
def get_tokens():
    # Sample tokens for gallery
    tokens = [
        {
            'id': 'EXO-1001',
            'name': 'Kepler-442b',
            'rarity': 'Ultra Rare',
            'confidence': 95.8,
            'period': 112.3,
            'radius': 1.34,
            'temp': 4402,
            'fundingGoal': 25000,
            'currentFunding': 18500
        },
        {
            'id': 'EXO-1002',
            'name': 'TRAPPIST-1e',
            'rarity': 'Rare',
            'confidence': 92.3,
            'period': 6.1,
            'radius': 0.92,
            'temp': 2559,
            'fundingGoal': 30000,
            'currentFunding': 12000
        },
        {
            'id': 'EXO-1003',
            'name': 'Proxima Centauri b',
            'rarity': 'Ultra Rare',
            'confidence': 97.1,
            'period': 11.2,
            'radius': 1.17,
            'temp': 3042,
            'fundingGoal': 50000,
            'currentFunding': 35000
        }
    ]
    return jsonify(tokens)

@app.route('/api/fund', methods=['POST'])
def fund():
    data = request.json
    token_id = data.get('tokenId')
    amount = data.get('amount', 100)
    
    return jsonify({
        'success': True,
        'message': f'Successfully funded {amount} USD to {token_id}',
        'txHash': f'0x{random.randint(10**63, 10**64-1):064x}'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
