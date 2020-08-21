import glassdoor_scraper as gs
import pandas as pd
path = "/Users/imbuhira/ds_projects/chromedriver"

df = gs.get_jobs('software developer', 1000, False, path, 10)
df.to_csv('glassdoor_jobs.csv', index=False)



