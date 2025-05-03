# Handwritten Digit Classification with CNN (MNIST)

## Overview

This project trains a convolutional neural network (CNN) on the MNIST dataset to classify handwritten digits (0–9).
It includes:

* Data loading & preprocessing
* Model definition, training & evaluation
* Loss & accuracy plotting
* Saving the trained model
* Predicting on custom input images

---

## 📦 Project Structure

```
.
├── main.py
├── mnist_model.h5        # saved Keras model
├── loss_plot.png         # training & validation loss over epochs
├── accuracy_plot.png     # training & validation accuracy over epochs
├── inputs/               # folder for custom input images
│   └── *.png / *.jpg
└── README.md
```

---

## 🛠️ Requirements

* Python 3.7+
* TensorFlow 2.x
* NumPy
* OpenCV (`cv2`)
* Matplotlib

Install via:

```bash
pip install tensorflow numpy opencv-python matplotlib
```

---

## 🚀 Usage

1. **Train & evaluate**

   ```bash
   python main.py
   ```

   * Trains for 20 epochs (with 20% validation split).
   * Prints final test accuracy & loss.
   * Saves model as `mnist_model.h5`.
   * Plots & displays per-epoch loss and accuracy.
   * Runs predictions on images in `./inputs`.

2. **View saved plots**

   * `loss_plot.png`
   * `accuracy_plot.png`

3. **Predict on new images**

   * Drop your grayscale digit images into `inputs/`
   * Run `main.py` again to see model outputs and sample plots.

---

## 📊 Training Results

* **Final Test Accuracy:** 0.98
* **Final Test Loss:** 0.05

| Epoch | Train Loss | Val Loss | Train Acc | Val Acc |
| :---: | :--------: | :------: | :-------: | :-----: |
|   1   |   0.5687   |  0.1056  |   0.8124  |  0.9664 |
|   …   |      …     |     …    |     …     |    …    |
|   20  |   0.0356   |  0.0645  |   0.9891  |  0.9832 |

*(See `loss_plot.png` & `accuracy_plot.png` for full curves.)*

---

## 📈 Plots

![Loss Plot](loss_plot.png)
*Model Loss over 20 Epochs*

![Accuracy Plot](accuracy_plot.png)
*Model Accuracy over 20 Epochs*

---

## 🔮 Future Work

* Experiment with deeper / residual architectures
* Add data augmentation (rotations, shifts, noise)
* Wrap into a web demo/API for real-time digit drawing

---

## 📝 License

MIT © 2025 Sora Owada
