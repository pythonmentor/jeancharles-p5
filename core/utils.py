import argparse
import logging as lg
import sys
from sys import (stdout, path)

logger = lg.getLogger(__name__)


def parse_arguments():
    """Parse_arguments parsing args
     parameters :
        --datafile : name of file map without extension """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--nbcategory", help=""" Maximum categories number
        """, default="10")
    parser.add_argument("-c", "--country", help=""" Country where data are selected from 
        """, default='France')
    parser.add_argument("-n", "--nbproducts", help="""  Maximum products number
        """, default="100000")
    parser.add_argument("-gp", "--get_product", help="""  Get product object by id
        """, default="0")
    parser.add_argument("-gpsl", "--get_products_subst_list", help="""  Get product subsitute list by id
        """, default="0")
    parser.add_argument("-gpm", "--get_products_list_by_match", help="""  Get product by match on key words
        between the names of products or categories. Wildcad '*' is allowed.
        """, default="")
    parser.add_argument("-ssp", "--set_substitute_product", help="""  Set relation product,substitute by id
        """, default="")
    parser.add_argument("-r", "--reload", help="Reload database from Openfactsfood services",
        action="store_true")

    return parser.parse_args()


def set_logger():
    """set log environement."""
    # Set logging stuff
    fh = lg.StreamHandler(stdout)
    formatter = lg.Formatter('%(asctime)s - %(levelname)s -'
                             ' %(filename)s - %(funcName)s - %(message)s')
    fh.setFormatter(formatter)
    logger = lg.getLogger()

    logger.addHandler(fh)
    logger.setLevel(lg.DEBUG)

