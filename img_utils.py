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

# using 'np.uint8(img)' causes some pixels to be missing
def save_img(img:Image, path:str, convert_to:str):
    img.convert(convert_to).save(path)

def calc_compr_val(dim:int, compr_perc:int):
    return dim - int(dim * (compr_perc / 100))

def get_compressed_svd(img:Image, compr_perc:int):
    img_arr = np.asarray(img)
    return get_compressed_svd(img_arr, compr_perc)

def get_compressed_svd(arr:list, compr_perc:int):
    U, S, V = np.linalg.svd(arr)

    compr_val = calc_compr_val(dim=S.shape[0], compr_perc=compr_perc)

    return U[:, :compr_val], S[:compr_val], V[:compr_val, :]

def compress_grayscale_img(img:Image, compr_perc:int):
    grayscale_img = img.convert('L')
    U_compr, S_compr, V_compr = get_compressed_svd(grayscale_img, compr_perc)

    return Image.fromarray(np.matrix(U_compr) * np.diag(S_compr) * np.matrix(V_compr))

def compress_rgb_img(img:Image, compr_perc:int):
    red_img_arr = np.array(img)[:, :, 0]
    green_img_arr = np.array(img)[:, :, 1]
    blue_img_arr = np.array(img)[:, :, 2]

    U_r_compr, S_r_compr, V_r_compr = get_compressed_svd(red_img_arr, compr_perc)
    U_g_compr, S_g_compr, V_g_compr = get_compressed_svd(green_img_arr, compr_perc)
    U_b_compr, S_b_compr, V_b_compr = get_compressed_svd(blue_img_arr, compr_perc)

    red_img_arr_compr = np.matrix(U_r_compr) * np.diag(S_r_compr) * np.matrix(V_r_compr)
    green_img_arr_compr = np.matrix(U_g_compr) * np.diag(S_g_compr) * np.matrix(V_g_compr)
    blue_img_arr_compr = np.matrix(U_b_compr) * np.diag(S_b_compr) * np.matrix(V_b_compr)

    rgb_compr_img_arr = np.zeros((np.array(img).shape[0], np.array(img).shape[1], 3))
    rgb_compr_img_arr[:, :, 0] = red_img_arr_compr
    rgb_compr_img_arr[:, :, 1] = green_img_arr_compr
    rgb_compr_img_arr[:, :, 2] = blue_img_arr_compr
    rgb_compr_img_arr = np.clip(rgb_compr_img_arr, 0, 255)
    rgb_compr_img_arr = np.around(rgb_compr_img_arr).astype(int)

    return Image.fromarray(rgb_compr_img_arr.astype(np.uint8))