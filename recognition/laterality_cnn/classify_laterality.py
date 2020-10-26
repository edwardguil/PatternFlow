import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
import os
import random
import glob

#Specify directory of data
data_dir = os.path.join("C:", "Users", "delic", ".keras", "datasets", "AKOA_Analysis")

#Split the dataset - 20% validation, 80% training
batch_size = 32
img_height = 228
img_width = 260

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    labels = 'inferred',
    validation_split=0.2,
    subset='training',
    seed=111,
    image_size = (img_height, img_width),
    batch_size = batch_size,
    color_mode = 'grayscale'
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    labels = 'inferred',
    validation_split=0.2,
    subset='validation',
    seed=111,
    image_size = (img_height, img_width),
    batch_size = batch_size,
    color_mode = 'grayscale'
)

class_names = train_ds.class_names

# #Visualise data
# plt.figure(figsize=(10, 10))
# for images, labels in train_ds.take(1):
#   for i in range(9):
#     ax = plt.subplot(3, 3, i + 1)
#     plt.imshow(images[i].numpy().astype("uint8")[:,:,0])
#     plt.title(class_names[labels[i]])
#     plt.axis("off")
# plt.show()

# for image_batch, labels_batch in train_ds:
#     print(image_batch.shape)
#     print(np.min(image_batch[0]), np.max(image_batch[0]))
#     print(labels_batch.shape)
#     break

#Standardize the data
normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)

#Configure dataset for performance
AUTOTUNE = tf.data.experimental.AUTOTUNE
train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# checkpoint_path = "training/ckpt01.ckpt"
# checkpoint_dir = os.path.dirname(checkpoint_path)

# n_epochs = 200

# cp_callback = tf.keras.callbacks.ModelCheckpoint(
#     filepath=checkpoint_path,
#     save_weights_only=True,
#     verbose=1,
#     save_freq=n_epochs*X_train.shape[0]
# )

# #Specify directory of data
# data_dir = os.path.join("C:", "Users", "delic", ".keras", "datasets", "AKOA_Analysis")

# #Load all the filenames
# filenames = glob.glob(data_dir + '/*/*.png')
# image_count = len(filenames)

# #Split the dataset - 20% validation, 80% training
# batch_size = 32
# img_height = 228
# img_width = 260
# random.shuffle(filenames)
# val_size = int(image_count * 0.2)
# val_images = filenames[:val_size]
# train_images = filenames [val_size:]

# #Extract labels
# train_labels = [fn.split(os.path.sep)[-2] for fn in train_images]
# val_labels = [fn.split(os.path.sep)[-2] for fn in val_images]

# class_names = sorted(set(train_labels))

# #Create tensorflow datasets
# train_ds = tf.data.Dataset.from_tensor_slices((train_images, train_labels))
# val_ds = tf.data.Dataset.from_tensor_slices((val_images, val_labels))

# train_ds = train_ds.shuffle(len(train_images))
# val_ds = val_ds.shuffle(len(val_images))

# #Map filenames and labels to data arrays
# def map_fn(filename, label):
#     # Load the raw data from the file as a string.
#     img = tf.io.read_file(filename)
#     # Convert the compressed string to a 3D uint8 tensor.
#     img = tf.image.decode_jpeg(img, channels=1) # channels=3 for RGB, channels=1 for grayscale
#     # Resize the image to the desired size.
#     img = tf.image.resize(img, (img_height, img_width))
#     # Standardise values to be in the [0, 1] range.
#     img = tf.cast(img, tf.float32) / 255.0
#     # One-hot encode the label.
#     one_hot = tf.cast(label == class_names, tf.uint8)
#     # Return the processed image and label.
#     return img, one_hot

# train_ds = train_ds.map(map_fn)
# val_ds = val_ds.map(map_fn)

# #Visualise data
# image_batch, label_batch = next(iter(train_ds.batch(9)))

# plt.figure(figsize=(10, 10))
# for i in range(9):
#     plt.subplot(3, 3, i+1)
#     plt.imshow(image_batch[i][:,:,0])
#     label = tf.argmax(label_batch[i])
#     plt.title(class_names[label])
#     plt.axis('off')
# plt.show()
