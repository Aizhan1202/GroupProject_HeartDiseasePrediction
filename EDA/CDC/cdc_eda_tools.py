import pandas as pd

def is_diabetic_hemo(row):
    if row['LBXGH'] >= 6.5:
        return 1
    else:
        return 0

def merge_data_diabetes(df_one,df_two):
    df_merged = df_one.merge(right=df_two,on='SEQN',how='inner')
    df_merged['HasDiabetes'] = df_merged.apply(lambda row: is_diabetic_hemo(row), axis=1)
    return df_merged

def diabetes_corr(df_merged):
    correlation = df_merged.corr()
    return correlation['HasDiabetes'].abs().sort_values(ascending=False)