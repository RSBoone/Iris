# Iris
Personal 'Artificially Intelligent' Assistant, Iris (Intelligent InteRactive System)

Developing Iris is a side project for me. Inspiried by Ironman's JARVIS, the goal is to develop an opensource AI that can communicate with people and do random tasks. 

Some goals I would like to achieve:
1) Use CMUSphinx and pyTTSX3 to create a STT and TTS package that works offline so I don't have to rely on Google.
  1.5) Implement machine learning to continuously improve that model/package.
2) Add web-scraping functionality to retreive data from sources like FRED and the BLS.
3) Add regression and other econometric analysis methods to Iris to perform computations on the above.

More will be added over time. All of the goals above should be achievable by voice request alone. 

For example: "Iris, download the latest financial data from FRED and run an analysis on the labor force participation rate."
would cause Iris to ask a series of quesions that would narrow down parameters for the analysis. Once those parameters are 
given, Iris would execute that analysis and return the results.

The above would take serious development, but is achievable. 

Packages considered for the above tasks:
  1) SciPy
  2) NumPy
  3) Pandas
  
Packages for future tasks
 1) PySal - For Spatial Econometrics
  
Packages for NLP/TTS/STT development:
 1) CMU Sphinx / Pocket Sphinx

Thoughts on Iris' eventual functionality:

The ability to perform analyses of any kind is dependent on the ability to recognize a problem and react accordingly. Meta-Processing will have to be built in for Iris to recognize the difference between catergorical, numeric, and ordinal data, as well as the ability to clean gaps in the data 'she' is parsing accordingly. Without a sufficiently advanced neural network architecture that can do this, a series of tests and methods to handle the various situations Iris may come across will have to be coded. This, along with making notes about the data, and the issues therein, will lend credibility to the robustness of any analysis performed.
