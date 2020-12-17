# Bootcamp-ETL-Project

## Datasets

- [Medicare Dataset for The nation](Resources/cms_data_2.csv)
- 2010-2019 Census Population Dataset for the nation

## Field of Interests

- Star Rating
- COPD Mortality (Chronic obstructive pulmonary disease)
- HF Mortality (Heart Failure)
- AMI Mortality (Acute Myocardial Infarction)
- PN Mortality (Pneumonia)
- Census population for Portland

## Agenda for this Data for Future use

Infant mortality by zipcode

- Use zipcode heatmap
- Possible filter for low average household incomes
  For this project we pulled date from the CMS Data site as well as the census site. We hope to use this project as a staging and in helping to plan for the next project.
  This was our process:

1. We explored the available data on the CMS site and decided that looking at four measures for mortality were our primary focus. This was because this data was available for almost 100% of the hospitals in the database. This extracted as a CSV.
1. We explored the data on the census site and discovered that the two datasets had aligned data for zip code, state, and county. This required the use of an API key and extracted as a CSV.
1. We scraped the table on the census site to obtain the state codes.
1. We pulled all the above-mentioned datasets into the repository.
1. From there we used Jupyter Notebooks to clean and explore the data further.
   - For the CMS data we first created a notebook to do the following:
     - Read in the CMS data
     - Only bring in the columns we wanted
     - Get rid of any null values if any but there were none.
     - Removed all instances whereupon there not a score for a measure
     - Removed all measures that were not the 4 measures we were interested in
     - Exported to a new CSV
   - For the census data we created a notebook and did the following:
     - Read in the FIPS State codes and the census data
     - Brought in the columns we wanted
     - Created a for loop to create a dataframe with data we wanted
     - Created a function to create a state abbreviation for every state
     - Changed the county names to be all caps to match the county names in the CMS dataset.
     - Exported to new csv
1. At that point we read the two CSV noted in step 5 to a new database to prepare the information for the ultimate pipeline. In this notebook we used SQL Alchemy to merge the two into one.
   - At this point there was an issue with the county names in the census and the county names in the CMS dataset so we went through and fixed those issues.
   - We then set it up to be able to create the pipeline
1. Jay describe the pipeline
1. In order to recreate the data you would want in a SQL Query and the QRY to run do the following:
![Top Html](images/ETL_diagram.png)
![Top Html](images/ERDdb.jpg)
