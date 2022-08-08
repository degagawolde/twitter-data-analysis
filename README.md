# Twitter-Data-Analysis

### Repository Creation using template
1. Use the template given in ["Creating a repository from a template."](https://docs.github.com/en/articles/creating-a-repository-from-a-template), I created a repository called Twitter-Data-Analysis.
2. After that I cloned my repository on my local machine.
### Data Preparation
1. After downloading the data from [here](https://drive.google.com/drive/folders/19G8dmehf9vU0u6VTKGV-yWsQOn3IvPsd), I extracted it and get two json file data (global_twitter_data.json, and africa_twitter_data.json)

3. After that I created a git branch “bugfix” to fix the bugs in the fix_clean_tweets_dataframe.py and fix_extract_dataframe.py. While converting the raw json file to pandas dataframe, we have to use appropriate keywords. 
5. To fix the bugs in clean_tweets_dataframe.py, we have to carefully consider the data type conversion in pandas dataframe.

7. Create a new branch called “testing” for updating the unit tests in the test/ folder to be applicable to the code you fixed. 
    a. Build your unit and integration tests to run on small data (< 1 MB) that you copied from what is provided - avoid pushing large data to github
    b. Think about the key elements (units can be functions, classes, or modules; multiple of them working together to accomplish a task requires integration testing) of the code base you are working on. Write the following
      - Unit tests: for individual key functions and classes
      - Integration tests: for the integration of multiple units working together
8. After completing the unit and integration tests, merge  the “testing” branch with the main branch
9. In all cases when you merge, make sure you first do Pull Request, review, then accept the merge.
10. Use github actions in your repository such that when you git push new code (or merge a branch) to the main branch, the unit test in tests/*.py runs automatically. All tests should pass.


After Completing this Challenge, you would have explore  
- Unittesting
- Modular Coding
- Software Engineering Best Practices
- Python Package Structure
- Bug Fix (Debugging)

Have Fun and Cheers
