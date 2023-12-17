from PIL import Image
import numpy as np
import os
import glob

img_extensions = ('png', 'jpg', 'jpeg', 'webp', 'bmp')

def get_image_paths(folder_path: str):
    full_path = os.path.join(os.getcwd(), folder_path)

    image_paths = []
    for ext in img_extensions:
        image_paths.extend(glob.glob(os.path.join(full_path, '*.' + ext)))

    return image_paths

def read_image(path:str):
    return Image.open(path)

def save_img(img:Image, path:str):
    path_to_save = path.replace("images", "compr_images")
    img.convert('RGB').save(path_to_save)
    return path_to_save

def compress_grayscale_img(img:Image, compr_perc:int):
    gray_img_arr = np.asarray(img.convert('L'))
    U, S, V = np.linalg.svd(gray_img_arr)

    dim_S = S.shape[0]
    compr_val = dim_S - int(dim_S * (compr_perc / 100))

    return Image.fromarray(np.matrix(U[:, :compr_val]) * np.diag(S[:compr_val]) * np.matrix(V[:compr_val, :]))
