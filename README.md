
---

# YOLO Spaceship Detection

This project trains a YOLOv8 model to detect Elite: Dangerous spaceships in a 3D environment and perform live detection on your screen.

Currently detects the rear profile of Anaconda, Cobra Mk III, Diamondback Explorer, and Python ships. 

Current iteration lacks variety in data so it's too overfitted to be useful, but you can find my dataset under Releases.

---
## **Usage**

### **Train the Model**
Run the training script:
```bash
python yolo_ships.py
```

### **Live Detection**
Put the created weight file `best.pt` into ready_models` or use the one I left there.

Run the live detection script:
```bash
python live_scan.py
```

---