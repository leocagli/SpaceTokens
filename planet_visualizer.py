from PIL import Image, ImageDraw, ImageFilter
import random
import math
import io
import base64

class PlanetVisualizer:
    """Genera imágenes procedurales de exoplanetas basadas en datos reales"""
    
    def __init__(self, size=512):
        self.size = size
        
    def generate_planet_image(self, planet_data):
        """Genera imagen del planeta basada en sus características"""
        img = Image.new('RGB', (self.size, self.size), color='#000000')
        draw = ImageDraw.Draw(img)
        
        # Calcular color según temperatura
        temp = planet_data.get('st_teff', 5778)  # Default: temperatura del Sol
        color = self._temperature_to_color(temp)
        
        # Calcular tamaño según radio
        radius_earth = planet_data.get('pl_rade', 1.0)
        planet_radius = int(min(self.size * 0.35 * radius_earth, self.size * 0.45))
        
        # Centro de la imagen
        center_x = self.size // 2
        center_y = self.size // 2
        
        # Dibujar atmósfera (glow)
        for i in range(5):
            glow_radius = planet_radius + (i * 8)
            alpha = 255 - (i * 40)
            glow_color = tuple([int(c * alpha / 255) for c in color])
            draw.ellipse(
                [center_x - glow_radius, center_y - glow_radius,
                 center_x + glow_radius, center_y + glow_radius],
                fill=glow_color
            )
        
        # Dibujar planeta principal
        draw.ellipse(
            [center_x - planet_radius, center_y - planet_radius,
             center_x + planet_radius, center_y + planet_radius],
            fill=color
        )
        
        # Añadir textura (manchas)
        self._add_texture(draw, center_x, center_y, planet_radius, color)
        
        # Añadir estrellas de fondo
        self._add_stars(draw)
        
        # Aplicar blur suave
        img = img.filter(ImageFilter.GaussianBlur(radius=1))
        
        return img
    
    def _temperature_to_color(self, temp):
        """Convierte temperatura estelar a color del planeta"""
        if temp < 3500:  # Estrella fría (roja)
            return (180, 80, 60)
        elif temp < 5000:  # Estrella naranja
            return (200, 140, 100)
        elif temp < 6000:  # Estrella amarilla (como el Sol)
            return (100, 150, 200)
        elif temp < 7500:  # Estrella blanca
            return (150, 180, 220)
        else:  # Estrella caliente (azul)
            return (80, 120, 200)
    
    def _add_texture(self, draw, cx, cy, radius, base_color):
        """Añade manchas/textura al planeta"""
        random.seed(hash(str(base_color)))
        for _ in range(random.randint(15, 30)):
            spot_x = cx + random.randint(-radius//2, radius//2)
            spot_y = cy + random.randint(-radius//2, radius//2)
            spot_radius = random.randint(radius//10, radius//4)
            
            # Color más oscuro para manchas
            spot_color = tuple([max(0, c - 30) for c in base_color])
            
            draw.ellipse(
                [spot_x - spot_radius, spot_y - spot_radius,
                 spot_x + spot_radius, spot_y + spot_radius],
                fill=spot_color
            )
    
    def _add_stars(self, draw):
        """Añade estrellas al fondo"""
        random.seed(42)
        for _ in range(100):
            x = random.randint(0, self.size)
            y = random.randint(0, self.size)
            brightness = random.randint(150, 255)
            size = random.choice([1, 1, 1, 2])
            draw.ellipse([x, y, x+size, y+size], fill=(brightness, brightness, brightness))
    
    def image_to_base64(self, img):
        """Convierte imagen PIL a base64 para web"""
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    
    def save_image(self, img, filepath):
        """Guarda imagen en disco"""
        img.save(filepath, 'PNG')
