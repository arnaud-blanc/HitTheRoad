import pandas as pd

# liste des variables triées selon leur importance dans le modèle GBC
liste_var_tri_GBC = [
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
    "plan_1",
    "presence_ado",
    "int_giratoire-place",
    "prof_1",
    "prof_3",
    "plan_4",
    "prof_4",
    "atm_contrast_lum-autre",
    "choc_impact_Multiple",
    "infra_aménagement",
    "atm_perturb_air",
]


# liste des variables triées selon leur importance dans le modèle RF
liste_var_tri_RF = [
    "densité_dep_pop",
    "accident_grave_right",
    "agg_in",
    "circ_2",
    "choc_impact_Arriere",
    "lum_jour",
    "obs",
    "catv_poids_B: 0.15-1.5T",
    "prof_1",
    "plan_1",
    "presence_ado",
    "int_out",
    "atm_précipitations",
    "presence_pers_agee",
    "atm_contrast_lum-autre",
    "infra_aménagement",
    "catv_poids_E: >7.5T",
    "nbv_0_à_4",
    "int_giratoire-place",
    "choc_impact_Multiple",
    "prof_3",
    "prof_4",
    "atm_perturb_air",
    "plan_4",
]

df = pd.DataFrame(
    {"Gradient Boosting Classifier": liste_var_tri_GBC, "Random Forest": liste_var_tri_RF}
)

liste_definition = sorted(list(set(liste_var_tri_GBC) | set(liste_var_tri_RF)))

accident_grave_right = "taux d'accidents graves dans la zone du buffer"

agg_in = "en agglomération"

atm_contrast_lum_autre = "temps éblouissant ou couvert ou autre"

atm_perturb_air = "brouillard, fumée, vent, fort ou tempête"

atm_precipitations = "pluie légère, pluie, neige, grêle"

catv_poids_B = "véhicules entre 0.15 et 1.5 tonne"

catv_poids_E = "véhicules supérieurs à : 7.5 tonnes"

choc_impact_Arriere = "impact par l'arrière"

choc_impact_Multiple = "impacts multiples"

circ_2 = "circulation à double sens"

densite_dep_pop = "densité de population départementale"

infra_amenagement = "carrefour aménagé, zone piétonne, zone de péage"

int_giratoire_place = "présence d'un rond-point d'une place"

int_out = "à l'extérieur d'une intersection"

lum_jour = "en journée"

nbv_0_a_4 = "nombre de voies de 0 à 4"

obs = "nombre d'obstacles"

plan_1 = "tracé en plan : partie rectiligne"

plan_4 = 'tracé en plan : en "S"'

presence_ado = "présence d'adolescents"

presence_pers_agee = "présence de personnes âgées"

prof_1 = "déclivité de la route à l'endroit de l'accident : plat"

prof_3 = "déclivité de la route à l'endroit de l'accident : sommet de côte"

prof_4 = "déclivité de la route à l'endroit de l'accident : bas de côte"


df2 = pd.DataFrame(
    {
        "variables": liste_definition,
        "définitions": [
            accident_grave_right,
            agg_in,
            atm_contrast_lum_autre,
            atm_perturb_air,
            atm_precipitations,
            catv_poids_B,
            catv_poids_E,
            choc_impact_Arriere,
            choc_impact_Multiple,
            circ_2,
            densite_dep_pop,
            infra_amenagement,
            int_giratoire_place,
            int_out,
            lum_jour,
            nbv_0_a_4,
            obs,
            plan_1,
            plan_4,
            presence_ado,
            presence_pers_agee,
            prof_1,
            prof_3,
            prof_4,
        ],
    }
)
