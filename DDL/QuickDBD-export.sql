-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "census" (
    "county_name" VARCHAR(40)   NOT NULL,
    "state" VARCHAR(40)   NOT NULL,
    "household_median_income" INT   NOT NULL,
    "family_median_income" INT   NOT NULL,
    "total_population" INT   NOT NULL,
    "state_code" VARCHAR(40)   NOT NULL,
    "county_code" VARCHAR(40)   NOT NULL,
    "state_abbr" VARCHAR(40)   NOT NULL,
    CONSTRAINT "pk_census" PRIMARY KEY (
        "county_name","state_abbr"
     )
);

CREATE TABLE "cms" (
    "cms_ID"  SERIAL  NOT NULL,
    "facility_ID" VARCHAR(40)   NOT NULL,
    "facility_Name" VARCHAR(120)   NOT NULL,
    "address" VARCHAR(120)   NOT NULL,
    "city" VARCHAR(40)   NOT NULL,
    "state" VARCHAR(40)   NOT NULL,
    "zip_Code" VARCHAR(40)   NOT NULL,
    "county_Name" VARCHAR(120)   NOT NULL,
    "measure_ID" VARCHAR(80)   NOT NULL,
    "measure_Name" VARCHAR(120)   NOT NULL,
    "denominator" INT   NOT NULL,
    "score" NUMERIC   NOT NULL,
    "lower_Estimate" NUMERIC   NOT NULL,
    "higher_Estimate" NUMERIC   NOT NULL,
    "start_Date" DATE   NOT NULL,
    "end_Date" DATE   NOT NULL,
    CONSTRAINT "pk_cms" PRIMARY KEY (
        "cms_ID"
     )
);

ALTER TABLE "cms" ADD CONSTRAINT "fk_cms_state_county_Name" FOREIGN KEY("state", "county_Name")
REFERENCES "census" ("state_abbr", "county_name");

