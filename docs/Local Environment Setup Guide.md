
## General Notes
I have reworked the setup and repo, so that it is now installable as a package and it can be easily converted into a library with poetry later.

The purpose of this setup is that our code is reproducible and that we all work with the same development environment locally.
### Prerequisites
- Conda installed
- pip installed
- VScode installed (in principal you can also use PyCharm, I've avoided IDE specific configs)
	- VScode extensions: Python, Jupyter (if you want to run notebooks locally)
	- For more useful extensions, see the Additional VScode extensions section


# Setup Steps

## 1. Clone the repository

`git clone https://github.com/NeuralSpiral/supervised-soup-project.git`

`cd supervised-soup-project`

---

## 2. Create a `.env` file

In the project root directory, create a file named `.env`:

`touch .env`

Edit the file and add the following lines:

`DATA_PATH=/home/username/path/to/dataset`

`RESULTS_PATH=results`

Notes:
- Look at the .env.example file for reference

- `DATA_PATH` should point to your local copy of the dataset. I recommend to keep it inside the repo in data, but it can be anywhere you want. 
- Because the data folder is in the gitignore in order to keep the repo size small, you need to download the dataset and put it in the specified path, if you want to use it locally.

---

## 3. Run the local setup script

Run the setup script to create the Conda environment and install dependencies:

`bash scripts/local_setup.sh`

This script will:

- Create the Conda environment (`supervised-soup-env`)
    
- Install all dependencies from `environment.yml`
    
- Install the CPU-only version of PyTorch to keep the local setup lighter
    

If successful, you should see: 

`Environment setup complete!`

---

## 4. Activate the environment

To activate the environment manually:

`conda activate supervised-soup-env`

---
## 5. Install as a package

To allow for clean imports, install our project as a local package with:

`pip install -e .`

You can check if the package is installed by running:

`pip show supervised_soup`

---

## 5. Test the setup

Verify the setup by running:

`python tests/setup_test.py`

Everything should work if you see:

`"Looks good."`

---

## 6. Open in VS Code

In the project root, open VS Code:

`code .`

Then select  our conda environment `supervised-soup-env` as your Python interpreter.


---
---

## Note on Colab

For training in Colab:
- The Colab setup cell will install the same dependencies, except that torch and torchvision will have the default GPU version for training.

For setting up a new colab notebook see the colab_setup.ipynb




## Updating, deactivating and removing the environment

If the dependencies in yml have changed, run locally inside the active cond environment from the repo root:
`conda env update -f environment.yml --prune`

To deactivate run:
`conda deactivate`

To remove the environment:
`conda env remove -n supervised-soup-env`

## Additional VScode extensions
- Pylance (linter)
- GitLens

## Sources
- https://goodresearch.dev/

- https://chanind.github.io/2023/06/04/academics-open-source-research-code-python-tips.html