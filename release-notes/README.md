# README

### TL;DR
- This folder contains **releaase notes** divided by **product**.
- They must be **comprehanded by any user** of the platform/product.
- They rarely contain links to pull requests or other developer focused tools.

## How is this content created?

All **release notes** are created using an iterative approch involving members of multuple teams: developers, App Team, product owners.

The process is coordinated by the current scrum master. They are reponsible for coordinating the team effort and making sure eveything is in place before the release.


## Scrum master procedures

The scrum master takes care of enforcing deadlines. His final goal is to produce an email sent to the App Team containing information about:
- where, when and waht to test
- pretify release drafts

The following actions should be taken (details below):

1. ask PO(s) (Nik) for the next review date. Be insistent. I mean it: **BE INSISTENT!**
1. coordinate with team when to deploy to `staging` and `production`
1. once dates are available create the **deadlines calendar** and post it to the team on mattermost (reminders about important deadlines)
1. ask developers to fill out the release drafts per product
1. ensure NIH Staging is properly deployed
1. inform App Team after the review when the deployment is ready for testing

### 1. `review date`

Ask Nik insisitntly for a review date as soon as possible. It will be much harder to organise the rest without it.

### 2. `releases to staging and production`

Ask team members if it si possible to release to:
- `staging` 1 day before the reivew and
- `production` after the App Team finishes testing staging (usually one or two days alfter)

### 3. `deadlines calendar`

The following deadelines must be established:

- `prs_merge` (pull requests merge date):  users have to get PRs (which must be testes by the App Team) merged in master by the end of this day
- `staging_release` (staging release date): PRs are moved to staging enviornemtn to which App Team will have access
- `review_meeting` (review date): the day of the review provided by Nik
- `start_app_team` (first day of testing): this day (included) App Team will have exclusive access to the NIH Staging deployment
- `end_app_team` (last day of testing): this day (included) by the end of the day App Team will be done testing
- `prod_release` (production release): staging changes are moved to production on this day

```shell
python scripts/3_deadlines_calendar.py <DATE> <DATE> <DATE> <DATE> <DATE> <DATE>
```

`<DATE>` format: `dd.mm` where `dd` is a valid caldendar day and `mm` is valid calendar month

**NOTE:** make sure to enforce important deadlines (1/2 days before they expire) like:
- date and time when `all PRs` need to be `merged` before release to staging
- date and time when `release drafts` need to be `completed`


### 4. `release drafts compliation`

Ideally these are done before the reiview. The App Team will most likeley see them only during the testing days
The email to the App Team shoudl be sent briefly after the review is over.

Use the following script to generate the new release drafts for all the products.
A message to be posted to mattermost is also provided, `COMPILE THE DATE AND TIME` for the deadline, before posting it.

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light:

```shell
python scripts/4_make_release_drafts.py <VERSION>
```

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light:


### 5. `staging deplyed`

Ensure with the team that staging is properly deployed. Check the following:
- staging release to NIH Staging deployment occurred
- sim4life services released

### 6. `email App Team`

Compose and send out email to inform the App Team when they can start testign the deployment.


# After Hotfixing

Please note, that if you hotfix a change to a production deployment, you have to run the below command and follow it's istructions.

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light:

```shell
python scripts/run_after_hotfix_to_prod.py <VERSION>
```

`<VERSION>` format: `X.X.X` where `X` is a number

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light:
