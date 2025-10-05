# 🌌 Space Tokens - NASA Exoplanet NFTs

Tokeniza exoplanetas descubiertos por NASA usando IA y blockchain. Proyecto para NASA Space Apps Challenge.

## 🚀 Flujo del Proyecto

1. **Data Collection**: Datos reales de NASA Exoplanet Archive (misiones Kepler/TESS)
2. **AI Classification**: Modelo ML analiza período orbital, radio, temperatura estelar
3. **Image Generation**: Visualización procedural del planeta basada en datos reales
4. **IPFS Upload**: Imagen + metadata subidos a IPFS
5. **Token Generation**: Candidatos con alta confianza se convierten en NFTs
6. **Rarity Assignment**: Basado en zona habitable y características únicas
7. **Funding Mechanism**: Coleccionistas financian investigación de exoplanetas específicos

## 🎨 Características

- **Imágenes Generadas**: Visualización procedural basada en temperatura estelar y radio
- **IPFS Storage**: Imágenes y metadata en IPFS (Pinata)
- **Filecoin Calibration**: NFTs minteados en testnet de Filecoin
- **NASA Data**: Datos reales del Exoplanet Archive
- **Rarity System**: Ultra Rare, Rare, Uncommon, Common
- **Funding**: Sistema de financiamiento para investigación

## 📦 Instalación

```bash
cd space-tokens
pip install -r requirements.txt
python app.py
```

## 🔧 Configuración

### IPFS (Pinata)
Edita `ipfs_uploader.py`:
```python
api_key = 'TU_PINATA_API_KEY'
api_secret = 'TU_PINATA_SECRET'
```

### Filecoin Wallet
Obtén FIL testnet: https://faucet.calibration.fildev.network/

## 🌐 API Endpoints

- `GET /` - Frontend
- `GET /api/tokens` - Lista de exoplanetas tokenizados
- `POST /api/classify` - Clasifica candidato con IA
- `POST /api/mint` - Mintea NFT con imagen generada
- `POST /api/preview` - Preview de imagen del planeta
- `POST /api/fund` - Financia investigación
- `GET /api/nasa/fetch` - Obtiene datos frescos de NASA

## 🎯 Tecnologías

- **Backend**: Flask + Python
- **Blockchain**: Web3.py + Filecoin
- **Storage**: IPFS (Pinata)
- **Images**: Pillow (generación procedural)
- **Data**: NASA Exoplanet Archive API
- **AI**: scikit-learn

## 📊 Metadata NFT

```json
{
  "name": "Kepler-442b",
  "description": "Exoplanet with 87% habitability score",
  "image": "ipfs://QmXxx.../kepler442b.png",
  "attributes": [
    {"trait_type": "Habitability", "value": 87},
    {"trait_type": "Rarity", "value": "Ultra Rare"},
    {"trait_type": "Orbital Period", "value": "112.3 days"},
    {"trait_type": "Radius", "value": "1.34 Earth radii"}
  ]
}
```

## 🖼️ Generación de Imágenes

Las imágenes se generan proceduralmente basadas en:
- **Color**: Temperatura de la estrella anfitriona
- **Tamaño**: Radio del planeta
- **Textura**: Manchas aleatorias para variación
- **Atmósfera**: Efecto glow según características

## 🌟 Rarity Tiers

- **Ultra Rare** (>80 habitability): Zona habitable perfecta
- **Rare** (60-80): Candidato prometedor
- **Uncommon** (40-60): Interesante para estudio
- **Common** (<40): Datos básicos

## 📝 Smart Contract

Contrato ERC-721 en Filecoin con:
- Mint con metadata URI
- Funding mechanism
- Habitability scores on-chain
- Withdraw funds (owner only)

Ver `contracts/SpaceTokens.sol`

## 🚀 Deploy

```bash
# Local
python app.py

# Producción (Heroku)
git push heroku main
```

## 🔗 Links

- NASA Exoplanet Archive: https://exoplanetarchive.ipac.caltech.edu/
- Filecoin Calibration: https://faucet.calibration.fildev.network/
- Pinata IPFS: https://pinata.cloud/

---

**Preservando descubrimientos científicos en blockchain descentralizado** 🌍🚀
