#!/usr/bin/env bash
# Local environment setup script

set -e

ENV_NAME="supervised-soup-env"
YML_FILE="environment.yml"

echo "Setting up local environment: $ENV_NAME"

# check if conda is installed
if ! command -v conda &> /dev/null; then
  echo "Conda not found. Please install it."
  exit 1
fi

# create environment
echo "Creating conda environment from $YML_FILE..."
conda env create -f "$YML_FILE"

echo "Activating environment..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"

# install the CPU-only PyTorch to avoid unnecessary large CUDA files
echo "Installing CPU-only PyTorch ..."
pip install torch==2.8.0+cpu torchvision==0.23.0+cpu \
  --index-url https://download.pytorch.org/whl/cpu

# verify installation
echo "Verifying installation..."
python -c "import torch, torchvision; print('Torch:', torch.__version__, '| Torchvision:', torchvision.__version__)"

echo "Environment setup complete."
