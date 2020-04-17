#Active Contributor Metric by Jessie Murphey

Question: What is the current number of active contributors on a project?

## Description
This metric is meant to be used on the of a repository of an open source project by tracking the commits by contributors over a time period.

## Objectives	
By tracking which contributors are actively adding new content to a repository a company is more accurately able to access the health of the given project. This directly plays into a company being able to access “The Bus Factor” of their project, because for example if say if a project has 10 contributors, but only 1 active contributor it is likely to die if the one active contributor stops. Whereas if you just look at the total of contributors it would give them a false sense of who is working on the project.

## Implementation
By tracking the commits of a repository, we can see the exact contributor that made the commit and the date. We can then track how many contributors there are in total, and which ones have made commits recently. Each contributor will start as active but, if a contributor has not made a commit in a given amount of time, they will be marked as inactive. The company itself could set the amount of time before the contributor is marked as inactive, or it could just be a standard set time period for all repositories.

###Filters (optional)
The contributors’ ID, the time-span for inactivity (how long a contributor must not add a new commit to be considered inactive), (possibly) lines of code (to see the amount contributed)

###Visualizations (optional)
This metric can be represented in a simple table show the names of the contributors, their active/inactive status, and the date of their last commit (with the number of lines of code, optional). 

### Tools Providing the Metric
The Github API can view commits for a repository, which will show the contributor and date. https://developer.github.com/v3/git/commits/ 

### Data Collection Strategies (Optional)
A way to collect data for this metric would be to use the Github api to GET each commit in a repository and create a simple database using MySQL to track which person contributed and when.

## References
The Retention section (Section 4) of this guide is a extremely useful reference to this metric and goes into more detail and includes more parameters to evaluating how many people are actively contributing to your project https://opensource.guide/metrics/
