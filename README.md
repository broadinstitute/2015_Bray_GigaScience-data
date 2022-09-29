# Bray GigaScience data

To reproduce the profiles in this repo, run the profiling-recipe. But run the following two steps to create metadata files and fix well position names

### Create metadata files
Install the conda environment in `create_metadata/environment.yml` and run the notebook `create_metadata.ipynb` to create all the metadata and platemap files.

### Fix well names
Use the same conda enviroment as above and run `fix_well_position.py` to change the well names from `a01` to `A01` in the aggregated profiles. Run the recipe only after fixing the names of the wells.
