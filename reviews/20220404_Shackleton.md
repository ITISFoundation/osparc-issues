# Review Meeting - 04/04/2022 @ 11:00 CET

<p align="center">
<img width="250" alt="Ernest Shackleton" src="https://i.inews.co.uk/content/uploads/2022/03/SEI_92405157-1-760x1056.jpg">
</p>

## Sprint 🏃

- **Ernest Shackleton**
- 🕐 PM1(Mar.9) - RM(Apr.4)
- Scrum Master: [IP]

### Users Feedback

- [closed](https://github.com/ITISFoundation/osparc-issues/issues?q=is%3Aissue+sort%3Areactions+state%3Aclosed+updated%3A%3E%3D2022-03-09) since last RM
- [resolved (FB)](https://z43.manuscript.com/f/filters/?ixProject=45&ixStatus=0&maxrecords=50&resolvedInLast=3&sColumns=Category-Favorite-Case-TitleComment-Area-Priority-Status-DateResolved-DateOpened-OpenedBy&sSorts=LastUpdated.descending-Priority&sView=grid-flat) since last RM
- [opened](https://github.com/ITISFoundation/osparc-issues/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions)

### Dashboards 📊

- [Product Backlog](https://github.com/orgs/ITISFoundation/projects/3) (PO view)
- [Sprint Scrum Wall](https://app.zenhub.com/workspaces/osparc---scrum-wall-5c9260f3d76ef51f6b0fe78d/board?repos=118596920,174557929,151701223,135289610,118910047,181836792,167586968) (Developers view)
  - NEW [sprint wall](https://github.com/orgs/ITISFoundation/projects/9) (developers view)
- Activity: [sprint-PRs] and [sprint-MRs]

### Deployed environments 🚀

- AWS cluster (us-east-1)
  - [staging_aws](https://staging.osparc.io) (Testers only - [changelogs])
  - [production_aws](https://osparc.io) ([changelogs])
- Z43 cluster (ch-zh)
  - [staging_z43](http://osparc-staging.speag.com) (Testers only - [changelogs])
  - [production_z43](http://osparc.speag.com) ([changelogs])
- [master](https://osparc-master.speag.com) (ch-zh) (Developers only)

## Agenda

| PO        | Topic       | Title                                                                                                      | Presenter  | Status    | Duration | Start-Time |
|-----------|-------------|------------------------------------------------------------------------------------------------------------|------------|-----------|----------|------------|
| 5         | file-system | [#513] M5 Filesystem integration                                                                           |            |           |          | 10:05      |
| 1         |             | <blockquote>[#580] osparc-fs: Internals</blockquote>                                                       | [MaG]      | Ongoing   | 3'       |            |
| 2         |             | <blockquote> [#578] osparc-fs: Hardware</blockquote>                                                       | [DK]       | Ongoing   | 3'       |            |
| 5         |             | <blockquote> [#579] osparc-fs: Remote Mounts</blockquote>                                                  |            | Paused    |          |            |
| 3         | scheduler   | [#349] S-D25.4 Simulation framework SCHEDULER Y4M05                                                        |[SAN], [ALL]| Ongoing   | 10'      | 10:11      |
| 19        |             | <blockquote>[#350] S-D25.5 Simulation Framework resource allocation Y4M05 </blockquote>                    |            | Ongoing   |          |            |
| 4         | s4l web     | [#519] M1–12 Enhancements of the modeling/simulator/postpro service and framework                          |[CR], [MaG] | Ongoing   | 14'      | 10:21      |
| 6         | meta        | [#353] S-D22.2 Meta-Modeling sensitivity analysis Y4M08                                                    | [PC]       | Done      | 8'       | 10:35      |
| 7         |             | <blockquote>[#354] S-D22.3 Meta-Modeling uncertainty assessment Y4M10</blockquote>                         |            | Done      |          |            |
| 8         |             | <blockquote>[#515] M6 Support for unit conversion and detection of compatible ports                        | [OM]       | Ongoing   | 4'       | 10:43      |
| 9         |             | <blockquote>[#355] S-D22.4 Meta-Modeling optimizer module Y4M12                                            |            | Ongoing   |          |            |
| 16        | control     | [#510] M4 Modular platform for the generation and exploration of control strategies                        | [EI]       | Ongoing   | 8'       | 10:47      |
| 9         |             | <blockquote>[#555] Coupling API</blockquote>                                                               |            | Ongoing   |          |            |
| 12        | TI          | [#91] TI Planning                                                                                          | [OM]       | Ongoing   | 3'       | 10:55      |
| 13        | UI/UX, support | [#546], [#517] oSPARC UI/UX: Team Black and Support                                                     | [OM]       | Ongoing   | 8'       | 10:58      |
|           | integration | [#522] M5 Extend/Create onboarding facilities                                                              |            | Ongoing   |          |            |
|           |             | <blockquote>[#2409] Service integration (or service onboarding) backlog</blockquote>                       | [ANE]      | Ongoing   | 1'       | 11:06      |
| 15        |             | <blockquote>[#595] Comsol license server</blockquote>                                                      | [KZ]       | Paused    | 1'       | 11:07      |
| 20        |  resources  | [#576] Control, provide, and track resources                                                               | [SAN]      | Ongoing   | 1'       | 11:08      |
| 17        | maintenance | [#428] Maintenance/scaling of the platform                                                                 | [PC]       | Ongoing   | 5'       | 11:09      |
| 18        |             | [#509] M1–9 Cybersecurity and privacy                                                                      | [DK]       | Ongoing   | 2'       | 11:14      |
| 21        |             | [#545] Portal work                                                                                         | [IP]       | Ongoing   | 1'       | 11:16      |
| 22        |             | [#26] support onboarding of SPARC computational models, S-D1, Y3M1-12                                      | [KZ]       | Ongoing   | 1'       | 11:17      |
|           | devops      | [#529] M1–12 DevOps: platform monitoring and maintenance; fixing of stability issues; down-time reduction  | [ALL], [DK]| Ongoing   | 5'       | 11:18      |

##### Status Legend

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

<!--References PLEASE KEEP ALPHABETICAL ORDER!!! -->

[all]: https://github.com/Surfict
[ane]: https://github.com/GitHK
[bl]: https://github.com/dyollb
[dk]: https://github.com/mrnicegyu11
[cr]: https://github.com/colinRawlings
[ip]: https://github.com/ignapas
[kz]: https://github.com/KZzizzle
[mag]: https://github.com/mguidon
[om]: https://github.com/odeimaiz
[pc]: https://github.com/pcrespov
[san]: https://github.com/sanderegg
[syr]: https://zmt.swiss/about/about-zmt/all-staff/reboux-sylvain/
[tn]: https://itis.swiss/who-we-are/staff-members/all-staff/newton-taylor/
[ei]: https://github.com/elisabettai
[j-d4]: https://github.com/ITISFoundation/osparc-issues/issues/62
[j-d7.a]: https://github.com/ITISFoundation/osparc-issues/issues/21
[j-d35]: https://github.com/ITISFoundation/osparc-issues/issues/31
[j-d33]: https://github.com/ITISFoundation/osparc-issues/issues/33
[j-d20]: https://github.com/ITISFoundation/osparc-issues/issues/48
[j-d21]: https://github.com/ITISFoundation/osparc-simcore/issues/1065
[j-d28.a]: https://github.com/ITISFoundation/osparc-simcore/issues/1066
[j-d29]: https://github.com/ITISFoundation/osparc-issues/issues/37
[s-d2]: https://github.com/ITISFoundation/osparc-simcore/issues/1069
[s-d18]: https://github.com/ITISFoundation/osparc-issues/issues/9
[s-d7]: https://github.com/ITISFoundation/osparc-issues/issues/21
[s-d10]: https://github.com/ITISFoundation/osparc-issues/issues/18
[s-d22]: https://github.com/ITISFoundation/osparc-issues/issues/5
[s-d12]: https://github.com/ITISFoundation/osparc-issues/issues/16
[s-d15]: https://github.com/ITISFoundation/osparc-issues/issues/12
[s-d12]: https://github.com/ITISFoundation/osparc-issues/issues/16
[s-d6]: https://github.com/ITISFoundation/osparc-issues/issues/22
[s-d5]: https://github.com/ITISFoundation/osparc-issues/issues/23
[s-d21]: https://github.com/ITISFoundation/osparc-issues/issues/6
[s-d4]: https://github.com/ITISFoundation/osparc-issues/issues/24
[s-d1]: https://github.com/ITISFoundation/osparc-issues/issues/26
[s-d26]: https://github.com/ITISFoundation/osparc-issues/issues/332
[s-d27.2]: https://github.com/ITISFoundation/osparc-issues/issues/357
[n-d1]: https://github.com/ITISFoundation/osparc-issues/issues/68
[n-d2]: https://github.com/ITISFoundation/osparc-issues/issues/91
[tb-backlog]: https://github.com/ITISFoundation/osparc-issues/projects/4
[z43-backlog]: https://z43.fogbugz.com/f/filters/1112/osparc-cases
[sprint-prs]: https://github.com/pulls?page=1&q=is%3Apr+archived%3Afalse+user%3AITISFoundation+closed%3A%3E2021-11-15
[sprint-mrs]: https://git.speag.com/groups/oSparc/-/merge_requests?scope=all&utf8=%E2%9C%93&state=all
[changelogs]: https://github.com/ITISFoundation/osparc-simcore/releases

[#26]: https://github.com/ITISFoundation/osparc-issues/issues/26
[#91]: https://github.com/ITISFoundation/osparc-issues/issues/91
[#349]: https://github.com/ITISFoundation/osparc-issues/issues/349
[#350]: https://github.com/ITISFoundation/osparc-issues/issues/350
[#355]: https://github.com/ITISFoundation/osparc-issues/issues/355
[#353]: https://github.com/ITISFoundation/osparc-issues/issues/353
[#354]: https://github.com/ITISFoundation/osparc-issues/issues/354
[#428]: https://github.com/ITISFoundation/osparc-issues/issues/428
[#509]: https://github.com/ITISFoundation/osparc-issues/issues/509
[#510]: https://github.com/ITISFoundation/osparc-issues/issues/510
[#513]: https://github.com/ITISFoundation/osparc-issues/issues/513
[#515]: https://github.com/ITISFoundation/osparc-issues/issues/515
[#517]: https://github.com/ITISFoundation/osparc-issues/issues/517
[#519]: https://github.com/ITISFoundation/osparc-issues/issues/519
[#522]: https://github.com/ITISFoundation/osparc-issues/issues/522
[#529]: https://github.com/ITISFoundation/osparc-issues/issues/529
[#545]: https://github.com/ITISFoundation/osparc-issues/issues/545
[#546]: https://github.com/ITISFoundation/osparc-issues/issues/546
[#555]: https://github.com/ITISFoundation/osparc-issues/issues/555
[#557]: https://github.com/ITISFoundation/osparc-issues/issues/557
[#576]: https://github.com/ITISFoundation/osparc-issues/issues/576
[#577]: https://github.com/ITISFoundation/osparc-issues/issues/577
[#578]: https://github.com/ITISFoundation/osparc-issues/issues/578
[#579]: https://github.com/ITISFoundation/osparc-issues/issues/579
[#580]: https://github.com/ITISFoundation/osparc-issues/issues/580
[#595]: https://github.com/ITISFoundation/osparc-issues/issues/595

[#2409]: https://github.com/ITISFoundation/osparc-simcore/issues/2409
