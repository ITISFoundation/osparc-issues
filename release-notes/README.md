# README

### TL;DR
- This folder contains **releaase notes** divided by **product**.
- They must be **comprehanded by any user** of the platform/product.
- They rarely contain links to pull requests or other developer focused tools.

## How is this content created?

All **release notes** are created using an iterative approch involving members of multuple teams: developers, app team, product owners.

The process is coordinated by the current scrum master. They are reponsible for coordinating the team effort and making sure eveything is in place before the release.


## Scrum master procedures

The scrum master hast to take care of making sure that the deadlines are on track for letting the App Team know when it's tiem to test.
Usually a schedule with the following logic must be created.

1. ask POs (Nik) for the next review date, **BE INSISTENT!**
1. once the date is established create the **deadlines calendar** and post it to the team on mattermost
1. ask developers to fill out the drafts per product, ideally before the reiview but it's OK if they fill them out before the email to the app team is sent out
1. ensure all required components are present in NIH Staging deployment
1. inform App Team when the deployment is availale for testing

### 1. review date

Ask Nik insisitntly for a review date as soon as possible. It will be much harder to organise the rest without it.

### 2. deadlines calendar

The following deadelines must be established:

- `prs_merge` (pull requests merge date):  users have to get PRs (which must be testes by the App Team) merged in master by the end of this day
- `staging_release` (staging release date): PRs are moved to staging enviornemtn to which App Team will have access
- `review_meeting` (review date): the day of the review provided by Nik
- `start_app_team` (first day of testing): this day (included) App Team will have exclusive access to the NIH Staging deployment
- `end_app_team` (last day of testing): this day (included) by the end of the day App Team will be done testing
- `prod_release` (production release): staging changes are moved to production on this day

```shell
python scripts/deadlines_calendar.py <DATE> <DATE> <DATE> <DATE> <DATE> <DATE>
```

`<DATE>` format: `dd.mm` where `dd` is a valid caldendar day and `mm` is valid calendar month


### 3. release drafts compliation

Use the following script to generate the new release drafts for all the products.
A message to be posted to mattermost is also provided, `COMPILE THE DATE AND TIME` for the deadline, before posting it.

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light

```shell
python scripts/make_release_drafts.py <VERSION>
```

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light


1. time schedule for release & app team testing
2. put together drafts
3. convert drafts to final version before release
4. (Optional) In case of hotfixes to production instructions

## After Hotfixing

Please note, that if you hotfix a change to a production deployment, you have to run the below command and follow it's istructions.

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light:

```shell
python scripts/run_after_hotfix_to_prod.py <VERSION>
```

`<VERSION>` format: `X.X.X` where `X` is a number

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light:
