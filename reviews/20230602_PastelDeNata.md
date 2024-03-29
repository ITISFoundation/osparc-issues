# Review Meeting - June 2, 2023 @ 10:00 CET

<img width="600" alt="image" src="https://github.com/ITISFoundation/osparc-issues/assets/32402063/1ee34262-8c3d-4fd1-858b-6c98eafb1825">

## Sprint 🏃
- [**Pastel de Nata**](https://en.wikipedia.org/wiki/Pastel_de_nata) 🧁
- 🕐 PM1(May 10) - PM2(May 12+15) - RM(June 2)
- Scrum Master: [PC]

### Users Feedback

- [closed](https://github.com/issues?q=is%3Aissue+user%3AITISFoundation+archived%3Afalse+is%3Aclosed+label%3AFeedback+closed%3A%3E2023-05-01+) since last RM
- [opened](https://github.com/ITISFoundation/osparc-issues/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions)

### Dashboards 📊

- [Product Backlog](https://github.com/orgs/ITISFoundation/projects/13) (PO view)
- [Sprint Scrum Wall](https://github.com/orgs/ITISFoundation/projects/9) (developers view)
- Activity: [sprint-PRs](https://github.com/pulls?q=is%3Apr+user%3AITISFoundation+archived%3Afalse+milestone%3A%22Pastel+de+Nata%22) and [sprint-MRs](https://git.speag.com/groups/oSparc/-/merge_requests)

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


### Agenda 📝

|PO|Topic|Title|Presenter|Status|Duration|Start-Time|
|--|--|--|--|--|--|--|
|1|s4l:web|[#923] sim4life.io - WP1:  Web Presence| [OM] [Nik]  |**In Progress**| 5' |10:05|
|2||<blockquote>[#949] sim4life.io - WP2: Product</blockquote>| [OM] |**In Progress**| 3' |10:10|
|3|resources|[#922] sim4life.io - WP3: Tracking of resource usage| [SAN] |**In Progress**| 4' |10:13|
|4|s4l:web|[#950] sim4life.io - WP4: Computational backend| [SAN] [MaG] |**In Progress**| 8' |10:17|
|5||<blockquote>[#951] sim4life.io - WP5: Dynamic services backend</blockquote>||**In Progress**|||
|6|API|[#952] sim4life.io - WP6: API| [PC] |**In Progress**| 2' |10:25|
|7||[#953] sim4life.io -  WP7: Platform improvements| [PC] |**In Progress**| 2' |10:27|
|8|s4l:web|[#933] sim4life.io - WP8: s4l:web| [MaG], [CR] |**In Progress**| 2' + 1'|10:29|
|9|portal|[#682] M7 Pulling files from the Portal| [PC] on behalf of [IP] |**In Progress**| 1' |10:32|
|10||<blockquote>[#683] M7 Create (Model) Service Section on the Portal</blockquote>| [EI] |**Resolved**| 1'|10:33|
|11|metamodeling|[#767] metamodeling framework (functionality for cedric and mads)| [PC] [MB]  |**In Progress**| 4' |10:34|
|13|API|[#668] DRC & o2S API| [PC] |**In Progress**| 1' |10:38|
|14|TIP|[#831] TIP v2| [OM] |**In Progress**| 2' |10:39 |
|16|dy-services|[#638] improving dynamic-sidecar design| [SAN] on behalf of [ANE] |**In Progress**| 3' |10:41|
|19|user request|[#886] user requests (10%)| |**Ongoing**|||
|12||<blockquote>[#716] Organization of OSPARC User Workspace</blockquote>| [MD] |**In Progress**| 1' |10:44|
|15||<blockquote>[#419] Allow for dynamic number of input ports in dynamic services</blockquote>| [OM] |**Resolved**| 3' |10:45|  
|17||<blockquote>[#909] notify sharer of studies when sharee does not have access to services inside study</blockquote>| [OM] [MD] |**Resolved**| 2' |10:48|
|18||<blockquote>[#747] Clicking on logger while opening large study crashes the browser</blockquote>| [OM] |**In Progress**| 1' |10:50|
|20||[#697] M8 Attribute (& Charge) Resource Usage||**Todo**|||
|21|app|[#684] M1-12 Proactive onboarding of services and models| [EI] |**Ongoing**|3'|10:51|
|22|maintenance|[#675] M1-12 Maintenance and DevOps| [PC] |**Ongoing**| 2' |10:54 |
|23|API|[#711] M4 Launch Computational Study Parameters from Portal| [PC] |**In Progress**| 1' |10:56|
|24||<blockquote>[#681] M4 Support MAP-Core for simulations on the Portal</blockquote>|  [PC] |**Ongoing**| 1' |10:57|
|25|portal|[#674] M1-12 Portal development work | [MaG] on behalf of [IP]  |**Ongoing**| 1' |10:58|
|26|z43|[#885] AppTeam Std Simulations on S4L/AWS| [MaG] |**In Progress**| 1' |10:59|
|27|resources|[#618] personalizable resource limits| [SAN] |**In Progress**| 1' |11:00|
|28|portal|[#673] M9 SDS and cMIS (model-related metadata exposed on the Portal)| [EI] on behalf of [ANE] |**In Progress**|3'|11:01|



##### Status Legend

- _Todo_: no work done on this issue. This is the first time it apprears in a sprint.
- _Paused_: this issue was not scheduled/skipped for this sprint
- _In Progress_: this issue is still under development
- _Resolved_: no more work left to do on this issue. PO can review an decide to close or reopen.
- _Ongoing_: a recurrent task

[online]: http://status.osparc.io/
[operational]: https://git.speag.com/oSparc/e2e-testing/-/pipelines
[performant]: https://git.speag.com/oSparc/e2e-portal-testing/-/pipelines


[#923]: https://github.com/ITISFoundation/osparc-issues/issues/923
[#949]: https://github.com/ITISFoundation/osparc-issues/issues/949
[#922]: https://github.com/ITISFoundation/osparc-issues/issues/922
[#950]: https://github.com/ITISFoundation/osparc-issues/issues/950
[#951]: https://github.com/ITISFoundation/osparc-issues/issues/951
[#952]: https://github.com/ITISFoundation/osparc-issues/issues/952
[#953]: https://github.com/ITISFoundation/osparc-issues/issues/953
[#933]: https://github.com/ITISFoundation/osparc-issues/issues/933
[#682]: https://github.com/ITISFoundation/osparc-issues/issues/682
[#683]: https://github.com/ITISFoundation/osparc-issues/issues/683
[#767]: https://github.com/ITISFoundation/osparc-issues/issues/767
[#716]: https://github.com/ITISFoundation/osparc-issues/issues/716
[#668]: https://github.com/ITISFoundation/osparc-issues/issues/668
[#831]: https://github.com/ITISFoundation/osparc-issues/issues/831
[#419]: https://github.com/ITISFoundation/osparc-issues/issues/419
[#638]: https://github.com/ITISFoundation/osparc-issues/issues/638
[#909]: https://github.com/ITISFoundation/osparc-issues/issues/909
[#747]: https://github.com/ITISFoundation/osparc-issues/issues/747
[#886]: https://github.com/ITISFoundation/osparc-issues/issues/886
[#697]: https://github.com/ITISFoundation/osparc-issues/issues/697
[#684]: https://github.com/ITISFoundation/osparc-issues/issues/684
[#675]: https://github.com/ITISFoundation/osparc-issues/issues/675
[#711]: https://github.com/ITISFoundation/osparc-issues/issues/711
[#681]: https://github.com/ITISFoundation/osparc-issues/issues/681
[#674]: https://github.com/ITISFoundation/osparc-issues/issues/674
[#885]: https://github.com/ITISFoundation/osparc-issues/issues/885
[#618]: https://github.com/ITISFoundation/osparc-issues/issues/618
[#673]: https://github.com/ITISFoundation/osparc-issues/issues/673

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
[MB]:https://github.com/bisgaard-itis
[Nik]:https://github.com/drniiken
