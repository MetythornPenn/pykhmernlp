# import argparse
# #
# from utils import preprocess_phylypo_sample
# from networks import JAWSModel

# parser = argparse.ArgumentParser(
#     description='Run the segmentation on one sample text file.')
# parser.add_argument('config', type=str, help='Path to config file.')
# parser.add_argument('model_path', type=str, help='Path to model weight file.')
# parser.add_argument('sample', type=str,
#                     help='Path to the input text file containing the text to segment.')

# args = parser.parse_args()

# model = JAWSModel(args.config)
# model.load(args.model_path)

# with open(args.sample, 'r') as input_file:
#     preprocessed, _ = preprocess_phylypo_sample(input_file.read())
#     out = model.segment(preprocessed)

# with open(args.sample.replace(".txt", ".seg.txt"), "w") as outfile:
#     outfile.write(out)
from utils import preprocess_khpos_sample
from networks import JAWSModel

# Define your parameters directly
config = "./configs/config.gat.json"
# model_path = "./output/best_weights.pt"
model_path = "./pretrained/best_weights.gat.pt"
sample_path = "./sample.txt"

# Load the model
model = JAWSModel(config)
model.load(model_path)

# Read the sample text
with open(sample_path, 'r', encoding='utf-8') as input_file:
    preprocessed, _ = preprocess_khpos_sample(input_file.read())
    out = model.segment(preprocessed)

# Write the segmented output to a file
with open(sample_path.replace(".txt", ".seg.txt"), "w", encoding='utf-8') as outfile:
    outfile.write(out)
