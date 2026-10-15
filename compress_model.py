
import joblib
import os

# Original model file
input_file = "Model_Pipeline.pkl"

# Compressed model file
output_file = "Model_Pipeline_compressed.pkl"

print("Original size:",
      round(os.path.getsize(input_file) / (1024 * 1024), 2), "MB")

# Load the trained pipeline
model = joblib.load(input_file)

# Save it with compression
joblib.dump(model, output_file, compress=3)

print("Compressed size:",
      round(os.path.getsize(output_file) / (1024 * 1024), 2), "MB")

print("Compression completed!")
