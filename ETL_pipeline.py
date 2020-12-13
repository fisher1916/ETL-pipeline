# Import packages that do the specific tasks
import fips_state_codes as fsc

#
# Main processing pipeline function
#


def process_pipleine():

    print("Starting ETL processing...")

    fsc.extract_codes()

    print("Completed ETL processing...")


process_pipleine()
