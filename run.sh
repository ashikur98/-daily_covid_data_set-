#!/bin/bash

cd ~/Documents/Projects/-daily_covid_data_set-
python3 run.py
git add covid_19_country_data.csv
git commit -m 'daily automate data update'
git push