'''
One-time fix for all the class IDs because I messed up stuff one time. 
But this just makes sure that all the class IDs are correct,
assuming everything is in the correct directory.
'''

import os

# Paths to the directories containing images and labels together
directories = [
    "yolo_dataset/anaconda",
    "yolo_dataset/cobra_mk3",
    "yolo_dataset/diamondback_explorer",
    "yolo_dataset/python",
]

# Mapping of directories to class IDs
class_mapping = {
    "anaconda": "0",
    "cobra_mk3": "1",
    "diamondback_explorer": "2",
    "python": "3",
}

def fix_labels(directory, class_id):
    # Iterate through all files in the directory
    for file in os.listdir(directory):
        if file.endswith((".jpg", ".png")):  # Check if it's an image file
            # Get the corresponding label file
            label_file = os.path.splitext(file)[0] + ".txt"
            label_path = os.path.join(directory, label_file)

            # If the label file doesn't exist, create an empty one
            if not os.path.exists(label_path):
                with open(label_path, "w") as f:
                    pass  # Create an empty file
                print(f"Created empty label file: {label_path}")
            else:
                # If the label file exists, set all class IDs to the correct class ID
                with open(label_path, "r") as f:
                    lines = f.readlines()

                fixed_lines = []
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) > 0:
                        parts[0] = class_id  # Set the class ID to the correct value
                        fixed_lines.append(" ".join(parts))

                # Write the fixed labels back to the file
                with open(label_path, "w") as f:
                    f.write("\n".join(fixed_lines))
                print(f"Fixed labels in: {label_path}")

# Process all directories
for directory in directories:
    # Extract the class name from the directory path
    class_name = os.path.basename(directory)
    if class_name in class_mapping:
        fix_labels(directory, class_mapping[class_name])

print("All label files processed. Class IDs corrected.")