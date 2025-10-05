import requests
import pandas as pd
from datetime import datetime

class NASAExoplanetScraper:
    def __init__(self):
        self.base_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
        
    def fetch_exoplanets(self, limit=100):
        """Fetch exoplanet data from NASA Exoplanet Archive"""
        query = f"""
        SELECT TOP {limit}
            pl_name, hostname, sy_snum, sy_pnum, discoverymethod,
            disc_year, pl_orbper, pl_rade, pl_masse, pl_eqt,
            st_teff, st_rad, st_mass, sy_dist
        FROM ps
        WHERE pl_rade IS NOT NULL 
        AND pl_orbper IS NOT NULL
        AND st_teff IS NOT NULL
        ORDER BY disc_year DESC
        """
        
        params = {
            'query': query,
            'format': 'json'
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                return []
            
            # Process and clean data
            exoplanets = []
            for planet in data:
                exoplanets.append({
                    'name': planet.get('pl_name', 'Unknown'),
                    'host_star': planet.get('hostname', 'Unknown'),
                    'discovery_method': planet.get('discoverymethod', 'Unknown'),
                    'discovery_year': planet.get('disc_year', 0),
                    'orbital_period': planet.get('pl_orbper', 0),
                    'radius': planet.get('pl_rade', 0),
                    'mass': planet.get('pl_masse', 0),
                    'equilibrium_temp': planet.get('pl_eqt', 0),
                    'star_temp': planet.get('st_teff', 0),
                    'star_radius': planet.get('st_rad', 0),
                    'star_mass': planet.get('st_mass', 0),
                    'distance': planet.get('sy_dist', 0),
                    'fetched_at': datetime.now().isoformat()
                })
            
            return exoplanets
            
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []
    
    def calculate_habitability_score(self, planet):
        """Calculate habitability score based on planet characteristics"""
        score = 0
        
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
