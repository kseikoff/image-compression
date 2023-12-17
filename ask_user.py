import os

def ask_img_to_open(images:list):
    image_to_open = 0
    while not (0 < image_to_open <= len(images)):
        try:
            print("List of image names:")
            for image_path in images:
                print(os.path.basename(image_path))

            image_to_open = int(input("Enter image number (int) in range " + "1..." + str(len(images)) + ": "))
        except ValueError:
            pass

    return image_to_open

def ask_img_compr_val(dim:int):
    compr_val = 0
    while not (0 < compr_val <= dim):
        try:
            compr_val = int(input("Enter compression value (int) in range " + "1..." + str(dim) + ": "))
        except ValueError:
            pass
        
    return compr_val