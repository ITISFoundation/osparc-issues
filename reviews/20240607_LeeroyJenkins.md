# Review Meeting - June 07, 2024
<img width="400" alt="image" src="https://github.com/ITISFoundation/osparc-issues/assets/87664284/d60c9ced-eb80-466e-8389-b040b45afa64">

## Sprint 🏃
- [**Leeroy Jenkins**](https://en.wikipedia.org/wiki/Leeroy_Jenkins)
- Scrum Master: [SCA]

### Dashboards 📊

- [POs' Backlog](https://github.com/orgs/ITISFoundation/projects/15/views/14) (PM1)
- [Sprint Scrum Wall](https://github.com/orgs/ITISFoundation/projects/15/views/11) (developers' view)

### Agenda 📝

|Topic|Title|Presenter|Status| Start-Time| Duration |
|--|--|--|--|--|--|
||**DevOps Update**|[DK],[YH]|_Ongoing_||2'
|[#1407]|**Meta-modeling deployed to production**||||
||[#1417] Release to production and testing with selected group of users|[MB]|_Only user testing missing_||3'
|[#1332]|**NIH Year 7**||||
||[#1092] Facilitation of service creation|[EI]|_Done_||2'
||[#1340] sim4life.lite reduced mode (CAD editing)|[MaG]|_Done_||1'
||[#1087] Tutorial 3|[EI]|_Done_||1'
|[#1404]|**Sim4Life service versioning**||||
||[#1419] Release a new sim4life.lite version||_In Progress_||0'
||[#1420] Release 8.0.1 on sim4life.io/.science||_In Progress_||0'
|[#1309]|**TIP v3 on AWS**|[MS], [OM]|_In Progress_||8'
|[#1313]|**Filesystem concept**||| |
||[#1442] Use EFS to cache user data|[MD]|||5'
|[#1327]|**Performance Improvements for Large Projects**|[SAN]|_Ongoing_|| 1'
|[#1328]|**Maintenance / Dev Issues**|[SAN]|_Ongoing_|| 1'
|[#716]|**Project Folders in User Workspace**|[OM]|||2'
|[#1409]|**UX of credits burning**|||
||[#1474] Hide credits indicator by default|[OM]|_Done_||2'
|[#1406]|**Sim4Life Desktop+Web UI Unification**|[SCA]|_In Progress_||1'
|[#1317]|**S4L: UI Form Layouts**|[IP]|_In Progress_||2'
|[#1305]|**sim4life.io User Feedback**||||
||[198087](https://z43.fogbugz.com/f/cases/198087/Improve-search-feature) Improve search feature|[JQ]|_In Progress_||1'
|[#1331]|**S4L Application Features**||||
||[#1471] Parse solver stages|[MaG]|_Done_||1'
||[#1480] Dark themes for manual and API documentation|[MaG]|_Done_||1'
|[#1395]|**App-team admin panel**||_Paused_||
|[#1408]|**Release Notes improvements**||_Paused_||


##### Status Legend

- _Todo_: no work done on this issue. This is the first time it apprears in a sprint.
- _Paused_: this issue was not scheduled/skipped for this sprint
- _In Progress_: this issue is still under development
- _Done_: no more work left to do on this issue. PO can review an decide to close or reopen.
- _Ongoing_: a recurrent task

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


[online]: http://status.osparc.io/
[operational]: https://git.speag.com/oSparc/e2e-testing/-/pipelines
[performant]: https://git.speag.com/oSparc/e2e-portal-testing/-/pipelines

[s4l-feedback]: https://z43.fogbugz.com/f/filters/1437/00-Sim4Life-web-Testing-w-Backlog

[#631]: https://github.com/ITISFoundation/osparc-ops-environments/issues/631
[#632]: https://github.com/ITISFoundation/osparc-ops-environments/issues/632
[#645]: https://github.com/ITISFoundation/osparc-ops-environments/issues/645

[#716]: https://github.com/ITISFoundation/osparc-issues/issues/716
[#1080]: https://github.com/ITISFoundation/osparc-issues/issues/1080
[#1087]: https://github.com/ITISFoundation/osparc-issues/issues/1087
[#1092]: https://github.com/ITISFoundation/osparc-issues/issues/1092
[#1155]: https://github.com/ITISFoundation/osparc-issues/issues/1155
[#1102]: https://github.com/ITISFoundation/osparc-issues/issues/1102
[#1112]: https://github.com/ITISFoundation/osparc-issues/issues/1112
[#1291]: https://github.com/ITISFoundation/osparc-issues/issues/1291
[#1305]: https://github.com/ITISFoundation/osparc-issues/issues/1305
[#1306]: https://github.com/ITISFoundation/osparc-issues/issues/1306
[#1307]: https://github.com/ITISFoundation/osparc-issues/issues/1307
[#1309]: https://github.com/ITISFoundation/osparc-issues/issues/1309
[#1310]: https://github.com/ITISFoundation/osparc-issues/issues/1310
[#1311]: https://github.com/ITISFoundation/osparc-issues/issues/1311
[#1312]: https://github.com/ITISFoundation/osparc-issues/issues/1312
[#1313]: https://github.com/ITISFoundation/osparc-issues/issues/1313
[#1315]: https://github.com/ITISFoundation/osparc-issues/issues/1315
[#1317]: https://github.com/ITISFoundation/osparc-issues/issues/1317
[#1318]: https://github.com/ITISFoundation/osparc-issues/issues/1318
[#1320]: https://github.com/ITISFoundation/osparc-issues/issues/1320
[#1321]: https://github.com/ITISFoundation/osparc-issues/issues/1321
[#1322]: https://github.com/ITISFoundation/osparc-issues/issues/1322
[#1324]: https://github.com/ITISFoundation/osparc-issues/issues/1324
[#1325]: https://github.com/ITISFoundation/osparc-issues/issues/1325
[#1326]: https://github.com/ITISFoundation/osparc-issues/issues/1326
[#1327]: https://github.com/ITISFoundation/osparc-issues/issues/1327
[#1328]: https://github.com/ITISFoundation/osparc-issues/issues/1328
[#1329]: https://github.com/ITISFoundation/osparc-issues/issues/1329
[#1330]: https://github.com/ITISFoundation/osparc-issues/issues/1330
[#1331]: https://github.com/ITISFoundation/osparc-issues/issues/1331
[#1332]: https://github.com/ITISFoundation/osparc-issues/issues/1332
[#1333]: https://github.com/ITISFoundation/osparc-issues/issues/1333
[#1335]: https://github.com/ITISFoundation/osparc-issues/issues/1335
[#1336]: https://github.com/ITISFoundation/osparc-issues/issues/1336
[#1337]: https://github.com/ITISFoundation/osparc-issues/issues/1337
[#1339]: https://github.com/ITISFoundation/osparc-issues/issues/1339
[#1340]: https://github.com/ITISFoundation/osparc-issues/issues/1340
[#1342]: https://github.com/ITISFoundation/osparc-issues/issues/1342
[#1343]: https://github.com/ITISFoundation/osparc-issues/issues/1343
[#1345]: https://github.com/ITISFoundation/osparc-issues/issues/1345
[#1349]: https://github.com/ITISFoundation/osparc-issues/issues/1349
[#1351]: https://github.com/ITISFoundation/osparc-issues/issues/1351
[#1360]: https://github.com/ITISFoundation/osparc-issues/issues/1360
[#1362]: https://github.com/ITISFoundation/osparc-issues/issues/1362
[#1363]: https://github.com/ITISFoundation/osparc-issues/issues/1363
[#1364]: https://github.com/ITISFoundation/osparc-issues/issues/1364
[#1366]: https://github.com/ITISFoundation/osparc-issues/issues/1366
[#1380]: https://github.com/ITISFoundation/osparc-issues/issues/1380
[#1381]: https://github.com/ITISFoundation/osparc-issues/issues/1381
[#1382]: https://github.com/ITISFoundation/osparc-issues/issues/1382
[#1395]: https://github.com/ITISFoundation/osparc-issues/issues/1395
[#1396]: https://github.com/ITISFoundation/osparc-issues/issues/1396
[#1404]: https://github.com/ITISFoundation/osparc-issues/issues/1404
[#1406]: https://github.com/ITISFoundation/osparc-issues/issues/1406
[#1407]: https://github.com/ITISFoundation/osparc-issues/issues/1407
[#1408]: https://github.com/ITISFoundation/osparc-issues/issues/1408
[#1409]: https://github.com/ITISFoundation/osparc-issues/issues/1409
[#1417]: https://github.com/ITISFoundation/osparc-issues/issues/1417
[#1419]: https://github.com/ITISFoundation/osparc-issues/issues/1419
[#1420]: https://github.com/ITISFoundation/osparc-issues/issues/1420
[#1442]: https://github.com/ITISFoundation/osparc-issues/issues/1442
[#1471]: https://github.com/ITISFoundation/osparc-issues/issues/1471
[#1474]: https://github.com/ITISFoundation/osparc-issues/issues/1474
[#1480]: https://github.com/ITISFoundation/osparc-issues/issues/1480


[#5293]: https://github.com/ITISFoundation/osparc-simcore/issues/5293
[#5336]: https://github.com/ITISFoundation/osparc-simcore/issues/5336
[#5493]: https://github.com/ITISFoundation/osparc-simcore/issues/5493
[#5554]: https://github.com/ITISFoundation/osparc-simcore/issues/5554
[#5606]: https://github.com/ITISFoundation/osparc-simcore/issues/5606
[#5614]: https://github.com/ITISFoundation/osparc-simcore/issues/5614
[#5625]: https://github.com/ITISFoundation/osparc-simcore/issues/5625
[#5627]: https://github.com/ITISFoundation/osparc-simcore/issues/5627
[#5628]: https://github.com/ITISFoundation/osparc-simcore/issues/5628
[#5630]: https://github.com/ITISFoundation/osparc-simcore/issues/5630
[#5694]: https://github.com/ITISFoundation/osparc-simcore/issues/5694


[ANE]:https://github.com/GitHK
[BL]:https://github.com/dyollb
[DK]:https://github.com/mrnicegyu11
[EI]:https://github.com/elisabettai
[IP]:https://github.com/ignapas
[MB]:https://github.com/bisgaard-itis
[MD]:https://github.com/matusdrobuliak66
[MaG]:https://github.com/mguidon
[MS]:https://github.com/Konohana0608
[Nik]:https://github.com/drniiken
[OM]:https://github.com/odeimaiz
[PC]:https://github.com/pcrespov
[SAN]:https://github.com/sanderegg
[SB]:https://github.com/sbenkler
[SCA]:https://github.com/SCA-ZMT
[TN]:https://github.com/newton1985
[YH]:https://github.com/YuryHrytsuk
[JQ]:https://github.com/jsaq007
[WVG]: https://github.com/wvangeit
