import requests
from datetime import datetime

class NASAExoplanetScraper:
    def __init__(self):
        self.base_url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI"
        
    def fetch_exoplanets(self, limit=100):
        """Fetch exoplanet data from NASA Exoplanet Archive using the correct API"""
        # Use the 'cumulative' table (Kepler Objects of Interest) with proper API parameters
        params = {
            'table': 'cumulative',
            'format': 'json',
            'select': 'kepoi_name,kepler_name,koi_disposition,koi_period,koi_prad,koi_teq,koi_steff,koi_srad,koi_slogg,koi_score'
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=30)
            response.raise_for_status()
            
            # The API returns data in a different format, check if it's a list or has a data field
            data = response.json()
            
            # Handle different response formats
            if isinstance(data, dict) and 'data' in data:
                planets_data = data['data']
            elif isinstance(data, list):
                planets_data = data
            else:
                print(f"Unexpected data format: {type(data)}")
                return []
            
            if not planets_data:
                return []
            
            # Process and clean data - limit results and filter for valid data
            exoplanets = []
            for i, planet in enumerate(planets_data):
                if i >= limit * 2:  # Get more data to filter
                    break
                
                # Filter for planets with valid data
                if (planet.get('koi_prad') and planet.get('koi_period') and 
                    planet.get('koi_steff') and planet.get('koi_prad') > 0 and 
                    planet.get('koi_period') > 0 and planet.get('koi_steff') > 0):
                    
                    # Use Kepler name if available, otherwise use KOI name
                    planet_name = planet.get('kepler_name') or planet.get('kepoi_name', 'Unknown')
                    
                    exoplanets.append({
                        'name': planet_name,
                        'host_star': planet.get('kepoi_name', 'Unknown').split('.')[0] if planet.get('kepoi_name') else 'Unknown',
                        'discovery_method': 'Transit',
                        'discovery_year': 2015,  # Approximate for Kepler data
                        'orbital_period': planet.get('koi_period', 0),
                        'radius': planet.get('koi_prad', 0),
                        'mass': 0,  # Not available in cumulative table
                        'equilibrium_temp': planet.get('koi_teq', 0),
                        'star_temp': planet.get('koi_steff', 0),
                        'star_radius': planet.get('koi_srad', 0),
                        'star_mass': 0,  # Not available in cumulative table
                        'distance': 0,  # Not available in cumulative table
                        'koi_score': planet.get('koi_score', 0),
                        'disposition': planet.get('koi_disposition', 'Unknown'),
                        'fetched_at': datetime.now().isoformat()
                    })
                    
                    if len(exoplanets) >= limit:
                        break
            
            return exoplanets
            
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []
    
    def calculate_habitability_score(self, planet):
        """Calculate habitability score based on planet characteristics"""
        score = 0
        
        # Use KOI score as base if available
        if planet.get('koi_score'):
            score = planet['koi_score'] * 100
        
        # Radius similar to Earth (0.5 - 2.0 Earth radii)
        if 0.5 <= planet['radius'] <= 2.0:
            score += 30
        
        # Temperature in habitable range (200-350K)
        if 200 <= planet['equilibrium_temp'] <= 350:
            score += 30
        
        # Orbital period (similar to Earth ~365 days)
        if 200 <= planet['orbital_period'] <= 500:
            score += 20
        
        # Star temperature (similar to Sun ~5778K)
        if 4000 <= planet['star_temp'] <= 7000:
            score += 20
        
        return min(score, 100)
    
    def classify_rarity(self, habitability_score):
        """Classify planet rarity based on habitability"""
        if habitability_score >= 80:
            return "Ultra Rare"
        elif habitability_score >= 60:
            return "Rare"
        elif habitability_score >= 40:
            return "Uncommon"
        else:
            return "Common"

if __name__ == "__main__":
    scraper = NASAExoplanetScraper()
    planets = scraper.fetch_exoplanets(10)
    
    for planet in planets:
        score = scraper.calculate_habitability_score(planet)
        rarity = scraper.classify_rarity(score)
        print(f"{planet['name']}: {rarity} (Score: {score})")
