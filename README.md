# 🌌 Space Tokens - Tokenizing the Universe

AI-powered exoplanet discovery platform that converts NASA data into collectible NFTs to fund space science research.

## 🚀 NASA Space Apps Challenge 2024

**Challenge**: A World Away: Hunting for Exoplanets with AI

## ✨ Features

- 🤖 **AI Classification**: Machine learning model to identify exoplanet candidates
- 🎨 **NFT Tokenization**: Convert discoveries into unique collectible tokens
- 💰 **Science Funding**: Direct funding mechanism for space research
- 📊 **Real NASA Data**: Based on Kepler/TESS mission data
- 🌟 **Rarity System**: Ultra Rare, Rare, Uncommon, Common based on habitability

## 🛠️ Tech Stack

- **Backend**: Python + Flask
- **AI/ML**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Blockchain**: Filecoin + Web3.py
- **Smart Contracts**: Solidity (ERC-721 NFT)
- **Data Source**: NASA Exoplanet Archive API

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/yourusername/space-tokens.git
cd space-tokens

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Visit `http://localhost:5000`

## 🎯 How It Works

1. **Data Collection**: Real-time scraping from NASA Exoplanet Archive API
2. **AI Classification**: ML model analyzes orbital period, radius, star temperature
3. **Habitability Scoring**: Calculate Earth-similarity index (0-100)
4. **NFT Minting**: Mint ERC-721 tokens on Filecoin with IPFS metadata
5. **Token Generation**: High-confidence candidates become NFTs
6. **Rarity Assignment**: Based on habitability zone and unique characteristics
7. **Funding Mechanism**: Smart contract escrow for research funding

## 🌟 Rarity Tiers

- **Ultra Rare**: Earth-like planets in habitable zone (1-1.5 R⊕, 200-400 day period)
- **Rare**: Potentially habitable (1.5-2 R⊕)
- **Uncommon**: Interesting candidates (2-3 R⊕)
- **Common**: Confirmed exoplanets

## 📊 Model Performance

- **Accuracy**: 92.5%
- **Training Data**: NASA Kepler Mission TCEs
- **Features**: Orbital period, planet radius, star temperature
- **Algorithm**: Random Forest Classifier

## 🎨 Token Metadata

Each token includes:
- Unique ID (EXO-XXXX)
- Planet name
- Rarity tier
- AI confidence score
- Orbital characteristics
- Funding goal and progress

## 🚀 Deployment

### Heroku

```bash
# Login to Heroku
heroku login

# Create app
heroku create space-tokens

# Deploy
git push heroku main
```

### Render

1. Connect GitHub repository
2. Select Python environment
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`

## 🔗 API Endpoints

- `GET /api/tokens` - Get all minted tokens
- `POST /api/classify` - Classify new exoplanet
- `POST /api/mint` - Mint NFT for exoplanet
- `POST /api/fund` - Fund research
- `GET /api/nasa/fetch` - Fetch fresh NASA data

## 📝 Future Enhancements

- [ ] Train ML model with full Kepler dataset
- [ ] Deploy to Filecoin mainnet
- [ ] IPFS pinning service integration
- [ ] Community DAO for funding decisions
- [ ] 3D visualization with Three.js
- [ ] Telescope observation scheduling API

## 🤝 Contributing

Contributions welcome! Please read CONTRIBUTING.md first.

## 📄 License

MIT License - see LICENSE file

## 🙏 Acknowledgments

- NASA Exoplanet Archive
- Kepler and TESS missions
- Space Apps Challenge organizers

---

**Built for NASA Space Apps Challenge 2024** 🚀
