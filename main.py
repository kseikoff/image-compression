import ask_user
import img_utils

if __name__=="__main__":
    png_imgs = img_utils.get_image_paths(folder_path='images')
    img_to_open = ask_user.ask_img_to_open(png_imgs)
    compr_perc = ask_user.ask_img_compression_percentage()

    print("Please, wait...")
    img_path = png_imgs[img_to_open - 1]
    img = img_utils.read_image(img_path)
    compr_img = img_utils.compress_grayscale_img(img, compr_perc)
    
    save_path = img_utils.save_img(compr_img, img_path)
    if (save_path != None):
        print(f"Done! Check compressed image at path {save_path}")
    else:
        print("We're sorry, something went wrong")
