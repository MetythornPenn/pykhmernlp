# import os
# import argparse
# #
# from utils import VOCAB
# from networks import JAWSModel
# from datasets import build_dataset


# parser = argparse.ArgumentParser(description='Run the training loop.')
# parser.add_argument('config', type=str, help='Path to config file.', default="./configs/config.gat.json")
# parser.add_argument('dataset_path', type=str,
#                     default="./dataset.txt",
#                     help='Path to dataset. (text file if of type khpos or directory if of type phylypo)')
# parser.add_argument('--output_dir', type=str,
#                     default="./output",
#                     help='Path to output directory.')
# parser.add_argument('--dataset_type', type=str,
#                     help='The type of dataset to use',
#                     default="khpos",
#                     choices=['khpos', 'phylypo'])
# parser.add_argument('--lr', type=float,
#                     help='The learning rate',
#                     default=0.01)
# parser.add_argument('--early_stopping_patience', type=int,
#                     help='The learning rate',
#                     default=10)
# parser.add_argument('--epochs', type=int,
#                     help='The number of epochs to train',
#                     default=None)
# args = parser.parse_args()


# dataset = build_dataset(
#     args.dataset_path,
#     args.dataset_type
# )


# model = JAWSModel(args.config)

# model.fit(
#     data=dataset,
#     epochs=args.epochs,
#     learning_rate=args.lr,
#     model_temp_dir=args.output_dir,
#     early_stopping_patience=args.early_stopping_patience,
# )

# output_filename = os.path.basename(args.config).replace(".json",  ".pt")
# model.save(os.path.join(args.output_dir, output_filename))


import os
from utils import VOCAB
from networks import JAWSModel
from datasets import build_dataset

import torch

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")  # Use GPU
    print("CUDA is available. Using GPU.")
else:
    device = torch.device("cpu")   # Use CPU
    print("CUDA is not available. Using CPU.")

# Now, you can use `device` to move tensors and models to the selected device.


# Define your parameters directly
config = "./configs/config.gat.json"
dataset_path = "./dataset.txt"
output_dir = "./output"
dataset_type = "khpos"  # or "phylypo"
lr = 0.01
early_stopping_patience = 10
epochs = None

# Build dataset
dataset = build_dataset(dataset_path, dataset_type)

# Initialize model
model = JAWSModel(config)

# Train the model
model.fit(
    data=dataset,
    epochs=epochs,
    learning_rate=lr,
    model_temp_dir=output_dir,
    early_stopping_patience=early_stopping_patience,
)

# Save the trained model
output_filename = os.path.basename(config).replace(".json",  ".pt")
model.save(os.path.join(output_dir, output_filename))
