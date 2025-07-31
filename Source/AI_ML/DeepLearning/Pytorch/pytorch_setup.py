# Install dependencies
# Cuda Toolkit: https://developer.nvidia.com/cuda-toolkit
# Cuda installer: https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local
# Latest PyTorch: https://pytorch.org/get-started/locally/
# Torch using Pip: pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Import the dependencies
import torch

#Verify Torch
x = torch.rand(5, 3)
print(x)

#Verify Cuda
print("Cuda available: ", torch.cuda.is_available())
