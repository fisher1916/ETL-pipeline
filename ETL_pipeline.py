# Import packages that do the specific tasks
import fips_state_codes as fsc
import clean_cms as cc
import census_data as cd
#
# Main processing pipeline function
#


def process_pipleine():

    print(">>> Starting ETL processing... <<<")

    # Extract and clean fips state codes
    fsc.extract_codes()

    # Read and Clean CMS Data
    cc.scrub_cms_data()

    # Access Census API and pull income and population data
    cd.census_data_api_extract()

    print(">>> Completed ETL processing... <<<")


process_pipleine()
