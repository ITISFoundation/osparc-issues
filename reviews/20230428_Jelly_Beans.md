# Review Meeting - 28/04/2023 @ 10:00 CET

## Sprint 🏃
- **Jelly Beans**
- 🕐 PM1(04/04) - RM(28/04)
- Scrum Master: [SAN]

### Users Feedback

- [closed](https://github.com/issues?q=is%3Aissue+user%3AITISFoundation+archived%3Afalse+is%3Aclosed+label%3AFeedback+closed%3A%3E2023-03-30+) since last RM
- [opened](https://github.com/ITISFoundation/osparc-issues/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions)

### Dashboards 📊

- [Product Backlog](https://github.com/orgs/ITISFoundation/projects/3) (PO view)
- [Sprint Scrum Wall](https://github.com/orgs/ITISFoundation/projects/9) (developers view)
- Activity: [sprint-PRs](https://github.com/pulls?q=is%3Apr+user%3AITISFoundation+archived%3Afalse+milestone%3A%22Jelly+Beans%22) and [sprint-MRs](https://git.speag.com/groups/oSparc/-/merge_requests)

### Deployed environments 🚀

- AWS cluster (us-east-1)
  - [staging_aws](https://staging.osparc.io) (Testers only)
  - [production_aws](https://osparc.io)
- Z43 cluster (ch-zh)
  - [staging_z43](http://osparc-staging.speag.com) (Testers only)
  - [production_z43](http://osparc.speag.com)
  - [ti-plan.itis.swiss](http://ti-plan.itis.swiss)
  - [master](https://osparc-master.speag.com) (developers only)

- [Platform releases](https://github.com/ITISFoundation/osparc-simcore/releases)

| PO  | Topic        | Title                                                                             | Presenter | Status      | Start-Time | Duration |
| --- | ------------ | --------------------------------------------------------------------------------- | --------- | ----------- | ---------- | -------- |
| 1   | API          | [#830] Portal - OSPARC connection                                                 | [PC]      |             |    10:05        |        |
|     |              | <blockquote>[#682] M7 Pulling files from Portal</blockquote>                             |           | In Progress |            |   3'         |
|     |              | <blockquote>[#683] M7 Create (Model) Service Section on the Portal</blockquote>          |           | Resolved    |            |   1'      |
|     |              | <blockquote>[#711] M4 Launch Computational Study Parameters from Portal</blockquote>     |           | In Progress |            |   2'       |
|     |              | <blockquote>[#681] M4 support MAP-Core for simulation on the Portal</blockquote>         |           | OnGoing     |            |   1'      |
|     |              | <blockquote>[#673] M9 SDS and cMIS (model-related metadata exposed on the Portal)</blockquote> |     | ToDo        |            |   1'       |
| 7   | metamodeling | [#767] metamodeling framework (functionality for cedric and mads)                 | [PC]      | In Progress |   10:13         |    4'      |
| 8   | dy-services  | [#638] improving dynamic-sidecar design                                           | [SAN] ([ANE])     | In Progress |    10:17        |     2'     |
| 9   | z43          | [#885] AppTeam Std Simulations on S4L/AWS                                         | [SAN] ([MaG]) | In Progress |10:19 |    2'      |
| 10  | z43          | [#933] 🚀s4l:web                                                                 | [CR] | In Progress  |10:21 | CR(+BL): 8'         |
| 12  | z43          | [#929] "Anonymous User Experience" Mode                                           | [OM]      | In Progress |    10:29        |    2'    |
| 13  | z43          | [#931] S4L Introduction Mode, Helpers/Tippies                                     | [OM]      | In Progress |   10:31         |    3'    |
| 14  | user_request | [#886] user requests (10%)                                                        | [OM] [...]| Ongoing     |    10:34        |    5'    |
| 15   | z43          | [#831] TIP v2                                                                    | [SAN]          | Paused      |    10:39        |    0'    |
|   | z43          | <blockquote>[#880] placeholder TIP field libraries</blockquote>                     | [SAN]          | Paused      |            |    0'   |
| 16 | z43         | [#930] UX: Introductory Mode for Simulation Tab | [SAN] ([MaG] [IP]) | ToDo |  | 0'  |
| 17 | z43         | [#923] Product Design: Web Presence, Product                                        | [OM]      | Resolved    |   10:39         | 3'      |
| 18 | z43         | [#922] Billing & Tracking: User Metrics |  [ALL] ([DK])    | Ongoing |10:42 | 2' |
| 19  | metrics      | [#881] basic monitoring functionality                                             | [ALL] ([DK])      | In Progress |   10:44      |  1'      |
| 20  | resources    | [#920] Resource Control: Personalized Resources | [SAN] | In Progress | 10:45| 0' |
| 21  | resources    | <blockquote>[#618] personalizable resource limits</blockquote>                                             | [SAN]     | In Progress |    10:45        | 1'       |
| 22  |              | [#917] Users notify users | [PC] [OM] | ToDo |10:46 | 0' |
| 23  | app          | [#694] M1-12 Proactive onboarding of services and models                          | [EI]      | Ongoing     |    10:46        |   5'    |
| 24  | maintenance  | [#675] M1-12 Maintenance and DevOps                                               | [PC] [ALL] | Ongoing    |   10:51        |   3'+2'     |
| 25  | portal       | [#674] M1-12 Portal development work                                              | [SAN] ([IP])      | Ongoing     |   10:56         |   0'     |





##### Status Legend

- _Todo_: no work done on this issue. This is the first time it apprears in a sprint.
- _Paused_: this issue was not scheduled/skipped for this sprint
- _In Progress_: this issue is still under development
- _Resolved_: no more work left to do on this issue. PO can review an decide to close or reopen.
- _Ongoing_: a recurrent task

[online]: http://status.osparc.io/
[operational]: https://git.speag.com/oSparc/e2e-testing/-/pipelines
[performant]: https://git.speag.com/oSparc/e2e-portal-testing/-/pipelines


[#355]: https://github.com/ITISFoundation/osparc-issues/issues/355
[#618]: https://github.com/ITISFoundation/osparc-issues/issues/618
[#638]: https://github.com/ITISFoundation/osparc-issues/issues/638
[#654]: https://github.com/ITISFoundation/osparc-issues/issues/654
[#657]: https://github.com/ITISFoundation/osparc-issues/issues/657
[#668]: https://github.com/ITISFoundation/osparc-issues/issues/668
[#673]: https://github.com/ITISFoundation/osparc-issues/issues/673
[#674]: https://github.com/ITISFoundation/osparc-issues/issues/674
[#675]: https://github.com/ITISFoundation/osparc-issues/issues/675
[#676]: https://github.com/ITISFoundation/osparc-issues/issues/676
[#681]: https://github.com/ITISFoundation/osparc-issues/issues/681
[#682]: https://github.com/ITISFoundation/osparc-issues/issues/682
[#683]: https://github.com/ITISFoundation/osparc-issues/issues/683
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
[#878]: https://github.com/ITISFoundation/osparc-issues/issues/878
[#879]: https://github.com/ITISFoundation/osparc-issues/issues/879
[#880]: https://github.com/ITISFoundation/osparc-issues/issues/880
[#881]: https://github.com/ITISFoundation/osparc-issues/issues/881
[#885]: https://github.com/ITISFoundation/osparc-issues/issues/885
[#886]: https://github.com/ITISFoundation/osparc-issues/issues/886
[#917]: https://github.com/ITISFoundation/osparc-issues/issues/917
[#920]: https://github.com/ITISFoundation/osparc-issues/issues/920
[#922]: https://github.com/ITISFoundation/osparc-issues/issues/922
[#923]: https://github.com/ITISFoundation/osparc-issues/issues/923
[#929]: https://github.com/ITISFoundation/osparc-issues/issues/929
[#930]: https://github.com/ITISFoundation/osparc-issues/issues/930
[#931]: https://github.com/ITISFoundation/osparc-issues/issues/931
[#933]: https://github.com/ITISFoundation/osparc-issues/issues/933


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
