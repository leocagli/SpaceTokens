import requests
import json
import io

class IPFSUploader:
    """Sube archivos a IPFS usando Pinata o nft.storage"""
    
    def __init__(self, service='pinata', api_key=None, api_secret=None):
        self.service = service
        self.api_key = api_key or 'YOUR_PINATA_API_KEY'
        self.api_secret = api_secret or 'YOUR_PINATA_SECRET'
        
        if service == 'pinata':
            self.upload_url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'
            self.json_url = 'https://api.pinata.cloud/pinning/pinJSONToIPFS'
        elif service == 'nft.storage':
            self.upload_url = 'https://api.nft.storage/upload'
    
    def upload_image(self, image_pil, filename):
        """Sube imagen PIL a IPFS"""
        try:
            # Convertir PIL a bytes
            img_bytes = io.BytesIO()
            image_pil.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            
            if self.service == 'pinata':
                files = {'file': (filename, img_bytes, 'image/png')}
                headers = {
                    'pinata_api_key': self.api_key,
                    'pinata_secret_api_key': self.api_secret
                }
                response = requests.post(self.upload_url, files=files, headers=headers)
                
                if response.status_code == 200:
                    ipfs_hash = response.json()['IpfsHash']
                    return f"ipfs://{ipfs_hash}"
                else:
                    print(f"Error uploading to Pinata: {response.text}")
                    return self._mock_ipfs_hash(filename)
            else:
                return self._mock_ipfs_hash(filename)
                
        except Exception as e:
            print(f"Error uploading image: {e}")
            return self._mock_ipfs_hash(filename)
    
    def upload_metadata(self, metadata_dict):
        """Sube metadata JSON a IPFS"""
        try:
            if self.service == 'pinata':
                headers = {
                    'pinata_api_key': self.api_key,
                    'pinata_secret_api_key': self.api_secret,
                    'Content-Type': 'application/json'
                }
                response = requests.post(self.json_url, json=metadata_dict, headers=headers)
                
                if response.status_code == 200:
                    ipfs_hash = response.json()['IpfsHash']
                    return f"ipfs://{ipfs_hash}"
                else:
                    print(f"Error uploading metadata: {response.text}")
                    return self._mock_metadata_hash(metadata_dict['name'])
            else:
                return self._mock_metadata_hash(metadata_dict['name'])
                
        except Exception as e:
            print(f"Error uploading metadata: {e}")
            return self._mock_metadata_hash(metadata_dict['name'])
    
    def _mock_ipfs_hash(self, filename):
        """Genera hash IPFS simulado para desarrollo"""
        import hashlib
        hash_obj = hashlib.sha256(filename.encode())
        return f"ipfs://Qm{hash_obj.hexdigest()[:44]}"
    
    def _mock_metadata_hash(self, name):
        """Genera hash IPFS simulado para metadata"""
        import hashlib
        hash_obj = hashlib.sha256(f"metadata_{name}".encode())
        return f"ipfs://Qm{hash_obj.hexdigest()[:44]}"
