# Iris

## VERSION 0.1.0

#### CONTRIBUTOR NOTES
- Make a pull request on a new branch, not on the master branch.

-----------------
'Artificially Intelligent' Digital Assistant, Iris (Intelligent InteRactive System)

Inspiried by Ironman's JARVIS, the goal of the Iris project is to develop an opensource general AI. 

Long term goals for Iris' capabilities:
 1. To hear and speak without the use of third party software
 2. To discern what task is being requested and to take the necessary actions to perform that task
 3. To self analyze and improve performance

Long term goals will be concretized and divided into short term goals. After each short term goal is completed, NLP code will be added for vocal command.

Current short term goals relating to each long term goal:

1. NLP
    1. Research use of the CMU Sphinx packages to create a training dataset for voice recognition
    2. Research different Text to Speech packages
 
2. Analyses
    1. Add web-scraping / data retrieval functionality to retreive data from sources like FRED and the BLS. 
    2. Add regression and other econometric analysis methods to Iris to perform computations on various market data.
    3. Researching spatial econometric packages and developing one if their is no specialized package.
 
3. Meta & management
    1. Researching different benchmarking software
    2. Brainstorming and planning out self-evaluating/recoding meta-programming.

Packages considered for the above short term goals:
  - CMU Sphinx / Pocket Sphinx, PyTTSX3
  - SciPy, NumPy, Pandas, SKLearn, Matplotlib, PySal
  - TDB

-----------------
Expectations for full development:

With a fully functioning Iris program, offering the request

> "Iris, download the latest financial data from FRED and run an analysis on the labor force participation rate."

would cause Iris to scrape the lastest data from FRED on the labor force participation rate, and ask questions pertaining to the type of analysis to run (OLS, ARMA, GLM, etc.) Iris should be able to examine the data and determine the efficacy of the request. For instance, a time series analysis should be rejected if the data at hand is cross-sectional.

Over time, and by experience, Iris should be able to 'remember' types of analyses. If the same analysis or one of a similar type is requested, it should be run again without the need for parameters to be given. Iris should also announce an estimated time for completion based off of past analysis benchmarking.

Packages considered to help with the above full development:
  - [`tqdm`](https://github.com/tqdm/tqdm) (progress bar manager)
  - [`fredapi`](https://github.com/mortada/fredapi) (FRED API Package)
