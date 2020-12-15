import pandas as pd

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, extract

from db_info import db_user, db_password, db_name

import datetime

# TODO: CREATE COMMENT FOR WHAT THIS DOES
def fix_county_name(string):
    
    if string == "DEKALB":
        return "DE KALB" 
    if string == "DUPAGE":
        return "DU PAGE" 
    elif string == "DISTRICT OF COLUMBIA":
        return "THE DISTRICT"
    elif string == "ANCHORAGE MUNICIPALITY":
        return "ANCHORAGE"
    elif string == "PRINCE GEORGE\'S":
        return "PRINCE GEORGES"
    elif string == "MCDOWELL":
        return "MC DOWELL"
    elif string == "MCHENRY":
        return "MC HENRY"
    elif string == "LASALLE":
        return "LA SALLE"
    elif string == "MCKEAN":
        return "MC KEAN"
    elif string == "MCDUFFIE":
        return "MC DUFFIE"
    elif string == "EAST BATON ROUGE":
        return "E. BATON ROUGE"
    elif string == "LAPORTE":
        return "LA PORTE"
    elif string == "DEWITT":
        return "DE WITT"
    elif string == "JUNEAU CITY AND BOROUGH":
        return "JUNEAU"
    elif string == "KENAI PENINSULA BOROUGH":
        return "KENAI PENINSULA"
    elif string == "MATANUSKA-SUSITNA BOROUGH":
        return "MATANUSKA-SUSITNA"    
    elif string == "DESOTO":
        return "DE SOTO"
    elif string == "DOÑA ANA":
        return "DONA ANA"
    elif string == "LA PAZ":
        return "LAPAZ"
    elif string == "MCLEAN":
        return "MC LEAN"
        elif string == "MCCRACKEN":
        return "MC CRACKEN"
    elif string == "MCDONOUGH":
        return "MC DONOUGH"    
    elif string == "KETCHIKAN GATEWAY BOROUGH":
        return "KETCHIKAN GATEWAY"
    elif string == "SCOTTS BLUFF":
        return "SCOTT BLUFF"
    elif string == "NORTHUMBERLAND":
        return "NORTHUMBERLND"   
    elif string == "MCLENNAN":
        return "MC LENNAN"
    elif string == "MCMINN":
        return "MC MINN"
    elif string == "FAIRBANKS NORTH STAR BOROUGH":
        return "FAIRBANKS NORTH STAR"
    elif string == "MCLEOD":
        return "MC LEOD"
    elif string == "YELLOW MEDICINE":
        return "YELLOW MEDCINE"
    elif string == "SITKA CITY AND BOROUGH":
        return "SITKA BOROUGH"
    else: 
        return string
    

def cms_data_load():

    print("<< Starting cms processing... >>")

    print("connecting to database processing...")
    # Create the engine
    connect_string = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_name}"
    engine = create_engine(connect_string)

    # reflect an existing database into a new model
    Base = automap_base()

    # reflect the tables
    Base.prepare(engine, reflect=True)

    # We can view all of the classes that automap found
    Base.classes.keys()

    # Save references to each table
    Census = Base.classes.census
    Cms = Base.classes.cms

    print("reading dataframes...")

    # Read in target dataframes
    census_df = pd.read_csv("ETL-Results/census_data.csv", dtype=str)
    cms_df = pd.read_csv("ETL-Results/four_mort_measures.csv", dtype=str)

    # Save formatted county names
    census_df['County Name'] = census_df['County Name'].apply(lambda x: fix_county_name(x))

    

    print("<< Completed cms processing... >>")



