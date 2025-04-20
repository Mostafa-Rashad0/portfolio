from PIL import Image, ImageDraw, ImageFont
import os

def create_gradient_background(size, start_color=(106, 17, 203), end_color=(37, 117, 252)):
    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)
    
    for y in range(size):
        r = start_color[0] + (end_color[0] - start_color[0]) * y // size
        g = start_color[1] + (end_color[1] - start_color[1]) * y // size
        b = start_color[2] + (end_color[2] - start_color[2]) * y // size
        draw.line([(0, y), (size, y)], fill=(r, g, b))
    
    return img

def create_favicon(size):
    # Create gradient background
    img = create_gradient_background(size)
    draw = ImageDraw.Draw(img)
    
    # Calculate font size (approximately 60% of image size)
    font_size = int(size * 0.6)
    
    try:
        # Try to use Arial font, fallback to default if not available
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            # Try Windows system font path
            font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", font_size)
        except:
            # Use default font if Arial is not available
            font = ImageFont.load_default()
    
    # Draw the letter "R"
    text = "R"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Draw white text with slight offset for shadow effect
    draw.text((x+2, y+2), text, fill=(0, 0, 0, 50), font=font)
    draw.text((x, y), text, fill="white", font=font)
    
    return img

def main():
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create favicon directory if it doesn't exist
    favicon_dir = os.path.join(script_dir, 'static', 'favicon')
    os.makedirs(favicon_dir, exist_ok=True)
    
    # Generate different sizes
    sizes = {
        'favicon-16x16.png': 16,
        'favicon-32x32.png': 32,
        'apple-touch-icon.png': 180,
        'android-chrome-192x192.png': 192,
        'android-chrome-512x512.png': 512
    }
    
    for filename, size in sizes.items():
        favicon = create_favicon(size)
        output_path = os.path.join(favicon_dir, filename)
        favicon.save(output_path)
        print(f"Generated {filename} at {output_path}")

if __name__ == '__main__':
    main() 