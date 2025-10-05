from web3 import Web3
import json
import hashlib
from datetime import datetime

class FilecoinNFTMinter:
    def __init__(self, rpc_url="https://api.calibration.node.glif.io/rpc/v1"):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract_address = None
        
    def generate_metadata(self, planet_data):
        """Generate NFT metadata for exoplanet"""
        metadata = {
            "name": planet_data['name'],
            "description": f"Exoplanet {planet_data['name']} discovered via {planet_data['discovery_method']}",
            "image": f"ipfs://QmHash/{planet_data['name']}.png",
            "attributes": [
                {"trait_type": "Host Star", "value": planet_data['host_star']},
                {"trait_type": "Discovery Year", "value": planet_data['discovery_year']},
                {"trait_type": "Discovery Method", "value": planet_data['discovery_method']},
                {"trait_type": "Orbital Period", "value": f"{planet_data['orbital_period']:.2f} days"},
                {"trait_type": "Radius", "value": f"{planet_data['radius']:.2f} Earth radii"},
                {"trait_type": "Mass", "value": f"{planet_data['mass']:.2f} Earth masses"},
                {"trait_type": "Temperature", "value": f"{planet_data['equilibrium_temp']:.0f} K"},
                {"trait_type": "Distance", "value": f"{planet_data['distance']:.2f} parsecs"},
                {"trait_type": "Rarity", "value": planet_data['rarity']},
                {"trait_type": "Habitability Score", "value": planet_data['habitability_score']}
            ],
            "external_url": f"https://exoplanets.nasa.gov/exoplanet-catalog/{planet_data['name']}/",
            "created_at": datetime.now().isoformat()
        }
        return metadata
    
    def generate_token_id(self, planet_name):
        """Generate unique token ID from planet name"""
        hash_object = hashlib.sha256(planet_name.encode())
        return int(hash_object.hexdigest()[:16], 16)
    
    def mint_nft(self, planet_data, owner_address, metadata_uri=''):
        """Mint NFT for exoplanet (simulation)"""
        token_id = self.generate_token_id(planet_data['name'])
        
        if not metadata_uri:
            metadata = self.generate_metadata(planet_data)
            metadata_uri = self.store_on_ipfs(metadata)
        else:
            metadata = self.generate_metadata(planet_data)
        
        # Simulate minting transaction
        tx_hash = f"0x{hashlib.sha256(f'{token_id}{owner_address}'.encode()).hexdigest()}"
        
        return {
            'success': True,
            'token_id': token_id,
            'tx_hash': tx_hash,
            'metadata': metadata,
            'metadata_uri': metadata_uri,
            'contract_address': '0xSpaceTokensNFT...',
            'network': 'Filecoin Calibration Testnet'
        }
    
    def store_on_ipfs(self, metadata):
        """Store metadata on IPFS (simulation)"""
        # In production, use web3.storage or nft.storage
        metadata_hash = hashlib.sha256(json.dumps(metadata).encode()).hexdigest()
        ipfs_hash = f"Qm{metadata_hash[:44]}"
        return f"ipfs://{ipfs_hash}"

class SpaceTokenContract:
    """Smart contract interface for Space Tokens"""
    
    ABI = [
        {
            "inputs": [
                {"name": "to", "type": "address"},
                {"name": "tokenId", "type": "uint256"},
                {"name": "uri", "type": "string"}
            ],
            "name": "mint",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [{"name": "tokenId", "type": "uint256"}],
            "name": "tokenURI",
            "outputs": [{"name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function"
        }
    ]
    
    BYTECODE = "0x608060405234801561001057600080fd5b50..."  # Simplified
    
    @staticmethod
    def get_contract_code():
        """Get Solidity contract code"""
        return '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SpaceTokens is ERC721URIStorage, Ownable {
    uint256 private _tokenIdCounter;
    
    mapping(uint256 => uint256) public habitabilityScores;
    mapping(uint256 => string) public planetNames;
    mapping(uint256 => uint256) public fundingGoals;
    mapping(uint256 => uint256) public currentFunding;
    
    event TokenMinted(uint256 indexed tokenId, string planetName, uint256 habitabilityScore);
    event FundingReceived(uint256 indexed tokenId, address funder, uint256 amount);
    
    constructor() ERC721("Space Tokens", "SPACE") Ownable(msg.sender) {}
    
    function mint(
        address to,
        string memory planetName,
        string memory uri,
        uint256 habitabilityScore,
        uint256 fundingGoal
    ) public onlyOwner returns (uint256) {
        uint256 tokenId = _tokenIdCounter++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
        
        habitabilityScores[tokenId] = habitabilityScore;
        planetNames[tokenId] = planetName;
        fundingGoals[tokenId] = fundingGoal;
        
        emit TokenMinted(tokenId, planetName, habitabilityScore);
        return tokenId;
    }
    
    function fundResearch(uint256 tokenId) public payable {
        require(_ownerOf(tokenId) != address(0), "Token does not exist");
        require(msg.value > 0, "Must send funding");
        
        currentFunding[tokenId] += msg.value;
        emit FundingReceived(tokenId, msg.sender, msg.value);
    }
    
    function withdrawFunds(uint256 tokenId) public onlyOwner {
        uint256 amount = currentFunding[tokenId];
        require(amount > 0, "No funds to withdraw");
        
        currentFunding[tokenId] = 0;
        payable(owner()).transfer(amount);
    }
}
'''

if __name__ == "__main__":
    minter = FilecoinNFTMinter()
    
    # Example planet data
    planet = {
        'name': 'Kepler-442b',
        'host_star': 'Kepler-442',
        'discovery_method': 'Transit',
        'discovery_year': 2015,
        'orbital_period': 112.3,
        'radius': 1.34,
        'mass': 2.3,
        'equilibrium_temp': 233,
        'distance': 1206,
        'rarity': 'Ultra Rare',
        'habitability_score': 85
    }
    
    result = minter.mint_nft(planet, '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb')
    print(f"Minted Token ID: {result['token_id']}")
    print(f"Transaction: {result['tx_hash']}")
