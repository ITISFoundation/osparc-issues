# README

### TL;DR
- This folder contains **releaase notes** divided by **product**.
- They must be **comprehanded by any user** of the platform/product.
- They rarely contain links to pull requests or other developer focused tools.

## How is this content created?

All **release notes** are created using an iterative approch involving members of multuple teams: developers, app team, product owners.

The process is coordinated by the current scrum master. They are reponsible for coordinating the team effort and making sure eveything is in place before the release.


## Scrum master procedures


1. time schedule for release & app team testing
2. put together drafts
3. convert drafts to final version before release
4. (Optional) In case of hotfixes to production instructions

## After Hotfixing

Please note, that if you hotfix a change to a production deployment, you have to run the below command and follow it's istructions.

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light:

```shell
python scripts/run_after_hotfix_to_prod.py
```

:warning: Do not forget to commit and push the changes in the reposity! :rotating_light:
