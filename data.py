from idlelib.iomenu import encoding

import pandas as pd

dataFrame = pd.read_csv(
    'database/data.csv',
    encoding='latin1',
    delimiter=';')

def filter_nm_candidato(nm_candidato):
    results = dataFrame[dataFrame["NM_CANDIDATO"].str.contains(nm_candidato, case=False, na=False)]
    return results[['NR_CANDIDATO', 'NM_CANDIDATO', 'NM_URNA_CANDIDATO', "DS_CARGO", "NM_UE", 'NM_PARTIDO', 'SG_PARTIDO', 'SQ_CANDIDATO']]

def filter_nm_urna_candidato(nm_urna_candidato):
    results = dataFrame[dataFrame["NM_URNA_CANDIDATO"].str.contains(nm_urna_candidato, case=False, na=False)]
    return results[['NR_CANDIDATO', 'NM_CANDIDATO', 'NM_URNA_CANDIDATO', "DS_CARGO", "NM_UE", 'NM_PARTIDO', 'SG_PARTIDO', 'SQ_CANDIDATO']]

def filter_ds_cargo(ds_cargo):
    results = dataFrame[dataFrame["DS_CARGO"].str.contains(ds_cargo, case=False, na=False)]
    return results[["NR_CANDIDATO", "NM_CANDIDATO", "NM_URNA_CANDIDATO", "DS_CARGO", "NM_UE", "NM_PARTIDO", "SG_PARTIDO", "SQ_CANDIDATO"]]

def filter_sg_partido(sg_partido):
    results = dataFrame[dataFrame["SG_PARTIDO"] == sg_partido]
    return results[["NR_CANDIDATO", "NM_CANDIDATO", "NM_URNA_CANDIDATO", "DS_CARGO", "NM_UE", "NM_PARTIDO", "SG_PARTIDO", "SQ_CANDIDATO"]]

def filter_nm_partido(nm_partido):
    results = dataFrame[dataFrame["NM_PARTIDO"].str.contains(nm_partido, case=False, na=False)]
    return results[["NR_CANDIDATO", "NM_CANDIDATO", "NM_URNA_CANDIDATO", "DS_CARGO", "NM_UE", "NM_PARTIDO", "SG_PARTIDO", "SQ_CANDIDATO"]]

def filter_nr_candidato(nr_candidato):
    results = dataFrame[dataFrame["NR_CANDIDATO"] == nr_candidato]
    return results[["NR_CANDIDATO", "NM_CANDIDATO", "NM_URNA_CANDIDATO", "DS_CARGO", "NM_UE", "NM_PARTIDO", "SG_PARTIDO", "SQ_CANDIDATO"]]

def filter_nm_ue(nm_ue):
    results = dataFrame[dataFrame["NM_UE"].str.contains(nm_ue, case=False, na=False)]
    return results[["NR_CANDIDATO", "NM_CANDIDATO", "NM_URNA_CANDIDATO", "DS_CARGO", "NM_UE", "NM_PARTIDO", "SG_PARTIDO", "SQ_CANDIDATO"]]

def filter_sq_candidato(sq_candidato):
    results = dataFrame[dataFrame["SQ_CANDIDATO"] == sq_candidato]
    return results[["NR_CANDIDATO", "NM_CANDIDATO", "NM_URNA_CANDIDATO", "DS_CARGO", "NM_UE", "NM_PARTIDO", "SG_PARTIDO", "SQ_CANDIDATO"]]

def results_initial(number):
    return dataFrame.head(number)[["NR_CANDIDATO", "NM_CANDIDATO", "NM_URNA_CANDIDATO", "DS_CARGO", "NM_UE", "NM_PARTIDO", "SG_PARTIDO", "SQ_CANDIDATO"]]

redesFrame = pd.read_csv('database/redes.csv',
                         encoding='latin1',
                         delimiter=';')

def filter_media_sq_candidato(sq_candidato):
    results = redesFrame[redesFrame["SQ_CANDIDATO"] == sq_candidato]
    return results[['DS_URL']]

bensFrame = pd.read_csv('database/bens.csv',
                        encoding='latin1',
                        delimiter=';')


def find_bens_value(sq_candidato):
    result = bensFrame[bensFrame['SQ_CANDIDATO'] == sq_candidato]

    if (result.empty):
        return 0.0

    result['VR_BEM_CANDIDATO'] = result['VR_BEM_CANDIDATO'].str.replace(',', '.')
    total = result['VR_BEM_CANDIDATO'].astype(float).sum()

    return float(total)
