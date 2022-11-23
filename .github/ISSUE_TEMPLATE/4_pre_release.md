---
name: Pre-release to staging
about: Creates an issue to pre-release from master to staging deploy (includes hotfixes)
title: '🚀 Pre-release master -> staging_SPRINTNAME_VERSION (DATE)'
labels: 'release'
assignees: 'pcrespov'
---

In preparation for [pre-release](https://github.com/ITISFoundation/osparc-simcore/releases). Here an initial (incomplete) list of tasks to prepare before pre-releasing:


- [ ] Draft changelog from commits list (see [docs/releasing-workflow-instructions.md](https://github.com/ITISFoundation/osparc-simcore/blob/6cae77e5444f825f67fca65876922c8d26901fd2/docs/releasing-workflow-instructions.md))
- [ ] Check important changes 🚨
- [ ] Devops check (⚠️ devops)
- [ ] e2e testing check
- [ ] Pre-release summary
- [ ] Pre-release assessment

---

<!-- Staging is an intermediate environment between development (master) and production that allows us to test in isolation
changes in the framework. In addition, the pre-release workflow shall be used as a simulation to production that can help us to
anticipate changes and mitigate failures. 

Explain what motivates this pre-release? Which important changes we might pay attention to? How should we
test them? Is there anything in particular we should monitor?

TIPs:

- Start this section with a *motivation* 
- Mark commits with 🚨 to warn about possible issues. Contact PR creator to understand how to test/target
- It is preferable that pre-releases should address the outcome of a single sprint at a time. This might be done by pre-releasing to
staging just after the sprint review, and then hotfix staging all fixes to staging that have been solved during the subsequent sprint.
Mark all the commits that were cherry picked for a hotfix as [ 📌  ``staging_switzer_5``]

-->



#  Devops check (⚠️ devops)
<!-- The goal here is to analyze the PRs marked with (⚠️ devops).  We should determine and prepare necessary changes required in the environments configs. 

This procedure should be taken also as an exercise in preparation for the release to production as well.
 -->


# e2e testing check
<!-- Check that e2e in master: are there any major known issues? 

Keep an agenda of what has been reported on every daily
-->
- Mon. ...
- Tue.
- Wed.
- Thu.
- Fri.


# [Commits (in order)](https://github.com/ITISFoundation/osparc-simcore/commits/master)
<!-- List of commits for this release. 

Copy&paste list produced by ``make release`` 

These items create cross links to PR issues

- Mark important changes 🚨
- Mark cherry-picks for hotfixes with 📌
-->

# Draft Changelog
```markdown
<!-- Changelog follow structure defined in https://keepachangelog.com/en/1.0.0/ -->


## Added / Changed / Removed
<!-- Added for new features.  -->
<!-- Changed for changes in existing functionality.  -->
<!-- for now removed features. -->

## Deprecated
<!-- for soon-to-be removed features. -->

## Fixed
<!-- for any bug fixes. -->

## Security / Maintenance
<!--  Security in case of vulnerabilities.
	or some maintanence work on CI/CD/tests/scripts
 -->


**Legend**

- ✨ New feature
- 🐛 Fixes bugs
- ♻️ Refactors code
- ⬆️ Upgrades dependencies
- 🔒️ Fixes security issues
- 🔨 Adds or updates development scripts or CI.
- 🚨 Important change. REQUIRES target testing before releasing to production. Steps to test appended as ``[TODO:  ... ]``
- 📌 can be cherry-picked to production
```



# Pre-release summary

- what:  <!-- ```make release-staging name=switzer version=2 git_sha=dbcc9a645f25468ed57d227c42e8daad6ccb62d8``` -->
- who: <!-- @Surfict @GitHK  -->
- when: <!-- THURSDAY Oct.20, afternoon -->



# Pre-release assessment

<!-- How did the release go? Any incidents, problems, difficulties, unexpected issues, ... during the release process? 
Notes on special warnings or configurations we should pay attention ... or in general any relevant information that helps us 
mitigate the risk of failure when releasing to production
-->
