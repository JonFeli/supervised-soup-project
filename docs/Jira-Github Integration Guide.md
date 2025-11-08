

In order for the git-integration with Jira to sync progress automatically we have to reference the keys of the work items (epics, tasks, subtasks) in the branch name and commit messages.

## ![blue book](https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/32x32/1f4d8.png)Instructions

1. Find the key for the Jira work item you want to link to (e.g. on the board: “SSXP-14”)
    
2. Check out a new branch in your repo, using the work item key in the branch name. For example, `git checkout -b SSXP-14-<branch-name>`.
    
3. When committing changes to your branch, use the key in your commit message to link those commits to the development panel in your Jira work item. For example, `git commit -m "SSXP-14 <summary of commit>"`.
    

Make sure the key is formatted correctly (case-sensitive)!

## ![clipboard](https://pf-emoji-service--cdn.us-east-1.prod.public.atl-paas.net/standard/ef8b0642-7523-4e13-9fd3-01b65648acf6/32x32/1f4cb.png) Related articles

- Page:
    https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/