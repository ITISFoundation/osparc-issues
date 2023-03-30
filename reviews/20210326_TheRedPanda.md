# Review Meeting - 2021/03/26 @ 10:45

- Sprint
  - **The Red Panda** (Cute being)
  - 🕐 PM1(05/03)-PM2(09/03) -(*12 wd*)- RM(26/03)
  - Scrum Master: [IP], [ALL]
- **Dashboards** 📊
  - [Product Backlog](https://github.com/orgs/ITISFoundation/projects/3) (PO view)
  - [Scrum Wall](https://app.zenhub.com/workspaces/osparc---scrum-wall-5c9260f3d76ef51f6b0fe78d/board?repos=118596920,174557929,151701223,135289610,118910047,181836792,167586968)  (Developers view)
  - Activity: [sprint-PRs] and [sprint-MRs]
- **Deployed environments** 🚀
  - AWS cluster (us-east-1)
    - [staging_aws](https://staging.osparc.io) (Testers only - [changelogs])
    - [production_aws](https://osparc.io) ([changelogs])
  - Z43 cluster (ch-zh)
    - [staging_z43](http://osparc-staging.speag.com) (Testers only - [changelogs])
    - [production_z43](http://osparc.speag.com) ([changelogs])
  - [master](https://osparc-master.speag.com) (ch-zh) (Developers only)
- **User entries**
  - [osparc-issues](https://github.com/ITISFoundation/osparc-issues/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions)
  - [resolved fogbugz cases during this sprint](https://z43.manuscript.com/f/filters/?ixProject=45&ixStatus=0&maxrecords=50&resolvedInLast=3&sColumns=Category-Favorite-Case-TitleComment-Area-Priority-Status-DateResolved-DateOpened-OpenedBy&sSorts=LastUpdated.descending-Priority&sView=grid-flat)

## Agenda

| Issue  | Title                                                                         | Presenter            | Status               | Duration   | Start Time |
| ------ | ----------------------------------------------------------------------------- | -------------------- | -------------------- | ---------- | ---------- |
| [#405] | eth lecture                                                                   | [SAN] / [team]       | In progress          | 3min       |     10:45       |
| [#403] | working group: workshop follow-up                                             | [MaG]                | In progress          | 1min       |    10:48        |
| [#328] | S-D22 .1 Meta-Modeling Infrastructure Y4M08                                   | [MaG]                | In progress          | 1min      |      10:49      |
| [#342] | J-D18.2. data-awareness-Python-layer for JupyterLab Y4M06                     | [PC]                 | In progress          | 3min       |    10:50        |
| [#331] | S-D25 .1 Simulation Framework FUNCTIONALITY Y4M04                             | [MaG]                | In progress          | 10min     |    10:53        |
| [#304] | Prep2Go: creating features to support complex S4L scripts                     | [PC]                 | In progress          | 10min     |    11:03        |
| [#428] | maintenance/scaling of the platform                                           | [SAN]                | In progress          | 10min      |    11:13        |
| [#349] | S-D25.4 Simulation Framework SCHEDULER Y4M05                                  | [SAN] / [ANE]        | In progress          | 7min       |   11:23         |
| [#356] | S-D24 .3/.4 o2S2PARC framework metadata and TSR Y4M04                         | [OM] / [PC]          | In progress          | 1min           |   11:30         |
| [#407] | UI: S4L/ EM Sim Service                                                       | [MAG]                | Paused               | 1min       |    11:31        |
| [#91]  | TI Treatment Planning                                                         | [MaG]                | Paused               | 0min       |    11:32        |
| [#410] | Gitlab Failover & High Availability Setup                                     | [ANE]                | In progress          | 2min       |      11:32      |
| [#425] | export into SDS format                                                        | [ANE]                | Done                 | 8min       |      11:34      |
| [#350] | S-D25 .4 Simulation Framework resource allocation Y4M05                       | [ALL]                | Paused               | 0min       |    11:42        |
| [#333] | S-D27 .1 User-Driven Service Creation iframe elements Y4M06                   | [KZ] / [MAG]         | In progress          | 10min      |    11:42        |
| [#26]  | support onboarding of SPARC computational mode, S-D1, Y3M1-12                 | [KZ]                 | Ongoing              | 2min       |    11:52        |
| [#232] | Placeholder for Team Black feedback                                           | [OM]                 | Ongoing              | 12min      |     11:54       |
| [#325] | S-D6 Provenance and Change History of (Derived) Data and Models Y4M03         | [PC]                 | Paused               | 0min       |    12:06        |
| [#343] | J-D13.1.5 Dynamic dataset viewer simulation component Y4M03                   | [PC]                 | In progress          | 1min       |     12:06       |
| [#363] | modeler & postpro completeness                                                | [MaG]                | Paused               | 0min       |      12:07      |
| *      | Update on DevOps                                                              | [ALL]                | Ongoing              | 3min          |   12:07         |
| *      | Platform stability [[#1426]]: [online]+[operational]+[performant]?            | [SAN]                | Ongoing              | see [#428] |      12:10      |
| *      | Others                                                                        |



[online]:http://status.osparc.io/
[operational]:https://git.speag.com/oSparc/e2e-testing/-/pipelines
[performant]:https://git.speag.com/oSparc/e2e-portal-testing/-/pipelines


## Progress

Needs PO update, see previous reviews

## Blockers

Needs PO update, see previous reviews


<!--References PLEASE KEEP ALPHABETICAL ORDER!!! -->

[#5]:https://github.com/ITISFoundation/osparc-issues/issues/5
[#6]:https://github.com/ITISFoundation/osparc-issues/issues/6
[#8]:https://github.com/ITISFoundation/osparc-issues/issues/8
[#9]:https://github.com/ITISFoundation/osparc-issues/issues/9
[#12]:https://github.com/ITISFoundation/osparc-issues/issues/12
[#13]:https://github.com/ITISFoundation/osparc-issues/issues/13
[#16]:https://github.com/ITISFoundation/osparc-issues/issues/16
[#18]:https://github.com/ITISFoundation/osparc-issues/issues/18
[#21]:https://github.com/ITISFoundation/osparc-issues/issues/21
[#22]:https://github.com/ITISFoundation/osparc-issues/issues/22
[#24]:https://github.com/ITISFoundation/osparc-issues/issues/24
[#26]:https://github.com/ITISFoundation/osparc-issues/issues/26
[#31]:https://github.com/ITISFoundation/osparc-issues/issues/31
[#68]:https://github.com/ITISFoundation/osparc-issues/issues/68
[#91]:https://github.com/ITISFoundation/osparc-issues/issues/91
[#93]:https://github.com/ITISFoundation/osparc-issues/issues/93
[#130]:https://github.com/ITISFoundation/osparc-issues/issues/130
[#162]:https://github.com/ITISFoundation/osparc-issues/issues/162
[#163]:https://github.com/ITISFoundation/osparc-issues/issues/163
[#164]:https://github.com/ITISFoundation/osparc-issues/issues/164
[#166]:https://github.com/ITISFoundation/osparc-issues/issues/166
[#232]:https://github.com/ITISFoundation/osparc-issues/issues/232
[#264]:https://github.com/ITISFoundation/osparc-issues/issues/264
[#265]:https://github.com/ITISFoundation/osparc-issues/issues/265
[#266]:https://github.com/ITISFoundation/osparc-issues/issues/266
[#273]:https://github.com/ITISFoundation/osparc-issues/issues/273
[#304]:https://github.com/ITISFoundation/osparc-issues/issues/304
[#306]:https://github.com/ITISFoundation/osparc-issues/issues/306
[#307]:https://github.com/ITISFoundation/osparc-issues/issues/307
[#309]:https://github.com/ITISFoundation/osparc-issues/issues/309
[#325]:https://github.com/ITISFoundation/osparc-issues/issues/325
[#326]:https://github.com/ITISFoundation/osparc-issues/issues/326
[#327]:https://github.com/ITISFoundation/osparc-issues/issues/327
[#328]:https://github.com/ITISFoundation/osparc-issues/issues/328
[#329]:https://github.com/ITISFoundation/osparc-issues/issues/329
[#331]:https://github.com/ITISFoundation/osparc-issues/issues/331
[#332]:https://github.com/ITISFoundation/osparc-issues/issues/332
[#333]:https://github.com/ITISFoundation/osparc-issues/issues/333
[#341]:https://github.com/ITISFoundation/osparc-issues/issues/341
[#342]:https://github.com/ITISFoundation/osparc-issues/issues/342
[#343]:https://github.com/ITISFoundation/osparc-issues/issues/343
[#344]:https://github.com/ITISFoundation/osparc-issues/issues/344
[#345]:https://github.com/ITISFoundation/osparc-issues/issues/345
[#348]:https://github.com/ITISFoundation/osparc-issues/issues/348
[#349]:https://github.com/ITISFoundation/osparc-issues/issues/349
[#350]:https://github.com/ITISFoundation/osparc-issues/issues/350
[#356]:https://github.com/ITISFoundation/osparc-issues/issues/356
[#363]:https://github.com/ITISFoundation/osparc-issues/issues/363
[#365]:https://github.com/ITISFoundation/osparc-issues/issues/365
[#393]:https://github.com/ITISFoundation/osparc-issues/issues/393
[#399]:https://github.com/ITISFoundation/osparc-issues/issues/399
[#403]:https://github.com/ITISFoundation/osparc-issues/issues/403
[#404]:https://github.com/ITISFoundation/osparc-issues/issues/404
[#405]:https://github.com/ITISFoundation/osparc-issues/issues/405
[#406]:https://github.com/ITISFoundation/osparc-issues/issues/406
[#407]:https://github.com/ITISFoundation/osparc-issues/issues/407
[#410]:https://github.com/ITISFoundation/osparc-issues/issues/410
[#425]:https://github.com/ITISFoundation/osparc-issues/issues/425
[#428]:https://github.com/ITISFoundation/osparc-issues/issues/428
[#436]:https://github.com/ITISFoundation/osparc-issues/issues/436

[#54]:https://github.com/ITISFoundation/osparc-simcore/issues/54
[#496]:https://github.com/ITISFoundation/osparc-simcore/issues/496
[#505]:https://github.com/ITISFoundation/osparc-simcore/issues/505
[#1204]:https://github.com/ITISFoundation/osparc-simcore/issues/1204
[#1426]:https://github.com/ITISFoundation/osparc-simcore/issues/1426

[#38]:https://github.com/ITISFoundation/osparc-services/pull/38

[ALL]:https://github.com/Surfict
[IP]:https://github.com/ignapas
[KZ]:https://github.com/KZzizzle
[MaG]:https://github.com/mguidon
[OM]:https://github.com/odeimaiz
[PC]:https://github.com/pcrespov
[SAN]:https://github.com/sanderegg
[ANE]:https://github.com/GitHK
[TN]:https://itis.swiss/who-we-are/staff-members/all-staff/newton-taylor/


[J-D4]:https://github.com/ITISFoundation/osparc-issues/issues/62
[J-D7.a]:https://github.com/ITISFoundation/osparc-issues/issues/21
[J-D35]:https://github.com/ITISFoundation/osparc-issues/issues/31
[J-D33]:https://github.com/ITISFoundation/osparc-issues/issues/33
[J-D20]:https://github.com/ITISFoundation/osparc-issues/issues/48
[J-D21]:https://github.com/ITISFoundation/osparc-simcore/issues/1065
[J-D28.a]:https://github.com/ITISFoundation/osparc-simcore/issues/1066
[J-D29]:https://github.com/ITISFoundation/osparc-issues/issues/37

[S-D2]:https://github.com/ITISFoundation/osparc-simcore/issues/1069
[S-D18]:https://github.com/ITISFoundation/osparc-issues/issues/9
[S-D7]:https://github.com/ITISFoundation/osparc-issues/issues/21
[S-D10]:https://github.com/ITISFoundation/osparc-issues/issues/18
[S-D22]:https://github.com/ITISFoundation/osparc-issues/issues/5
[S-D12]:https://github.com/ITISFoundation/osparc-issues/issues/16
[S-D15]:https://github.com/ITISFoundation/osparc-issues/issues/12
[S-D12]:https://github.com/ITISFoundation/osparc-issues/issues/16
[S-D6]:https://github.com/ITISFoundation/osparc-issues/issues/22
[S-D5]:https://github.com/ITISFoundation/osparc-issues/issues/23
[S-D21]:https://github.com/ITISFoundation/osparc-issues/issues/6
[S-D4]:https://github.com/ITISFoundation/osparc-issues/issues/24
[S-D1]:https://github.com/ITISFoundation/osparc-issues/issues/26
[S-D26]:https://github.com/ITISFoundation/osparc-issues/issues/332

[N-D1]:https://github.com/ITISFoundation/osparc-issues/issues/68
[N-D2]:https://github.com/ITISFoundation/osparc-issues/issues/91

[TB-Backlog]:https://github.com/ITISFoundation/osparc-issues/projects/4
[Z43-Backlog]:https://z43.fogbugz.com/f/filters/1112/osparc-cases

[sprint-PRs]:https://github.com/pulls?q=is%3Apr+archived%3Afalse+user%3AITISFoundation+created%3A%3E2021-03-09
[sprint-MRs]:https://git.speag.com/groups/oSparc/-/merge_requests?scope=all&utf8=%E2%9C%93&state=all
[changelogs]:https://github.com/ITISFoundation/osparc-simcore/releases
