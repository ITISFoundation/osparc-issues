# Review Meeting - 07/11/2022 @ 10:00 CET

## Sprint 🏃

- [**Katherine Switzer**](https://www.youtube.com/watch?v=fOGXvBAmTsY)  (First woman officially completing a marathon, Boston 1967)
- 🕐 PM1(Oct17) - RM(Nov07)
- Scrum Master: [EI](https://github.com/elisabettai)

### Users Feedback

- [closed](https://github.com/pulls?q=is%3Apr+archived%3Afalse+user%3AITISFoundation+closed%3A%3E2022-10-07) since last RM
- [opened](https://github.com/ITISFoundation/osparc-issues/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions)

### Dashboards 📊

- [Product Backlog](https://github.com/orgs/ITISFoundation/projects/3) (PO view)
- [Sprint Scrum Wall](https://app.zenhub.com/workspaces/osparc---scrum-wall-5c9260f3d76ef51f6b0fe78d/board?repos=118596920,174557929,151701223,135289610,118910047,181836792,167586968) (developers view)
- [PM2 board](https://github.com/orgs/ITISFoundation/projects/9) (developers view)
- Activity: [sprint-PRs] and [sprint-MRs]

### Deployed environments 🚀

- AWS cluster (us-east-1)
  - [staging_aws](https://staging.osparc.io) (Testers only - [changelogs])
  - [production_aws](https://osparc.io) ([changelogs])
- Z43 cluster (ch-zh)
  - [staging_z43](http://osparc-staging.speag.com) (Testers only - [changelogs])
  - [production_z43](http://osparc.speag.com) ([changelogs])
  - [ti-plan.itis.swiss](http://ti-plan.itis.swiss)
  - [master](https://osparc-master.speag.com) (delopers only)

| PO  | Topic        | Title                                                                                      | Presenter | Status          | Duration | Start-Time |
| --- | ------------ | ------------------------------------------------------------------------------------------ | --------- | --------------- | -------- | ---------- |
| 1   | dy-services  | [#638] improving dynamic-sidecar design                                                    | ANE       | **In Progress** | 3 min    |  10:05     |
|     |              | <blockquote>[#3447] Allow selective starting/stopping of dynamic services</blockquote>     | SAN       | **In Progress** | 7 min    |  10:08     |
| 2   | maintenance  | [#675] M1-12 Maintenance and DevOps                                                        | SA/PC/DK  | **Ongoing**     | 5 min    |  10:15     |
| 4   | devops       | [#657] Autoscaling - Dynamic Services                                                      | SAN       | **In Progress** | 3 min    |  10:20     |
|     |              | <blockquote>[#735] Migrate Postgres to newer version</blockquote>                          | DK        | **In Progress** | 2 min    |  10:23     |
| 22  | metamodeling | [#626] meta-modeling                                                                       | PC        | **In Progress** | 5 min    |  10:25     |
| 3   |              | <blockquote>[#355] S-D22.4 Meta-Modeling optimizer module Y4M12</blockquote>               | PC        | **In Progress** | 5 min    |  10:30     |
| 5   | s4l:web      | [#741] s4l light features & ui                                                             | CR/IP/MaG/OM | **In Progress** | 15 min   |  10:35  |
| 7   |              | <blockquote>[#740] Deploy S4L light on AWS</blockquote>                                    | DK        | **In Progress** | 3 min    |    10:50   |
|     |              | <blockquote>[#740] oSPARC - S4L:Light</blockquote>                                         | OM        | **In Progress** | 3 min    |    10:53   |
|     | user request | [#743] follow up on TN’s user-test and TIP’s stress-test                                   | EI        | **In Progress** | 2 min    |    10:56   |
|     | UI           | [#671] M1-12: oSPARC Usability (UI/UX improvements based on users and Team Black feedback) | OM        | **In Progress** | 8 min    |    10:58   |
|     | user request | [#644] Cannot see Pennsieve data files                                                     | SAN       | **Resolved**    | 2 min    |    11:06   |
| 17  | metrics      | [#688] M3 Additional o²S²PARC Metrics                                                      | EI        | **In Progress** | 3 min    |    11:08   |
| 6   | API          | [#687] M2 Access to log after job was run (via API)                                        | PC        | **Resolved**    | 5 min    |    11:11   |
| 8   |              | <blockquote>[#686] M2 Query I/O Port Descriptors for Study via API</blockquote>            | PC        | **In Progress** | 3 min    |    11:16   |
| 21  | app          | [#684] M1-12 Push Publication of More Modeling Studies on the Portal Itself                | EI        | **Ongoing**     | 1 min    |    11:19   |
| 16  | portal       | [#674] M1-12 Portal development work                                                       | IP        | **Ongoing**     | 3 min    |    11:20   |
| 13  | TIP          | [#670] TIP - FollowUp Items                                                                |           | **Paused**      |    |       |
|    |           |                                                                |       |      | END TIME    |    11:23   |

##### Status Legend

- _Todo_: no work done on this issue. This is the first time it apprears in a sprint.
- _Paused_: this issue was not scheduled/skipped for this sprint
- _In Progress_: this issue is still under development
- _Resolved_: no more work left to do on this issue. PO can review an decide to close or reopen.
- _Ongoing_: a recurrent task

[online]: http://status.osparc.io/
[operational]: https://git.speag.com/oSparc/e2e-testing/-/pipelines
[performant]: https://git.speag.com/oSparc/e2e-portal-testing/-/pipelines

## Progress

Needs PO update, see previous reviews

## Blockers

Needs PO update, see previous reviews

[#638]: https://github.com/ITISFoundation/osparc-issues/issues/638
[#3447]: https://github.com/ITISFoundation/osparc-issues/issues/3447
[#675]: https://github.com/ITISFoundation/osparc-issues/issues/675
[#657]: https://github.com/ITISFoundation/osparc-issues/issues/657
[#735]: https://github.com/ITISFoundation/osparc-issues/issues/735
[#626]: https://github.com/ITISFoundation/osparc-issues/issues/626
[#355]: https://github.com/ITISFoundation/osparc-issues/issues/355
[#741]: https://github.com/ITISFoundation/osparc-issues/issues/741
[#740]: https://github.com/ITISFoundation/osparc-issues/issues/740
[#743]: https://github.com/ITISFoundation/osparc-issues/issues/743
[#671]: https://github.com/ITISFoundation/osparc-issues/issues/671
[#644]: https://github.com/ITISFoundation/osparc-issues/issues/644
[#688]: https://github.com/ITISFoundation/osparc-issues/issues/688
[#687]: https://github.com/ITISFoundation/osparc-issues/issues/687
[#686]: https://github.com/ITISFoundation/osparc-issues/issues/686
[#684]: https://github.com/ITISFoundation/osparc-issues/issues/684
[#674]: https://github.com/ITISFoundation/osparc-issues/issues/674
[#670]: https://github.com/ITISFoundation/osparc-issues/issues/670
