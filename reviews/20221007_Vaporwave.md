# Review Meeting - 07/10/2022 @ 09:30 CET

## Sprint 🏃

- **vaporwave**  (Zurich's favorite architectural style)
- 🕐 PM1(Sept09) - RM(Oct07)
- Scrum Master: [DK]

### Users Feedback

- [closed](https://github.com/pulls?q=is%3Apr+archived%3Afalse+user%3AITISFoundation+closed%3A%3E2022-08-05) since last RM
- [resolved (FB)](https://z43.manuscript.com/f/filters/?ixProject=45&ixStatus=0&maxrecords=50&resolvedInLast=3&sColumns=Category-Favorite-Case-TitleComment-Area-Priority-Status-DateResolved-DateOpened-OpenedBy&sSorts=LastUpdated.descending-Priority&sView=grid-flat) since last RM
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
  - [master](https://osparc-master.speag.com) (Developers only)

## Agenda

|PO|Topic|Title|Presenter|Status|Duration|Start-Time|
|--|--|--|--|--|--|--|
|0|dy-services|[#638] improving dynamic-sidecar design|ANE, PC, SAN|**In Progress**||9:30|
|1|TIP|[#670] TIP - FollowUp Items|OM, DK, PC, SAN|**Todo**|||
|2|filesystem|[#617] 5Gb limit|SAN, PC|**In Progress**|||
| xx |              | <blockquote>[#513] M5 Filesystem integration</blockquote>                                                                              |           | **In Progress** |          |            |
| xx |              | <blockquote>[#579] osparc-fs: Remote Mounts</blockquote>                                                                               |           | Paused          |          |            |
| xx |              | <blockquote>[#580] osparc-fs: Internals</blockquote>                                                                                   |           | Paused          |          |            |
|3|support|[#558] Fix duplicate feature for large studies|OM, SAN|**In Progress**|||
|0|metrics|[#688] M3 Additional o²S²PARC Metrics|EI, ANE|**Todo**|||
|4|z43|[#654] z43 publishing (working group)|MaG|**Ongoing**|||
|0|maintenance|[#675] M1-12 Maintenance and DevOps|DK, SAN, ALL|**Ongoing**|||
| xx | metamodeling | [#626] meta-modeling                                                                                                                   | PC        | Paused          |          |            |
| xx |              | <blockquote>[#353] S-D22.2 Meta-Modeling sensitivity analysis Y4M08</blockquote>                                                       | PC        | Paused          |          |            |
| xx |              | <blockquote>[#354] S-D22.3 Meta-Modeling uncertainty assessment  Y4M10</blockquote>                                                    | PC        | Paused          |          |            |
| xx |              | <blockquote>[#625] port annotation</blockquote>                                                                                        | PC        | **??** |       |      |
| xx |              | <blockquote>[#515] M6 Support for unit conversion and detection of compatible ports</blockquote>                                       | PC        | Paused          |          |            |
| xx |              | <blockquote>[#516] M7 Dynamic checking during pipeline execution, whether input arguments to services satisfy constraints</blockquote> | PC        | Paused          |          |            |
| 5 |              | <blockquote>[#355] S-D22.4 Meta-Modeling optimizer module Y4M12</blockquote>                                                           | PC,OM    | Paused          |          |            |
| 15 | scheduler    | [#349] S-D25.4 Simulation framework SCHEDULER Y4M05                                                                                    | PC,ALL       | **In Progress** |          |            |
| 15 |              | <blockquote>[#350] S-D25.5 Simulation Framework resource allocation Y4M05</blockquote>                                                 | PC, ALL       | **In Progress** |          |            |
|6|scheduler|<blockquote>[#657] Autoscaling - Dynamic Services</blockquote>|PC, ALL|**In Progress**|||
|9|scheduler|<blockquote>[#656] Autoscaling - Computational Backend</blockquote>|PC, ALL|**In Progress**|||
|7|API|[#668] DRC & o2S API|PC, MaG|**Todo**|||
|8|s4l:web|[#519] M1–12 Enhancements of the modeling/simulator/postpro service and framework|IP, OM, MAG, CR|**In Progress**|||
|10|resources|[#618] personalizable resource limits|PC, SAN|Paused|||
| XX |              | <blockquote>[#576] control, provide, and track resources</blockquote>                                                                  |           | **Todo**        |          |            |
| 0  | control      | [#555] coupling API    | EI | ??          |     |     |
| 0  |              | <blockquote>[#510] M4 Modular platform for the generation and exploration of control strategies</blockquote>                           |  EI         | Paused          |          |            |
|11|API|[#686] M2 Query I/O Port Descriptors for Study via API|PC|**Todo**|||
|12|devops|[#655] Storage HW follow-up|DK|**Ongoing**||
|0|integration|[#658] Dynamic Service Deprecation|OM, SAN, DK|**In Progress**|||
|13|filesystem|[#580] osparc-fs: Internals|MaG|Paused|||
|17|portal|[#545] Portal work|IP|**Resolved**|||
|0|iSeg|[#665]  Automatically Save iSeg Output|MaG|**Todo**|||
| 0  | support      | [#594] Add Save Button                                                                                                                 | PC        | **In Progress** |     |    |
| 27 | support      | [#26] support onboarding of SPARC computational models, S-D1, Y3M1-12                                                                  | EI | **Ongoing**     |      |      |
| 28 | support      | [#232] Placeholder for Team Black feedback                                                                                             | EI  | **Ongoing**     |          |            |
| 0  | support      | [#620] Automatically Open iSeg Input                                                                                                   | MAG        | **Todo**        |    |    |
| 0  | support      | [#665] Automatically Save iSeg Output                                                                                                  | MAG        | **Todo**        |          |            |
|0|user request|[#662] Delete study feature: specify study name</blockquote>|OM|**Resolved**|||




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

<!--References PLEASE KEEP ALPHABETICAL ORDER!!! -->

[all]: https://github.com/Surfict
[ane]: https://github.com/GitHK
[bl]: https://github.com/dyollb
[dk]: https://github.com/mrnicegyu11
[cr]: https://github.com/colinRawlings
[ip]: https://github.com/ignapas
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

[#638]: https://github.com/ITISFoundation/osparc-issues/issues/638
[#670]: https://github.com/ITISFoundation/osparc-issues/issues/670
[#617]: https://github.com/ITISFoundation/osparc-issues/issues/617
[#558]: https://github.com/ITISFoundation/osparc-issues/issues/558
[#654]: https://github.com/ITISFoundation/osparc-issues/issues/654
[#355]: https://github.com/ITISFoundation/osparc-issues/issues/355
[#657]: https://github.com/ITISFoundation/osparc-issues/issues/657
[#668]: https://github.com/ITISFoundation/osparc-issues/issues/668
[#519]: https://github.com/ITISFoundation/osparc-issues/issues/519
[#656]: https://github.com/ITISFoundation/osparc-issues/issues/656
[#618]: https://github.com/ITISFoundation/osparc-issues/issues/618
[#686]: https://github.com/ITISFoundation/osparc-issues/issues/686
[#655]: https://github.com/ITISFoundation/osparc-issues/issues/655
[#580]: https://github.com/ITISFoundation/osparc-issues/issues/580
[#545]: https://github.com/ITISFoundation/osparc-issues/issues/545
[#675]: https://github.com/ITISFoundation/osparc-issues/issues/675
[#428]: https://github.com/ITISFoundation/osparc-issues/issues/428
[#529]: https://github.com/ITISFoundation/osparc-issues/issues/529
[#701]: https://github.com/ITISFoundation/osparc-issues/issues/701
[#702]: https://github.com/ITISFoundation/osparc-issues/issues/702
[#700]: https://github.com/ITISFoundation/osparc-issues/issues/700
[#688]: https://github.com/ITISFoundation/osparc-issues/issues/688
[#693]: https://github.com/ITISFoundation/osparc-issues/issues/693
[#594]: https://github.com/ITISFoundation/osparc-issues/issues/594
[#658]: https://github.com/ITISFoundation/osparc-issues/issues/658
[#665]: https://github.com/ITISFoundation/osparc-issues/issues/665
[#652]: https://github.com/ITISFoundation/osparc-issues/issues/652
[#662]: https://github.com/ITISFoundation/osparc-issues/issues/662
[#412]: https://github.com/ITISFoundation/osparc-issues/issues/412
[#626]: https://github.com/ITISFoundation/osparc-issues/issues/626
[#638]: https://github.com/ITISFoundation/osparc-issues/issues/638
[#617]: https://github.com/ITISFoundation/osparc-issues/issues/617
[#513]: https://github.com/ITISFoundation/osparc-issues/issues/513
[#579]: https://github.com/ITISFoundation/osparc-issues/issues/579
[#580]: https://github.com/ITISFoundation/osparc-issues/issues/580
[#578]: https://github.com/ITISFoundation/osparc-issues/issues/578
[#558]: https://github.com/ITISFoundation/osparc-issues/issues/558
[#618]: https://github.com/ITISFoundation/osparc-issues/issues/618
[#91]: https://github.com/ITISFoundation/osparc-issues/issues/91
[#519]: https://github.com/ITISFoundation/osparc-issues/issues/519
[#349]: https://github.com/ITISFoundation/osparc-issues/issues/349
[#545]: https://github.com/ITISFoundation/osparc-issues/issues/545
[#621]: https://github.com/ITISFoundation/osparc-issues/issues/621
[#626]: https://github.com/ITISFoundation/osparc-issues/issues/626
[#353]: https://github.com/ITISFoundation/osparc-issues/issues/353
[#354]: https://github.com/ITISFoundation/osparc-issues/issues/354
[#625]: https://github.com/ITISFoundation/osparc-issues/issues/625
[#515]: https://github.com/ITISFoundation/osparc-issues/issues/515
[#516]: https://github.com/ITISFoundation/osparc-issues/issues/516
[#355]: https://github.com/ITISFoundation/osparc-issues/issues/355
[#555]: https://github.com/ITISFoundation/osparc-issues/issues/555
[#510]: https://github.com/ITISFoundation/osparc-issues/issues/510
[#546]: https://github.com/ITISFoundation/osparc-issues/issues/546
[#428]: https://github.com/ITISFoundation/osparc-issues/issues/428
[#509]: https://github.com/ITISFoundation/osparc-issues/issues/509
[#576]: https://github.com/ITISFoundation/osparc-issues/issues/576
[#350]: https://github.com/ITISFoundation/osparc-issues/issues/350
[#26]: https://github.com/ITISFoundation/osparc-issues/issues/26
[#232]: https://github.com/ITISFoundation/osparc-issues/issues/232
[#529]: https://github.com/ITISFoundation/osparc-issues/issues/529
[#654]: https://github.com/ITISFoundation/osparc-issues/issues/654
[#594]: https://github.com/ITISFoundation/osparc-issues/issues/594
[#657]: https://github.com/ITISFoundation/osparc-issues/issues/657
[#656]: https://github.com/ITISFoundation/osparc-issues/issues/656
[#655]: https://github.com/ITISFoundation/osparc-issues/issues/655
[#620]: https://github.com/ITISFoundation/osparc-issues/issues/620
[#658]: https://github.com/ITISFoundation/osparc-issues/issues/658
[#665]: https://github.com/ITISFoundation/osparc-issues/issues/665