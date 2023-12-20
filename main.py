import ask_user
import img_utils

folder_path = "images"
compr_folder_path = "compr_images"

if __name__=="__main__":
    png_imgs = img_utils.get_image_paths(folder_path)
    img_to_open = ask_user.ask_img_to_open(png_imgs)
    compr_perc = ask_user.ask_img_compression_percentage()

    print("Please, wait...")
    img_path = png_imgs[img_to_open - 1]
    img = img_utils.read_image(img_path)
    compr_img = img_utils.compress_rgb_img(img, compr_perc)
    
    save_path = img_path.replace(folder_path, compr_folder_path)
    img_utils.save_img(compr_img, save_path, convert_to='RGB')
    print(f"Done! Check compressed image at path {save_path}")
