from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator

# Define the data directories
train_dir = r'C:\Users\Sahal\FLOWERS RECOGNITION\training_set'
validation_dir = r'C:\Users\Sahal\FLOWERS RECOGNITION\test_set'

# Define hyperparameters
batch_size = 32
epochs = 10
image_size = (224, 224)

# Create a data generator with data augmentation for the training set
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,  # Rescale pixel values to [0, 1]
    rotation_range=20,   # Randomly rotate images
    width_shift_range=0.2,  # Randomly shift images horizontally
    height_shift_range=0.2,  # Randomly shift images vertically
    horizontal_flip=True,   # Randomly flip images horizontally
    shear_range=0.2,        # Apply shear transformations
    zoom_range=0.2,         # Randomly zoom into images
    fill_mode='nearest'     # Fill in missing pixels with the nearest value
)

# Create a data generator for the validation set (no augmentation)
validation_datagen = ImageDataGenerator(rescale=1.0/255.0)

# Load and prepare the training dataset
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical'
)

# Load and prepare the validation dataset
validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical'
)

# Build a simple convolutional neural network (CNN) model
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(5, activation='softmax')  # Adjust the output units to match the number of flower classes
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

# Save the trained model
model.save('flower_classification_model.h5')
