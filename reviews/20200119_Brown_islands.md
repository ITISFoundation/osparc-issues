# Review Meeting - 2020/01/20@11am

  - Sprint Name: [Brown Islands](https://wiki.lspace.org/mediawiki/Brown_Islands)
  - Scrum Master: [OM]
  - Dashboards
    - [Product Backlog](https://github.com/orgs/ITISFoundation/projects/3)
    - [Dev Dashboard](https://app.zenhub.com/workspaces/osparc---scrum-wall-5c9260f3d76ef51f6b0fe78d/board?milestones=Brown%20Islands%232020-01-20&filterLogic=any&repos=174557929,151701223,167586968,118910047,124380478,210862626,135289610,181836792,118596920&showPRs=false&showClosed=false)
  - Deployed environments
    - [master](https://osparc01.speag.com/) [developers only]
    - [staging](https://staging.osparc.io) [testers only]
    - [production](https://osparc.io)

  - [Release descriptions](https://github.com/ITISFoundation/osparc-simcore/releases)

## Agenda

| Issue            | Title                                                   | Presenter   | Status             | Duration | Time |
| ---------------- | ------------------------------------------------------- | ----------- | ------------------ | ---------| ---- |
| [#505]</br>[#12] | Large Models/Results Rendering & Interaction (M9; D4.a)<br/>Postpro workbench; [S-D15], Y3M6                                   | [MaG]           | In progress        |  5min    |      |
| [#68]</br>[#21]  | Everybody at z43 uses osparc for python/matlab scripting<br/>Simple creation of data-processing modules, [S-D7], Y3M2,4,5,2-12 | [PC]            | In progress        |  5min    |      |
| [#93]            | Move Dalco Cluster to Z43                               | [ALL] [MaG] | In progress        |  3min    |      |
| [#18]            | Macro/templates, towards guided mode, [S-D10], Y3M4     | [OM]        | In progress        |  5min    |      |
| [#5]             | AWS, [S-D22], Y3M5,1-12                                 | [ALL]       | In progress        |  5min    |      |
| [#54]            | Platform Resource Management                            | [SAN]       | In progress | 10min    |      |
| [#6]             | DevOps                                                  | [ALL] [SAN] | In progress        |  5min    |      |
|                  |                                                         |             |                    |          |      |
| [#1204]          | UI Improvements ![](img/pi-issue.png)                   | [IP] [OM]   | In progress        | 10min    |      |



## Progress

| Deliverable | Due | Title                                                                     | % Done | Notes |
| ----------- | --- | ------------------------------------------------------------------------- | ------ | ----- |
| J-D3        | M1  | Retreat prep                                                              | 100    | Retreat has taken place |
| J-D15       | M1  | Documentation agreement                                                   | 75     | Requirements established |
| S-D26       | M1  | Idea Lab subaward                                                         | 100    | The subaward has been setup and preparations are ongoing |
|             |     |                                                                           |        |       |
| [S-D2]      | M2  | OpenCOR / CellML module & PMR S-D2, M2 #1069                              | 75     | First version implemented, will be revisited as part of the simplified creation of data analysis services task |
| [J-D33]     | M2  | Publication linking, J-D33, Y3M2,8 #33                                    | 100     | Meta-data sections throughout SIM-CORE support linking to pdf, webpages; awaiting MAP-CORE functionality to automatically surface publications (based on DOI?) |
| J-D3        | M2  | Retreat                                                                   | 100    |       |
| J-D6.a      | M2  | Conference list                                                           | 50     |       |
| [J-D21]     | M2  | DRC feedback/issue collection and tracking (Infrastructure) - J-D21 #1065 | 100    |       |
| [J-D28.a]   | M2  | Portal testing (Testing and Infrastructure) - J-D28 #1066                 |        | oSPARC end-to-end testing infrastructure established      |
| [J-D7.a]    | M2  | simple creation of data-processing modules, S-D7, Y3M2,4,5,2-12 #21       | 100    | survey drafted, work on functionality started      |
| S-D24       | M2  | UI/UX subaward                                                            | 100    | first phase contracted, ongoing |
| S-D7        |     | data analysis and visualization                                           | 25     | survey has been drafted |
| S-D3g       |     | metrics                                                                   | 75     | metrics have been selected and prepared for presentation to steering committee
|             |     |                                                                           |        |       |
| [S-D18]     | M3  | NEUROFAUNA rat                                                            | 75     |       |
| J-D3e       | M3  | DRC Governance strategies                                                 | 100    |       |
| [J-D4]      | M3  | slide-decks (marketing material)                                          | 80     |       |
| [J-D20]     | M3  | White paper outlining SPARC data standards and QC metrics for SPARC data depositors |        |       |
| [J-D29]     | M3  | Data access/cost structure                                                |        |       |
|             |     |                                                                           |        |       |
| [S-D10]     | M4  | macro/templates, towards guided mode                                      |        |       |
|             |     |                                                                           |        |       |
| [S-D22]     | M5  | AWS                                                                       |        |       |
| [S-D16]     | M5  | o2S2PARC API                                                              |        |       |



## Blockers
- [ ] S-D18: decaying rat prevents reimaging required to properly segment the PNS; registration-based approach will be tried, to merge PNS images from previously scanned rat
- [ ] S-D9: Gazelle requires support in scheduling their meetings and calls with focus groups, stake owners, etc.



<!--References PLEASE KEEP ALPHABETICAL ORDER!!! -->

[#5]:https://github.com/ITISFoundation/osparc-issues/issues/5
[#6]:https://github.com/ITISFoundation/osparc-issues/issues/6
[#12]:https://github.com/ITISFoundation/osparc-issues/issues/12
[#18]:https://github.com/ITISFoundation/osparc-issues/issues/18
[#21]:https://github.com/ITISFoundation/osparc-issues/issues/21
[#54]:https://github.com/ITISFoundation/osparc-simcore/issues/54
[#68]:https://github.com/ITISFoundation/osparc-issues/issues/68
[#93]:https://github.com/ITISFoundation/osparc-issues/issues/93
[#505]:https://github.com/ITISFoundation/osparc-simcore/issues/505
[#1204]:https://github.com/ITISFoundation/osparc-simcore/issues/1204


[ALL]:https://github.com/Surfict
[IP]:https://github.com/ignapas
[KZ]:https://github.com/KZzizzle
[MaG]:https://github.com/mguidon
[OM]:https://github.com/odeimaiz
[PC]:https://github.com/pcrespov
[SAN]:https://github.com/sanderegg


[J-D4]:https://github.com/ITISFoundation/osparc-issues/issues/62
[J-D7.a]:https://github.com/ITISFoundation/osparc-issues/issues/21
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
