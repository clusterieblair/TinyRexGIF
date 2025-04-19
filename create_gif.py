import imageio.v2 as imageio
import os

folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "GIF")

image_files = [f for f in os.listdir(folder_path) if f.startswith("dino") and f.endswith(".png")]

image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

image_paths = [os.path.join(folder_path, file) for file in image_files]

output_path = os.path.join(os.path.expanduser("~"), "Desktop", "my_dino_animation.gif")

with imageio.get_writer(output_path, mode='I', duration=0.3, loop=10) as writer:
    for filename in image_paths:
        image = imageio.imread(filename)
        writer.append_data(image)

print(f"Dino GIF created at: {output_path}")