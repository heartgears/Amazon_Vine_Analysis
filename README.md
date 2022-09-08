# Amazon_Vine_Analysis

# Overview of the analysis
The purpose of this analysis is to determine the efficacy of Amazon's paid Vine program for product reviews. Companies pay a small fee to Amazon and provide products to Amazon Vine members who then review the product. The main question for this analysis is whether or not there is a positive bias skew for the data.

# Technology & Requirements
* Data Tools: Amazon_Reviews_ETL.ipynb and Vine_Review_Analysis.ipynb.
* Software: Python 3.9, Visual Studio Code 1.50.0, Anaconda 4.8.5, Jupyter Notebook 6.1.4, PySpark, and Pandas
* Storage: Amazon S3 Bucket

# Results
The main results of the analysis are as follows:

**How many Vine reviews and non-Vine reviews were there?**
![Deliverable_2.1_Screenshot](https://github.com/heartgears/Amazon_Vine_Analysis/blob/main/Screenshots/number_of_reviews.png)

**How many Vine reviews were 5 stars? How many non-Vine reviews were 5 stars?** 
![Deliverable_2.2_Screenshot](https://github.com/heartgears/Amazon_Vine_Analysis/blob/main/Screenshots/number_five_star_ratings.png)

**What percentage of Vine reviews were 5 stars? What percentage of non-Vine reviews were 5 stars?** 
![Deliverable_2.3_Screenshot](https://github.com/heartgears/Amazon_Vine_Analysis/blob/main/Screenshots/percentages.png)

## Deliverable 1
* An Amazon Review dataset is extracted as a DataFrame
* The extracted dataset is transformed into four DataFrames
* All four DataFrames are loaded into their respective tables in pgAdmin

## Deliverable 2
* There is a DataFrame for the vine_table data
* The data is filtered to create a DataFrame where there are 20 or more total votes
* The data is filtered to create a DataFrame where the percentage of helpful_votes is equal to or greater than 50% 
* The data is filtered to create a DataFrame where there is a Vine review
* The data is filtered to create a DataFrame where there isn’t a Vine review
* The total number of reviews, the number of 5-star reviews, and the percentage 5-star reviews are calculated for all Vine and non-Vine reviews

# Summary: 

Based particularly on the results of 2.3, there is a positivity bias for the Amazon Vine reviews. 39% of product reviews on Amazon are positive, compared to 51% for the Amazon Vine reviews. Another analysis that could be conducted to support this would be to evaluate the negative reviews, and see if there are a lower percentage of one star reviews for Vine products than overall. However, the dataset used for Vine reviews is very small, which may make this sample unrepresentative of the whole. Additional analyses on other Vine datasets should be conducted to confirm the results of this particular analysis.  
