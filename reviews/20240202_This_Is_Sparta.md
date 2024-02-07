# Review Meeting - February 02, 2024
<img width="712" alt="image" src="https://github.com/ITISFoundation/osparc-issues/assets/32402063/7f3f0ae8-8868-487b-98cf-2c10c4999de7">

## Sprint 🏃
- [**This is Sparta!**](20240202_This_Is_Sparta.md)
- Scrum Master: [MB]

### Users Feedback

- [closed](https://github.com/issues?q=is%3Aissue+user%3AITISFoundation+archived%3Afalse+is%3Aclosed+label%3AFeedback+closed%3A%3E2024-01-08+) since last RM
- [opened](https://github.com/ITISFoundation/osparc-issues/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions)

### Dashboards 📊

- [Product Backlog](https://github.com/orgs/ITISFoundation/projects/13) (PO view)
- [Sprint Scrum Wall](https://github.com/orgs/ITISFoundation/projects/9) (developers view)
- Activity: [sprint-PRs](https://github.com/ITISFoundation/osparc-simcore/milestone/73?closed=1) and [sprint-MRs](https://git.speag.com/groups/oSparc/-/merge_requests)

### Deployed environments 🚀

- AWS cluster (us-east-1, ZMT)
  - [master_zmt](https://sim4life.io) (Testers only)
- AWS cluster (us-east-1, STRIDES)
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
|WP1|[#923] sim4life.io - WP1: Web Presence|[NIK], [AL](), [EO]()| |12:32 |3' |
||<blockquote> </blockquote>|[NIK], [AL](), [EO]()| |  | |
|WP2|[#949] sim4life.io - WP2: Product|[PC], [JQ]| | | |
||<blockquote> Logins need to be bound to product </blockquote>|[PC]| **Done** | 12:35 | 2' |
||<blockquote> Preferences for auto update </blockquote>| [JQ]| **Done** | 12:37 |2' |
||<blockquote> Sorting/filtering dashboard </blockquote>| [MaG] | **Todo** |  |0' |
||<blockquote> Thumbnails </blockquote>| [MaG] | **Todo** |  |0' |
|WP3|[#922] sim4life.io - WP3: Tracking of resource usage|[PC], [MD]| | | |
||<blockquote> Misaligned resource tracking </blockquote>|[MD]| **Done** | 12:39 | 3' |
|WP4|[#950] sim4life.io - WP4: Computational backend| [MaG]| | 12:42 |3' |
||<blockquote> Concurrency for computational backend </blockquote>|[MaG]|**Done** |  | |
||<blockquote> Progress reporting for iSolve jobs (multiport/parsing) </blockquote>| [MaG]|**Todo** |  | |
|WP5|[#951] sim4life.io - WP5: Dynamic services backend|[ANE]|**In Progress**| 12:45 | 3' |
||<blockquote> Shutdown cleanly in case credits < 0 </blockquote>|[MB], [ANE]|**In Progress**| | |
||<blockquote> Better log messages  </blockquote>| [ANE] |_In Progress_|  | |
||<blockquote> Spurious premature shutdown of services  </blockquote>| [ANE] |**Todo** |  | |
|WP6|[#952] sim4life.io - WP6: API| [MB], [PC]| | | |
||<blockquote> Block download of results if credits < 0 </blockquote>|[MB]| **Done**| 12:48 |2' |
||<blockquote> Block start of solver job if credits < 0 </blockquote>|[MB]| **Todo**|  |0' |
||<blockquote> Log streaming with > 200 jobs </blockquote>|[MB], [MaG](), [PC]()| **Todo**| 12:50 |1' |
|WP7|[#953] sim4life.io - WP7: Platform improvements| | | | |
||<blockquote> Disk space limits (limit based on pricing plan) </blockquote>| [JQ] | **In Progress**|  | |
||<blockquote> Polish billing center [#5078] </blockquote>| [MD], [IP] | **In progress**|  | 5' |
|WP8|[#933] sim4life.io - WP8: s4l:web|[MaG], [IP], [SCA]| | 12:51 |6' |
||<blockquote> Videostreaming </blockquote>| [MaG] | **Paused**|  | |
||<blockquote> Cursor, Ruler, Linked Tuples </blockquote>| [MaG] | **In progress**|  ||
||<blockquote> Groups in task manager </blockquote>| [MaG] | **In progress**|  | |
||<blockquote> Compression of smash files </blockquote>| [MaG] | **In progress**|  | |
|WP9|[#1030] sim4life.io - WP9: User Privacy|[NC], [DK], [AL]|  **In progress** | 12:57 | 1' |
|WP10|[#1027] Payment Service |[PC], [IP]| **In progress** | 12:58 | 4' |
||<blockquote> Move to self hosted payment gateway and thorough testing </blockquote>| [PC] | **Done** |  | |
||<blockquote> Mails upon recharge (stripe and sim4life)  </blockquote>| [PC] | **In Progress** |  | |
|MetaModelling|[#767] Metamodelling progress |[WVG]| **In progress** | 13:02 | 6' |
|Y7-NIH|[#1093] M1-12 Proactive onboarding of services and models|[EI]|  **Ongoing**| 13:08 | 3' |
|Maintenance|[#1108] [#1109] M1-12 Maintenance and DevOps| [DK], [YH], [SAN], [MD], [PC] |**Ongoing** | 13:11 | 4'|
||<blockquote> [#1101] Docker registry reorganization: images validation and deletion (Harbor?) </blockquote>| [DK], [MaG] | **Todo**| 13:15 | 1'|
|TIP| TI Planning Tool | [MEST] | | | |
||<blockquote> Published TIP v2.2 [#1154, #1158, #1160] </blockquote>| [MEST] | **Done**| 13:16  | 3' |
||<blockquote> Progress on Personalization [#1155] </blockquote>| [MEST]| **In Progress**| 13:19 | 3' |
|Portal| Portal work |[IP]| **In Progress** |  | 1' |
|Status| Summary, Showstoppers, Discussion |[MaG]| | 13:22 | 13' |



##### Status Legend

- _Todo_: no work done on this issue. This is the first time it apprears in a sprint.
- _Paused_: this issue was not scheduled/skipped for this sprint
- _In Progress_: this issue is still under development
- _Done_: no more work left to do on this issue. PO can review an decide to close or reopen.
- _Ongoing_: a recurrent task

[online]: http://status.osparc.io/
[operational]: https://git.speag.com/oSparc/e2e-testing/-/pipelines
[performant]: https://git.speag.com/oSparc/e2e-portal-testing/-/pipelines


[s4l-feedback]: https://z43.fogbugz.com/f/filters/1437/00-Sim4Life-web-Testing-w-Backlog
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
[#885]: https://github.com/ITISFoundation/osparc-issues/issues/885
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
[#681]: https://github.com/ITISFoundation/osparc-issues/issues/681
[#697]: https://github.com/ITISFoundation/osparc-issues/issues/697
[#694]: https://github.com/ITISFoundation/osparc-issues/issues/694
[#711]: https://github.com/ITISFoundation/osparc-issues/issues/711
[#681]: https://github.com/ITISFoundation/osparc-issues/issues/681
[#674]: https://github.com/ITISFoundation/osparc-issues/issues/674
[#675]: https://github.com/ITISFoundation/osparc-issues/issues/675
[#976]: https://github.com/ITISFoundation/osparc-issues/issues/976
[#1000]: https://github.com/ITISFoundation/osparc-issues/issues/1000
[#1027]: https://github.com/ITISFoundation/osparc-issues/issues/1027
[#1030]: https://github.com/ITISFoundation/osparc-issues/issues/1030
[#1031]: https://github.com/ITISFoundation/osparc-issues/issues/1031
[#1032]: https://github.com/ITISFoundation/osparc-issues/issues/1032
[#1073]: https://github.com/ITISFoundation/osparc-issues/issues/1073
[#1074]: https://github.com/ITISFoundation/osparc-issues/issues/1074
[#1093]: https://github.com/ITISFoundation/osparc-issues/issues/1093
[#1099]: https://github.com/ITISFoundation/osparc-issues/issues/1099
[#1108]: https://github.com/ITISFoundation/osparc-issues/issues/1108
[#1109]: https://github.com/ITISFoundation/osparc-issues/issues/1109
[#5078]: https://github.com/ITISFoundation/osparc-simcore/issues/5078

[#gl592]: https://git.speag.com/oSparc/osparc-s4l/-/issues/592
[#gl593]: https://git.speag.com/oSparc/osparc-s4l/-/issues/593
[#gl630]: https://git.speag.com/oSparc/osparc-s4l/-/issues/630

[ANE]:https://github.com/GitHK
[BL]:https://github.com/dyollb
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
[JQ]:https://github.com/jsaq007
[MEST]:https://github.com/konohana0608
[WVG]: https://github.com/wvangeit
