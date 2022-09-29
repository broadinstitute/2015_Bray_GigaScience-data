import pandas as pd

barcode_platemap = pd.read_csv('metadata/platemaps/CDRP/barcode_platemap.csv')

for plate in barcode_platemap.Assay_Plate_Barcode.unique():
    print(f'fixing plate {plate}')
    df = pd.read_csv(f'profiles/CDRP/{plate}/{plate}.csv.gz')
    df['Metadata_Well'] = df['Metadata_Well'].str.upper()
    df.to_csv(f'profiles/CDRP/{plate}/{plate}.csv.gz', index=False, compression='gzip', float_format="%.5g")
