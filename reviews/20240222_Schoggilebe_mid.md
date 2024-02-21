# Mid sprint review Meeting - February 22, 2024

## Sprint 🏃
- [**Schoggilebe**](20240222_Schoggilebe_mid.md)
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
  - [aws_master](https://osparc-master-zmt.click) (developers only)
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
|WP2|[#949] sim4life.io - WP2: Product|[PC], [JQ]| |  |  |
||<blockquote> Preferences for auto update </blockquote>| [JQ]| _Paused_ | 16:00 | 3' |
||<blockquote> Sorting/filtering dashboard </blockquote>| [JQ] | _In Progress_ | 16:05 | 3' |
||<blockquote> Thumbnails </blockquote>| [JQ] | _Done_ | 16:08 | 3' |
|WP7|[#953] sim4life.io - WP7: Platform improvements| | | | |
||<blockquote> Disk space limits (limit based on pricing plan) </blockquote>| [JQ] | _In Progress_ | 16:11 | 3' |
||<blockquote> Polish billing center [#5078] </blockquote>| [IP] [PC] | _In Progress_ | 16:14 | 10' |
|Status| Summary, Showstoppers, Discussion |[MaG]| | 16:24 | 6' |



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
