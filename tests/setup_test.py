'''
Tests the local setup, by checking if the imports of dependencies work.
'''
import importlib
import sys
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pydantic')


# List of core packages to check
main_dependencies = [
    "pip",
    "jupyter",
    "matplotlib",
    "torch",
    "torchvision",
    "timm",
    "torchmetrics",
    "wandb",
    "dotenv",
    "tqdm",
    "numpy",
    "pandas",
]

# check python version
print(f"\nPython version: {sys.version}\n")

# check dependencies
print("Checking environment dependencies...\n")

failed = []

for pkg in main_dependencies:
    try:
        # Try to import each package
        module = importlib.import_module(pkg)
        version = getattr(module, "__version__", "unknown")
        print(f"{pkg} - {version}")
    except Exception as e:
        # If there's an error, print the failure and the package name
        print(f"{pkg} - import failed: {e}")
        failed.append(pkg)

# Final message
print("\nLooks good!" if not failed else "\nIssues detected with:", failed)
