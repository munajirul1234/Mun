#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size, path):
    img = Image.new('RGBA', (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    
    # Background circle with gradient effect
    margin = size // 10
    draw.rounded_rectangle([margin, margin, size-margin, size-margin], 
                           radius=size//4, fill=(15, 25, 50, 255))
    
    # Inner glow
    inner = margin + size//16
    draw.rounded_rectangle([inner, inner, size-inner, size-inner],
                           radius=size//5, fill=(20, 40, 90, 200))
    
    # Book emoji approximation - draw a book shape
    bx = size // 4
    by = size // 4
    bw = size // 2
    bh = int(size * 0.5)
    
    # Left page
    draw.rectangle([bx, by, bx + bw//2 - 2, by + bh], fill=(79, 142, 247, 255))
    # Right page  
    draw.rectangle([bx + bw//2 + 2, by, bx + bw, by + bh], fill=(100, 160, 255, 255))
    # Spine
    draw.rectangle([bx + bw//2 - 3, by - 4, bx + bw//2 + 3, by + bh + 4], fill=(200, 220, 255, 255))
    # Lines on pages
    line_color = (150, 190, 255, 180)
    for i in range(3):
        y = by + bh//4 + i * (bh//5)
        draw.rectangle([bx + 4, y, bx + bw//2 - 8, y + max(2, size//64)], fill=line_color)
        draw.rectangle([bx + bw//2 + 8, y, bx + bw - 4, y + max(2, size//64)], fill=line_color)
    
    img.save(path)
    print(f"Created {path}")

os.makedirs('icons', exist_ok=True)
make_icon(192, 'icons/icon-192.png')
make_icon(512, 'icons/icon-512.png')
print("Icons created!")
