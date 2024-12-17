import os
import shutil
from sklearn.model_selection import train_test_split

# Define the dataset directory and subdirectories
dataset_dir = r'C:\Users\Hamza\Desktop\Deep Learning\Annotations YOLO format'
images_dir = os.path.join(dataset_dir, 'images')
labels_dir = os.path.join(dataset_dir, 'labels')

# Create lists of image and label file paths
images = [os.path.join(images_dir, f) for f in os.listdir(images_dir)]
labels = [os.path.join(labels_dir, f) for f in os.listdir(labels_dir)]

# Pair images with their corresponding labels
paired_files = list(zip(images, labels))

# Shuffle and split the dataset into training and validation sets
train_files, val_files = train_test_split(paired_files, test_size=0.2, random_state=42)

# Function to move files to their respective directories
def move_files(file_list, subset):
    for img_path, lbl_path in file_list:
        # Define the destination directories
        dest_img_dir = os.path.join(dataset_dir, subset, 'images')
        dest_lbl_dir = os.path.join(dataset_dir, subset, 'labels')
        
        # Create destination directories if they don't exist
        os.makedirs(dest_img_dir, exist_ok=True)
        os.makedirs(dest_lbl_dir, exist_ok=True)

        # Move the files
        shutil.move(img_path, os.path.join(dest_img_dir, os.path.basename(img_path)))
        shutil.move(lbl_path, os.path.join(dest_lbl_dir, os.path.basename(lbl_path)))

# Move the files to the train and validation directories
move_files(train_files, 'train')
move_files(val_files, 'val')

print("Dataset successfully split into training and validation sets.")
