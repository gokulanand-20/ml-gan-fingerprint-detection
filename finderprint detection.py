import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
train_dir = 'Data/Train' val_dir = 'Data/Val' IMG_SIZE = (224, 224)
BATCH_SIZE = 32
train_datagen = ImageDataGenerator(
rescale=1.0 / 255.0, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest' )
val_datagen = ImageDataGenerator(rescale=1.0 / 255.0)
train_gen = train_datagen.flow_from_directory(
train_dir, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='categorical' )
val_gen = val_datagen.flow_from_directory(
val_dir, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='categorical' )
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(train_gen.num_classes, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)
for layer in base_model.layers:
layer.trainable = False
model.compile(optimizer=Adam(learning_rate=1e-4),loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(
train_gen, validation_data=val_gen, epochs=2, steps_per_epoch=train_gen.samples // BATCH_SIZE, validation_steps=val_gen.samples // BATCH_SIZE
)
model.save('vgg16_finetuned.h5')
def predict_image(image_path):
img = tf.keras.preprocessing.image.load_img(image_path, target_size=IMG_SIZE)
img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch
prediction = model.predict(img_array)
class_idx = tf.argmax(prediction[0])
class_label = list(train_gen.class_indices.keys())[class_idx]
print(f"Image {image_path} is classified as: {class_label}")
predict_image(r'Real\466__F_Left_thumb_finger.BMP')
