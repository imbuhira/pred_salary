import glassdoor_scraper as gs
import pandas as pd
path = "/Users/imbuhira/ds_projects/chromedriver"

df = gs.get_jobs('software developer', 33, False, path, 10)
