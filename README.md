**GitHub project Scrapper and Analyzer**

* Search project by tag in Github Topics.
* [Radon](https://radon.readthedocs.io/en/latest/index.html) used to get code metrics.
* Write metrics to csv.

**Arguments**

- tag - search GitHub Topics tag
- file - filename to write results
- start - page to start scrapping
- end - page to end scrapping
 
**Metrics**

* **loc**: The number of lines of code (total)
* **lloc**: The number of logical lines of code
* **sloc**: The number of source lines of code (not necessarily
  corresponding to the LLOC)
* **comments**: The number of Python comment lines
* **multi**: The number of lines which represent multi-line strings
* **single_comments**: The number of lines which are just comments with
  no code
* **blank**: The number of blank lines (or whitespace-only ones)

Example of running script

```
python run.py --tag django --filename django_metrics.csv --start 1 --end 5
```