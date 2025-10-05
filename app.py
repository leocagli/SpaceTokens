from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pickle
import numpy as np
import random
from nasa_scraper import NASAExoplanetScraper
from web3_integration import FilecoinNFTMinter

app = Flask(__name__)
CORS(app)

# Initialize NASA scraper and Web3 minter
scraper = NASAExoplanetScraper()
minter = FilecoinNFTMinter()

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
    # Fetch real exoplanet data from NASA
    try:
        planets = scraper.fetch_exoplanets(10)
        tokens = []
        
        for planet in planets:
            habitability = scraper.calculate_habitability_score(planet)
            rarity = scraper.classify_rarity(habitability)
            
            tokens.append({
                'id': f"EXO-{minter.generate_token_id(planet['name']) % 10000}",
                'name': planet['name'],
                'rarity': rarity,
                'confidence': habitability,
                'period': planet['orbital_period'],
                'radius': planet['radius'],
                'temp': planet['star_temp'],
                'fundingGoal': random.randint(10000, 50000),
                'currentFunding': random.randint(0, 30000),
                'discoveryYear': planet['discovery_year'],
                'hostStar': planet['host_star']
            })
        
        return jsonify(tokens)
    except:
        # Fallback to sample data
        return jsonify([
            {'id': 'EXO-1001', 'name': 'Kepler-442b', 'rarity': 'Ultra Rare', 'confidence': 95.8, 'period': 112.3, 'radius': 1.34, 'temp': 4402, 'fundingGoal': 25000, 'currentFunding': 18500}
        ])

@app.route('/api/fund', methods=['POST'])
def fund():
    data = request.json
    token_id = data.get('tokenId')
    amount = data.get('amount', 100)
    
    # Simulate blockchain transaction
    tx_hash = f'0x{random.randint(10**63, 10**64-1):064x}'
    
    return jsonify({
        'success': True,
        'message': f'Successfully funded {amount} USD to {token_id}',
        'txHash': tx_hash,
        'network': 'Filecoin Calibration Testnet',
        'explorer': f'https://calibration.filfox.info/en/message/{tx_hash}'
    })

@app.route('/api/mint', methods=['POST'])
def mint_token():
    data = request.json
    planet_name = data.get('planetName')
    owner_address = data.get('ownerAddress', '0x0000000000000000000000000000000000000000')
    
    # Fetch planet data
    planets = scraper.fetch_exoplanets(100)
    planet_data = next((p for p in planets if p['name'] == planet_name), None)
    
    if not planet_data:
        return jsonify({'success': False, 'message': 'Planet not found'})
    
    # Calculate habitability and rarity
    habitability = scraper.calculate_habitability_score(planet_data)
    planet_data['habitability_score'] = habitability
    planet_data['rarity'] = scraper.classify_rarity(habitability)
    
    # Mint NFT
    result = minter.mint_nft(planet_data, owner_address)
    
    return jsonify(result)

@app.route('/api/nasa/fetch', methods=['GET'])
def fetch_nasa_data():
    limit = request.args.get('limit', 20, type=int)
    planets = scraper.fetch_exoplanets(limit)
    return jsonify({'success': True, 'count': len(planets), 'planets': planets})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
