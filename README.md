# Twitter-Data-Analysis
***
### Repository Creation using template
1. Use the template given in ["Creating a repository from a template."](https://docs.github.com/en/articles/creating-a-repository-from-a-template), I created a repository called Twitter-Data-Analysis.
2. After that I cloned my repository on my local machine.
***
### Data Preparation
1. After downloading the data from [here](https://drive.google.com/drive/folders/19G8dmehf9vU0u6VTKGV-yWsQOn3IvPsd), I extracted it and get two json file data (global_twitter_data.json, and africa_twitter_data.json)
2. After that I created a git branch “bugfix” to fix the bugs in the fix_clean_tweets_dataframe.py and fix_extract_dataframe.py. While converting the raw json file to pandas dataframe, we have to use appropriate keywords. Additionally, textblob python library(sentimental analysis tool) is used to generate polarity and subjectivity.
3. To fix the bugs in clean_tweets_dataframe.py, we have to carefully consider the data type conversion in pandas dataframe. Furthermore, removing or dropping unimportant rows or columns is the purpose of this challenge.
***
### Unittesting
1. First, to avoid pushing large dataset to the github I selected the first 25 tweets from the json file and created another json data 'test_data.json' in the data directory. 
- Unit tests: for individual key functions and classes
- Integration tests: for the integration of multiple units working together
***
### git commands
1. The most important thing I learned in this challenge is how to use the most important git commands(add, commit, branch, checkout, push)
2. The 'bugfix' is used for data extraction and cleaning while the 'testing' branch is used for unit tests.
3. After making changes I used git add . command to add files that are changed and git commit -m .. to commit the chang and git push .. to push it to the repository.
