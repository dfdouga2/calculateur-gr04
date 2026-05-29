def calculer_ttc(prix_ht: float, taux_tva: float) -> float:
    """
    Calcule le prix TTC à partir du prix HT et du taux de TVA.

    :param prix_ht: Le prix hors taxes
    :param taux_tva: Le taux de TVA en pourcentage
    :return: Le prix TTC
    """
    return prix_ht * 1.20
