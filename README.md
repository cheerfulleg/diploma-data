**GitHub project Scrapper and Analyzer**

* Search project by tag in Github Topics.
* [Radon](https://radon.readthedocs.io/en/latest/index.html) used to get code metrics.
* Write metrics to csv.

Arguments:
- tag - search GitHub Topics tag
- filename - filename to write results
- range_from - page to start scrapping
- range_t0 - page to end scrapping

Example of running script
```
python run.py django django_metrics.csv 1 5
```