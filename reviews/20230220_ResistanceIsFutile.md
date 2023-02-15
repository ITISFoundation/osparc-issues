# Review Meeting - 20/02/2023 @ 10:00 CET

## Sprint 🏃

<img width="931" alt="image" src="https://user-images.githubusercontent.com/32402063/219133918-f976243e-3cfd-4e43-8de1-c4a518843e47.png">

- **Resistance is Futile** (Call sign of some badass space vikings)
- 🕐 PM1(Jan18) - RM(Feb20)
- Scrum Master: [MaG]

### Users Feedback

- [closed](https://github.com/pulls?q=is%3Apr+archived%3Afalse+user%3AITISFoundation+closed%3A%3E2023-01-11) since last RM
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


| PO  | Topic        | Title                                                                             | Presenter | Status   | Start-Time | Duration |
| --- | ------------ | --------------------------------------------------------------------------------- | --------- | -------- | ---------- | -------- |
| 1   | dy-services  | [#638] improving dynamic-sidecar design                                           |           |          |            |          |
| 2   | devops       | [#657] Autoscaling - Dynamic Services                                             |           |          |            |          |
| 3   | s4l-lite     | <em>S4L<sup>lite</sup></em>                                                       |           |          |            |          |
| 4   |              | <blockquote>Platform updates</blockquote>                                         |           |          |            |          |
| 5   |              | <blockquote>Application Updates</blockquote>                                      |           |          |            |
| 6   |              | <blockquote>Internet Blocking/Video Streaming/Turn</blockquote>                   | [MaG]     | Resolved | 10'        |          |
| 8   | API          | [#830] Portal - osparc connection                                                 |           |          |            |          |
| 9   | platform     | [#829] you need to be logged in                                                   |           |          |            |          |
| 10  | TIP          | [#831] TIP v2                                                                     |           |          |            |          |
| 11  | resources    | [#618] personalizable resource limits                                             |           |          |            |          |
| 12  | app          | [#694] M1-12 Proactive onboarding of services and models                          |           |          |            |          |
| 13  | metamodeling | [#767] metamodeling framework (functionality for cedric and mads)                 | [PC]      | Paused   |            |          |
| 7   |              | <blockquote>[#693] M4 Creation of Own osparc services   </blockquote>             |           |          |            |          |
| 15  |              | <blockquote>[#355] S-D22.4 Meta-Modeling optimizer module Y4M12</blockquote>      |           |          |            |          |
| 14  | maintenance  | [#675] M1-12 Maintenance and DevOps                                               |           |          |            |          |
| 16  | API          | [#711] M4 Launch Computational Study Parameters from Portal                       |           |          |            |          |
| 17  |              | <blockquote>[#681] M4 Support MAP-Core for simulations on the Portal</blockquote> | [PC]      | Ongoing  | 1'         |          |
| 20  |              | <blockquote>[#668] DRC & o2S API</blockquote>                                     | [PC]      | Ongoing  | 1'         |          |
| 18  | portal       | [#674] M1-12 Portal development work                                              |           |          |            |          |


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

[#355]: https://github.com/ITISFoundation/osparc-issues/issues/355
[#618]: https://github.com/ITISFoundation/osparc-issues/issues/618
[#638]: https://github.com/ITISFoundation/osparc-issues/issues/638
[#654]: https://github.com/ITISFoundation/osparc-issues/issues/654
[#657]: https://github.com/ITISFoundation/osparc-issues/issues/657
[#668]: https://github.com/ITISFoundation/osparc-issues/issues/668
[#674]: https://github.com/ITISFoundation/osparc-issues/issues/674
[#675]: https://github.com/ITISFoundation/osparc-issues/issues/675
[#676]: https://github.com/ITISFoundation/osparc-issues/issues/676
[#681]: https://github.com/ITISFoundation/osparc-issues/issues/681
[#693]: https://github.com/ITISFoundation/osparc-issues/issues/693
[#694]: https://github.com/ITISFoundation/osparc-issues/issues/694
[#711]: https://github.com/ITISFoundation/osparc-issues/issues/711
[#740]: https://github.com/ITISFoundation/osparc-issues/issues/740
[#741]: https://github.com/ITISFoundation/osparc-issues/issues/741
[#765]: https://github.com/ITISFoundation/osparc-issues/issues/765
[#766]: https://github.com/ITISFoundation/osparc-issues/issues/766
[#767]: https://github.com/ITISFoundation/osparc-issues/issues/767
[#793]: https://github.com/ITISFoundation/osparc-issues/issues/793
[#829]: https://github.com/ITISFoundation/osparc-issues/issues/829
[#830]: https://github.com/ITISFoundation/osparc-issues/issues/830
[#831]: https://github.com/ITISFoundation/osparc-issues/issues/831


[MD]:https://github.com/matusdrobuliak66
[ALL]:https://github.com/Surfict
[ANE]:https://github.com/GitHK
[BL]:https://github.com/dyollb
[CR]:https://github.com/colinRawlings
[DK]:https://github.com/mrnicegyu11
[EI]:https://github.com/elisabettai
[IP]:https://github.com/ignapas
[MaG]:https://github.com/mguidon
[OM]:https://github.com/odeimaiz
[PC]:https://github.com/pcrespov
[SAN]:https://github.com/sanderegg
[EO]:https://github.com/eofli
[MB]:https://github.com/BouldiMelina
[CF]:https://github.com/cosfor1
[HBS]:https://github.com/habz-bs
