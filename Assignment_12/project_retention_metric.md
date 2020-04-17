# Project Retention Metric by Jessie Murphey

Question: What is the current number of active contributors on a project?

## Description
This metric is meant to be used on the of a repository of an open source project by tracking the contributions(reviews, comments, edits, commits) by contributors over a time period.

## Objectives	
By tracking which contributors are actively adding new content to a repository a company is more accurately able to access the health of the given project. Retention requires an inflow of new contributors as previously active contributors leave.

## Implementation
By tracking the changes of a repository, we can see each contribution and its contributor with the date. We can then track how many contributors there are in total, and which ones have made contributions recently. 
Each contributor will start as active but, if a contributor has not made a commit in a set amount of time, they will be marked as inactive. 
The company itself could set the amount of time before the contributor is marked as inactive, or it could just be a standard set time period for all repositories.

### Filters (optional)
- The contributors’ ID 
- The time-span for inactivity (how long a contributor must not add a new commit to be considered inactive)
- Type of contribution (edit, comment, reveiew, commit, etc.)
- (possibly) lines of code (to see the amount contributed)

### Visualizations (optional)
- This metric can be represented in a simple table show the names of the contributors, their active/inactive status, and the date of their last commit. 
- It can also split the data by type of contribution, for example having the option to only see the contributors who made commits recently, ect.

### Tools Providing the Metric
The Github API can view contributions for a repository, which will show the contributor and date.
GET /repos/:owner/:repo/stats/contributors

### Data Collection Strategies (Optional)
A way to collect data for this metric would be to use the Github api to GET each change in a repository and create a simple database using MySQL to track which person contributed, the type of contribution, and when.

## References
The Retention section (Section 4) of this guide is a extremely useful reference to this metric and goes into more detail and includes more parameters to evaluating how many people are actively contributing to your project https://opensource.guide/metrics/
