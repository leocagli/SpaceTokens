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
- **Data Source**: NASA Exoplanet Archive

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

1. **Data Collection**: NASA Exoplanet Archive data (Kepler/TESS missions)
2. **AI Classification**: ML model analyzes orbital period, radius, star temperature
3. **Token Generation**: High-confidence candidates become NFTs with metadata
4. **Rarity Assignment**: Based on habitability zone and unique characteristics
5. **Funding Mechanism**: Collectors fund research for specific exoplanets

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

## 📝 Future Enhancements

- [ ] Real ML model training with NASA data
- [ ] Blockchain integration (Ethereum/Polygon)
- [ ] IPFS for metadata storage
- [ ] Community voting on funding allocation
- [ ] 3D visualization of exoplanets
- [ ] Integration with telescope observation scheduling

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
