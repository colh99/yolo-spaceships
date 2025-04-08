'''
Used to turn the dataset into train and validation sets.
'''

import os
import shutil
import random

# Paths
base_dir = "yolo_dataset"
output_dir = "yolo_dataset_split"
classes = ["anaconda", "cobra_mk3", "diamondback_explorer", "python"]
train_ratio = 0.8  # 80% training, 20% validation

# Create output directories
for split in ["train", "val"]:
    for subdir in ["images", "labels"]:
        os.makedirs(os.path.join(output_dir, split, subdir), exist_ok=True)

# Split dataset
for cls in classes:
    class_dir = os.path.join(base_dir, cls)
    images = [f for f in os.listdir(class_dir) if f.endswith((".jpg", ".png"))]

    random.shuffle(images)
    split_idx = int(len(images) * train_ratio)
    train_images = images[:split_idx]
    val_images = images[split_idx:]

    for split, split_images in [("train", train_images), ("val", val_images)]:
        for image in split_images:
            # Copy image
            src_image_path = os.path.join(class_dir, image)
            dest_image_path = os.path.join(output_dir, split, "images", image)
            shutil.copy(src_image_path, dest_image_path)

            # Copy corresponding label
            label_file = image.rsplit(".", 1)[0] + ".txt"
            src_label_path = os.path.join(class_dir, label_file)
            dest_label_path = os.path.join(output_dir, split, "labels", label_file)
            if os.path.exists(src_label_path):
                shutil.copy(src_label_path, dest_label_path)

print(f"Dataset split completed. Train and validation sets are in '{output_dir}'.")