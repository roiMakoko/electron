from .import views
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views


app_name = "elec_meter"

urlpatterns = [
    path('', views.index,name="home"),
    path('logout', views.deconnexion,name="logout"),
    path('connexion', views.connexion,name="login"),
    path('nouvel-utilisateur', views.creer_utilisateur,name='register'),
    path('les-agents', views.liste_agents,name='liste_agents'),
    path('agent/<int:id>/details', views.details_agent,name='details_agent'),
    path('modifier-etat', views.changer_etat_activite, name='changer_etat_activite'),
    path('agent/modifier-infos-client', views.modifier_infos_client,name='modifier_infos_client'),
    path('agent/modifier-profile-agent', views.modifier_profile_agent,name='modifier_profile_agent'),
    path('gestion-des-droits', views.gestion_droits, name='gestion_droits'),
    #path('ajout-d-un-agent', views.add_agent,name='add_agent'),
    path('activate/<uidb64>/<token>/', views.activate,name='activate'),
    path('nouveau-compteur', views.nouveau_compteur,name='nouveau_compteur'),
    path('nouvelle-gateway', views.ajout_gateway,name='nouvelle_gateway'),
    path('gateways', views.liste_gateways,name='liste_gateways'),
    path('ajouter-une-province', views.ajax_ajouter_province,name='ajouter_province'),
    path('ajouter-une-ville', views.ajax_ajouter_ville,name='ajouter_ville'),
    path('recuperer-provinces', views.ajax_charger_provinces,name='charger_provinces'),
    #path('nouveau-client', views.nouveau_client,name='nouveau_client'),
    path('liste-des-villes', views.liste_villes,name='liste_villes'),
    path('les-compteurs', views.liste_compteurs,name='liste_compteurs'),
    path('liste-des-provinces', views.liste_province,name='liste_province'),
    path('client/home', views.client_home,name='client_home'),
    path('client/login', views.client_login,name='client_login'),
    path('validation', views.validate,name='validate'),
    path('ville/<int:pk>', views.details_ville,name='details_ville'),
    path('province/<int:pk>', views.details_province,name='details_province'),
    path('supprimer-une-province', views.supprimer_province,name='supprimer_province'),
    path('modifier-periode-de-push', views.modifier_periode_push,name='modifier_periode'),
    path('donnees/<str:num_compteur>/compteur', views.donnees_compteur,name='donnees_compteur'),
    path('modifier-image-de-profile', views.modifier_image_profile,name='modifier_image_profile'),
    path('modifier_etat_valve', views.modifier_etat_valve,name='modifier_etat_valve'),
    path('seeg-recharge-credit', views.recharger_credit_seeg,name='recharger_credit_seeg'),
    path('acheter-credit-compteur', views.recharger_compteur,name='recharger_compteur'),
    path('compteur/<str:num_compteur>/historique', views.historique_compteur,name='historique_compteur'),
    path('crediter-compte', views.crediter_compteur,name='crediter_compteur'),
    path('compteur/operations/<str:num_compteur>', views.transactions, name='transactions'),
    path('donnees-infos', views.donnees_infos,name='donnees_infos'),
    path('statistique/<str:devEUI>', views.stats_donnees_compteur,name='stats_donnees_compteur'),
    path('graphes/analyses', views.graphe_analyse,name='graphe_analyse'),
    path('graphes', views.graphes_compteur,name='graphes_compteur'),
    path('recharge des unites', views.recharge_unites,name='recharge_unites'),
    path('transfert-des-unités', views.transfer_credit,name='transfert'),
    path('suppression compteur', views.supprimer_compteur,name='suppression_compteur'),
    path('liste-clients', views.liste_clients,name='liste_clients'),
    path('details/<int:id>/client', views.details_client, name='details_client'),
    path('abonnement/<str:param1>/<str:param2>', views.creer_abonnement, name='nouvel_abonnement'),
    path('autocomplete-code-client', views.code_client_autocomplete, name='code_client_autocomplete'),
    path('graphes/consommations-semaine-passee', views.graphe_conso_semaine_passee,name='graphe_conso_semaine_passee'),
    path('graphes/moyenne-credit-par-mois', views.graphe_credit_par_mois,name='graphe_credit_par_mois'),
    path('graphes/recharge-hebdo-par-province', views.recharge_credit_par_province,name='recharge_credit_par_province'),
    path('profile/<int:id_agent>/edition', views.editer_profile,name='editer_profile'),
    path('edition-mot-de-passe', views.edition_mot_de_passe, name='edition_mot_de_passe'),
    path('compteuts/modification nom compteur', views.modifier_nom_compteur, name='modifier_nom_compteur'),
    path('profile/edition-donnees-personnelles', views.editer_donnees_personnelles,name='editer_donnees_personnelles'),
    path('re-initialiser-mot-de-passe', auth_views.PasswordResetView.as_view(template_name="elec_meter/forgot-password.html",
        success_url=reverse_lazy('elec_meter:password_reset_done'),email_template_name="elec_meter/password_reset_email.html"), name='reset_password'),
    path("verifiez-votre-messagerie",auth_views.PasswordResetDoneView.as_view(template_name="elec_meter/password_reset_done.html"),name="password_reset_done"),
    path('reinitialisation/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="elec_meter/password_reset_confirm.html",success_url=reverse_lazy('elec_meter:reset_complete')),name="password_reset_confirm"),
    path('nouveau-mot-de-passe/', auth_views.PasswordResetCompleteView.as_view(template_name="elec_meter/password_reset_complete.html"),name ='reset_complete'),
    path('client/statistiques/<str:devEUI>', views.client_stat_par_mois,name='client_stat_par_mois'),
    path('client/deconnexion', views.client_deconnexion,name='client_deconnexion'),
    path('nouveau-client', views.creer_client,name='nouveau_client'),
    path('nouveau-client', views.creer_client,name='nouveau_client'),
    path('regenration-code-client', views.regenerer_code_client, name='regeneration_code'),
    path('edition/<int:id_client>/client', views.editer_client, name='edition_client'),
    path('equivalence-unites-credits', views.creer_contrat,name='creer_contrat'),
    path('transfert-unites', views.envoi_unites,name='transfert_unites'),
    path('emprunter-unites', views.emprunter_unites,name='emprunter_unites'),
    path('creation-abonnement', views.creation_abonnement,name='creation_abonnement'),
    path('telecharger-fichier-compteurs', views.telecharger_fichier_compteur,name='telecharger_fichier_compteur'),
    path('compteurs-libres', views.liste_compteurs_libres,name='liste_compteurs_libres'),
    path('precharger-contrats', views.precharger_contrats,name='precharger_contrats'),
    path('geolocalisation-des-compteurs', views.voir_carte_compteur,name='voir_carte_compteur'),
    path('geolocalisation-des-getways', views.voir_carte_getways,name='voir_carte_getways'),
    path('charger-carte', views.charger_carte,name='charger_carte'),
    path('charger-carte-getway', views.charger_carte_getways,name='charger_carte_getways'),
    path('liste-contrats', views.contrats,name='contrats'),
    path('suppression-contrat', views.supprimer_contrat,name='supprimer_contrat'),
    path('details-contrat', views.details_contrat,name='details_contrat'),
    path('deveui-auto-complete', views.deveui_autocomplete,name='deveui_autocomplete'),
    path('emprunts/<str:deveui>/compteur', views.emprunts,name='emprunts'),
    path('compteur-libre', views.compteur_libre,name='compteur_libre'),
    path('donnees-mise-a-jour', views.refresh_data,name='refresh_data'),
    path('modifier-localisation', views.modifier_localisation_compteur,name='modifier_localisation_compteur'),
    #path('situation/<str:deveui>/compteur/<str:getway>', views.localisation_compteur, name='localisation_compteur'),
    path('centre-de-notifications', views.notifications, name='notifications'),
    path('compteurs-arretes-par-villes', views.compteur_arretes_par_villes, name='compteur_arretes_par_villes'),
    path('details-gateway', views.details_gateway, name='details_gateway'),
]

handler404 = views.page_not_found_view
