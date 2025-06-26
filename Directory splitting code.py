import os
import shutil
from sklearn.model_selection import train_test_split
def create_dirs(base_dir, dirs):
for d in dirs:
os.makedirs(os.path.join(base_dir, d), exist_ok=True)
def split_data(SOURCE, TRAINING, TESTING, VALIDATION, split_size):
all_files = os.listdir(SOURCE)
all_files = [os.path.join(SOURCE, f) for f in all_files if
os.path.isfile(os.path.join(SOURCE, f))]
train_files, temp_files = train_test_split(all_files, test_size=split_size[0] + split_size[1])
val_files, test_files = train_test_split(temp_files, test_size=split_size[1] / (split_size[0] +split_size[1]))
for file in train_files:
shutil.move(file, TRAINING)
for file in val_files:
shutil.move(file, VALIDATION)
for file in test_files:
shutil.move(file, TESTING)
# Paths to the original directories
source_dir = 'train1' categories = ['Real', 'Hard']
# Create new directories
base_dir = 'Data' train_dir = os.path.join(base_dir, 'Train')
val_dir = os.path.join(base_dir, 'Val')
test_dir = os.path.join(base_dir, 'Test')
# Create category directories within train, validation, and test
for category in categories:
create_dirs(train_dir, [category])
create_dirs(val_dir, [category])
create_dirs(test_dir, [category])
# Define split sizes: [validation size, test size]
split_size = [0.2, 0.1]
# Split data
for category in categories:
source_path = os.path.join(source_dir, category)
train_path = os.path.join(train_dir, category)
val_path = os.path.join(val_dir, category)
test_path = os.path.join(test_dir, category)
split_data(source_path, train_path, test_path, val_path, split_size)
print('Data splitting completed.')
