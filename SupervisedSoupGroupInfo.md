## Toolstack
Jira
Github
Colab
VScode
## Repo structure
#### Data
Since the ImagNetSubset is over 1 GB, I have added it to the gitignore, to keep the repo size small.
We will host the ImageNetSubset for training on google drive.
We can also upload the images for the final test set here.

#### Notebooks
In the notebooks folder we can save our colab notebooks.
I have added a colab_setup notebook that contains code to setup each notebook (git integration, paths, dependencies).

#### src
The src folder is for our main, stable and reusable code (e.g. dataloader, model and training logic)
That way we can keep our code modular and import what we need to the notebooks.
#### Requirements
In requirements.txt we will track our dependencies.

## Suggested workflow with git
I would suggest that whenever we work on something new, we do so on a separate branch and before we merge the other 2 review the code.
## Team links
github
colab
jira
confluence
resources website