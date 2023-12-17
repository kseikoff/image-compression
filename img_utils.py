import os
import glob

img_extensions = ('png', 'jpg', 'jpeg')

def get_image_paths(folder_path: str):
    full_path = os.path.join(os.getcwd(), folder_path)

    image_paths = []
    for ext in img_extensions:
        image_paths.extend(glob.glob(os.path.join(full_path, '*.' + ext)))

    return image_paths
