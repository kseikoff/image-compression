from PIL import Image
import numpy as np
import ask_user
import img_utils

if __name__=="__main__":
    png_imgs = img_utils.get_image_paths(folder_path='images')
    img_to_open = ask_user.ask_img_to_open(png_imgs)

    print("Please, wait...")
    gray_img_arr = np.asarray(Image.open(png_imgs[img_to_open - 1]).convert('L'))
    U, S, V = svd_gray_img_arr = np.linalg.svd(gray_img_arr)
    dim_S = S.shape[0]

    compr_val = ask_user.ask_img_compr_val(dim_S)
    compr_img = np.matrix(U[:, :compr_val]) * np.diag(S[:compr_val]) * np.matrix(V[:compr_val, :])

    # using 'np.uint8(compr_img)' instead of 'convert(par)' causes some pixels to be missing
    reconst_img = Image.fromarray(compr_img).convert('L')
    
    path_to_save = png_imgs[img_to_open - 1].replace("images", "compr_images")
    reconst_img.save(path_to_save)
    print("Done! Check compressed image at path " + path_to_save)
