# Bray GigaScience data

## Download the data
- Clone the repo.

```bash
git clone https://github.com/broadinstitute/2015_Bray_GigaScience-data.git
```

- Install [DVC](https://dvc.org/) and [Git LFS](https://git-lfs.com/).

- Download the files on Git LFS.

```bash
git lfs pull
```

- Download the profiles from S3.

```bash
dvc pull
```

## Re-generate the data

To reproduce the profiles in this repo, run the profiling-recipe. But run the following two steps to create metadata files and fix well position names

### Create metadata files
Install the conda environment in `create_metadata/environment.yml` and run the notebook `create_metadata.ipynb` to create all the metadata and platemap files.

### Fix well names
Use the same conda enviroment as above and run `fix_well_position.py` to change the well names from `a01` to `A01` in the aggregated profiles. Run the recipe only after fixing the names of the wells.

### Notes
`quality_control` step was not run because the `load_data.csv.gz` files did not have the column `Metadata_Row`. This column could be created and the `quality_control` step can be run later.

