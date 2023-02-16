# Exploratory Data Analysis (EDA) 

## What EDA?

Exploratory data analysis (EDA) is an iterative process of analyzing data sets to summarize their main characteristics through visualizations, graphical and/or numerical summaries. EDA is primarily used for seeing what the data can tell us beyond the formal modeling. 

The goal of EDA is to explore the data to gain a better understanding of the data before proceeding to formal analysis. EDA can help identify obvious errors, understand any patterns within the data, detect outliers or anomalous points, and find interesting relationships among the variables.
 
The insights drawn from EDA can then be used for more sophisticated data analysis or modeling, including machine learning. 

## Popular Python Libraries for Data Science 

- NumPy
- Pandas 
- Scikit-learn 
- Matplotlib 
- Seaborn 

## Initial Questions To Consider 

How many observations/rows are there?

How many variables/columns are there?

What kinds of variables are there? Categorical? Numerical? Both?

## Variable Types

### Qualitative Variables

A *qualitative variable* is also referred to as a *categorical variable* and takes on one value of a fixed number of possible values. 

Examples of qualitative variabels include:
- Level of education (High School Graduate, Associate's Degree, Bachelor's Degree, Master's Degree)
- Political Affiliation (Democrat, Republican, Independent)
- Neighborhood in Boston


### Quantitative Variables  

A *quantitative variable* is also referred to a *numeric variable* and represents a measured quantity. 

Examples of quantitative variables include: 
- Population of a city 
- Number of individuals in a household 
- Age of an individual
- Height of an individual 
- Inches of rainfall in a day

## Descriptive Statistics 

*Descriptive statistics* provide simple summaries about the set of observations. They can serve as a sanity check to make sure that your data makes sense or if it doesn't make sense identify potential errors in the data. 

Examples of descriptive statistics are:
- Estimates of central tendency (e.g. *mean, median*)
  - These values describe where most observations in the data set lie. 
  - The mean is commonly used, but is overly influenced by extreme outliers. 
  - The median is a more robust estimator of central tendency that is less influenced by extreme outliers.
  - The median does not consider the precise value of each observation and may not be where the bulk of the data is.  
- Spread (e.g. *standard deviation, inter-quartile range*)
  - These values describe how far the observations are scattered around the central tendency. 
  - Standard deviation quantifies spread about the mean. Similar to the mean, standard deviation is influenced by outliers. 
  - Inter-quartile range quantifies spread about the median.
  - Inter-quartile range is the difference between the 25% and 75% quantiles. 
  - Inter-quartile range is a more robust to outliers than standard deviation.  
- Extremes (e.g. min and max values)
  - Minimum value of the quantitative variable. 
  - Maximum value of the quantitative variable. 
  - Are these min and max values expected for this variable? Do they make sense?

Questions to consider when looking at descriptive statistics:
-  Which values are most common? Why is this the case?
-  Which values are uncommon? Does this make sense? Does this match your expectations?
    
## Visualizations 

Visualizations can uncover more insights about your data and can serve as a great mechanism for explaining your findings to others. 

Visualizations are useful in examining the distributions of variables, either categorical or numerical. 

- *Bar charts* can be used to examine the distribution of a categorical variable, where the x-axis are the different categories the variable can be and the y-axis are the counts.
  - Bar charts give a visual representation of the frequency of the different groups. 
- *Histograms* can be used to examine the distribution of a numerical variable.
  - Explore using a variety of *bin widths* when working with a histogram. Different bin widths may reveal different patterns. 
- *Box plots* can be used to display the distribution of a numerical variable broken down by a categorical variable. This is useful for visualizing a combination of variable types.   
- *Scatter plots* can be used to examine if a linear relationship exists between two quantitative variables. 
  - *Correlation* measures the strength of the linear relationship between two quantitative variables.
    - The correlation coefficient can take a value between -1 and 1. 
      - A correleation coefficient close to -1 is a strong negative relationship. 
      - A correlation coefficient close to 0 is a weak relationship. 
      - A correlation coefficient close to 1 is a strong positive relationship.  