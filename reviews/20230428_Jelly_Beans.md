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
| 1   | API          | [#830] Portal - OSPARC connection                                                 | [PC]  |             |            |        |
|     |              | <blockquote>M7 Pulling files from Portal</blockquote>          |           | In Progress    |            |          |
|     |              | <blockquote>M7 Create (Model) Service Section on the Portal</blockquote>          |           | Resolved    |            |          |
|     |              | <blockquote>M4 Launch Computational Study Parameters from Portal</blockquote>     |           | In Progress |            |          |
|     |              | <blockquote>M4 support MAP-Core for simulation on the Portal</blockquote>     |           | OnGoing |            |          |
|     |              | <blockquote>M9 SDS and cMIS (model-related metadata exposed on the Portal)</blockquote>                     |           | ToDo    |            |          |
| 7   | metamodeling | [#767] metamodeling framework (functionality for cedric and mads)                 | [PC]      | In Progress |                 |          |
| 8   | dy-services  | [#638] improving dynamic-sidecar design                                           | [ANE]     | In Progress |                 |        |
| 9   | z43          | [#885] AppTeam Std Simulations on S4L/AWS                                         | [SAN] ([CF]) ([MaG]) | In Progress |  |        |
| 10  | z43          | [#933] 🚀s4l:web                                                                 | [CR] [Mag] [BL] [OM] | In Progress  |  |    |
| 12  | z43          | [#929] "Anonymous User Experience" Mode | [OM] | ToDo | | |
| 13  | z43          | [#931] S4L Introduction Mode, Helpers/Tippies [OM] | In Progress | | |
| 14  | user_request | [#886] user requests (10%)                                                        | [OM] [...] | Ongoing     |            |       |
| 15   | z43          | [#831] TIP v2                                                                     |  | Paused |   |        |
|   | z43          | <blockquote>[#880] placeholder TIP field libraries</blockquote>                      |  | Paused |   |       |
| 16 | z43         | [#930] UX: Introductory Mode for Simulation Tab | [CR] [OM] [MaG] | ToDo |  |   |
| 17 | z43         | [#923] Product Design: Web Presence, Product | [OM] | Resolved | | |
| 18 | z43         | [#922] Billing & Tracking: User Metrics | [DK] | ToDo | | |
| 19  | metrics      | [#881] basic monitoring functionality                                             | [DK]      | In Progress |            |        |
| 20  | resources    | [#920] Resource Control: Personalized Resources | [SAN] | In Progress | | |
| 21  | resources    | [#618] <blockquote>personalizable resource limits</blockquote>                                             | [SAN]     | In Progress |            | 1'       |
| 22  |              | [#917] Users notify users | [PC] [OM] | ToDo | | |
| 23  | app          | [#694] M1-12 Proactive onboarding of services and models                          | [EI]      | Ongoing     |            |        |
| 24  | maintenance  | [#675] M1-12 Maintenance and DevOps                                               | [PC] [DK] | Ongoing     |            |        |
| 25  | portal       | [#674] M1-12 Portal development work                                              | [IP]      | Ongoing     |            |        |





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
[#878]: https://github.com/ITISFoundation/osparc-issues/issues/878
[#879]: https://github.com/ITISFoundation/osparc-issues/issues/879
[#880]: https://github.com/ITISFoundation/osparc-issues/issues/880
[#881]: https://github.com/ITISFoundation/osparc-issues/issues/881
[#885]: https://github.com/ITISFoundation/osparc-issues/issues/885
[#886]: https://github.com/ITISFoundation/osparc-issues/issues/886


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
