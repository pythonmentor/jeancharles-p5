#!/usr/bin/python3
# coding: utf-8
import sys

from core import utils
from core.dao.daoproduct import DaoProduct
from core.filler import Filler



import logging as lg

logger = lg.getLogger(__name__)


def main():
    args = utils.parse_arguments()
    # prepare les logs
    utils.set_logger()

    # option: chargement de la base
    if args.reload:
        Filler().start()
        sys.exit(0)

    if int(args.get_products_subst_list) > 0:
        id = int(args.get_products_subst_list)
        dao_product = DaoProduct()
        products = dao_product.get_products_subst_list_by_id(id)
        search_product = dao_product.get_product_by_id(id)
        print("******************************************************")
        print("Vous souhaitez un substitut pour le produit suivant :")
        print("******************************************************")
        print(search_product)
        print("******************************************************")
        print("Pur Beurre vous propose le substitut suivant :")
        print("******************************************************")
        for product in products:
            print(product)
        sys.exit(0)

    to_match = args.get_products_list_by_match
    if not str(to_match) == "":
        dao_product = DaoProduct()
        products = dao_product.get_products_list_by_match(to_match)
        print("******************************************************")
        print("Résultat de la recherche sur les mots clés suivants :")
        print("******************************************************")
        print(to_match)
        print("******************************************************")
        print("Produits correspondants :")
        print("******************************************************")
        for product in products:
            print(product)
        sys.exit(0)

    a_tuple = args.set_substitute_product
    if not str(a_tuple) == "":
        r_tuple = tuple(str(a_tuple).split(','))
        Filler().set_substitute_product(r_tuple)
        print("******************************************************")
        print("")
        print("******************************************************")
        sys.exit(0)


if __name__ == "__main__":
    main()