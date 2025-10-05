// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SpaceTokens is ERC721URIStorage, Ownable {
    uint256 private _tokenIdCounter;
    
    struct ExoplanetData {
        string planetName;
        string hostStar;
        uint256 habitabilityScore;
        uint256 fundingGoal;
        uint256 currentFunding;
        string rarity;
    }
    
    mapping(uint256 => ExoplanetData) public exoplanets;
    
    event TokenMinted(uint256 indexed tokenId, string planetName, uint256 habitabilityScore);
    event FundingReceived(uint256 indexed tokenId, address funder, uint256 amount);
    
    constructor() ERC721("Space Tokens", "SPACE") Ownable(msg.sender) {}
    
    function mint(
        address to,
        string memory planetName,
        string memory hostStar,
        string memory uri,
        uint256 habitabilityScore,
        uint256 fundingGoal,
        string memory rarity
    ) public onlyOwner returns (uint256) {
        uint256 tokenId = _tokenIdCounter++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
        
        exoplanets[tokenId] = ExoplanetData({
            planetName: planetName,
            hostStar: hostStar,
            habitabilityScore: habitabilityScore,
            fundingGoal: fundingGoal,
            currentFunding: 0,
            rarity: rarity
        });
        
        emit TokenMinted(tokenId, planetName, habitabilityScore);
        return tokenId;
    }
    
    function fundResearch(uint256 tokenId) public payable {
        require(_ownerOf(tokenId) != address(0), "Token does not exist");
        require(msg.value > 0, "Must send funding");
        
        exoplanets[tokenId].currentFunding += msg.value;
        emit FundingReceived(tokenId, msg.sender, msg.value);
    }
    
    function withdrawFunds(uint256 tokenId) public onlyOwner {
        uint256 amount = exoplanets[tokenId].currentFunding;
        require(amount > 0, "No funds to withdraw");
        
        exoplanets[tokenId].currentFunding = 0;
        payable(owner()).transfer(amount);
    }
}
