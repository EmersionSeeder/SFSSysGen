import os
import random
from PIL import Image

# Generate 1D noise pattern for each x-coordinate (single noise value per column)
def generate_1d_noise(width, seed=42):
    random.seed(seed)
    return [random.uniform(0, 1) for _ in range(width)]

# Smooth the noise values across columns (moving average)
def smooth_noise(noise, smoothing_factor=5):
    smoothed_noise = noise[:]
    for i in range(len(noise)):
        # Calculate a moving average of the surrounding values
        start = max(0, i - smoothing_factor)
        end = min(len(noise), i + smoothing_factor + 1)
        smoothed_noise[i] = sum(noise[start:end]) / (end - start)
    return smoothed_noise

# Generate a smooth noise heightmap with a wave effect
def generate_noise_heightmap(width=512, height=512, noise_strength=0.5, smoothing_factor=5, output_file="texture_heightmap.png", seed=42):
    # Get the directory where the current script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the sibling directory (assuming 'HEIGHTMAPS' is a sibling of the current directory)
    script_dir = os.path.join(os.path.dirname(current_dir), 'HEIGHTMAPS')

    
    # Create a fully transparent RGBA image
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pixels = image.load()

    # Generate 1D noise along the x-axis (heightmap threshold)
    noise = generate_1d_noise(width, seed)

    # Smooth the noise values to create a smooth transition
    smoothed_noise = smooth_noise(noise, smoothing_factor)

    for x in range(width):
        # Get the smoothed noise value for the current x-coordinate
        noise_value = smoothed_noise[x] * noise_strength  # Control how much the noise affects height
        
        for y in range(height):
            # If y is below the noise value (scaled by height), make the pixel opaque (black)
            if y > (noise_value * height):
                alpha = 255  # Fully transparent
            else:
                alpha = 0  # Fully opaque

            # Set the pixel color (black with varying alpha)
            pixels[x, y] = (0, 0, 0, alpha)  # Black with varying alpha

    # Save it to the directory where the script is located
    output_file = os.path.join(script_dir, output_file)
    image.save(output_file)
    print(f"Saved as {output_file}")

# Example usage
# generate_noise_heightmap(noise_strength=0.5, smoothing_factor=5)
