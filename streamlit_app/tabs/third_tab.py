import streamlit as st
import pandas as pd
import numpy as np
import predict
import altair as alt
import pydeck as pdk
from annotated_text import annotated_text
from streamlit_extras.let_it_rain import rain
from time import sleep
import table as d

title = "Prédictions"
sidebar_name = "Prédictions"


def run():

    if "name" not in st.session_state:
        st.session_state.name = ""

    st.title(title)

    st.markdown("---")

    col_title, col_tool = st.columns([0.2, 1])

    col_title.markdown("#### Paramètres")
    tool = col_tool.button(":wrench:", help=":tada:")

    if tool:
        st.text_input(
            ":green[Veuillez] :orange[saisir] :violet[votre] :red[prénom]", key="name"
        )
    if st.session_state.name != "":

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("---")
        st.balloons()
        sleep(2.5)
        annotated_text(
            ("Félicitation", "", "#8ef"),
            (f"{st.session_state.name}", "", "#faa"),
            ("!!", "", "#fea"),
            ("Vous", "", "#afa"),
            ("avez", "", "#fea"),
            ("découvert", "", "#8ef"),
            ("l'EASTER EGG", "", "#afa"),
            ("!!", "", "#fea"),
            ("  (＠＾◡＾)", "", "#faa"),
        )
        st.markdown("<br>", unsafe_allow_html=True)
        sleep(2)
        st.success(
            "Nous pouvons maintenant vous révéler l'origine du :red[nom] du projet"
        )

        sleep(2)

        with st.expander("C'est par ici"):
            rain(
                emoji="🎵",
                font_size=54,
                falling_speed=5,
                animation_length=2,
            )

            st.image("assets/ray_charles.jpg")
            st.markdown(
                "Vous le reconnaissez? C'est [***Ray Charles***](https://raycharles.com/) :musical_keyboard:."
            )
            st.markdown(
                "C'est la chanson ***Hit The Road Jack*** qui a inspiré le nom du projet !"
            )
            st.video("https://www.youtube.com/watch?v=uSiHqxgE2d0", start_time=5)
            st.info("Maintenant vous savez :red[T]:green[O]:orange[U]:blue[T] !")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("---")

    type_pred = st.selectbox(
        "Sur quelles données souhaitez-vous faire la prédiction ?",
        ("2021", "Accident au choix", "Personnalisé"),
    )

    choix_model = st.selectbox(
        "A l'aide de quel modèle de Machine Learning souhaitez-vous faire la prédiction ?",
        (
            "Random Forest",
            "Gradient Boosting for Classification",
        ),
    )

    if choix_model == "Random Forest":
        choix_model_tr = "RF"
    elif choix_model == "Gradient Boosting for Classification":
        choix_model_tr = "GBC"

    ### type_pred = 2021 ###

    # if 'nb_var' not in st.session_state:
    #    st.session_state['nb_var'] = 3

    if type_pred == "2021":
        st.markdown("---")
        nb_var = st.slider(
            "Choix du nombre de variables", min_value=3, max_value=24, value=3, step=1
        )
        st.markdown("---")

        st.markdown("#### Metrics pour un nombre de variable défini")

        col1, col2, col3 = st.columns([20, 20, 60])
        col1.metric(
            "Accuracy",
            round(predict.results_2021[choix_model_tr]["accuracy"][nb_var], 3),
        )
        col2.metric(
            "Recall", round(predict.results_2021[choix_model_tr]["recall"][nb_var], 3)
        )

        st.table(
            pd.DataFrame(
                predict.results_2021[choix_model_tr]["confusion"][nb_var],
                index=["True : 0", "True : 1"],
                columns=["Pred : 0", "Pred : 1"],
            )
        )

        # st.markdown("---")

        # st.markdown("### Evolution des metrics en fonction du nombre de variables")
        # Graphe de l'accuracy et du recall en fonciton du nombre de variables

        # x_plot = pd.Series(predict.results_2021[choix_model_tr]['accuracy'].keys())
        # y_acc = pd.Series(predict.results_2021[choix_model_tr]['accuracy'].values())
        # y_recall = pd.Series(predict.results_2021[choix_model_tr]['recall'].values())
        # source = pd.DataFrame({'Nb variables': x_plot, 'accuracy': y_acc, 'recall':y_recall })

        # base = alt.Chart(source).encode(alt.X('Nb variables'))
        # line_A = base.mark_line(color='#5276A7').encode(alt.Y('accuracy', axis=alt.Axis(titleColor='#5276A7'), scale=alt.Scale(domain=(0.72, 0.78))))
        # line_B = base.mark_line(color='#F18727').encode(alt.Y('recall', axis=alt.Axis(titleColor='#F18727'), scale=alt.Scale(domain=(0.54, 0.64))))

        # c = alt.layer(line_A, line_B).resolve_scale(y='independent')

        # st.altair_chart(c, use_container_width=True)

        st.markdown("---")
        st.markdown("#### Comparaison des modèles")

        selection = alt.selection_interval(bind="scales")

        chart = (
            alt.Chart(
                predict.df_results.loc[predict.df_results["metric"] == "accuracy"]
            )
            .mark_line()
            .encode(
                x=alt.X("nb_var", title="Nombre de variables"),
                y=alt.Y("valeur", title="", scale=alt.Scale(domain=(0.74, 0.78))),
                color=alt.Color("modele", title="Modèle"),
                tooltip=["modele", "nb_var", "valeur"],
            )
            .properties(title="Accuracy")
            .interactive()
            .add_selection(selection)
        )
        st.altair_chart(chart, use_container_width=True)

        chart = (
            alt.Chart(predict.df_results.loc[predict.df_results["metric"] == "recall"])
            .mark_line()
            .encode(
                x=alt.X("nb_var", title="Nombre de variables"),
                y=alt.Y("valeur", title="", scale=alt.Scale(domain=(0.55, 0.65))),
                color=alt.Color("modele", title="Modèle"),
                tooltip=["modele", "nb_var", "valeur"],
            )
            .properties(title="Recall")
            .interactive()
            .add_selection(selection)
        )
        st.altair_chart(chart, use_container_width=True)

    elif type_pred == "Accident au choix":
        st.markdown("---")
        choix_acc = st.select_slider(
            "Choix de l'accident", options=set(predict.data_map.Num_Acc_analyse)
        )

        st.markdown("---")
        st.markdown("#### Carte des accidents")

        data_map_acc = predict.data_map.loc[
            predict.data_map.Num_Acc_analyse == choix_acc
        ]
        st.pydeck_chart(
            pdk.Deck(
                map_style=None,
                initial_view_state=pdk.ViewState(
                    latitude=48.86, longitude=2.35, zoom=11
                ),
                layers=[
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=data_map_acc.loc[data_map_acc.Num_Acc != choix_acc],
                        get_position="[long, lat]",
                        get_radius=25,
                        get_color=("accident_grave === 1 ? [255, 0, 0] : [0, 255, 0]"),
                    ),
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=data_map_acc.loc[data_map_acc.Num_Acc == choix_acc],
                        get_position="[long, lat]",
                        get_radius=30,
                        get_color=(0, 0, 0),
                    ),
                ],
            )
        )

        st.markdown("---")
        st.markdown("#### Prédictions")

        if choix_model == "Random Forest":
            pred = predict.ex_acc.loc[predict.ex_acc.Num_Acc == choix_acc][
                "predict_RF"
            ].values
        elif choix_model == "Gradient Boosting for Classification":
            pred = predict.ex_acc.loc[predict.ex_acc.Num_Acc == choix_acc][
                "predict_GBC"
            ].values

        true = predict.ex_acc.loc[predict.ex_acc.Num_Acc == choix_acc][
            "accident_grave"
        ].values

        col1, col2, col3 = st.columns([40, 20, 40])

        with col1:
            col1.table(
                predict.var_acc[choix_acc].rename({choix_acc: "Valeurs"}, axis=1)
            )

        with col2:
            col2.image("assets/fleche.png")
            col2.image("assets/panneau travaux.png")

        with col3:
            if pred == 0:
                col3.write(f"Le modèle prédit un accident léger.")
            elif pred == 1:
                col3.write(f"Le modèle prédit un accident grave.")
            verif = st.button("Vérifiez !")

            if verif:
                if true == pred:
                    st.image("assets/hand ok.png")
                else:
                    st.image("assets/hand ko.png")

    elif type_pred == "Personnalisé":
        st.markdown("---")
        st.write("Définir le contexte de l'accident :")
        col1, col2 = st.columns(2)
        accident_grave = col1.number_input(
            "accident_grave",
            min_value=0.00,
            max_value=1.00,
            value=0.20,
            step=0.01,
            help=str(
                d.df2.loc[d.df2.variables == "accident_grave_right"][
                    "définitions"
                ].values
            ),
        )
        densite = col2.number_input(
            "densité_dep_pop",
            min_value=0,
            value=20000,
            step=500,
            help=str(
                d.df2.loc[d.df2.variables == "densite_dep_pop"]["définitions"].values
            ),
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            agg_in = st.checkbox(
                "agg_in",
                value=False,
                help=str(d.df2.loc[d.df2.variables == "agg_in"]["définitions"].values[0]),
            )
            obs = st.checkbox(
                "obs",
                value=False,
                help=str(d.df2.loc[d.df2.variables == "obs"]["définitions"].values[0]),
            )
            nbv_0_4 = st.checkbox(
                "nbv_0_à_4",
                value=False,
                help=str(
                    d.df2.loc[d.df2.variables == "nbv_0_à_4"]["définitions"].values[0]
                ),
            )
            plan_1 = st.checkbox(
                "plan_1",
                value=False,
                help=str(d.df2.loc[d.df2.variables == "plan_1"]["définitions"].values[0]),
            )
            catv_poids_B = st.checkbox(
                "catv_poids_B",
                value=False,
                help=str(
                    "véhicules entre 0.15 et 1.5 tonne"
                ),
            )
            atm_contrast_lum_autre = st.checkbox(
                "atm_contrast_lum-autre",
                value=False,
                help=str(
                    "temps éblouissant ou couvert ou autre"
                ),
            )

        with col2:
            circ_2 = st.checkbox(
                "circ_2",
                value=False,
                help=str(d.df2.loc[d.df2.variables == "circ_2"]["définitions"].values[0]),
            )
            choc_impact_Multiple = st.checkbox(
                "choc_impact_Multiple",
                value=False,
                help=str(
                    d.df2.loc[d.df2.variables == "choc_impact_Multiple"][
                        "définitions"
                    ].values[0]
                ),
            )
            presence_ado = st.checkbox(
                "presence_ado",
                value=False,
                help=str(
                    d.df2.loc[d.df2.variables == "presence_ado"]["définitions"].values[0]
                ),
            )
            int_giratoire_place = st.checkbox(
                "int_giratoire-place",
                value=False,
                help=str(
                    "présence d'un rond-point d'une place"
                ),
            )
            infra_aménagement = st.checkbox(
                "infra_aménagement",
                value=False,
                help=str(
                    "carrefour aménagé, zone piétonne, zone de péage"
                ),
            )

        with col3:
            choc_impact_Arriere = st.checkbox(
                "choc_impact_Arriere",
                value=False,
                help=str(
                    d.df2.loc[d.df2.variables == "choc_impact_Arriere"][
                        "définitions"
                    ].values[0]
                ),
            )
            lum_jour = st.checkbox(
                "lum_jour",
                value=False,
                help=str(
                    d.df2.loc[d.df2.variables == "lum_jour"]["définitions"].values[0]
                ),
            )
            prof_1 = st.checkbox(
                "prof_1",
                value=False,
                help=str(d.df2.loc[d.df2.variables == "prof_1"]["définitions"].values[0]),
            )
            prof_3 = st.checkbox(
                "prof_3",
                value=False,
                help=str(d.df2.loc[d.df2.variables == "prof_3"]["définitions"].values[0]),
            )
            int_out = st.checkbox(
                "int_out",
                value=False,
                help=str(d.df2.loc[d.df2.variables == "int_out"]["définitions"].values[0]),
            )
            presence_pers_agee = st.checkbox(
                "pers_agee",
                value=False,
                help=str(
                    d.df2.loc[d.df2.variables == "presence_pers_agee"][
                        "définitions"
                    ].values[0]
                ),
            )

        with col4:
            catv_poids_E = st.checkbox(
                "catv_poids_E",
                value=False,
                help=str(
                    "véhicules supérieurs à : 7.5 tonnes"
                ),
            )
            atm_précipitations = st.checkbox(
                "atm_précipitations",
                value=False,
                help=str(
                    d.df2.loc[d.df2.variables == "atm_précipitations"][
                        "définitions"
                    ].values[0]
                ),
            )
            plan_4 = st.checkbox(
                "plan_4",
                value=False,
                help=str(d.df2.loc[d.df2.variables == "plan_4"]["définitions"].values[0]),
            )
            prof_4 = st.checkbox(
                "prof_4",
                value=False,
                help=str(d.df2.loc[d.df2.variables == "prof_4"]["définitions"].values[0]),
            )
            atm_perturb_air = st.checkbox(
                "atm_perturb_air",
                value=False,
                help=str(
                    d.df2.loc[d.df2.variables == "atm_perturb_air"][
                        "définitions"
                    ].values[0]
                ),
            )

        st.markdown("---")

        X_test = pd.DataFrame(
            {
                "densité_dep_pop": densite,
                "accident_grave_right": accident_grave,
                "agg_in": agg_in,
                "circ_2": circ_2,
                "choc_impact_Arriere": choc_impact_Arriere,
                "catv_poids_B: 0.15-1.5T": catv_poids_B,
                "obs": obs,
                "presence_pers_agee": presence_pers_agee,
                "lum_jour": lum_jour,
                "catv_poids_E: >7.5T": catv_poids_E,
                "atm_précipitations": atm_précipitations,
                "int_out": int_out,
                "nbv_0_à_4": nbv_0_4,
                "plan_1": plan_1,
                "presence_ado": presence_ado,
                "int_giratoire-place": int_giratoire_place,
                "prof_1": prof_1,
                "prof_3": prof_3,
                "plan_4": plan_4,
                "prof_4": prof_4,
                "atm_contrast_lum-autre": atm_contrast_lum_autre,
                "choc_impact_Multiple": choc_impact_Multiple,
                "infra_aménagement": infra_aménagement,
                "atm_perturb_air": atm_perturb_air,
            },
            index=[0],
        )

        X_test_norm_simp = pd.DataFrame(index=X_test.index)

        for var in X_test.columns:
            mean = predict.scale.loc[predict.scale["var"] == var]["mean"].values
            scale = predict.scale.loc[predict.scale["var"] == var]["scale"].values

            X_test_norm_simp[var] = (X_test[var] - mean) / scale

        X_test_norm_simp = X_test_norm_simp.rename(
            {"plan_4": "plan_4.0", "plan_1": "plan_1.0"}, axis=1
        )

        if choix_model == "Random Forest":
            pred = predict.rf.predict(X_test_norm_simp)
        elif choix_model == "Gradient Boosting for Classification":
            pred = predict.gbc.predict(X_test_norm_simp)

        if pred == 1:
            pred2 = "Accident grave"

            col1, col2, col3 = st.columns([3, 4, 3])
            col2.metric("Prédiction", pred2)

            col1, col2 = st.columns(2)
            col1.image("assets/accident_grave1.png")
            col2.image("assets/accident_grave2.png")

        else:
            pred2 = "Accident léger"

            col1, col2, col3 = st.columns([3, 4, 3])

            with col2:
                col2.metric(":red[Prédiction :]", pred2)
                col2.image("assets/accident_leger.png")
