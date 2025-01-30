from PIL import Image, ImageDraw, ImageFont
import numpy as np
import importlib.resources as pkg_resources


class ProtactiveYantra:
    def __init__(self, width=800, height=600,font_path="lklug.ttf"):
        self.width = width
        self.height = height
        
        # Create image with aged parchment color
        self.image = Image.new('RGB', (width, height), (225, 207, 171))
        self.draw = ImageDraw.Draw(self.image)
        
        try:
            font_path = pkg_resources.files("yantra_patterns.fonts").joinpath(font_path)
            # Increased font size for better visibility
            self.font = ImageFont.truetype(font_path, width // 20)  # Larger font size
        except OSError:
            print("Warning: Sinhala font not found. Please install a Sinhala font.")
            self.font = ImageFont.load_default()

    def draw_double_line(self, start, end, color=(30, 30, 30), gap=3):
        """Draw a double line with specified gap"""
        # Calculate perpendicular vector
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = (dx*dx + dy*dy) ** 0.5
        if length == 0:
            return
        
        # Normalize and perpendicular
        dx, dy = dx/length, dy/length
        px, py = -dy*gap/2, dx*gap/2
        
        # Draw two parallel lines
        self.draw.line(
            [(start[0] + px, start[1] + py), (end[0] + px, end[1] + py)],
            fill=color,
            width=1
        )
        self.draw.line(
            [(start[0] - px, start[1] - py), (end[0] - px, end[1] - py)],
            fill=color,
            width=1
        )

    def draw_grid(self, rows=4, cols=6, line_color=(30, 30, 30)):
        """Draw double-line grid"""
        cell_width = self.width / cols
        cell_height = self.height / rows
        
        # Draw vertical double lines
        for i in range(cols + 1):
            x = i * cell_width
            self.draw_double_line(
                (x, 0),
                (x, self.height),
                line_color
            )
            
        # Draw horizontal double lines
        for i in range(rows + 1):
            y = i * cell_height
            self.draw_double_line(
                (0, y),
                (self.width, y),
                line_color
            )
            
        # Draw diagonal double lines
        self.draw_double_line(
            (0, 0),
            (self.width, self.height),
            line_color
        )
        self.draw_double_line(
            (self.width, 0),
            (0, self.height),
            line_color
        )



    def add_sinhala_text(self, text, rows=4, cols=6):
        """Add enhanced visible Sinhala text"""
        cell_width = self.width / cols
        cell_height = self.height / rows
        
        # More prominent golden color
        text_color = (184, 134, 11)  # Darker golden color
        
        for row in range(rows):
            for col in range(cols):
                x = col * cell_width + cell_width/2
                y = row * cell_height + cell_height/2
                
                # Get text bounds for centering
                if hasattr(self.font, 'getbbox'):
                    bbox = self.font.getbbox(text)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]
                else:
                    text_width, text_height = self.font.getsize(text)
                
                # Draw text with slight shadow for better visibility
                shadow_offset = 1
                # Draw shadow
                self.draw.text(
                    (x - text_width/2 + shadow_offset, y - text_height/2 + shadow_offset),
                    text,
                    font=self.font,
                    fill=(30, 30, 30)  # Shadow color
                )
                # Draw main text
                self.draw.text(
                    (x - text_width/2, y - text_height/2),
                    text,
                    font=self.font,
                    fill=text_color
                )

    def add_texture_effect(self):
        """Add refined texture effect"""
        pixels = self.image.load()
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = pixels[i, j]
                # Subtle noise for texture
                noise = np.random.randint(-15, 15)
                # Horizontal line texture
                line_texture = np.sin(j * 0.5) * 3
                r = max(0, min(255, r + noise + line_texture))
                g = max(0, min(255, g + noise + line_texture))
                b = max(0, min(255, b + noise + line_texture))
                pixels[i, j] = (int(r), int(g), int(b))

    def save(self, filename):
        """Save the yantra pattern"""
        self.image.save(filename)

def create_enhanced_yantra(filename, text="අ", width=800, height=600, rows=4, cols=6,sinhala=True):
    """
    Create an enhanced yantra pattern with double lines and clear text
    
    Parameters:
    filename: Output file name
    text: Sinhala text to repeat
    width: Image width
    height: Image height
    rows: Number of rows
    cols: Number of columns
    """
  
    if not sinhala:
        yantra = ProtactiveYantra(width,height,font_path="eng.ttf")
    yantra = ProtactiveYantra(width, height,font_path="lklug.ttf")
    yantra.draw_grid(rows, cols)
    yantra.add_sinhala_text(text, rows, cols)
    yantra.add_texture_effect()
    yantra.save(filename)

# # Example usage
# if __name__ == "__main__":
#     create_enhanced_yantra("yantra.png", "ඪ")