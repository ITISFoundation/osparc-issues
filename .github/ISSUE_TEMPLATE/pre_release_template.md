---
name: Pre-release to staging
about: Creates an issue to pre-release from master to staging deploy
title: ''
labels: ''
assignees: 'pcrespov'

---

# Pre-release master -> staging_XXXXX (DATE)


In preparation for [pre-release *staging_XXXXX*](https://github.com/ITISFoundation/osparc-simcore/releases). Here an initial (incomplete) list of tasks to prepare before pre-releasing:

- [ ] Draft changelog from commits list (see [docs/releasing-workflow-instructions.md](https://github.com/ITISFoundation/osparc-simcore/blob/6cae77e5444f825f67fca65876922c8d26901fd2/docs/releasing-workflow-instructions.md))
- [ ] Target pre-release date
- [ ] Set commit SHA to pre-release to staging
- [ ] Evaluate devops makred with (⚠️ devops)
- [ ] Define important changes 🚨


---

# Draft Changelog
Changelog follow structure defined in https://keepachangelog.com/en/1.0.0/


## Added
<!-- Added for new features.  -->
## Changed
<!-- Changed for changes in existing functionality.  -->
## Deprecated
<!-- for soon-to-be removed features. -->
## Removed
<!-- for now removed features. -->
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
- 🚨 important change. REQUIRES app-level testing before releasing to production
- 📌 can be cherry-picked to production
