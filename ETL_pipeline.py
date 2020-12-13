# Import packages that do the specific tasks
import fips_state_codes as fsc
import clean_cms as cc
#
# Main processing pipeline function
#


def process_pipleine():

    print(">>> Starting ETL processing... <<<")

    # Extract and clean fips state codes
    fsc.extract_codes()

    # Read and Clean CMS Data
    cc.scrub_cms_data()

    print(">>> Completed ETL processing... <<<")


process_pipleine()
