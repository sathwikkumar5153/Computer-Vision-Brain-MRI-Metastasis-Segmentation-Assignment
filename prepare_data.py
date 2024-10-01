import os
import shutil
from sklearn.model_selection import train_test_split

def prepare_dataset(data_dir, train_dir, test_dir, test_size=0.2):
    # Filter out the __MACOSX directory and any other hidden files
    image_files = [f for f in os.listdir(data_dir) 
                   if not f.startswith('.') and 
                   not f.endswith('_mask.tif') and
                   os.path.isfile(os.path.join(data_dir, f))]
    
    train_files, test_files = train_test_split(image_files, test_size=test_size, random_state=42)
    
    for file_list, target_dir in [(train_files, train_dir), (test_files, test_dir)]:
        for file in file_list:
            try:
                shutil.copy(os.path.join(data_dir, file), os.path.join(target_dir, file))
                mask_file = file.replace('.tif', '_mask.tif')
                if os.path.exists(os.path.join(data_dir, mask_file)):
                    shutil.copy(os.path.join(data_dir, mask_file), os.path.join(target_dir, mask_file))
            except PermissionError:
                print(f"Permission denied when trying to copy {file}. Skipping this file.")
            except FileNotFoundError:
                print(f"File {file} or its mask not found. Skipping this file.")

if __name__ == '__main__':
    data_dir = 'data'
    train_dir = 'data/train'
    test_dir = 'data/test'
    
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    
    prepare_dataset(data_dir, train_dir, test_dir)