import sys
import json
import random
import os
import math
import tkinter as tk
import threading
from PIL import Image, ImageEnhance
from tkinter import ttk, messagebox

# Seed
seed = random.randint(0,100000)
# Directories
script_dir = os.path.dirname(os.path.abspath(__file__))

chaos_dir = os.path.join(os.path.dirname(__file__), 'HEIGHTMAPS')
dev_path = os.path.join(os.path.dirname(__file__), 'DEVELOPMENT')
dev_folder = dev_path
gen_folder = os.path.join(script_dir, 'GENERATED')
sys.path.append('{dev_folder}')
sys.path.append(dev_path)

# Variables
maxPlanets = 20
stars = 32
true = True
false = False

import HeightmapGen

def generate_filename():
    letters = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
    number = random.randint(1, 9999)
    return f"{letters}-{number}"
import os
import random
import re

def apply_chaos_heightmaps(planet_data):
    # Path to HEIGHTMAPS folder (parent of DEVELOPMENT)
    chaos_dir = os.path.join(os.path.dirname(__file__), 'HEIGHTMAPS')
    chaos_files = [f for f in os.listdir(chaos_dir) if f.endswith('.png')]

    if not chaos_files:
        raise ValueError("No chaos heightmaps found in HEIGHTMAPS folder!")

    def replace_heightmap(match):
        original = match.group()
        if "CRATERS" in original or "PERLIN" in original:
            return original  # Keep it unchanged
        chaos_choice = random.choice(chaos_files)
        chaos_choice_no_ext = os.path.splitext(chaos_choice)[0]
        return f"AddHeightMap({chaos_choice_no_ext},"

    pattern = re.compile(r"AddHeightMap\([^\),]+")

    # Replace in terrainFormulaDifficulties
    for difficulty in planet_data["TERRAIN_DATA"]["terrainFormulaDifficulties"]:
        new_lines = []
        for line in planet_data["TERRAIN_DATA"]["terrainFormulaDifficulties"][difficulty]:
            new_line = pattern.sub(replace_heightmap, line)
            new_lines.append(new_line)
        planet_data["TERRAIN_DATA"]["terrainFormulaDifficulties"][difficulty] = new_lines

    # Replace in textureFormula
    if "textureFormula" in planet_data["TERRAIN_DATA"]:
        new_lines = []
        for line in planet_data["TERRAIN_DATA"]["textureFormula"]:
            new_line = pattern.sub(replace_heightmap, line)
            new_lines.append(new_line)
        planet_data["TERRAIN_DATA"]["textureFormula"] = new_lines
    log("Applied Chaos heightmap!")
    return planet_data

def find(target):
    # 1. Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = current_dir
    # 3. Name of the folder to search
    target_folder_name = target

    matches = []
    for item in os.listdir(parent_dir):
        full_path = os.path.join(parent_dir, item)
        if os.path.isdir(full_path) and item == target_folder_name:
            matches.append(full_path)

    if matches:
        print(f"Found folder(s) named '{target_folder_name}':")
        log(f"Found folder(s) named '{target_folder_name}':")
        for match in matches:
            print("→", match)
            return(match)
    else:
        print(f"No folders named '{target_folder_name}' found in {parent_dir}")
        log(f"Warning! '{target_folder_name}' is either renamed or missing!:")
def tint_image(image, tint_color=(0, 128, 255)):
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        r, g, b, a = image.split()

        # Create a solid color image and blend it with the original
        tint = Image.new('RGBA', image.size, tint_color + (0,))
        blended = Image.blend(image, tint, alpha=0.3)  # adjust alpha for tint strength
        return blended

def main(name, tint_color=(0, 128, 255), logName=""):
    out_folder = os.path.join(script_dir, 'TEXTURES')
    image_path = os.path.join(dev_folder, 'AirlessTemplate.png')

    if not os.path.exists(image_path):
        print("Image not found:", image_path)
        log(f"Warning! '{image_path}' is either renamed or missing!:")
        return

    # Open and tint the image
    image = Image.open(image_path)
    tinted_image = tint_image(image, tint_color)

    # Save or show the result
    output_path = os.path.join(out_folder, name)
    tinted_image.save(output_path)
    print("Tinted image saved to:", output_path)
    log(f"Image {logName} Saved!")
def main2(name, tint_color=(0, 128, 255), logName=""):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the DEVELOPMENT folder and the image
    dev_folder = os.path.join(script_dir, 'DEVELOPMENT')
    out_folder = os.path.join(script_dir, 'TEXTURES')
    image_path = os.path.join(dev_folder, 'JovianTemplate.png')

    if not os.path.exists(image_path):
        print("Image not found:", image_path)
        log(f"Warning! '{image_path}' is either renamed or missing!:")
        return

    # Open and tint the image
    image = Image.open(image_path)
    tinted_image = tint_image(image, tint_color)

    # Save or show the result
    output_path = os.path.join(out_folder, name)
    tinted_image.save(output_path)
    print("Tinted image saved to:", output_path)
    log(f"Image {logName} Saved!")
def main3(name, tint_color=(0, 128, 255), logName=""):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the DEVELOPMENT folder and the image
    dev_folder = os.path.join(script_dir, 'DEVELOPMENT')
    out_folder = os.path.join(script_dir, 'TEXTURES')
    image_path = os.path.join(dev_folder, 'AtmoTemplate.png')

    if not os.path.exists(image_path):
        print("Image not found:", image_path)
        log(f"Warning! '{image_path}' is either renamed or missing!:")
        return

    # Open and tint the image
    image = Image.open(image_path)
    tinted_image = tint_image(image, tint_color)

    # Save or show the result
    output_path = os.path.join(out_folder, name)
    tinted_image.save(output_path)
    print("Tinted image saved to:", output_path)
    log(f"Image {logName} Saved!")
def main4(name, tint_color=(0, 128, 255), logName=""):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the DEVELOPMENT folder and the image
    dev_folder = os.path.join(script_dir, 'DEVELOPMENT')
    out_folder = os.path.join(script_dir, 'TEXTURES')
    image_path = os.path.join(dev_folder, 'NeptunianTemplate.png')

    if not os.path.exists(image_path):
        print("Image not found:", image_path)
        log(f"Warning! '{image_path}' is either renamed or missing!:")
        return

    # Open and tint the image
    image = Image.open(image_path)
    tinted_image = tint_image(image, tint_color)

    # Save or show the result
    output_path = os.path.join(out_folder, name)
    tinted_image.save(output_path)
    print("Tinted image saved to:", output_path)
    log(f"Image {logName} Saved!")
def create_major_moon(planet_name, moon_number, output_folder, min, max, scale):
    moon_name = f"{planet_name}-{moon_number}"
    log(f"Generating moon {moon_name}...")
    planet_data = {
        "version": "1.5",
        "BASE_DATA": {
            "radius": 120000.0,
            "radiusDifficultyScale": {},
            "gravity": 3.27,
            "gravityDifficultyScale": {},
            "timewarpHeight": 2500.0,
            "velocityArrowsHeight": "NaN",
            "mapColor": {
                "r": 0.410344839,
                "g": 0.372679353,
                "b": 0.3495006,
                "a": 1.0
            },
            "significant": True,
            "rotateCamera": True
        },
        "TERRAIN_DATA": {
            "TERRAIN_TEXTURE_DATA": {
                "planetTexture": f"{moon_name}",
                "planetTextureCutout": 0.945,
                "surfaceTexture_A": "Dark_Dust",
                "surfaceTextureSize_A": {"x": 20.0, "y": 8.0},
                "surfaceTexture_B": "Hard_Rocks",
                "surfaceTextureSize_B": {"x": 30.0, "y": 14.0},
                "terrainTexture_C": "Soft_Rocks",
                "terrainTextureSize_C": {"x": 280.0, "y": 145.0},
                "surfaceLayerSize": 30.0,
                "minFade": 0.0,
                "maxFade": 1.0,
                "shadowIntensity": 13.0,
                "shadowHeight": 10.0
            },
            "terrainFormulaDifficulties": {
                "Normal": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 753982.236861550, 1)",
                    "OUTPUT = AddHeightMap(Mercury,753982.236861550, 500)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Hard": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 1507964.4737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,1507964.4737231007544, 1000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Realistic": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 15079644.737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,15079644.737231007544, 5000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ]
            },
            "textureFormula": [
                "OUTPUT = AddHeightMap(Perlin,15079.644737231, 1, Curve8)",
                "OUTPUT = ApplyCurve(Curve8)",
                "OUTPUT = ApplyCurve(Curve8)"
            ],
            "verticeSize": 2.0,
            "collider": True,
            "flatZones": [],
            "rocks": {
                "rockType": "Rock Square",
                "rockDensity": 0.5,
                "minSize": 0.1,
                "maxSize": 0.3,
                "powerCurve": 2.0,
                "maxAngle": 20.0
            }
        },
        "POST_PROCESSING": {
            "keys": [
                {
                    "height": 15000.0,
                    "shadowIntensity": 1.75,
                    "starIntensity": 1.0,
                    "hueShift": 0.0,
                    "saturation": 0.95,
                    "contrast": 1.2,
                    "red": 1.0,
                    "green": 1.0,
                    "blue": 1.0
                }
            ]
        },
        "ORBIT_DATA": {
            "parent": planet_name,
            "semiMajorAxis": 2895000000.0,
            "smaDifficultyScale": {},
            "eccentricity": 0.2,
            "argumentOfPeriapsis": 29.0,
            "direction": 1,
            "multiplierSOI": 2.0,
            "soiDifficultyScale": {}
        },
        "ACHIEVEMENT_DATA": {
            "Landed": True,
            "Takeoff": True,
            "Atmosphere": True,
            "Orbit": True,
            "Crash": True
        },
        "LANDMARKS": []
    }
    red = random.uniform(0,1)
    blue = random.uniform(0,1)
    green = random.uniform(0,1)
    planet_data["BASE_DATA"]["mapColor"]["r"] = red
    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(min,max)) * scale
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(2.5e7 * (min/41560), 5e7 * (max/132000)))
    planet_data["ORBIT_DATA"]["eccentricity"] = random.uniform(0.04,0.16)
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = random.uniform(0.0,360.0)
    main(f"{moon_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{moon_name}.png")
    filepath = os.path.join(output_folder, moon_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            json.dump(planet_data, f, indent=4)
            log(f"{moon_name} exported!")
def create_chaotic_major_moon(planet_name, moon_number, output_folder, min, max, scale):
    moon_name = f"{planet_name}-{moon_number}"
    log(f"Generating moon {moon_name}...")
    planet_data = {
        "version": "1.5",
        "BASE_DATA": {
            "radius": 120000.0,
            "radiusDifficultyScale": {},
            "gravity": 3.27,
            "gravityDifficultyScale": {},
            "timewarpHeight": 2500.0,
            "velocityArrowsHeight": "NaN",
            "mapColor": {
                "r": 0.410344839,
                "g": 0.372679353,
                "b": 0.3495006,
                "a": 1.0
            },
            "significant": True,
            "rotateCamera": True
        },
        "TERRAIN_DATA": {
            "TERRAIN_TEXTURE_DATA": {
                "planetTexture": f"{moon_name}",
                "planetTextureCutout": 0.945,
                "surfaceTexture_A": "Dark_Dust",
                "surfaceTextureSize_A": {"x": 20.0, "y": 8.0},
                "surfaceTexture_B": "Hard_Rocks",
                "surfaceTextureSize_B": {"x": 30.0, "y": 14.0},
                "terrainTexture_C": "Soft_Rocks",
                "terrainTextureSize_C": {"x": 280.0, "y": 145.0},
                "surfaceLayerSize": 30.0,
                "minFade": 0.0,
                "maxFade": 1.0,
                "shadowIntensity": 13.0,
                "shadowHeight": 10.0
            },
            "terrainFormulaDifficulties": {
                "Normal": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 753982.236861550, 1)",
                    "OUTPUT = AddHeightMap(Mercury,753982.236861550, 500)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Hard": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 1507964.4737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,1507964.4737231007544, 1000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Realistic": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 15079644.737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,15079644.737231007544, 5000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ]
            },
            "textureFormula": [
                "OUTPUT = AddHeightMap(Perlin,15079.644737231, 1, Curve8)",
                "OUTPUT = ApplyCurve(Curve8)",
                "OUTPUT = ApplyCurve(Curve8)"
            ],
            "verticeSize": 2.0,
            "collider": True,
            "flatZones": [],
            "rocks": {
                "rockType": "Rock Square",
                "rockDensity": 0.5,
                "minSize": 0.1,
                "maxSize": 0.3,
                "powerCurve": 2.0,
                "maxAngle": 20.0
            }
        },
        "POST_PROCESSING": {
            "keys": [
                {
                    "height": 15000.0,
                    "shadowIntensity": 1.75,
                    "starIntensity": 1.0,
                    "hueShift": 0.0,
                    "saturation": 0.95,
                    "contrast": 1.2,
                    "red": 1.0,
                    "green": 1.0,
                    "blue": 1.0
                }
            ]
        },
        "ORBIT_DATA": {
            "parent": planet_name,
            "semiMajorAxis": 2895000000.0,
            "smaDifficultyScale": {},
            "eccentricity": 0.2,
            "argumentOfPeriapsis": 29.0,
            "direction": 1,
            "multiplierSOI": 2.0,
            "soiDifficultyScale": {}
        },
        "ACHIEVEMENT_DATA": {
            "Landed": True,
            "Takeoff": True,
            "Atmosphere": True,
            "Orbit": True,
            "Crash": True
        },
        "LANDMARKS": []
    }
    planet_data = apply_chaos_heightmaps(planet_data)
    red = random.uniform(0,1)
    blue = random.uniform(0,1)
    green = random.uniform(0,1)
    planet_data["BASE_DATA"]["mapColor"]["r"] = red
    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(min,max)) * scale
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(2.5e7 * (min/41560), 5e7 * (max/132000)))
    planet_data["ORBIT_DATA"]["eccentricity"] = random.uniform(0.04,0.16)
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = random.uniform(0.0,360.0)
    main(f"{moon_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{moon_name}.png")
    filepath = os.path.join(output_folder, moon_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            json.dump(planet_data, f, indent=4)
            log(f"{moon_name} exported!")
def create_chaotic_airless_planet(star_name, planet_number, output_folder):
    planet_name = f"{star_name}-{planet_number}"
    log(f"Generating planet {planet_name}...")
    planet_data = {
        "version": "1.5",
        "BASE_DATA": {
            "radius": 120000.0,
            "radiusDifficultyScale": {},
            "gravity": 3.27,
            "gravityDifficultyScale": {},
            "timewarpHeight": 2500.0,
            "velocityArrowsHeight": "NaN",
            "mapColor": {
                "r": 0.410344839,
                "g": 0.372679353,
                "b": 0.3495006,
                "a": 1.0
            },
            "significant": True,
            "rotateCamera": True
        },
        "TERRAIN_DATA": {
            "TERRAIN_TEXTURE_DATA": {
                "planetTexture": f"{planet_name}",
                "planetTextureCutout": 0.945,
                "surfaceTexture_A": "Dark_Dust",
                "surfaceTextureSize_A": {"x": 20.0, "y": 8.0},
                "surfaceTexture_B": "Hard_Rocks",
                "surfaceTextureSize_B": {"x": 30.0, "y": 14.0},
                "terrainTexture_C": "Soft_Rocks",
                "terrainTextureSize_C": {"x": 280.0, "y": 145.0},
                "surfaceLayerSize": 30.0,
                "minFade": 0.0,
                "maxFade": 1.0,
                "shadowIntensity": 13.0,
                "shadowHeight": 10.0
            },
            "terrainFormulaDifficulties": {
                "Normal": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 753982.236861550, 1)",
                    "OUTPUT = AddHeightMap(Mercury,753982.236861550, 500)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Hard": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 1507964.4737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,1507964.4737231007544, 1000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Realistic": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 15079644.737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,15079644.737231007544, 5000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ]
            },
            "textureFormula": [
                "OUTPUT = AddHeightMap(Perlin,15079.644737231, 1, Curve8)",
                "OUTPUT = ApplyCurve(Curve8)",
                "OUTPUT = ApplyCurve(Curve8)"
            ],
            "verticeSize": 2.0,
            "collider": True,
            "flatZones": [],
            "rocks": {
                "rockType": "Rock Square",
                "rockDensity": 0.5,
                "minSize": 0.1,
                "maxSize": 0.3,
                "powerCurve": 2.0,
                "maxAngle": 20.0
            }
        },
        "POST_PROCESSING": {
            "keys": [
                {
                    "height": 15000.0,
                    "shadowIntensity": 1.75,
                    "starIntensity": 1.0,
                    "hueShift": 0.0,
                    "saturation": 0.95,
                    "contrast": 1.2,
                    "red": 1.0,
                    "green": 1.0,
                    "blue": 1.0
                }
            ]
        },
        "ORBIT_DATA": {
            "parent": star_name,
            "semiMajorAxis": 2895000000.0,
            "smaDifficultyScale": {},
            "eccentricity": 0.2,
            "argumentOfPeriapsis": 29.0,
            "direction": 1,
            "multiplierSOI": 2.0,
            "soiDifficultyScale": {}
        },
        "ACHIEVEMENT_DATA": {
            "Landed": True,
            "Takeoff": True,
            "Atmosphere": True,
            "Orbit": True,
            "Crash": True
        },
        "LANDMARKS": []
    }
    planet_data = apply_chaos_heightmaps(planet_data)
    red = random.uniform(0,1)
    blue = random.uniform(0,1)
    green = random.uniform(0,1)
    planet_data["BASE_DATA"]["mapColor"]["r"] = red
    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(100000,400000))
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(1e9,4e10))
    planet_data["ORBIT_DATA"]["eccentricity"] = random.uniform(0.05,0.25)
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = random.uniform(0.0,360.0)
    if __name__ == '__main__':
        main(f"{planet_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{planet_name}.png")
        filepath = os.path.join(output_folder, planet_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            json.dump(planet_data, f, indent=4)
            log(f"{planet_name} exported!")
            for i in range(1, int(random.uniform(0,4))):
                create_major_moon(planet_name, i, output_folder, 20000, 100000 * (planet_data["BASE_DATA"]["radius"]/315000),1)
def create_venusian_moon(planet_name, moon_number, output_folder, min, max, scale):
    moon_name = f"{planet_name}-{moon_number}"
    log(f"Generating moon {moon_name}...")
    planet_data = {
      "version": "1.5",
      "BASE_DATA": {
            "radius": 120000.0,
            "radiusDifficultyScale": {},
            "gravity": 3.27,
            "gravityDifficultyScale": {},
            "timewarpHeight": 2500.0,
            "velocityArrowsHeight": "NaN",
            "mapColor": {
                "r": 0.410344839,
                "g": 0.372679353,
                "b": 0.3495006,
                "a": 1.0
            },
            "significant": True,
            "rotateCamera": True
            },
      "ATMOSPHERE_PHYSICS_DATA": {
        "height": 40000.0,
        "density": 0.025,
        "curve": 13.0,
        "curveScale": {},
        "parachuteMultiplier": 1.0,
        "upperAtmosphere": 0.375,
        "heightDifficultyScale": {},
        "shockwaveIntensity": 1.0,
        "minHeatingVelocityMultiplier": 1.0
      },
      "ATMOSPHERE_VISUALS_DATA": {
        "GRADIENT": {
          "positionZ": 800,
          "height": 45000.0,
          "texture": f"Atmo_{planet_name}"
        },
        "CLOUDS": {
          "texture": "Earth_Clouds",
          "startHeight": -1500.0,
          "width": 9157.86,
          "height": 8500.0,
          "alpha": 1.0,
          "velocity": 1.0
        },
        "FOG": {
          "keys": [
            {
              "color": {
                "r": 0.836079836,
                "g": 0.8455882,
                "b": 0.559580445,
                "a": 0.0
              },
              "distance": 100.0
            },
            {
              "color": {
                "r": 0.815686345,
                "g": 0.788235366,
                "b": 0.709803939,
                "a": 1.0
              },
              "distance": 50000.0
              }
            ]
          }
        },
        "TERRAIN_DATA": {
            "TERRAIN_TEXTURE_DATA": {
                "planetTexture": "Deimos",
                "planetTextureCutout": 0.945,
                "surfaceTexture_A": "Dark_Dust",
                "surfaceTextureSize_A": {"x": 20.0, "y": 8.0},
                "surfaceTexture_B": "Hard_Rocks",
                "surfaceTextureSize_B": {"x": 30.0, "y": 14.0},
                "terrainTexture_C": "Soft_Rocks",
                "terrainTextureSize_C": {"x": 280.0, "y": 145.0},
                "surfaceLayerSize": 30.0,
                "minFade": 0.0,
                "maxFade": 1.0,
                "shadowIntensity": 13.0,
                "shadowHeight": 10.0
            },
            "terrainFormulaDifficulties": {
                "Normal": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 753982.236861550, 1)",
                    "OUTPUT = AddHeightMap(Mercury,753982.236861550, 500)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Hard": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 1507964.4737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,1507964.4737231007544, 1000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Realistic": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 15079644.737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,15079644.737231007544, 5000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ]
            },
            "textureFormula": [
                "OUTPUT = AddHeightMap(Perlin,15079.644737231, 1, Curve8)",
                "OUTPUT = ApplyCurve(Curve8)",
                "OUTPUT = ApplyCurve(Curve8)"
            ],
            "verticeSize": 2.0,
            "collider": True,
            "flatZones": [],
            "rocks": {
                "rockType": "Rock Square",
                "rockDensity": 0.5,
                "minSize": 0.1,
                "maxSize": 0.3,
                "powerCurve": 2.0,
                "maxAngle": 20.0
            }
        },
        "POST_PROCESSING": {
            "keys": [
              {
                "height": 500.0,
                "shadowIntensity": 1.35,
                "starIntensity": 0.0,
                "hueShift": 10.0,
                "saturation": 1.0,
                "contrast": 1.18,
                "red": 1.11,
                "green": 1.08,
                "blue": 0.85
              },
              {
                "height": 40000.0,
                "shadowIntensity": 1.75,
                "starIntensity": 0.0,
                "hueShift": 0.0,
                "saturation": 0.95,
                "contrast": 1.2,
                "red": 1.0,
                "green": 1.0,
                "blue": 1.0
              },
              {
                "height": 50000.0,
                "shadowIntensity": 1.75,
                "starIntensity": 0.0,
                "hueShift": 0.0,
                "saturation": 0.95,
                "contrast": 1.2,
                "red": 1.0,
                "green": 1.0,
                "blue": 1.0
              },
              {
                "height": 60000.0,
                "shadowIntensity": 1.75,
                "starIntensity": 1.0,
                "hueShift": 0.0,
                "saturation": 0.95,
                "contrast": 1.2,
                "red": 1.0,
                "green": 1.0,
                "blue": 1.0
                }
              ]
            },
        "ORBIT_DATA": {
            "parent": planet_name,
            "semiMajorAxis": 2895000000.0,
            "smaDifficultyScale": {},
            "eccentricity": 0.2,
            "argumentOfPeriapsis": 29.0,
            "direction": 1,
            "multiplierSOI": 2.0,
            "soiDifficultyScale": {}
        },
        "ACHIEVEMENT_DATA": {
            "Landed": True,
            "Takeoff": True,
            "Atmosphere": True,
            "Orbit": True,
            "Crash": True
        },
        "LANDMARKS": []
    }
    red = random.uniform(0,1)
    blue = random.uniform(0,1)
    green = random.uniform(0,1)
    planet_data["BASE_DATA"]["mapColor"]["r"] = red
    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(min,max)) * scale
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(2.5e7 * (min/41560), 5e7 * (max/132000)))
    planet_data["ORBIT_DATA"]["eccentricity"] = random.uniform(0.04,0.16)
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = random.uniform(0.0,360.0)
    main(f"{moon_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{moon_name}.png")
    filepath = os.path.join(output_folder, moon_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            json.dump(planet_data, f, indent=4)
            log(f"{moon_name} exported!")
def create_airless_planet(star_name, planet_number, output_folder):
    planet_name = f"{star_name}-{planet_number}"
    log(f"Generating planet {planet_name}...")
    planet_data = {
        "version": "1.5",
        "BASE_DATA": {
            "radius": 120000.0,
            "radiusDifficultyScale": {},
            "gravity": 3.27,
            "gravityDifficultyScale": {},
            "timewarpHeight": 2500.0,
            "velocityArrowsHeight": "NaN",
            "mapColor": {
                "r": 0.410344839,
                "g": 0.372679353,
                "b": 0.3495006,
                "a": 1.0
            },
            "significant": True,
            "rotateCamera": True
        },
        "TERRAIN_DATA": {
            "TERRAIN_TEXTURE_DATA": {
                "planetTexture": f"{planet_name}",
                "planetTextureCutout": 0.945,
                "surfaceTexture_A": "Dark_Dust",
                "surfaceTextureSize_A": {"x": 20.0, "y": 8.0},
                "surfaceTexture_B": "Hard_Rocks",
                "surfaceTextureSize_B": {"x": 30.0, "y": 14.0},
                "terrainTexture_C": "Soft_Rocks",
                "terrainTextureSize_C": {"x": 280.0, "y": 145.0},
                "surfaceLayerSize": 30.0,
                "minFade": 0.0,
                "maxFade": 1.0,
                "shadowIntensity": 13.0,
                "shadowHeight": 10.0
            },
            "terrainFormulaDifficulties": {
                "Normal": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 753982.236861550, 1)",
                    "OUTPUT = AddHeightMap(Mercury,753982.236861550, 500)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Hard": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 1507964.4737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,1507964.4737231007544, 1000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ],
                "Realistic": [
                    "PLAINS = AddHeightMap(Mercury_Plains, 15079644.737231007544, 1)",
                    "OUTPUT = AddHeightMap(Mercury,15079644.737231007544, 5000)",
                    "OUTPUT = AddHeightMap(Craters,75398.223686155, 350, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,15079.644737231, 100, null, PLAINS)",
                    "OUTPUT = AddHeightMap(Craters,2356.19449019234, 12, null, PLAINS)",
                    "OUTPUT = AddHeightMap( Perlin,2513.27412287183, 3)"
                ]
            },
            "textureFormula": [
                "OUTPUT = AddHeightMap(Perlin,15079.644737231, 1, Curve8)",
                "OUTPUT = ApplyCurve(Curve8)",
                "OUTPUT = ApplyCurve(Curve8)"
            ],
            "verticeSize": 2.0,
            "collider": True,
            "flatZones": [],
            "rocks": {
                "rockType": "Rock Square",
                "rockDensity": 0.5,
                "minSize": 0.1,
                "maxSize": 0.3,
                "powerCurve": 2.0,
                "maxAngle": 20.0
            }
        },
        "POST_PROCESSING": {
            "keys": [
                {
                    "height": 15000.0,
                    "shadowIntensity": 1.75,
                    "starIntensity": 1.0,
                    "hueShift": 0.0,
                    "saturation": 0.95,
                    "contrast": 1.2,
                    "red": 1.0,
                    "green": 1.0,
                    "blue": 1.0
                }
            ]
        },
        "ORBIT_DATA": {
            "parent": star_name,
            "semiMajorAxis": 2895000000.0,
            "smaDifficultyScale": {},
            "eccentricity": 0.2,
            "argumentOfPeriapsis": 29.0,
            "direction": 1,
            "multiplierSOI": 2.0,
            "soiDifficultyScale": {}
        },
        "ACHIEVEMENT_DATA": {
            "Landed": True,
            "Takeoff": True,
            "Atmosphere": True,
            "Orbit": True,
            "Crash": True
        },
        "LANDMARKS": []
    }
    red = random.uniform(0,1)
    blue = random.uniform(0,1)
    green = random.uniform(0,1)
    planet_data["BASE_DATA"]["mapColor"]["r"] = red
    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(100000,400000))
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(1e9,4e10))
    planet_data["ORBIT_DATA"]["eccentricity"] = random.uniform(0.05,0.25)
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = random.uniform(0.0,360.0)
    if __name__ == '__main__':
        main(f"{planet_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{planet_name}.png")
        filepath = os.path.join(output_folder, planet_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            json.dump(planet_data, f, indent=4)
            log(f"{planet_name} exported!")
            for i in range(1, int(random.uniform(0,4))):
                create_major_moon(planet_name, i, output_folder, 20000, 100000 * (planet_data["BASE_DATA"]["radius"]/315000),1)
def create_jovian_planet(star_name, planet_number, output_folder):
    planet_name = f"{star_name}-{planet_number}"
    log(f"Generating planet {planet_name}...")
    planet_data = {
      "version": "1.5",
      "BASE_DATA": {
        "radius": 3500000.0,
        "radiusDifficultyScale": {},
        "gravity": 24.8,
        "gravityDifficultyScale": {},
        "timewarpHeight": 80000.0,
        "velocityArrowsHeight": 0.0,
        "mapColor": {
          "r": 1.0,
          "g": 0.66,
          "b": 0.43,
          "a": 1.0
        },
        "significant": True,
        "rotateCamera": True
      },
      "ATMOSPHERE_PHYSICS_DATA": {
        "height": 100000.0,
        "density": 0.025,
        "curve": 15.0,
        "curveScale": {},
        "parachuteMultiplier": 3.0,
        "upperAtmosphere": 0.3,
        "heightDifficultyScale": {},
        "shockwaveIntensity": 0.5,
        "minHeatingVelocityMultiplier": 1.0
      },
      "ATMOSPHERE_VISUALS_DATA": {
        "GRADIENT": {
          "positionZ": 40000,
          "height": 240000.0,
          "texture": f"Atmo_{planet_name}"
        },
        "CLOUDS": {
          "texture": "Earth_Clouds",
          "startHeight": 0.0,
          "width": 1200000.0,
          "height": 950000.0,
          "alpha": 0.65,
          "velocity": 0.0
        },
        "FOG": {
          "keys": []
        }
      },
      "TERRAIN_DATA": {
        "TERRAIN_TEXTURE_DATA": {
          "planetTexture": f"{planet_name}",
          "planetTextureCutout": 0.995,
          "surfaceTexture_A": "Ice",
          "surfaceTextureSize_A": {
            "x": -1.0,
            "y": -1.0
          },
          "surfaceTexture_B": "Ice",
          "surfaceTextureSize_B": {
            "x": -1.0,
            "y": -1.0
          },
          "terrainTexture_C": "Ice",
          "terrainTextureSize_C": {
            "x": -1.0,
            "y": -1.0
          },
          "surfaceLayerSize": 60.0,
          "minFade": 0.0,
          "maxFade": 0.6,
          "shadowIntensity": 0.0,
          "shadowHeight": 0.0
        },
        "terrainFormulaDifficulties": {},
        "textureFormula": [],
        "verticeSize": 10.0,
        "collider": false,
        "flatZones": []
      },
      "POST_PROCESSING": {
        "keys": [
          {
            "height": 0.0,
            "shadowIntensity": 1.4,
            "starIntensity": 1.0,
            "hueShift": 0.0,
            "saturation": 0.95,
            "contrast": 1.1,
            "red": 0.96,
            "green": 0.98,
            "blue": 1.0
          },
          {
            "height": 100000.0,
            "shadowIntensity": 1.65,
            "starIntensity": 1.0,
            "hueShift": 0.0,
            "saturation": 0.95,
            "contrast": 1.1,
            "red": 0.96,
            "green": 0.98,
            "blue": 1.0
          }
        ]
      },
      "ORBIT_DATA": {
        "parent": star_name,
        "semiMajorAxis": 38930000000.0,
        "smaDifficultyScale": {},
        "eccentricity": 0.0,
        "argumentOfPeriapsis": 0.0,
        "direction": 1,
        "multiplierSOI": 1.25,
        "soiDifficultyScale": {}
      },
      "ACHIEVEMENT_DATA": {
        "Landed": true,
        "Takeoff": true,
        "Atmosphere": true,
        "Orbit": true,
        "Crash": true
      },
      "LANDMARKS": []
    }
    red = random.uniform(0,1)
    blue = random.uniform(0,1)
    green = random.uniform(0,1)
    planet_data["BASE_DATA"]["mapColor"]["r"] = red
    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(1000000,4000000))
    planet_data["ATMOSPHERE_PHYSICS_DATA"]["height"] = (planet_data["BASE_DATA"]["radius"]/3500000) * 100000
    planet_data["ATMOSPHERE_VISUALS_DATA"]["height"] = (planet_data["BASE_DATA"]["radius"]/3500000) * 240000
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(2e9,1e11))
    planet_data["ORBIT_DATA"]["eccentricity"] = random.uniform(0.025,0.125)
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = random.uniform(0.0,360.0)
    if __name__ == '__main__':
        main2(f"{planet_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{planet_name}.png")
        main3(f"Atmo_{planet_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{planet_name}.png")
        filepath = os.path.join(output_folder, planet_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            log(f"{planet_name} exported!")
            json.dump(planet_data, f, indent=4)
    for i in range(1, int(random.uniform(2,20))):
        if random.randint(0,4) == 0:
            create_major_moon(planet_name, i, output_folder, 41560, 132000, 1)
        else:
            create_chaotic_major_moon(planet_name, i, output_folder, 41560, 132000, 1)
def create_neptunian_planet(star_name, planet_number, output_folder):
    planet_name = f"{star_name}-{planet_number}"
    log(f"Generating planet {planet_name}...")
    planet_data = {
      "version": "1.5",
      "BASE_DATA": {
        "radius": 3500000.0,
        "radiusDifficultyScale": {},
        "gravity": 24.8,
        "gravityDifficultyScale": {},
        "timewarpHeight": 80000.0,
        "velocityArrowsHeight": 0.0,
        "mapColor": {
          "r": 1.0,
          "g": 0.66,
          "b": 0.43,
          "a": 1.0
        },
        "significant": True,
        "rotateCamera": True
      },
      "ATMOSPHERE_PHYSICS_DATA": {
        "height": 100000.0,
        "density": 0.025,
        "curve": 15.0,
        "curveScale": {},
        "parachuteMultiplier": 3.0,
        "upperAtmosphere": 0.3,
        "heightDifficultyScale": {},
        "shockwaveIntensity": 0.5,
        "minHeatingVelocityMultiplier": 1.0
      },
      "ATMOSPHERE_VISUALS_DATA": {
        "GRADIENT": {
          "positionZ": 40000,
          "height": 240000.0,
          "texture": f"Atmo_{planet_name}"
        },
        "CLOUDS": {
          "texture": "Earth_Clouds",
          "startHeight": 0.0,
          "width": 1200000.0,
          "height": 950000.0,
          "alpha": 0.65,
          "velocity": 0.0
        },
        "FOG": {
          "keys": []
        }
      },
      "TERRAIN_DATA": {
        "TERRAIN_TEXTURE_DATA": {
          "planetTexture": f"{planet_name}",
          "planetTextureCutout": 0.995,
          "surfaceTexture_A": "Ice",
          "surfaceTextureSize_A": {
            "x": -1.0,
            "y": -1.0
          },
          "surfaceTexture_B": "Ice",
          "surfaceTextureSize_B": {
            "x": -1.0,
            "y": -1.0
          },
          "terrainTexture_C": "Ice",
          "terrainTextureSize_C": {
            "x": -1.0,
            "y": -1.0
          },
          "surfaceLayerSize": 60.0,
          "minFade": 0.0,
          "maxFade": 0.6,
          "shadowIntensity": 0.0,
          "shadowHeight": 0.0
        },
        "terrainFormulaDifficulties": {},
        "textureFormula": [],
        "verticeSize": 10.0,
        "collider": false,
        "flatZones": []
      },
      "POST_PROCESSING": {
        "keys": [
          {
            "height": 0.0,
            "shadowIntensity": 1.4,
            "starIntensity": 1.0,
            "hueShift": 0.0,
            "saturation": 0.95,
            "contrast": 1.1,
            "red": 0.96,
            "green": 0.98,
            "blue": 1.0
          },
          {
            "height": 100000.0,
            "shadowIntensity": 1.65,
            "starIntensity": 1.0,
            "hueShift": 0.0,
            "saturation": 0.95,
            "contrast": 1.1,
            "red": 0.96,
            "green": 0.98,
            "blue": 1.0
          }
        ]
      },
      "ORBIT_DATA": {
        "parent": star_name,
        "semiMajorAxis": 38930000000.0,
        "smaDifficultyScale": {},
        "eccentricity": 0.0,
        "argumentOfPeriapsis": 0.0,
        "direction": 1,
        "multiplierSOI": 1.25,
        "soiDifficultyScale": {}
      },
      "ACHIEVEMENT_DATA": {
        "Landed": true,
        "Takeoff": true,
        "Atmosphere": true,
        "Orbit": true,
        "Crash": true
      },
      "LANDMARKS": []
    }
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(315000 * 1.7, 315000 * 7))
    # Convert radius to Terran radii
    radius_terr = planet_data["BASE_DATA"]["radius"] / 315000
    # Assign color based on Neptune-like category
    if radius_terr < 3:
        # Mini-Neptune: greenish-blue range
        red = random.uniform(0.1, 0.3)
        green = random.uniform(0.6, 0.9)
        blue = random.uniform(0.6, 1.0)
    elif radius_terr < 4.2:
        # Neptune-sized: classic blue
        red = random.uniform(0.0, 0.2)
        green = random.uniform(0.2, 0.5)
        blue = random.uniform(0.6, 1.0)
    else:
        # Super-Neptune: warm hazy colors
        red = random.uniform(0.6, 1.0)
        green = random.uniform(0.5, 0.8)
        blue = random.uniform(0.2, 0.5)
    planet_data["BASE_DATA"]["mapColor"]["r"] = red
    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    planet_data["ATMOSPHERE_PHYSICS_DATA"]["height"] = (planet_data["BASE_DATA"]["radius"]/3500000) * 100000
    planet_data["ATMOSPHERE_VISUALS_DATA"]["height"] = (planet_data["BASE_DATA"]["radius"]/3500000) * 240000
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(2e9,2e11))
    planet_data["ORBIT_DATA"]["eccentricity"] = random.uniform(0.025,0.125)
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = random.uniform(0.0,360.0)
    if __name__ == '__main__':
        main4(f"{planet_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{planet_name}.png")
        main3(f"Atmo_{planet_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{planet_name}.png")
        filepath = os.path.join(output_folder, planet_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            log(f"{planet_name} exported!")
            json.dump(planet_data, f, indent=4)
    for i in range(1, int(random.uniform(2,20))):
        create_major_moon(planet_name, i, output_folder, 41560, 132000, 0.5)
def create_caseian_jovian_planet(output_folder):
    planet_name = "C" + (generate_filename())
    log_caseian(f"Generating planet {planet_name}...")
    planet_data = {
      "version": "1.5",
      "BASE_DATA": {
        "radius": 3500000.0,
        "radiusDifficultyScale": {},
        "gravity": 24.8,
        "gravityDifficultyScale": {},
        "timewarpHeight": 80000.0,
        "velocityArrowsHeight": 0.0,
        "mapColor": {
          "r": 1.0,
          "g": 0.66,
          "b": 0.43,
          "a": 1.0
        },
        "significant": True,
        "rotateCamera": True
      },
      "ATMOSPHERE_PHYSICS_DATA": {
        "height": 100000.0,
        "density": 0.025,
        "curve": 15.0,
        "curveScale": {},
        "parachuteMultiplier": 3.0,
        "upperAtmosphere": 0.3,
        "heightDifficultyScale": {},
        "shockwaveIntensity": 0.5,
        "minHeatingVelocityMultiplier": 1.0
      },
      "ATMOSPHERE_VISUALS_DATA": {
        "GRADIENT": {
          "positionZ": 40000,
          "height": 240000.0,
          "texture": f"Atmo_{planet_name}"
        },
        "CLOUDS": {
          "texture": "Earth_Clouds",
          "startHeight": 0.0,
          "width": 1200000.0,
          "height": 950000.0,
          "alpha": 0.65,
          "velocity": 0.0
        },
        "FOG": {
          "keys": []
        }
      },
      "TERRAIN_DATA": {
        "TERRAIN_TEXTURE_DATA": {
          "planetTexture": f"{planet_name}",
          "planetTextureCutout": 0.995,
          "surfaceTexture_A": "Ice",
          "surfaceTextureSize_A": {
            "x": -1.0,
            "y": -1.0
          },
          "surfaceTexture_B": "Ice",
          "surfaceTextureSize_B": {
            "x": -1.0,
            "y": -1.0
          },
          "terrainTexture_C": "Ice",
          "terrainTextureSize_C": {
            "x": -1.0,
            "y": -1.0
          },
          "surfaceLayerSize": 60.0,
          "minFade": 0.0,
          "maxFade": 0.6,
          "shadowIntensity": 0.0,
          "shadowHeight": 0.0
        },
        "terrainFormulaDifficulties": {},
        "textureFormula": [],
        "verticeSize": 10.0,
        "collider": false,
        "flatZones": []
      },
      "POST_PROCESSING": {
        "keys": [
          {
            "height": 0.0,
            "shadowIntensity": 1.4,
            "starIntensity": 1.0,
            "hueShift": 0.0,
            "saturation": 0.95,
            "contrast": 1.1,
            "red": 0.96,
            "green": 0.98,
            "blue": 1.0
          },
          {
            "height": 100000.0,
            "shadowIntensity": 1.65,
            "starIntensity": 1.0,
            "hueShift": 0.0,
            "saturation": 0.95,
            "contrast": 1.1,
            "red": 0.96,
            "green": 0.98,
            "blue": 1.0
          }
        ]
      },
      "ORBIT_DATA": {
        "parent": "Sagittarius A",
        "semiMajorAxis": 38930000000.0,
        "smaDifficultyScale": {},
        "eccentricity": 0.0,
        "argumentOfPeriapsis": 0.0,
        "direction": 1,
        "multiplierSOI": 1.25,
        "soiDifficultyScale": {}
      },
      "ACHIEVEMENT_DATA": {
        "Landed": true,
        "Takeoff": true,
        "Atmosphere": true,
        "Orbit": true,
        "Crash": true
      },
      "LANDMARKS": []
    }
    red = random.uniform(0,1)
    blue = random.uniform(0,1)
    green = random.uniform(0,1)
    planet_data["BASE_DATA"]["mapColor"]["r"] = red
    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(1.2841016e8,1.85569144e9))
    planet_data["ATMOSPHERE_PHYSICS_DATA"]["height"] = (planet_data["BASE_DATA"]["radius"]/3500000) * 100000
    planet_data["ATMOSPHERE_VISUALS_DATA"]["height"] = (planet_data["BASE_DATA"]["radius"]/3500000) * 240000
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(2e10,4e14))
    planet_data["ORBIT_DATA"]["eccentricity"] = 0
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = 0
    main2(f"{planet_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{planet_name}.png")
    main3(f"Atmo_{planet_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{planet_name}.png")
    filepath = os.path.join(output_folder, planet_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            json.dump(planet_data, f, indent=4)
            log_caseian(f"{planet_name} exported!")
    for i in range(1, int(random.uniform(2,25))):
        if round(random.uniform(0,1)) == 0:
            create_venusian_moon(planet_name, i, output_folder, max(2e8,planet_data["BASE_DATA"]["radius"] + 1e8), max(1e10,planet_data["BASE_DATA"]["radius"] + 4e9), 0.001)
        else:
            if round(random.uniform(0,1)) == 0:
                create_major_moon(planet_name, i, output_folder, max(2e8,planet_data["BASE_DATA"]["radius"] + 1e8), max(1e10,planet_data["BASE_DATA"]["radius"] + 4e9), 0.001)
            else:
                create_jovian_planet(planet_name, i, output_folder)
def create_venusian_planet(star_name, planet_number, output_folder):
    planet_name = f"{star_name}-{planet_number}"
    log(f"Generating planet {planet_name}...")
    planet_data = {
      "version": "1.5",
      "BASE_DATA": {
        "radius": 300000.0,
        "radiusDifficultyScale": {},
        "gravity": 8.87,
        "gravityDifficultyScale": {},
        "timewarpHeight": 35000.0,
        "velocityArrowsHeight": 3000.0,
        "mapColor": {
          "r": 0.789655149,
          "g": 0.6457909,
          "b": 0.49713105,
          "a": 1.0
        },
        "significant": true,
        "rotateCamera": true
      },
      "ATMOSPHERE_PHYSICS_DATA": {
        "height": 40000.0,
        "density": 0.025,
        "curve": 13.0,
        "curveScale": {},
        "parachuteMultiplier": 1.0,
        "upperAtmosphere": 0.375,
        "heightDifficultyScale": {},
        "shockwaveIntensity": 1.0,
        "minHeatingVelocityMultiplier": 1.0
      },
      "ATMOSPHERE_VISUALS_DATA": {
        "GRADIENT": {
          "positionZ": 800,
          "height": 45000.0,
          "texture": f"Atmo_{planet_name}"
        },
        "CLOUDS": {
          "texture": "Earth_Clouds",
          "startHeight": -1500.0,
          "width": 9157.86,
          "height": 8500.0,
          "alpha": 1.0,
          "velocity": 1.0
        },
        "FOG": {
          "keys": [
            {
              "color": {
                "r": 0.836079836,
                "g": 0.8455882,
                "b": 0.559580445,
                "a": 0.0
              },
              "distance": 100.0
            },
            {
              "color": {
                "r": 0.815686345,
                "g": 0.788235366,
                "b": 0.709803939,
                "a": 1.0
              },
              "distance": 50000.0
            }
          ]
        }
      },
      "TERRAIN_DATA": {
        "TERRAIN_TEXTURE_DATA": {
          "planetTexture": "Deimos",
          "planetTextureCutout": 0.945,
          "surfaceTexture_A": "Dust",
          "surfaceTextureSize_A": {
            "x": 32.0,
            "y": 14.0
          },
          "surfaceTexture_B": "Soft_Rocks",
          "surfaceTextureSize_B": {
            "x": 48.0,
            "y": 20.0
          },
          "terrainTexture_C": "Blured",
          "terrainTextureSize_C": {
            "x": 2000.0,
            "y": 650.0
          },
          "surfaceLayerSize": 60.0,
          "minFade": 0.0,
          "maxFade": 0.8,
          "shadowIntensity": 6.0,
          "shadowHeight": 6.5
        },
        "terrainFormulaDifficulties": {
          "Normal": [
            "OUTPUT = AddHeightMap(Venus, 1884955.592153875, 4000)",
            "PLAINS = AddHeightMap(Venus_Plains, 1884955.5921538759, 1)",
            "OUTPUT = AddHeightMap( Perlin,6283.18530717959, 8, Curve1, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,3490.65850398866, 5, Curve1, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,1449.96584011837, 1.6, Curve1)",
            "OUTPUT = AddHeightMap( Perlin,942.477796076938, 1.5, Curve1, PLAINS)",
            "M = AddHeightMap( Perlin,47123.8898038469, 1, Curve2, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,26927.9370307697, 200, Curve1, M)",
            "M2 = AddHeightMap( Perlin,269279.370307697, 1, Curve2, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,94247.7796076938, 1300, Curve1, M2)"
          ],
          "Hard": [
            "OUTPUT = AddHeightMap(Venus, 3769911.18430775, 8000)",
            "PLAINS = AddHeightMap(Venus_Plains, 3769911.184307751, 1)",
            "OUTPUT = AddHeightMap( Perlin,6283.18530717959, 8, Curve1, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,3490.65850398866, 5, Curve1, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,1449.96584011837, 1.6, Curve1)",
            "OUTPUT = AddHeightMap( Perlin,942.477796076938, 1.5, Curve1, PLAINS)",
            "M = AddHeightMap( Perlin,47123.8898038469, 1, Curve2, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,26927.9370307697, 200, Curve1, M)",
            "M2 = AddHeightMap( Perlin,269279.370307697, 1, Curve2, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,94247.7796076938, 1300, Curve1, M2)"
          ],
          "Realistic": [
            "OUTPUT = AddHeightMap(Venus, 37699111.8430775, 80000)",
            "PLAINS = AddHeightMap(Venus_Plains, 37699111.84307751, 1)",
            "OUTPUT = AddHeightMap( Perlin,6283.18530717959, 8, Curve1, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,3490.65850398866, 5, Curve1, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,1449.96584011837, 1.6, Curve1)",
            "OUTPUT = AddHeightMap( Perlin,942.477796076938, 1.5, Curve1, PLAINS)",
            "M = AddHeightMap( Perlin,47123.8898038469, 1, Curve2, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,26927.9370307697, 200, Curve1, M)",
            "M2 = AddHeightMap( Perlin,269279.370307697, 1, Curve2, PLAINS)",
            "OUTPUT = AddHeightMap( Perlin,94247.7796076938, 1300, Curve1, M2)"
          ]
        },
        "textureFormula": [],
        "verticeSize": 2.0,
        "collider": true,
        "flatZones": [],
        "rocks": {
          "rockType": "Rock Square",
          "rockDensity": 0.1,
          "minSize": 0.2,
          "maxSize": 0.5,
          "powerCurve": 2.0,
          "maxAngle": 20.0
        }
      },
      "POST_PROCESSING": {
        "keys": [
          {
            "height": 500.0,
            "shadowIntensity": 1.35,
            "starIntensity": 0.0,
            "hueShift": 10.0,
            "saturation": 1.0,
            "contrast": 1.18,
            "red": 1.11,
            "green": 1.08,
            "blue": 0.85
          },
          {
            "height": 40000.0,
            "shadowIntensity": 1.75,
            "starIntensity": 0.0,
            "hueShift": 0.0,
            "saturation": 0.95,
            "contrast": 1.2,
            "red": 1.0,
            "green": 1.0,
            "blue": 1.0
          },
          {
            "height": 50000.0,
            "shadowIntensity": 1.75,
            "starIntensity": 0.0,
            "hueShift": 0.0,
            "saturation": 0.95,
            "contrast": 1.2,
            "red": 1.0,
            "green": 1.0,
            "blue": 1.0
          },
          {
            "height": 60000.0,
            "shadowIntensity": 1.75,
            "starIntensity": 1.0,
            "hueShift": 0.0,
            "saturation": 0.95,
            "contrast": 1.2,
            "red": 1.0,
            "green": 1.0,
            "blue": 1.0
          }
        ]
      },
      "ORBIT_DATA": {
        "parent": star_name,
        "semiMajorAxis": 5410000000.0,
        "smaDifficultyScale": {},
        "eccentricity": 0.0,
        "argumentOfPeriapsis": 0.0,
        "direction": 1,
        "multiplierSOI": 2.0,
        "soiDifficultyScale": {}
      },
      "ACHIEVEMENT_DATA": {
        "Landed": true,
        "Takeoff": true,
        "Atmosphere": true,
        "Orbit": true,
        "Crash": true
      },
      "LANDMARKS": []
    }
    red = random.uniform(0,1)
    blue = random.uniform(0,1)
    green = random.uniform(0,1)
    planet_data["BASE_DATA"]["mapColor"]["r"] = red
    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    # Update all FOG colors
    for key in planet_data["ATMOSPHERE_VISUALS_DATA"]["FOG"]["keys"]:
        key["color"]["r"] = red
        key["color"]["g"] = green
        key["color"]["b"] = blue

    # Update all POST_PROCESSING red values
    for key in planet_data["POST_PROCESSING"]["keys"]:
        key["red"] = red
        key["green"] = green
        key["blue"] = blue

    planet_data["BASE_DATA"]["mapColor"]["b"] = blue
    planet_data["BASE_DATA"]["mapColor"]["g"] = green
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(315000*0.8,315000*1.1))
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(7.48e9*0.5,7.48e9*0.8))
    planet_data["ORBIT_DATA"]["eccentricity"] = random.uniform(0.05,0.25)
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = random.uniform(0.0,360.0)
    if __name__ == '__main__':
        main3(f"Atmo_{planet_name}.png", (int(red*255),int(green*255),int(blue*255)),f"{planet_name}.png")
        filepath = os.path.join(output_folder, planet_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            json.dump(planet_data, f, indent=4)
            log(f"{planet_name} exported!")
            for i in range(1, int(random.uniform(0,4))):
                create_major_moon(planet_name, i, output_folder, 20000, 100000 * (planet_data["BASE_DATA"]["radius"]/315000),1)
def create_terran_planet(star_name, planet_number, output_folder):
    planet_name = f"{star_name}-{planet_number}"
    log(f"Life on {planet_name} is forming...")
    planet_data = {
  "version": "1.5",
  "BASE_DATA": {
    "radius": 315000.0,
    "radiusDifficultyScale": {},
    "gravity": 9.8,
    "gravityDifficultyScale": {},
    "timewarpHeight": 25000.0,
    "velocityArrowsHeight": 5000.0,
    "mapColor": {
      "r": 0.45,
      "g": 0.68,
      "b": 1.0,
      "a": 1.0
    },
    "significant": true,
    "rotateCamera": true
  },
  "ATMOSPHERE_PHYSICS_DATA": {
    "height": 30000.0,
    "density": 0.005,
    "curve": 10.0,
    "curveScale": {},
    "parachuteMultiplier": 1.0,
    "upperAtmosphere": 0.333,
    "heightDifficultyScale": {},
    "shockwaveIntensity": 1.0,
    "minHeatingVelocityMultiplier": 1.0
  },
  "ATMOSPHERE_VISUALS_DATA": {
    "GRADIENT": {
      "positionZ": 4000,
      "height": 45000.0,
      "texture": "Atmo_Earth"
    },
    "CLOUDS": {
      "texture": "Earth_Clouds",
      "startHeight": 1200.0,
      "width": 40845.87,
      "height": 36000.0,
      "alpha": 0.1,
      "velocity": 2.0
    },
    "FOG": {
      "keys": [
        {
          "color": {
            "r": 0.461872876,
            "g": 0.463235319,
            "b": 0.3644572,
            "a": 0.09803922
          },
          "distance": 500.0
        },
        {
          "color": {
            "r": 0.647058845,
            "g": 0.848739564,
            "b": 0.891,
            "a": 0.117647059
          },
          "distance": 3000.0
        },
        {
          "color": {
            "r": 0.647058845,
            "g": 0.848739564,
            "b": 1.0,
            "a": 0.416
          },
          "distance": 30000.0
        }
      ]
    }
  },
  "TERRAIN_DATA": {
    "TERRAIN_TEXTURE_DATA": {
      "planetTexture": "Earth",
      "planetTextureCutout": 1.0,
      "surfaceTexture_A": "Blured",
      "surfaceTextureSize_A": {
        "x": 20.0,
        "y": 8.0
      },
      "surfaceTexture_B": "None",
      "surfaceTextureSize_B": {
        "x": -1.0,
        "y": -1.0
      },
      "terrainTexture_C": "Blured",
      "terrainTextureSize_C": {
        "x": 100.0,
        "y": 30.0
      },
      "surfaceLayerSize": 40.0,
      "minFade": 0.0,
      "maxFade": 1.0,
      "shadowIntensity": 6.0,
      "shadowHeight": 15.0
    },
    "terrainFormulaDifficulties": {
      "Normal": [
        "OUTPUT = AddHeightMap(Perlin,19030.8016515536, 35)",
        "OUTPUT = AddHeightMap(Perlin,2452.54445075783, 5)",
        "OUTPUT = AddHeightMap(Perlin,1319.46891450771, 1)"
      ]
    },
    "textureFormula": [],
    "verticeSize": 4.0,
    "collider": true,
    "flatZones": [
      {
        "height": 18.0,
        "angle": 1.5707,
        "width": 900.0,
        "transition": 200.0
      }
    ]
  },
  "POST_PROCESSING": {
    "keys": [
      {
        "height": 0.0,
        "shadowIntensity": 1.35,
        "starIntensity": 0.0,
        "hueShift": 0.0,
        "saturation": 0.95,
        "contrast": 1.2,
        "red": 1.03,
        "green": 1.02,
        "blue": 1.0
      },
      {
        "height": 7000.0,
        "shadowIntensity": 1.5,
        "starIntensity": 0.0,
        "hueShift": 0.0,
        "saturation": 0.95,
        "contrast": 1.2,
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      {
        "height": 25000.0,
        "shadowIntensity": 1.75,
        "starIntensity": 0.0,
        "hueShift": 0.0,
        "saturation": 0.95,
        "contrast": 1.2,
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      {
        "height": 40000.0,
        "shadowIntensity": 1.75,
        "starIntensity": 0.0,
        "hueShift": 0.0,
        "saturation": 0.95,
        "contrast": 1.2,
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      {
        "height": 50000.0,
        "shadowIntensity": 1.75,
        "starIntensity": 1.0,
        "hueShift": 0.0,
        "saturation": 0.95,
        "contrast": 1.2,
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
        }
      ]
    },
      "ORBIT_DATA": {
        "parent": star_name,
        "semiMajorAxis": 5410000000.0,
        "smaDifficultyScale": {},
        "eccentricity": 0.0,
        "argumentOfPeriapsis": 0.0,
        "direction": 1,
        "multiplierSOI": 2.0,
        "soiDifficultyScale": {}
      },
      "ACHIEVEMENT_DATA": {
        "Landed": true,
        "Takeoff": true,
        "Atmosphere": true,
        "Orbit": true,
        "Crash": true
      },
      "LANDMARKS": []
    }
    planet_data["BASE_DATA"]["radius"] = int(random.uniform(315000*0.4,315000*1.6))
    planet_data["ORBIT_DATA"]["semiMajorAxis"] = int(random.uniform(7.48e9*0.5,7.48e9*0.8))
    planet_data["ORBIT_DATA"]["eccentricity"] = random.uniform(0.05,0.25)
    planet_data["ORBIT_DATA"]["argumentOfPeriapsis"] = random.uniform(0.0,360.0)
    filepath = os.path.join(output_folder, planet_name + ".txt")
    with open(filepath, "w", encoding="utf-8") as f:
            json.dump(planet_data, f, indent=4)
            log(f"Life on {planet_name} has developed...")
            for i in range(1, int(random.uniform(0,2))):
                create_major_moon(planet_name, i, output_folder, 20000, 100000 * (planet_data["BASE_DATA"]["radius"]/315000),1)
# Define the base template
def genStar():
    name = generate_filename()
    filename = name + ".txt"
    log(f"Generating Star {name}...")
    star_template = {
        "BASE_DATA": {
            "name": "Sun",
            "radius": 31500000,  # will be randomized
            "gravity": 100,
            "timewarpHeight": 500000.0,
            "mapColor": {"r": 1.0, "g": 1.0, "b": 1.0},
            "mapResolution": 500,
            "hideNameMultiplier": 80.0
        },
        "ATMOSPHERE_DATA": {
            "PHYSICS": {"height": 1000000.0, "density": 0.025, "curve": 15.0},
            "GRADIENT": {
                "positionZ": 40000,
                "gradientHeight": 95287500,  # will be scaled with radius
                "gradientTexture": "Atmo_Sun"
            },
            "CLOUDS": {
                "cloudTexture": "None",
                "startHeight": 0,
                "height": 950000,
                "repeatX": 0.25,
                "alpha": 0.6499999761581421,
                "cloudVelocity": 0.0
            },
            "FOG": {"keys": []}
        },
        "ORBIT_DATA": {
            "parent": "Sagittarius A",
            "orbitHeight": 20200000000000.0,  # will be randomized
            "multiplierSOI": 4,
            "orbitLineResolution": 100
        }
    }

    # Randomization ranges
    radius = random.uniform(2.0e7, 4.0e7)  # between 20M and 40M
    gradient_scale = radius / 31500000  # scale based on original radius
    gradient_height = 95287500 * gradient_scale
    orbit_height = random.uniform(1.5e12, 2.5e16)  # between 15T and 25T

    # Update the template
    star_template["BASE_DATA"]["radius"] = radius
    star_template["BASE_DATA"]["mapColor"]["r"] = 1
    star_template["BASE_DATA"]["mapColor"]["g"] = radius / 31500000
    star_template["BASE_DATA"]["mapColor"]["b"] = radius / 31500000
    star_template["ATMOSPHERE_DATA"]["GRADIENT"]["gradientHeight"] = gradient_height
    star_template["ORBIT_DATA"]["orbitHeight"] = orbit_height

    # Prepare output folder and file
    output_folder = gen_folder
    if output_folder is None:
        raise FileNotFoundError("GENERATED folder not found in parent directory.")

    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, filename)
    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        for section, content in star_template.items():
            f.write(f"●{section}●\n")
            f.write(json.dumps(content, indent=4))
            f.write("\n\n")

    output_file
    num_planets = int(random.uniform(1,maxPlanets))
    star_name = filename[:-4]  # remove ".txt"
    for i in range(1, num_planets + 1):
        if random.randint(0,8) == 1:
            create_terran_planet(star_name, i, output_folder)
        else:
            if random.randint(0,4) == 1:
                create_jovian_planet(star_name, i, output_folder)
            else:
                if random.randint(0,2) == 1:
                    create_venusian_planet(star_name, i, output_folder)
                else:
                    create_airless_planet(star_name, i, output_folder)
                    import json
bary = {
    "BASE_DATA": {
        "name": "Barycenter",
        "radius": 350.0,
        "gravity": 1000000000.0,
        "timewarpHeight": 0.0,
        "mapColor": {
            "r": 0.0,
            "g": 0.0,
            "b": 0.0
        },
        "mapResolution": 500,
        "hideNameMultiplier": 800000000000000000000000000.0
    },

    "ATMOSPHERE_DATA": {
        "PHYSICS": {
            "height": 0.0,
            "density": 0.0,
            "curve": 0.0
        },
        "GRADIENT": {
            "positionZ": 0,
            "gradientHeight": 0.0,
            "gradientTexture": "None"
        },
        "CLOUDS": {
            "cloudTexture": "None",
            "startHeight": 0,
            "height": 0,
            "repeatX": 0.0,
            "alpha": 0.0,
            "cloudVelocity": 0.0
        },
        "FOG": {
            "keys": []
        }
    },

    "ORBIT_DATA": {
        "parent": "Sagittarius A",
        "semiMajorAxis": 20200000000000.0,
        "multiplierSOI": 9.0,
        "orbitLineResolution": 2
    },

    "POST_PROCESSING": {
        "keys": [
            {
                "height": 0.0,
                "shadowIntensity": 1.399999976158142,
                "hueShift": 0.0,
                "saturation": 0.949999988079071,
                "contrast": 1.100000023841858,
                "red": 0.9599999785423279,
                "green": 0.9800000190734863,
                "blue": 1.0
            },
            {
                "height": 100000.0,
                "shadowIntensity": 1.649999976158142,
                "hueShift": 0.0,
                "saturation": 0.949999988079071,
                "contrast": 1.100000023841858,
                "red": 0.9599999785423279,
                "green": 0.9800000190734863,
                "blue": 1.0
            }
        ]
    }
}

def write_barycenter(name="Barycenter", maxPlanet=maxPlanets, terranRarity=5, dist=0):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = gen_folder
    os.makedirs(output_folder, exist_ok=True)

    filename = os.path.join(output_folder, f"{name}.txt")
    seperation = random.uniform(1.5e8, 2.5e10)
    user_max_planets = int(max_planets_entry.get())
    user_terran_rarity = int(terran_rarity_entry.get())
    genStar_custom(user_max_planets, user_terran_rarity, name, seperation, name + '-A', 1)
    genStar_custom(user_max_planets, user_terran_rarity, name, -seperation, name + '-B', -1)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(bary, f, indent=4)
        log(f"Barycenter {name} generated.")

# GUI Settings and tkinter variables
def start_generation_thread():
    total_planets = [0]
    planet_counter = [0]

    progress_label2.config(text="Generating planets...")
    progress_var2.set(0)
    thread = threading.Thread(target=generate_systems)
    thread.start()

def generate_systems():
    try:
        user_stars = int(star_count_entry.get())
        user_max_planets = int(max_planets_entry.get())
        user_caseian_rarity = int(caseian_rarity_entry.get())
        user_terran_rarity = int(terran_rarity_entry.get())
        selected_galaxy = galaxy_type_var.get()  # Reserved for later use
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")
        return

    progress_bar["maximum"] = user_stars
    progress_var.set(0)
    for i in range(1, math.ceil(user_stars * 4)):
        seed2 = seed + i*16
        HeightmapGen.generate_noise_heightmap(noise_strength=0.5, smoothing_factor=5, seed=seed2, output_file=f"Chaos_{i}.png")
    for i in range(user_stars):
        progress_var.set(i + 1)
        progress_label.config(text=f"Generating stars... {i+1}/{user_stars}")
        root.update_idletasks()
        genStar_custom(
            maxPlanets=user_max_planets,
            terranRarity=user_terran_rarity,
            progress_var=progress_var,
            progress_label=progress_label
        )
    for i in range(1, math.ceil(user_stars / 2) + 1):
        if random.randint(0, user_caseian_rarity) == 1:
            create_caseian_jovian_planet(find("GENERATED"))

    progress_label.config(text="Generation complete!")
    progress_label2.config(text="Generation complete.")
# Modified genStar with parameters
def genStar_custom(maxPlanets, terranRarity, parent="Sagittarius A", dist=0, name="Sagittarius A", direction=1, progress_var=None, progress_label=None):
    star_template = {
        "BASE_DATA": {
            "name": "Sun",
            "radius": 31500000,
            "gravity": 100,
            "timewarpHeight": 500000.0,
            "mapColor": {"r": 1.0, "g": 1.0, "b": 1.0},
            "mapResolution": 500,
            "hideNameMultiplier": 80.0
        },
        "ATMOSPHERE_DATA": {
            "PHYSICS": {"height": 1000000.0, "density": 0.025, "curve": 15.0},
            "GRADIENT": {
                "positionZ": 40000,
                "gradientHeight": 95287500,
                "gradientTexture": "Atmo_Sun"
            },
            "CLOUDS": {
                "cloudTexture": "None",
                "startHeight": 0,
                "height": 950000,
                "repeatX": 0.25,
                "alpha": 0.6499999761581421,
                "cloudVelocity": 0.0
            },
            "FOG": {"keys": []}
        },
        "ORBIT_DATA": {
            "parent": parent,
            "orbitHeight": 0,
            "multiplierSOI": 4,
            "orbitLineResolution": 100
        }
    }
    
    if dist == 0:
        star_template["ORBIT_DATA"]["orbitHeight"] = random.uniform(1.5e12, 2.5e16)
    else:
        star_template["ORBIT_DATA"]["orbitHeight"] = dist
    radius = random.uniform(2.0e7, 4.0e7)
    gradient_scale = radius / 31500000
    star_template["BASE_DATA"]["radius"] = radius
    star_template["BASE_DATA"]["mapColor"]["g"] = radius / 31500000
    star_template["BASE_DATA"]["mapColor"]["b"] = radius / 31500000
    star_template["ATMOSPHERE_DATA"]["GRADIENT"]["gradientHeight"] = 95287500 * gradient_scale

    output_folder = gen_folder
    if output_folder is None:
        raise FileNotFoundError("GENERATED folder not found.")

    os.makedirs(output_folder, exist_ok=True)
    if name == "Sagittarius A":
        starname = generate_filename()
        filename = starname + ".txt"
    else:
        filename = name + ".txt"
    output_file = os.path.join(output_folder, filename)

    with open(output_file, "w", encoding="utf-8") as f:
        for section, content in star_template.items():
            f.write(f"●{section}●\n")
            f.write(json.dumps(content, indent=4))
            f.write("\n\n")

        num_planets = int(random.uniform(1, maxPlanets))
    star_name = filename[:-4]
    progress_bar2["maximum"] = num_planets + 1
    progress_var2.set(0)
    for i in range(1, num_planets + 1):
        # Generate one planet per loop
        if random.randint(0, terranRarity) == 1:
            create_terran_planet(star_name, i, output_folder)
        elif random.randint(0, 4) == 1:
            create_jovian_planet(star_name, i, output_folder)
        elif random.randint(0, 2) == 1:
            create_venusian_planet(star_name, i, output_folder)
        elif random.randint(2, 7) != 2 and random.randint(2, 7) != 3:
            create_neptunian_planet(star_name, i, output_folder)
        else:
            create_airless_planet(star_name, i, output_folder)

        # Update progress based on i
        if progress_var2 is not None and progress_label2 is not None:
            progress_var2.set(i)
            progress_label2.config(text=f"Generating planets for {starname}... {i}/{num_planets}")
            root.update_idletasks()

def log(msg):
    print(msg)  # fallback to terminal
    try:
        log_area.config(state=tk.NORMAL)
        log_area.insert(tk.END, msg + "\n")
        log_area.yview(tk.END)
        log_area.config(state=tk.DISABLED)
    except Exception as e:
        print(f"[LOG ERROR] {e}")

def log_caseian(message):
    try:
        log_area.config(state=tk.NORMAL)
        log_area.insert(tk.END, message + "\n", "caseian")
        log_area.yview(tk.END)
        log_area.config(state=tk.DISABLED)
    except Exception as e:
        print(f"[LOG ERROR] {e}")

# ----- GUI SETUP -----
from PIL import Image, ImageTk

# ---- ROOT SETUP ----
root = tk.Tk()
root.title("Planetary System Generator")
root.geometry("420x380")
root.state("zoomed")  # Windows only
root.configure(bg="#1e0033")

# ---- STYLE SETUP ----
style = ttk.Style()
style.theme_use("default")

style.configure("TFrame", background="#1e0033")
style.configure("TLabel", background="#1e0033", foreground="white")
style.configure("TButton", background="#1e0033", foreground="white")
style.configure("TProgressbar", troughcolor="#1e0033", background="#6a00cc")

# ---- FRAME SETUP ----
frame = ttk.Frame(root, padding=12)
frame.pack(fill="both", expand=True)

from tkinter.scrolledtext import ScrolledText

log_area = ScrolledText(frame, height=10, bg="black", fg="lime", insertbackground="white")
log_area.pack(fill="both", expand=False, padx=10, pady=(10, 0))
log_area.config(state=tk.DISABLED)  # Start as read-only

icon_path = os.path.join(dev_folder, 'logo.ico')
root.iconbitmap(icon_path)

logo_path = os.path.join(dev_folder, 'logo.png')
logo_img = Image.open(logo_path)
logo_img = logo_img.resize((100, 100))  # Optional: adjust size
logo = ImageTk.PhotoImage(logo_img)

logo_label = ttk.Label(frame, image=logo)
logo_label.image = logo  # Prevent garbage collection
logo_label.pack(pady=10)

move = (0,200)

# Input Fields
ttk.Label(frame, text="Star Count:").pack(padx=move)
star_count_entry = ttk.Entry(frame)
star_count_entry.insert(0, "16")
star_count_entry.pack(padx=move,pady=(0, 10))

ttk.Label(frame, text="Max Planets per Star:").pack(padx=move)
max_planets_entry = ttk.Entry(frame)
max_planets_entry.insert(0, "20")
max_planets_entry.pack(padx=move,pady=(0, 10))

ttk.Label(frame, text="Terran Rarity (lower is more common):").pack(padx=move)
terran_rarity_entry = ttk.Entry(frame)
terran_rarity_entry.insert(0, "8")
terran_rarity_entry.pack(padx=move,pady=(0, 10))

ttk.Label(frame, text="Caseian Rarity (lower is more common):").pack(padx=move)
caseian_rarity_entry = ttk.Entry(frame)
caseian_rarity_entry.insert(0, "2")
caseian_rarity_entry.pack(padx=move,pady=(0, 10))

ttk.Label(frame, text="Galaxy Type (future feature):").pack(padx=move)
galaxy_type_var = tk.StringVar()
galaxy_type_dropdown = ttk.Combobox(frame, textvariable=galaxy_type_var, state="readonly")
galaxy_type_dropdown["values"] = ("Spiral", "Elliptical", "Irregular", "Clustered", "Amplified", "Insane")
galaxy_type_dropdown.current(0)
galaxy_type_dropdown.pack(padx=move,pady=(0, 20))

log_area.tag_config("caseian", foreground="#ff66cc", font=("Courier", 16, "bold"))

# Start and Progress
generate_button = ttk.Button(frame, text="Start Generation", command=start_generation_thread)
generate_button.pack(pady=(10, 10))

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(frame, length=350, variable=progress_var)
progress_bar.pack()

progress_label = ttk.Label(frame, text="Waiting to start...")
progress_label.pack()

progress_var2 = tk.IntVar()
progress_bar2 = ttk.Progressbar(frame, length=350, variable=progress_var2)
progress_bar2.pack()

progress_label2 = ttk.Label(frame, text="Waiting to start...")
progress_label2.pack()

root.mainloop()