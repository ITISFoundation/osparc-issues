# Review Meeting - July 7, 2023 @ 11:00 CET

<img width="600" alt="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Albert_Eckhout_1610-1666_Brazilian_fruits.jpg/1024px-Albert_Eckhout_1610-1666_Brazilian_fruits.jpg">

## Sprint 🏃
- [**Watermelon**](https://en.wikipedia.org/wiki/Watermelon)
- 🕐 PM1(June 09) - PM2(June 12+13) - RM(July 07)
- Scrum Master: [PC]

### Users Feedback

- [closed](https://github.com/issues?q=is%3Aissue+user%3AITISFoundation+archived%3Afalse+is%3Aclosed+label%3AFeedback+closed%3A%3E2023-06-09+) since last RM
- [opened](https://github.com/ITISFoundation/osparc-issues/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions)

### Dashboards 📊

- [Product Backlog](https://github.com/orgs/ITISFoundation/projects/13) (PO view)
- [Sprint Scrum Wall](https://github.com/orgs/ITISFoundation/projects/9) (developers view)
- Activity: [sprint-PRs](https://github.com/pulls?q=is%3Apr+user%3AITISFoundation+archived%3Afalse+milestone%3A%22Watermelon%22) and [sprint-MRs](https://git.speag.com/groups/oSparc/-/merge_requests)

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

|Topic|Title|Presenter|Status| Start-Time| Duration |
|--|--|--|--|--|--|
|WP1|[#923] sim4life.io - WP1:  Web Presence|[Nik], [OM]|**In Progress**|11:55 |1'|
|WP2|[#949] sim4life.io - WP2: Product|[OM]|**In Progress**|11:56|2'|
|WP3|[#922] sim4life.io - WP3: Tracking of resource usage|[SAN],  [MD]|**In Progress**|11:58| 15'|
|WP4|[#950] sim4life.io - WP4: Computational backend|[SAN]|**In Progress**|||
||<blockquote>[#885] AppTeam Std Simulations on S4L/AWS</blockquote>|-|**In Progress**|||
||<blockquote>[#618] personalizable resource limits</blockquote>|[SAN]|**In Progress**|||
|WP5|[#951] sim4life.io - WP5: Dynamic services backend|[ANE],[SAN]|**In Progress**|12:13|3'|
||<blockquote>[#638] improving dynamic-sidecar design</blockquote>|[ANE]|**In Progress**|12:16|1'|
||<blockquote>[#618] personalizable resource limits</blockquote>|[SAN]|**In Progress**|||
|WP6|[#952] sim4life.io - WP6: API| [PC], [MB]|**In Progress**|12:17|5'|
|WP7|[#953] sim4life.io -  WP7: Platform improvements|[PC]|**In Progress**|||
||<blockquote>[#979] Project home page</blockquote>|[OM], [BL]  |**In Progress**|12:22|5'|
||<blockquote>[#716] Folders in User Workspace</blockquote>|[MD], [OM]|**Todo**|||
||<blockquote>[#977] projects folders</blockquote>|[MD], [OM]|**Duplicated**|||
||<blockquote>[#980] Fast navigation between projects</blockquote>|[MD], [OM], [PC], [SAN]|**Todo**|||
||<blockquote>[#917] Users notify users</blockquote>|[OM]|**Done**|12:27|3'|
|WP8|[#933] sim4life.io - WP8: s4l:web|[CR]|**In Progress**|12:30|7'|
||<blockquote>[#931] S4L Introduction Mode, Helpers/Tippies</blockquote>|[IP]|**In Progress**|12:37| 5'|
||<blockquote>[#881] basic monitoring functionality</blockquote>|[MaG]|**In Progress**|12:42|3'|
||<blockquote>[#621] API framework for iSolve</blockquote>|[MaG]|**In Progress**|12:45|1'|
||<blockquote>[#929] Anonymous User Experience Mode</blockquote>|[MaG], [OM], [PC]|**Todo**|||
||<blockquote>[#930] UX: Introductory Mode for Simulation Tab</blockquote>|[CR], [IP], [MaG]|**Todo**|||
|TIP|[#831] TIP v2|[MaG] |**In Progress**|12:46|1'|
|Y6-M7|[#682] M7 Pulling files from the Portal|[IP] |**Done**|12:47| 5' |
||<blockquote>[#683] M7 Create (Model) Service Section on the Portal</blockquote>|[EI]|**Done**|12:52| 1'|
|ITIS|[#767] metamodeling framework (functionality for cedric and mads)|[PC]|**In Progress**|12:53|2'|
|Y6-API|[#668] DRC & o2S API|[PC], [MB] |**In Progress**|12:55|3'|
||<blockquote>[#690] M10 API for import and export of data</blockquote>|[PC]|**Todo**|||
||<blockquote>[#692] M10 Accept Pointers from DRC API</blockquote>|[PC]|**Todo**|||
||<blockquote>[#710] M12 API tutorial</blockquote>| [MB]|**In Progress**|12:58|1'|
|Y6-M9|[#673] M9 SDS and cMIS (model-related metadata exposed on the Portal)|[ANE]|**In Progress**|12:59|2'|
|Y6-M8|[#697] M8 Attribute (& Charge) Resource Usage| [DK] |**In Progress**|13:01|1'|
|Y6-NIH|[#694] M1-12 Proactive onboarding of services and models|[EI]|**Ongoing**|13:02|8'|
|Y6-MIH|[#711] M4 Launch Computational Study Parameters from Portal| [PC]|**Done**|13:10|1'|
||<blockquote>[#681] M1-12 Support MAP-Core for simulations on the Portal</blockquote>|[PC]|**Ongoing**|13:11|1'|
||<blockquote>[#674] M1-12 Portal development work </blockquote>|[IP]|**Ongoing**|13:12|1'|
|Maintenance|[#675] M1-12 Maintenance and DevOps| [DK], [PC]|**Ongoing**|13:13|6'|
|Z43|[#976] Z43 Energy Monitoring|[DK], [ALL]|**Ongoing**|13:19|2'|
|Z43|[#1000] Sim4Life with Electron: proof of concept|[SCA]|**Ongoing**|13:21|1'|




##### Status Legend

- _Todo_: no work done on this issue. This is the first time it apprears in a sprint.
- _Paused_: this issue was not scheduled/skipped for this sprint
- _In Progress_: this issue is still under development
- _Done_: no more work left to do on this issue. PO can review an decide to close or reopen.
- _Ongoing_: a recurrent task

[online]: http://status.osparc.io/
[operational]: https://git.speag.com/oSparc/e2e-testing/-/pipelines
[performant]: https://git.speag.com/oSparc/e2e-portal-testing/-/pipelines




[#923]: https://github.com/ITISFoundation/osparc-issues/issues/923
[#949]: https://github.com/ITISFoundation/osparc-issues/issues/949
[#922]: https://github.com/ITISFoundation/osparc-issues/issues/922
[#950]: https://github.com/ITISFoundation/osparc-issues/issues/950
[#885]: https://github.com/ITISFoundation/osparc-issues/issues/885
[#618]: https://github.com/ITISFoundation/osparc-issues/issues/618
[#951]: https://github.com/ITISFoundation/osparc-issues/issues/951
[#638]: https://github.com/ITISFoundation/osparc-issues/issues/638
[#952]: https://github.com/ITISFoundation/osparc-issues/issues/952
[#953]: https://github.com/ITISFoundation/osparc-issues/issues/953
[#979]: https://github.com/ITISFoundation/osparc-issues/issues/979
[#716]: https://github.com/ITISFoundation/osparc-issues/issues/716
[#977]: https://github.com/ITISFoundation/osparc-issues/issues/977
[#980]: https://github.com/ITISFoundation/osparc-issues/issues/980
[#917]: https://github.com/ITISFoundation/osparc-issues/issues/917
[#933]: https://github.com/ITISFoundation/osparc-issues/issues/933
[#931]: https://github.com/ITISFoundation/osparc-issues/issues/931
[#881]: https://github.com/ITISFoundation/osparc-issues/issues/881
[#621]: https://github.com/ITISFoundation/osparc-issues/issues/621
[#929]: https://github.com/ITISFoundation/osparc-issues/issues/929
[#930]: https://github.com/ITISFoundation/osparc-issues/issues/930
[#831]: https://github.com/ITISFoundation/osparc-issues/issues/831
[#682]: https://github.com/ITISFoundation/osparc-issues/issues/682
[#683]: https://github.com/ITISFoundation/osparc-issues/issues/683
[#767]: https://github.com/ITISFoundation/osparc-issues/issues/767
[#668]: https://github.com/ITISFoundation/osparc-issues/issues/668
[#690]: https://github.com/ITISFoundation/osparc-issues/issues/690
[#692]: https://github.com/ITISFoundation/osparc-issues/issues/692
[#710]: https://github.com/ITISFoundation/osparc-issues/issues/710
[#673]: https://github.com/ITISFoundation/osparc-issues/issues/673
[#697]: https://github.com/ITISFoundation/osparc-issues/issues/697
[#694]: https://github.com/ITISFoundation/osparc-issues/issues/694
[#711]: https://github.com/ITISFoundation/osparc-issues/issues/711
[#681]: https://github.com/ITISFoundation/osparc-issues/issues/681
[#674]: https://github.com/ITISFoundation/osparc-issues/issues/674
[#675]: https://github.com/ITISFoundation/osparc-issues/issues/675
[#976]: https://github.com/ITISFoundation/osparc-issues/issues/976
[#1000]: https://github.com/ITISFoundation/osparc-issues/issues/1000


[ALL]:https://github.com/Surfict
[ANE]:https://github.com/GitHK
[BL]:https://github.com/dyollb
[CR]:https://github.com/colinRawlings
[DK]:https://github.com/mrnicegyu11
[EI]:https://github.com/elisabettai
[IP]:https://github.com/ignapas
[MB]:https://github.com/bisgaard-itis
[MD]:https://github.com/matusdrobuliak66
[MaG]:https://github.com/mguidon
[Nik]:https://github.com/drniiken
[OM]:https://github.com/odeimaiz
[PC]:https://github.com/pcrespov
[SAN]:https://github.com/sanderegg
[SB]:https://github.com/sbenkler
[SCA]:https://github.com/SCA-ZMT
[TN]:https://github.com/newton1985
[YH]:https://github.com/YuryHrytsuk
