# README

### TL;DR
- This folder contains **releaase notes** divided by **product**.
- They must be **comprehanded by any user** of the platform/product.
- Scrum master orchestrates their process of creation.

## How is this content created?

All **release notes** are created using an iterative approch involving members of multuple teams: developers, App Team, product owners.

The process is coordinated by the current scrum master. They are reponsible for coordinating the team effort and making sure eveything is in place before the release.


## Scrum master procedures

The scrum master takes care of enforcing deadlines. Their goal is to produce an email sent to the App Team containing information about:
- where, when and what to test
- ask App Team to rewrite the `draft release notes` into user readable `release notes`

The following procedure is suggested (more details below):

1. ask PO(s) (Nik) for the next review date. Be insistent. I mean it: **BE INSISTENT!**
1. coordinate with team when to deploy to `staging` and `production`
1. once dates are available create the **deadlines calendar** and post it to the team on Mattermost (reminders about important deadlines)
1. ask developers to fill out the release drafts per product
1. ensure NIH Staging is properly deployed
1. inform App Team after the review when the deployment is ready for testing
1. ensure all drafts have been converted to a non draft form (including the rewording) before release

### 1. `review date`

Ask Nik (be insistent) for the review date as soon as possible.
It is impossible to organise without a release date.

### 2. `pick staging and production release dates`

Ask team members if it is possible to release to:
- `staging` 1 day before the review
- `production` after the App Team finishes testing staging (usually one or two days after)

### 3. `deadlines calendar`

The following deadlines must be established (pass them in this order to the below cli):

- `prs_merge` (pull requests merge date) `usually one day before release to staging`: users have to get PRs (which must be testes by the App Team) merged in master by the end of this day
- `staging_release` (staging release date) `decided with team`: PRs are moved to staging environment to which App Team will have access
- `review_meeting` (review date) `decide by PO(s)`: the day of the review provided by Nik
- `start_app_team` (first day of testing) `first day after review`: this day (included) App Team will have exclusive access to the NIH Staging deployment
- `end_app_team` (last day of testing) `second day after review`: this day (included) by the end of the day App Team will be done testing
- `prod_release` (production release) `decided with team`: staging changes are moved to production on this day

```shell
python scripts/3_deadlines_calendar.py <DATE> <DATE> <DATE> <DATE> <DATE> <DATE>
```
- `<DATE>` format: `dd.mm` where `dd` is a valid calendar day and `mm` is valid calendar month

**NOTE:** make sure to enforce important deadlines (1/2 days before they expire) like:
- date and time when `all PRs` need to be `merged` before release to staging
- date and time when `release drafts` need to be `completed`


### 4. `release drafts compilation`

Ideally these are done before the review. The App Team will most likely see them only during testing.
The email to the App Team should be sent briefly after the review is over.

Use the following script to generate the new release drafts for all the products.
A Mattermost message is also provided.

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light:

```shell
python scripts/4_make_release_drafts.py <VERSION> <DATE> <TIME>
```
- `<VERSION>` format: `X.X.X` where `X` is a number
- `<DATE>` format: `dd.mm` where `dd` is a valid calendar day and `mm` is valid calendar month
- `<TIME>` format: `HH.MM` where `HH` is a valid hour and `MM` is valid minute


:warning: Do not forget to commit and push the changes in the repository! :rotating_light:


### 5. `staging deployed`

Ensure with the team that staging is properly deployed. Check the following:
- staging release to NIH Staging deployment occurred
- sim4life services released

### 6. `email App Team`

Compose and send out email to inform the App Team when they can start testign the deployment.

```shell
python scripts/6_app_team_email.py <DATE> <DATE> <VERSION>
```
- `<DATE>` format: `dd.mm` where `dd` is a valid calendar day and `mm` is valid calendar month
- `<VERSION>` format: `X.X.X` where `X` is a number

### 7. `no drafts left before release`

Check all products and make sure all the release drafts have been converted. Talk with the responsible people:
- `s4l`: App Team
- `tip`: (not decided yet), so it's the current scrum master
- `osparc`: (not decided yet), so it's the current scrum master

# After Hot-fixing

Please note, that if you hot-fix a change to a production deployment, you have to run the below command and follow it's instructions.

:warning: Do not forget to commit and push the changes in the repository! :rotating_light:

```shell
python scripts/run_after_hotfix_to_prod.py <VERSION>
```
- `<VERSION>` format: `X.X.X` where `X` is a number

:warning: Do not forget to commit and push the changes in the repository! :rotating_light:
