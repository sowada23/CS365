import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os

# Load MNIST data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# normalize means all data would be in ragne between 0 to 1
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# Reshape data to add a channel dimension
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# define model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(32, (3, 3), strides = (1, 1), padding = 'same', activation = 'relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2), padding = 'same'))
model.add(tf.keras.layers.Conv2D(64, (3, 3), strides = (2, 2), padding = 'same', activation = 'relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2), padding = 'same'))
model.add(tf.keras.layers.Conv2D(128, (3, 3), strides = (2, 2), padding = 'same', activation = 'relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2), padding = 'valid'))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# compile model
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# train our model
# epoch means how many times deos the model see the same data
history = model.fit(x_train, y_train, epochs=1,validation_split=0.2)

# see the accuracy of the modelimport pandas as pdå
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
print(f"Loss: {loss:.2f}")

# save model
model.save(filepath='mnist_model.h5')
print("Model saved successfully.")

# 1) Prepare data
epochs      = range(1, len(history.history['loss']) + 1)
train_loss  = history.history['loss']
val_loss    = history.history['val_loss']
train_acc   = history.history['accuracy']
val_acc     = history.history['val_accuracy']

# 2) Ensure output directory exists
save_dir = './plot'
os.makedirs(save_dir, exist_ok=True)

# 3) Plot & save Loss
plt.figure(figsize=(8,5))
plt.plot(epochs, train_loss, 'o-', label='Train Loss')
plt.plot(epochs, val_loss,   's-', label='Val Loss')
plt.title('Model Loss over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.xticks(epochs)
plt.legend()
plt.grid(True)
loss_path = os.path.join(save_dir, 'loss_plot.png')
plt.savefig(loss_path, dpi=300, bbox_inches='tight')
print(f"Loss plot saved to {loss_path}")
plt.close()

# 4) Plot & save Accuracy
plt.figure(figsize=(8,5))
plt.plot(epochs, train_acc, 'o-', label='Train Accuracy')
plt.plot(epochs, val_acc,   's-', label='Val Accuracy')
plt.title('Model Accuracy over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.xticks(epochs)
plt.legend()
plt.grid(True)
acc_path = os.path.join(save_dir, 'accuracy_plot.png')
plt.savefig(acc_path, dpi=300, bbox_inches='tight')
print(f"Accuracy plot saved to {acc_path}")
plt.close()


# Make predictions on new images
input_dir = "./inputs"
for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)
    img = cv.imread(file_path, cv.IMREAD_GRAYSCALE)
    img = np.invert(np.array([img]))
    img = np.expand_dims(img, axis=-1)
    prediction = model.predict(img)
    print('-------------------')
    print("The predicted output is: ", np.argmax(prediction))
    print('-------------------')
    plt.imshow(img[0], cmap = plt.cm.binary)
    plt.show()
    
