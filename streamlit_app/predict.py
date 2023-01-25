import pickle
import pandas as pd
from joblib import dump, load


# 2021 preds 

# Results dict
f = open('../data/result_2021_dic.pkl', 'rb')
results_2021 = pickle.load(f)
f.close()


df_results = pd.DataFrame.from_dict({(i,j,k): results_2021[i][j][k]
                           for i in results_2021.keys() 
                           for j in results_2021[i].keys()
                            for k in results_2021[i][j].keys()},
                       orient='index', columns=['valeur']).reset_index()
df_results['modele'] = df_results['index'].apply(lambda x: x[0])
df_results['metric'] = df_results['index'].apply(lambda x: x[1])
df_results['nb_var'] = df_results['index'].apply(lambda x: x[2])



# Exemples predictions


ex_acc = pd.read_csv("../data/Ex_accidents_streamlit_v2.csv", index_col=0)
buffer = pd.read_csv("../data/ex_accident_buffer.csv", index_col=0)


# Dataframe with main accident and buffer accidents for map
data_map1 = ex_acc[['Num_Acc','lat','long','accident_grave']].rename({'Num_Acc':'Num_Acc_analyse'}, axis = 1)
data_map1['Num_Acc'] = ex_acc.Num_Acc

data_map2 = buffer.rename({'Num_Acc_left':'Num_Acc_analyse',
                          'Num_Acc_right':'Num_Acc',
                          'lat_right':'lat',
                          'long_right':'long',
                          'accident_grave_right':'accident_grave'}, axis = 1)

data_map = pd.concat([data_map1, data_map2], axis=0)

for i, num in enumerate(set(data_map.Num_Acc_analyse)):
    data_map['Num_Acc_analyse'] = data_map['Num_Acc_analyse'].replace(num, i)
    ex_acc['Num_Acc'] = ex_acc['Num_Acc'].replace(num, i)
    

## Affichage des features

df = ex_acc.set_index('Num_Acc')[[
    "densité_dep_pop",
    "accident_grave_right",
    "agg_in",
    "circ_2",
    "choc_impact_Arriere",
    "catv_poids_B: 0.15-1.5T",
    "obs",
    "presence_pers_agee",
    "lum_jour",
    "catv_poids_E: >7.5T",
    "atm_précipitations",
    "int_out",
    "nbv_0_à_4",
    "plan_1.0",
    "presence_ado",
    "int_giratoire-place",
    "prof_1",
    "prof_3",
    "plan_4.0",
    "prof_4",
    "atm_contrast_lum-autre",
    "choc_impact_Multiple",
    "infra_aménagement",
    "atm_perturb_air",
]].rename({'plan_1.0':'plan_1', 'plan_4.0':'plan_4'})

for col in df.columns :
    if col != "accident_grave_right":
        df[col] = df[col].apply(round).astype('str')
    else:
        df[col] = df[col].apply(lambda x : f'{x:.2%}').astype('str')

var_acc = {}
for acc in df.index:
    var_acc[acc] = df.loc[df.index==int(acc)].transpose()






# Personnalized predictions 

gbc = load('../data/gbc.joblib')
rf = load('../data/rf.joblib')


scale = pd.read_csv("../data/param_scale.csv", index_col=0)
