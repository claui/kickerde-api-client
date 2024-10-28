# pylint: disable=too-many-lines

"""Upstream primary key for a league or tournament."""

from enum import IntEnum


class LeagueId(IntEnum):
    """Upstream primary key for a league or tournament."""

    BUNDESLIGA = 1
    """Bundesliga"""

    BUNDESLIGA_2 = 2
    """2. Bundesliga"""

    DFB_LIGA_3 = 3
    """3. Liga"""

    BUNDESLIGA_WOMEN = 4
    """Google Pixel Frauen-Bundesliga"""

    BUNDESLIGA_PO = 12
    """Bundesliga-Relegation"""

    BUNDESLIGA_2_PO = 23
    """2. Bundesliga-Relegation"""

    RLN = 45
    """Regionalliga Nord"""

    RLNO = 46
    """Regionalliga Nordost"""

    RLW = 47
    """Regionalliga West"""

    RLSW = 48
    """Regionalliga Südwest"""

    RLBY = 49
    """Regionalliga Bayern"""

    FIFA_WORLD_CUP = 101
    """Weltmeisterschaft"""

    DFB_POKAL = 102
    """DFB-Pokal"""

    UEFA_CL = 103
    """Champions League"""

    UEFA_EL = 104
    """Europa League"""

    UEFA_EURO_Q = 106
    """EM-Qualifikation"""

    UEFA_EM = 107
    """Europameisterschaft"""

    UEFA_EL_Q = 109
    """Europa-League-Qualifikation"""

    FIFA_WORLD_CUP_Q_EUROPE = 110
    """WM-Qualifikation Europa"""

    FIFA_WORLD_CUP_Q_ASIA = 111
    """WM-Qualifikation Asien"""

    FIFA_WORLD_CUP_Q_AFRICA = 112
    """WM-Qualifikation Afrika"""

    FIFA_WORLD_CUP_Q_OCEANIA = 113
    """WM-Qualifikation Ozeanien"""

    ASIA_CUP = 114
    """Asien-Cup"""

    FIFA_WORLD_CUP_Q_NORTHERN_AMERICA = 115
    """WM-Qualifikation Nord- und Mittelamerika"""

    UEFA_EM_WOMEN = 117
    """Frauen-EM"""

    FIFA_CONFEDERATIONS_CUP = 118
    """Confederations Cup"""

    FIFA_WORLD_CUP_WOMEN = 119
    """Frauen-WM"""

    UEFA_CL_WOMEN = 120
    """Women's Champions League"""

    OLYMPICS_MEN = 121
    """Olympiaturnier Männer"""

    OLYMPICS_WOMEN = 122
    """Olympiaturnier Frauen"""

    FIFA_U_20_WORLD_CUP = 123
    """U-20-Weltmeisterschaft"""

    UEFA_UNDER21 = 124
    """U-21-Europameisterschaft"""

    HANDBALL_OLYMPICS_MEN = 126
    """Olympiaturnier Männer"""

    HANDBALL_OLYMPICS_WOMEN = 127
    """Olympiaturnier Frauen"""

    BASKETBALL_OLYMPICS_MEN = 129
    """Olympiaturnier Männer"""

    CONCACAF_GOLD = 132
    """CONCACAF-Gold-Cup"""

    FIFA_CLUB_WORLD_CUP = 133
    """Klub-Weltmeisterschaft"""

    ASIA_CUP_Q = 134
    """Asien-Cup Qualifikation"""

    CONMEBOL_LIBERTADORES = 141
    """Copa Libertadores"""

    CONMEBOL_SUDAMERICANA = 142
    """Copa Sudamericana"""

    UEFA_NL = 150
    """UEFA Nations League"""

    UEFA_CONFERENCE_LEAGUE = 160
    """Conference League"""

    UEFA_CONFERENCE_LEAGUE_Q = 161
    """Conference-League-Qualifikation"""

    NBA_PO = 198
    """NBA Play-offs"""

    NHL_PO = 199
    """Stanley Cup - Play-offs"""

    FIFA_U_17_WORLD_CUP = 200
    """U-17-Weltmeisterschaft"""

    CAF_AFCON = 201
    """Afrika-Cup"""

    OFC_NATIONS_CUP = 203
    """Ozeanien-Meisterschaft"""

    CONMEBOL_COPA_AMERICA = 205
    """Copa America"""

    UEFA_UNDER17 = 206
    """U-17-Europameisterschaft"""

    UEFA_UNDER19 = 207
    """U-19-Europameisterschaft"""

    DFB_A_JUNIOREN = 409
    """DM-Endrunde A-Junioren"""

    DFB_B_JUNIOREN = 419
    """DM-Endrunde B-Junioren"""

    DFB_POKAL_JUNIOREN = 420
    """DFB-Junioren-Pokal"""

    PREMIER_LEAGUE = 500
    """Premier League"""

    ICE_HOCKEY_OLYMPICS_MEN = 601
    """Eishockey-Olympiaturnier Männer"""

    ICE_HOCKEY_OLYMPICS_WOMEN = 602
    """Eishockey-Olympiaturnier Frauen"""

    SERIE_A = 700
    """Serie A"""

    LA_LIGA = 900
    """La Liga"""

    FRIENDLIES = 999
    """Freundschaftsspiele"""

    HANDBALL_WORLD_CHAMPIONSHIP = 1001
    """Weltmeisterschaft"""

    LIGUE_1 = 1701
    """Ligue 1"""

    DBU_SUPERLIGA = 1704
    """3F Superliga"""

    OFB_BUNDESLIGA = 1705
    """Admiral-Bundesliga"""

    SFV_SUPER_LEAGUE = 1706
    """Credit Suisse Super League"""

    TURKIYE_SUPER_LIG = 1707
    """Trendyol SüperLig"""

    ELITESERIEN = 1708
    """Eliteserien"""

    EKSTRAKLASA = 1710
    """PKO Ekstraklasa"""

    RBFA_DIVISION_1A = 1711
    """Jupiler Pro League"""

    LPF_LIGA_1 = 1713
    """SuperLiga"""

    J1_LEAGUE = 1714
    """J-League"""

    ALLSVENSKAN = 1715
    """Allsvenskan"""

    PRIMEIRA_LIGA = 1716
    """Liga Portugal Betclic"""

    HNL_1 = 1717
    """1. HNL"""

    CZECH_LEAGUE_1 = 1718
    """Chance Liga"""

    ALPHA_ETHNIKI = 1719
    """Stoiximan Super League"""

    RFU_PREMIER_LEAGUE = 1720
    """Premier Liga"""

    FSS_SUPER_LEAGUE = 1721
    """Mozzart Bet SuperLiga"""

    PARVA_LIGA = 1722
    """Parva Liga"""

    CAMPEONATO_BRASILEIRO_A = 1723
    """Campeonato Brasileiro A"""

    SFZ_LIGA_1 = 1724
    """Niké Liga"""

    PREMJER_LIHA = 1725
    """Premjer-Liha"""

    AFA_LPF = 1726
    """Liga Profesional de Futbol"""

    VEIKKAUSLIIGA = 1727
    """Veikkausliiga"""

    SLOVENSKA_NOGOMETNA_LIGA = 1728
    """Prva Liga Telemach"""

    FMF_SUPER_LIGA = 1729
    """Super Liga - Phase 1"""

    EROVNULI_LIGA = 1730
    """Erovnuli Liga"""

    SCOTTISH_PREMIERSHIP = 1732
    """Scottish Premiership"""

    NED = 1733
    """Eredivisie"""

    CYP = 1734
    """Cyta Championship"""

    VIRS = 1735
    """Virsliga"""

    YKK = 1736
    """Ykkönen"""

    ISR = 1737
    """Ligat Ha'al"""

    SCOM = 1740
    """Scottish Premiership - Meisterrunde"""

    SCOA = 1741
    """Scottish Premiership - Abstiegsrunde"""

    ISL_D1 = 1742
    """Besta deild karla"""

    NIR = 1744
    """Sports Direct Premiership"""

    WAL = 1745
    """Cymru Premier"""

    ALIG = 1746
    """A-Lyga"""

    EST = 1747
    """A. LeCoq Premium Liiga"""

    MAZ = 1748
    """Prva Liga"""

    FR_D1 = 1749
    """Betri deildin"""

    ALB = 1754
    """Kategoria Superiore"""

    AND = 1756
    """Primera Divisio"""

    MLT = 1757
    """BOV Premier League"""

    ASE = 1758
    """Premyer Liqasi"""

    BGRM = 1763
    """Parva Liga - Meisterrunde"""

    BGRA = 1764
    """Parva Liga - Abstiegsrunde"""

    ARM = 1769
    """Armenian Premier League"""

    NSL = 1770
    """Isuzu UTE A-League Men"""

    BIH = 1772
    """wwin liga"""

    LUX = 1773
    """BGL Ligue"""

    MLS = 1776
    """Major League Soccer"""

    MLS_PO = 1777
    """MLS Play-offs"""

    NFLPO = 1778
    """NFL-Play-offs"""

    KAS = 1781
    """Premier League"""

    SMR = 1782
    """Campionato Dilettanti"""

    AUSFIN = 1785
    """Isuzu UTE A-League Men - Finalrunde"""

    MOLPOK = 1786
    """Cupa Moldovei"""

    CHA = 1800
    """Championship"""

    L1 = 1801
    """League One"""

    DEL = 1802
    """Deutsche Eishockey-Liga"""

    NHL = 1803
    """National Hockey League"""

    LIGUE2 = 1804
    """Ligue 2"""

    NFL = 1805
    """National Football League"""

    NBA = 1806
    """National Basketball Association"""

    LALIG2 = 1807
    """La Liga 2"""

    SERIEB = 1808
    """Serie B"""

    NED2 = 1809
    """Keuken Kampioen Divisie"""

    FA = 1810
    """FA Cup"""

    BPOK = 1811
    """Coupe de Belgique"""

    DKPOK = 1812
    """DBU Pokalen"""

    FPOK = 1813
    """Coupe de France"""

    APOK = 1814
    """ÖFB-UNIQA-Cup"""

    COPA = 1815
    """Copa del Rey"""

    COPPA = 1816
    """Coppa Italia"""

    BEK = 1817
    """KNVB Beker"""

    TRPOK = 1818
    """Türkiye Kupasi"""

    DHBPOK = 1819
    """DHB-Pokal Männer"""

    HBL = 1820
    """Bundesliga"""

    HANDBALL_EM = 1821
    """Europameisterschaft"""

    LCUP = 1822
    """League Cup"""

    BEL2 = 1823
    """Challenger Pro League"""

    A_D1 = 1824
    """2. Liga"""

    DK2 = 1825
    """1. Division"""

    CHAL = 1826
    """dieci Challenge League"""

    ASSOCIATION_TEST_MATCHES = 1829
    """Fußball-Vereine Freundschaftsspiele"""

    NATIONAL_TEAMS_TEST_MATCHES = 1830
    """Nationalteams Freundschaftsspiele"""

    ICE_HOCKEY_TEST_MATCHES = 1832
    """Freundschaftsspiele"""

    BASKETBALL_ASSOCIATION_TEST_MATCHES = 1835
    """Freundschaftsspiele Vereine"""

    BASKETBALL_TEST_MATCHES = 1836
    """Freundschaftsspiele"""

    HANDBALL_ASSOCIATION_TEST_MATCHES = 1837
    """Freundschaftsspiele Vereine"""

    HANDBALL_TEST_MATCHES = 1838
    """Freundschaftsspiele"""

    L2 = 1839
    """League Two"""

    ADE = 1840
    """OBOS-ligaen"""

    SWE2 = 1841
    """Superettan"""

    SCO_FA = 1842
    """Scottish FA Cup"""

    CHPOK = 1843
    """Schweizer Cup"""

    SPOK = 1844
    """Svenska Cupen"""

    PPOK = 1845
    """Taca de Portugal"""

    GR2 = 1846
    """Super League 2"""

    HANDBALL_CL = 1849
    """Champions League Männer"""

    FINPOK = 1852
    """Suomen Cup"""

    FINABS = 1853
    """Veikkausliiga - Abstiegsrunde"""

    FINMEI = 1854
    """Veikkausliiga - Meisterrunde"""

    CSA = 1855
    """Championship -  Aufstiegs-Play-offs"""

    L1A = 1856
    """League One -  Aufstiegs-Play-offs"""

    L2A = 1857
    """League Two -  Aufstiegs-Play-offs"""

    ELH = 1858
    """European League"""

    AQ = 1860
    """Aufstiegsspiele Serie A"""

    NMCUP = 1863
    """Norgesmesterskapet"""

    WMQSA = 1865
    """WM-Qualifikation Südamerika"""

    HANDBALL_WMQ = 1867
    """WM-Qualifikation"""

    TEST21 = 1870
    """U-21-Nationalteams Freundschaftsspiele"""

    CLQ = 1872
    """Champions-League-Qualifikation"""

    FRASC = 1875
    """Trophee des Champions"""

    PSC = 1876
    """Supercup"""

    ENGSC = 1877
    """Community Shield"""

    DHB_SC = 1878
    """DHB-Supercup"""

    EMQFR = 1879
    """EM-Qualifikation Frauen"""

    WMQFR = 1880
    """WM-Qualifikation Frauen"""

    TEST20 = 1881
    """U-20-Nationalteams Freundschaftsspiele"""

    SPASC = 1882
    """Supercopa"""

    ALLQ = 1885
    """Schweden Relegation"""

    FINREL = 1886
    """Relegation"""

    ELITEQ = 1888
    """Norwegen Relegation"""

    TESTF = 1890
    """Frauen-Nationalteams Freundschaftsspiele"""

    NLG = 1891
    """National League"""

    NIR_LC = 1892
    """JBE League Cup"""

    SMR_PO = 1896
    """Campionato Play-off"""

    NLA = 1897
    """National League -  Aufstiegs-Play-offs"""

    BBL = 1898
    """easyCredit BBL"""

    SCO_LC = 1902
    """League Cup"""

    HUN = 1904
    """OTP Bank Liga"""

    NIRM = 1908
    """Sports Direct Premiership - Meisterrunde"""

    NIRA = 1909
    """Sports Direct Premiership - Abstiegsrunde"""

    MEX = 1911
    """Liga BBVA MX"""

    MEXPO = 1912
    """Liga BBVA MX - Play-offs"""

    BEL2PO = 1914
    """Challenger Pro League - Play-offs"""

    EIR = 1921
    """Airtricity League"""

    DELPO = 1980
    """DEL Play-offs"""

    SPCUP = 1990
    """Spengler-Cup"""

    OLQ = 1991
    """Olympia-Qualifikation"""

    A_WM = 1992
    """Weltmeisterschaft"""

    CYPOK = 1993
    """Kypello Kyprou"""

    IRLPOK = 1994
    """FAI Cup"""

    UNGPOK = 1995
    """Magyar Kupa"""

    RUMPOK = 1996
    """Cupa Romaniei"""

    UKRPOK = 1997
    """Kubok Ukrainy"""

    SLOPOK = 1998
    """Pokal Slovenije"""

    SRBPOK = 1999
    """Kup Srbije"""

    UEFASC = 2000
    """UEFA-Supercup"""

    ISC = 2001
    """Supercoppa"""

    EMQU21 = 2002
    """EM-Qualifikation U 21"""

    GRPOK = 2004
    """Kypello Elladas"""

    PLPOK = 2005
    """Puchar Polski"""

    SKPOK = 2006
    """Slovenský Pohár"""

    EMQU19 = 2011
    """EM-Qualifikation U 19"""

    BLPO = 2013
    """Bundesliga Play-offs"""

    RUSPOK = 2014
    """Kubok Rossii"""

    CZPOH = 2017
    """MOL Cup"""

    DFBPF = 2018
    """DFB-Pokal Frauen"""

    CROPOK = 2019
    """Hrvatski Nogometni Kup"""

    BULPOK = 2020
    """Kupa na Bulgaria"""

    MAZPOK = 2021
    """Cup na Severna Makedonija"""

    ISRPOK = 2022
    """State Cup"""

    HANDBALL_BUNDESLIGA_RELEGATION = 2023
    """Bundesliga-Relegation"""

    HANDBALL_EMQ = 2024
    """EM-Qualifikation"""

    BLS = 2027
    """1. Liga"""

    BASKETBALL_EM = 2028
    """Basketball-EM"""

    EIRQ = 2030
    """Relegation 1. Liga"""

    CROSC = 2031
    """Supercup"""

    POLSC = 2033
    """Superpuchar Polski"""

    BSC = 2034
    """Supercup"""

    NLJCS = 2035
    """Johan Cruijff Schaal"""

    SC = 2036
    """Super Cup"""

    BASKETBALL_WM = 2037
    """Weltmeisterschaft Männer"""

    BASKETBALL_EL = 2040
    """Euroleague"""

    ECUP = 2041
    """Eurocup"""

    BASKETBALL_EMQ = 2042
    """EM-Qualifikation"""

    DCUP = 2045
    """Deutschland-Cup"""

    HANDBALL_EMFR = 2046
    """Frauen-Europameisterschaft"""

    DEL2 = 2047
    """DEL 2"""

    DEL2PO = 2052
    """DEL 2 Play-offs"""

    DEL2PD = 2053
    """DEL 2 Play-downs"""

    RUSSC = 2054
    """Supercup"""

    ISLPOK = 2056
    """Borgunarbikar"""

    BLSPOK = 2058
    """Kywok Belarusi"""

    HANDBALL_SC = 2062
    """Supercup"""

    EFL = 2063
    """Bristol Street Motors Trophy"""

    HANDBALL_WMFR = 2064
    """Frauen-Weltmeisterschaft"""

    NIRPOK = 2065
    """Irish Cup"""

    ESTPOK = 2066
    """Eesti Karikas"""

    GEOPOK = 2067
    """David Kipiani Cup"""

    WMF = 2068
    """Frauen-Weltmeisterschaft"""

    SUIBAR = 2070
    """Barrage Credit Suisse Super League"""

    URU = 2071
    """Primera Division"""

    UKRSC = 2072
    """Supercup"""

    BULSC = 2073
    """Supercup"""

    WCEH = 2074
    """World Cup of Hockey"""

    BIHPOK = 2077
    """Kup Bosne i Herzegovine"""

    CSL = 2078
    """Chinese Super League"""

    SCOCS = 2079
    """Scottish Championship"""

    FRPOK = 2081
    """Steypakappingin"""

    SHL = 2082
    """Swedish Hockey League"""

    ICE = 2083
    """ICE"""

    FIN = 2084
    """Liiga"""

    CH = 2085
    """National League"""

    SAFF = 2087
    """Südasien-Meisterschaft"""

    WAG = 2088
    """Westasien-Meisterschaft"""

    AUTPO = 2089
    """ICE Play-offs"""

    CHPO = 2090
    """National League Play-offs"""

    SHLPO = 2091
    """SHL Play-offs"""

    B_WM = 2092
    """WM Division I"""

    CHPD = 2093
    """National League Play-downs"""

    FINPO = 2094
    """Liiga Play-offs"""

    WALPOK = 2095
    """Welsh Cup"""

    ALBPOK = 2096
    """Kupa e Shqiperise"""

    NEDREL = 2097
    """Relegation Eredivisie"""

    ARMPOK = 2099
    """Armenischer Pokal"""

    LITPOK = 3000
    """LFF Taure"""

    LETPOK = 3001
    """Latvijas Kauss"""

    MATPOK = 3002
    """FA Trophy"""

    ANDPOK = 3003
    """Copa Constitucio"""

    SMRPOK = 3004
    """Coppa Titano"""

    ASEPOK = 3005
    """Aserbaidschanischer Pokal"""

    KASPOK = 3006
    """Kubok Kazakstana"""

    LUXPOK = 3007
    """Coupe de Luxembourg"""

    TEST16 = 3016
    """U-16-Nationalteams Freundschaftsspiele"""

    TEST17 = 3017
    """U-17-Nationalteams Freundschaftsspiele"""

    TEST18 = 3018
    """U-18-Nationalteams Freundschaftsspiele"""

    TEST19 = 3019
    """U-19-Nationalteams Freundschaftsspiele"""

    EMQU17 = 3020
    """U-17-EM-Qualifikation"""

    WMQPO = 4001
    """WM-Qualifikation Play-offs"""

    MNT = 4002
    """Meridianbet 1. CFL"""

    TRSC = 4003
    """Supercup"""

    RUMSC = 4004
    """Supercupa Romaniei"""

    CYSC = 4005
    """Supercup"""

    RECOPA = 4006
    """Recopa Sudamericana"""

    BBCCUP = 4007
    """BBL Champions Cup"""

    BLFR = 4033
    """Frauen-Bundesliga"""

    AFRCQ = 4035
    """Afrika-Cup-Qualifikation"""

    TEST15 = 4038
    """U-15-Nationalteams Freundschaftsspiele"""

    SOASI = 4044
    """Südostasien-Meisterschaft"""

    GCUP = 4046
    """Golf-Cup"""

    SVKMEI = 4049
    """Niké Liga - Meisterrunde"""

    SVKABS = 4050
    """Niké Liga - Abstiegsrunde"""

    ALGARVE_CUP = 4051
    """Algarve Cup"""

    SRBM = 4053
    """Mozzart Bet SuperLiga - Meisterrunde"""

    SRBA = 4054
    """Mozzart Bet SuperLiga - Abstiegsrunde"""

    MNTPOK = 4055
    """Kup Crne Gore"""

    BUNDESLIGA_WOMEN_PO = 4056
    """2. Frauen-Bundesliga Aufstiegsspiele"""

    BQ = 4058
    """Play-Out Serie B"""

    CHL = 4059
    """Campeonato Itau"""

    BOL = 4060
    """Division de Futbol Profesional"""

    PERU = 4061
    """Liga 1"""

    TURKIYE_1_LIG = 4072
    """TFF 1. Lig"""

    LIEP = 4073
    """FL1 Aktiv-Cup"""

    AUTP = 4075
    """ICE Hockey League Platzierungsrunde"""

    OLYQ = 4077
    """Olympia-Qualifikationsturnier"""

    OSTASI = 4078
    """Ostasien-Meisterschaft"""

    CYPM = 4079
    """Cyta Championship - Meisterrunde"""

    CYPA = 4081
    """Cyta Championship - Abstiegsrunde"""

    TURKIYE_SUPER_LIG_Q = 4084
    """SüperLig-Qualifikation"""

    ZAF = 4087
    """Premier Soccer League"""

    WMF20 = 4090
    """U-20-Frauen-WM"""

    DFL_SC = 4218
    """Supercup"""

    AFCCLE = 4222
    """AFC Champions League Elite"""

    CAFCL = 4223
    """CAF Champions League"""

    BELM = 4225
    """Jupiler Pro League - Meisterrunde"""

    P2 = 4240
    """Liga Portugal 2"""

    BASKETBALL_BUNDESLIGA_FRAUEN = 4243
    """Basketball-Bundesliga-Frauen"""

    SHG = 4245
    """EHT Beijer Hockey Games"""

    C1CUP = 4246
    """EHT Channel One Cup"""

    KARJ = 4247
    """EHT Karjala Cup"""

    CZHG = 4248
    """EHT Carlson Hockey Games"""

    VIRSPO = 4249
    """Virsliga Play-Off"""

    PERUPO = 4252
    """Peru - Finale"""

    BBLPOK = 4254
    """BBL-Pokal"""

    BLFRPO = 4258
    """Basketball-Bundesliga-Frauen Play-Offs"""

    ISRA = 4260
    """Ligat Ha'al - Abstiegsrunde"""

    ISRM = 4261
    """Ligat Ha'al - Meisterrunde"""

    BELECL = 4262
    """Jupiler Pro League - Qualirunde Conference League"""

    NEDECP = 4263
    """Eredivisie - Play-offs ECL"""

    GR2AUF = 4264
    """Play-off Super League 2"""

    GR2AB = 4265
    """Play-out Super League 2"""

    USOC = 4529
    """U.S. Open Cup"""

    RLWFR = 4530
    """Frauen-Regionalliga West"""

    RLNFR = 4531
    """Frauen-Regionalliga Nord"""

    RLNOFR = 4532
    """Frauen-Regionalliga Nordost"""

    RLSFR = 4533
    """Frauen-Regionalliga Süd"""

    RLSWFR = 4534
    """Frauen-Regionalliga Südwest"""

    BELFR = 4535
    """Super League Vrouwen"""

    DENFR = 4536
    """Kvindeligaen"""

    FRFR = 4537
    """Premiere Ligue"""

    FINFR = 4538
    """Kansallinen Liiga"""

    ISLFR = 4539
    """Besta deild kvenna"""

    ITAFR = 4540
    """Serie A femminile"""

    NEDFR = 4541
    """Vrouwen Eredivisie"""

    NORFR = 4542
    """Toppserien"""

    AUTFR = 4543
    """Admiral Frauen Bundesliga"""

    POLFR = 4544
    """Ekstraliga kobiet"""

    RUSFR = 4545
    """Supreme Division"""

    SWEFR = 4546
    """Damallsvenskan"""

    CHFR = 4547
    """Women’s Super League"""

    CZEFR = 4548
    """I. Liga Zen"""

    NWSL = 4549
    """National Women's Soccer League"""

    ENGFR = 4550
    """Women's Super League"""

    WALMEI = 4552
    """Cymru Premier - Meisterrunde"""

    WALABS = 4553
    """Cymru Premier - Abstiegsrunde"""

    BELAB = 4554
    """Jupiler Pro League - Abstiegsrunde"""

    CHFRF = 4556
    """Women’s Super League Finalrunde"""

    WALPOE = 4557
    """Cymru Premier - Play-offs ECL"""

    LALI2A = 4562
    """La Liga 2 - Aufstiegsrunde"""

    TCUP = 5026
    """Telekom Cup"""

    EMQPO = 5031
    """EM-Qualifikation-Play-offs"""

    COPARG = 5034
    """Copa Argentina"""

    COPBRA = 5035
    """Copa do Brasil"""

    HBL2 = 5037
    """2. Handball-Bundesliga"""

    RLREL = 5040
    """Regionalliga Aufstiegsspiele"""

    URUMEI = 5041
    """Meisterschafts-Play-off"""

    ARGREL = 5047
    """Liga Profesional de Futbol - Relegation"""

    WMF17 = 6045
    """U-17-Frauen-WM"""

    CONCC = 6065
    """CONCACAF Champions Cup"""

    OFCCL = 6066
    """OFC Champions League"""

    RUS2 = 6070
    """FNL"""

    LPSH = 6071
    """Landespokal Schleswig-Holstein"""

    LPHH = 6072
    """Landespokal Hamburg"""

    LPHB = 6073
    """Landespokal Bremen"""

    LPNS = 6074
    """Landespokal Niedersachsen"""

    LPNR = 6075
    """Landespokal Niederrhein"""

    LPMR = 6076
    """Landespokal Mittelrhein"""

    LPWF = 6077
    """Landespokal Westfalen"""

    LPRL = 6078
    """Landespokal Rheinland"""

    LPSW = 6079
    """Landespokal Südwest"""

    LPSL = 6080
    """Landespokal Saarland"""

    LPHS = 6081
    """Landespokal Hessen"""

    LPBA = 6082
    """Landespokal Baden"""

    LPSB = 6083
    """Landespokal Südbaden"""

    LPWUE = 6084
    """Landespokal Württemberg"""

    LPBY = 6085
    """Landespokal Bayern"""

    LPMV = 6086
    """Landespokal Mecklenburg-Vorpommern"""

    LPSA = 6087
    """Landespokal Sachsen-Anhalt"""

    LPBL = 6088
    """Landespokal Berlin"""

    LPBB = 6089
    """Landespokal Brandenburg"""

    LPSC = 6090
    """Landespokal Sachsen"""

    LPTH = 6091
    """Landespokal Thüringen"""

    REL3 = 6092
    """Aufstiegsspiele zur 3. Liga"""

    RUSREL = 6095
    """Relegation Premier Liga"""

    KHL = 6096
    """Kontinental Hockey League"""

    POL2 = 6097
    """I liga"""

    CZE2 = 6099
    """Chance Narodni Liga"""

    PAR = 6101
    """Primera Division de Paraguay"""

    ECU = 6102
    """LigaPro"""

    VEN = 6104
    """Liga FUTVE"""

    KOL = 6105
    """Liga BetPlay Dimayor"""

    AUDIC = 6106
    """Audi Cup"""

    ITA_CA = 6127
    """Serie C, Girone A"""

    ITA_CB = 6128
    """Serie C, Girone B"""

    VAE = 6129
    """Arabian Gulf League"""

    QAT = 6130
    """Stars League"""

    GPD = 6131
    """Gibraltar Premier Division"""

    UEFAYL = 6132
    """UEFA Youth League"""

    KOLA = 6138
    """Liga BetPlay Dimayor - Gruppe A"""

    KOLB = 6139
    """Liga BetPlay Dimayor - Gruppe B"""

    KOLFIN = 6140
    """Primera A - Finale"""

    KHL_PO = 6144
    """KHL Play Offs"""

    GIBPOK = 6146
    """Rock Cup"""

    SCOREL = 6147
    """Relegation Scottish Premiership"""

    ITACPO = 6148
    """Serie C, Play-offs"""

    PORREL = 6149
    """Relegation Liga Portugal Betclic"""

    VENFIN = 6150
    """Venezuela, Gruppe A"""

    VENPO = 6151
    """Venezuela, Gruppe B"""

    SRBREL = 6153
    """Relegation Mozzart Bet SuperLiga"""

    SLOREL = 6154
    """Relegation Prva Liga Telemach"""

    MNTREL = 6155
    """Relegation Meridianbet 1. CFL"""

    ITA_CC = 6157
    """Serie C, Girone C"""

    HOCKEY_CHL = 6158
    """Champions Hockey League"""

    ECUFIN = 6185
    """Meisterschaftsfinale"""

    EC_BB = 6204
    """FIBA Europe Cup"""

    CONFED_PO = 6205
    """Play-off Confed-Cup"""

    ENGFR2 = 6206
    """Women's Championship"""

    ESTREL = 6209
    """Relegation"""

    CAQ = 6212
    """Copa America Qualifikation"""

    SBC = 6213
    """SheBelieves-Cup"""

    ROUM = 6214
    """SuperLiga - Meisterrunde"""

    ROUA = 6215
    """SuperLiga - Abstiegsrunde"""

    NIRECL = 6216
    """Sports Direct Premiership - Play-offs ECL"""

    ITACSC = 6217
    """Serie C, Supercoppa"""

    KVX = 6221
    """ALBI MALL Superliga e Kosoves"""

    BBCL = 6228
    """Basketball Champions League"""

    NBAPRE = 6241
    """NBA Preseason"""

    NHLPRE = 6242
    """NHL Preseason"""

    NWSLF = 6243
    """NWSL Finals"""

    TACA_DA_LIGA = 6247
    """Taca da Liga"""

    DENM = 6250
    """3F Superliga - Meisterrunde"""

    KOSPOK = 6257
    """Kosovar Cup"""

    DENECL = 6261
    """3F Superliga - Qualirunde Conference League"""

    DENAB = 6262
    """3F Superliga - Abstiegsrunde"""

    BGRECLQ = 6264
    """Parva Liga - Qualirunde Conference League"""

    URUINT = 6265
    """Zwischenrunde"""

    ROUREL = 6266
    """Relegation SuperLiga"""

    NFL_P = 6267
    """NFL-Preseason"""

    ALIGR = 6282
    """A-Lyga Relegation"""

    WMQ_BB = 6283
    """WM-Qualifikation"""

    KOR = 6286
    """K League 1"""

    BELFRM = 6288
    """Super League Vrouwen - Meisterrunde"""

    FRAREL = 6289
    """Relegation Ligue 1"""

    UKRREL = 6290
    """Relegation Premjer-Liha"""

    BOLPO = 6291
    """Play-Offs"""

    ZWEITE_BUNDESLIGA_FRAUEN = 6294
    """2. Frauen-Bundesliga"""

    CZ_ELH = 7043
    """Extra Liga"""

    CORFIN = 7058
    """Finalrunde"""

    KORREL = 7059
    """Südkorea-Abstieg"""

    FRA3 = 7060
    """Championnat National"""

    AUSFR = 7061
    """Ninja A-League"""

    ESPFR = 7062
    """Liga F"""

    U20SA = 7063
    """U-20-Südamerikameisterschaft"""

    INDIEN = 7064
    """Indian Super League"""

    USL_CH = 7065
    """USL Championship"""

    EGY = 7066
    """Egyptian Premier League"""

    J2L = 7067
    """J2 League"""

    SL = 7068
    """Super League"""

    THAI = 7070
    """Thai-Liga"""

    VIE = 7071
    """V.League"""

    FINFRM = 7072
    """Kansallinen Liiga - Meisterrunde"""

    GFL = 7076
    """German Football League"""

    KOR2 = 7077
    """K League 2"""

    CHINA2 = 7078
    """China League One"""

    BRA2 = 7079
    """Campeonato Brasileiro B"""

    SAUDI = 7080
    """Saudi Professional League"""

    IRAN = 7081
    """Persian Gulf Pro League"""

    FINFRR = 7083
    """Kansallinen Liiga - Abstiegsrunde"""

    INDPO = 7084
    """Indian Super League Play-offs"""

    AUSFRF = 7085
    """Australian W-League Finale"""

    DENFRF = 7086
    """Kvindeligaen - Meisterrunde"""

    ELH_PO = 7087
    """Extraliga - Play-Offs"""

    FACUPF = 7088
    """Women's FA Cup"""

    A_MEI = 7089
    """Admiral-Bundesliga - Meistergruppe"""

    A_QUA = 7090
    """Admiral-Bundesliga - Qualifikationsgruppe"""

    U17EMF = 7092
    """U-17-Frauen-EM"""

    U17EQF = 7093
    """U-17-Frauen-EM-Quali"""

    U19EMF = 7094
    """U-19-Frauen-EM"""

    CONNL = 7095
    """CONCACAF Nations League"""

    KANADA = 7102
    """Canadian Premier League"""

    CZEMEI = 7103
    """Chance Liga - Meisterrunde"""

    CZEABS = 7104
    """Chance Liga - Abstiegsrunde"""

    CZEFRF = 7105
    """I. Liga Zen - Meisterrunde"""

    CZPO = 7106
    """Chance Liga - Mittelfeld-Play-offs"""

    CCS = 7109
    """Canadian Championship"""

    ELPO = 7112
    """Admiral-Bundesliga - Play-offs ECL"""

    CZEREL = 7113
    """Tschechien Relegation 1/2"""

    SVKREL = 7115
    """Relegation Niké Liga"""

    SCOL1 = 7116
    """Scottish League One"""

    UZB = 7117
    """1. Liga"""

    ALGERIA = 7118
    """Ligue 1"""

    JAP_C = 7119
    """Emperor's Cup"""

    SCOL2 = 7120
    """Scottish League Two"""

    SLV = 7121
    """Primera Division"""

    CRI = 7122
    """Primera Division de Costa Rica"""

    AUTREM = 7123
    """Regionalliga Mitte"""

    AUTROS = 7124
    """Regionalliga Ost"""

    ROU2 = 7128
    """Liga II"""

    TUN = 7153
    """Ligue 1"""

    HND = 7155
    """Liga Betcris de Honduras"""

    SGLOBE = 7156
    """Super Globe"""

    GFL_PO = 7158
    """GFL-Play-offs"""

    USL_PO = 7159
    """USL Championship Play-offs"""

    CANFIN = 7160
    """Canadian Premier League - Finale"""

    KL_REL = 7162
    """Relegation K League"""

    CRIMEI = 7163
    """Primera Division de Costa Rica - Meisterschaftsfinale"""

    J2PO = 7165
    """J2 Play-offs"""

    ESLVF = 7167
    """El Salvador Meisterschaftsfinale"""

    EH20WM = 7168
    """Junioren-WM"""

    GIB_C = 7169
    """Gibraltar Championship"""

    GIB_R = 7170
    """Gibraltar Challenge Group"""

    UFL = 7172
    """UFL"""

    JPNSC = 7173
    """Supercup"""

    HANDBALL_OLYMPIA_Q = 7175
    """Olympia-Qualifikation"""

    POGRSL = 7176
    """Play-off Super League 1"""

    POUSL1 = 7177
    """Play-out Super League 1"""

    ROU2AU = 7184
    """Liga II - Aufstiegsrunde"""

    ITACOU = 7185
    """Serie C, Play-outs"""

    POLAUF = 7193
    """I liga - Aufstiegs-Play-offs"""

    NL3 = 7433
    """Betnation Divisie"""

    VIETNAM_LEAGUE = 7781
    """V.League Meisterrunde"""

    VIETNAM_LEAGUE_RELEGATION = 7782
    """V.League Abstiegsrunde"""

    PL2 = 7784
    """Premier League 2"""

    MSC = 7786
    """Magenta Sport Cup"""

    COPLIQ = 7788
    """Copa-Libertadores-Qualifikation"""

    ROU2AB = 7791
    """Liga II - Abstiegsrunde"""

    DEN2AU = 7792
    """1. Division - Aufstiegsrunde"""

    DEN2AB = 7793
    """1. Division - Abstiegsrunde"""

    ELF = 7795
    """European League of Football"""

    SCOTTISH_CHAMPIONSHIP_RELEGATION = 7801
    """Relegation Scottish Championship"""

    SCOTTISH_LEAGUE_ONE_RELEGATION = 7802
    """Relegation Scottish League One"""

    ARGPOM = 7803
    """Liga Profesional de Futbol - Play-offs Meisterschaft"""

    ROUECL = 7804
    """SuperLiga - Play-offs ECL"""

    ESP3PO = 7805
    """Primera Federacion, Play-offs"""

    GCQ = 7806
    """CONCACAF-Gold-Cup-Qualifikation"""

    BGRECL_PO = 7808
    """Parva Liga - Play-off ECL"""

    HNDFIN = 7811
    """Liga Betcris de Honduras - Finalrunde"""

    HB3NAT = 7812
    """Drei-Nationen-Turnier"""

    OLBBF = 7813
    """Olympiaturnier Frauen"""

    ESP3A = 7814
    """Primera Federacion - Grupo A"""

    ELF_PO = 7819
    """ELF-Play-offs"""

    ARAB = 7821
    """FIFA Arab Cup"""

    FINALISSIMA = 7947
    """Finalissima"""

    ACC = 7950
    """Arnold Clark Cup"""

    MAROK = 7973
    """Botola Pro1"""

    EURC = 7976
    """EHF Euro Cup"""

    TUNM = 8037
    """Ligue 1 - Meisterrunde"""

    TUNA = 8038
    """Ligue 1 - Abstiegsrunde"""

    PRO_A = 8039
    """Pro A"""

    U18_WM = 8040
    """U-18-WM"""

    INDO = 8041
    """BRI Liga 1"""

    CA_F = 8042
    """Copa America (Frauen)"""

    ESP3B = 8043
    """Primera Federacion - Grupo B"""

    U20_FRIENDLIES_WOMEN = 8044
    """U-20-Frauen-Nationalteams Freundschaftsspiele"""

    U19_FRIENDLIES_WOMEN = 8045
    """U-19-Frauen-Nationalteams Freundschaftsspiele"""

    U17_FRIENDLIES_WOMEN = 8046
    """U-17-Frauen-Nationalteams Freundschaftsspiele"""

    TEST_F = 8047
    """Fußball-Vereine Frauen Freundschaftsspiele"""

    NORFRF = 8048
    """Toppserien Finalrunde"""

    HANDBALL_ZWEITE_BUNDESLIGA_FRAUEN = 8050
    """2. Handball-Bundesliga Frauen"""

    TESTFR = 8051
    """Freundschaftsspiele Frauen"""

    EMQ19F = 8052
    """U-19-Frauen-EM-Quali"""

    RUSFRM = 8053
    """Supreme Division - Meisterrunde"""

    RUSFRP = 8054
    """Supreme Division - Platzierungsrunde"""

    NORFRR = 8055
    """Toppserien Relegationsrunde"""

    YKK_PO = 8056
    """Ykkönen Aufstieg"""

    YKK_PO_2 = 8057
    """Ykkönen Abstieg"""

    BJWNNO = 8058
    """B-Juniorinnen-Bundesliga Nord/Nordost"""

    BJWWSW = 8059
    """B-Juniorinnen-Bundesliga West/Südwest"""

    BJWS = 8060
    """B-Juniorinnen-Bundesliga Süd"""

    DM_BJW = 8061
    """DM-Endrunde B-Juniorinnen"""

    ISL_M = 8062
    """Besta deild karla-Meisterrunde"""

    ISL_A = 8063
    """Besta deild karla-Abstiegsrunde"""

    HANDBALL_WMF = 8064
    """Weltmeisterschaft Frauen"""

    CLHBFR = 8065
    """Champions League Frauen"""

    HBPOKF = 8066
    """DHB-Pokal Frauen"""

    CL_WOMEN_Q = 8067
    """Women's Champions League Qualifikation"""

    FINLAND_CL_PO = 8068
    """Veikkausliiga - Conference-League-Play-off"""

    FINALISSIMA_WOMEN = 8069
    """Women's Finalissima"""

    NFIN2 = 8070
    """Finalrunde OBOS-Ligaen"""

    TROCAM = 8071
    """Trofeo de Campeones"""

    HANDBALL_WMQ_FRAUEN = 8072
    """WM-Qualifikation Frauen"""

    MDAP2 = 8073
    """Super Liga - Phase 2"""

    SIHG = 8074
    """EHT SWISS Ice Hockey Games"""

    ITAFRM = 8077
    """Serie A femminile - Meisterrunde"""

    ITAFRA = 8078
    """Serie A femminile - Abstiegsrunde"""

    KSACUP = 8079
    """King's Cup"""

    U19SSR = 8080
    """U-19-Sonderspielrunde JBL"""

    U17SSR = 8081
    """U-17-Sonderspielrunde JBL"""

    UFLPO = 8082
    """UFL-Play-offs"""

    PRO_A_PO = 8083
    """Pro A Play-offs"""

    UEFA_NL_WOMEN = 8084
    """UEFA Women's Nations League"""

    U21WM = 8086
    """U-21-Weltmeisterschaft"""

    ITAABE = 8089
    """Entscheidungsspiel Serie A"""

    EMF = 8090
    """Basketball-EM Frauen"""

    LEAGUES_CUP = 8092
    """Leagues Cup"""

    ELHBFR = 8093
    """European League Frauen"""

    CAFANC = 8094
    """Zentralasienmeisterschaft"""

    AUTRWE = 8095
    """Regionalliga West"""

    CC = 8096
    """Club Challenge"""

    SWPL1 = 8097
    """Scottish Women’s Premier League"""

    U20EM = 8098
    """U-20-Europameisterschaft"""

    WNBA = 8099
    """WNBA"""

    U19WM = 8100
    """U-19-Weltmeisterschaft"""

    ARAB_CC = 8101
    """Arab Club Champions Cup"""

    AFCCLQ = 8102
    """AFC Champions League Elite Quali"""

    ISL_MR = 8103
    """Urvalsdeild Meisterrunde"""

    ISL_AR = 8104
    """Urvalsdeild Abstiegsrunde"""

    WNBAPO = 8105
    """WNBA Play-offs"""

    EMFQ = 8106
    """EM-Qualifikation Frauen"""

    AFL = 8107
    """African Football League"""

    CAFCCC = 8108
    """CAF Confederation Cup"""

    AFCCL2 = 8109
    """AFC Champions League Two"""

    U17SA = 8110
    """U-17-Südamerikameisterschaft"""

    U20AFR = 8111
    """U-20-Afrika-Cup"""

    U17AFR = 8112
    """U-17-Afrika-Cup"""

    U20ASI = 8113
    """U-20-Asienmeisterschaft"""

    U17ASI = 8114
    """U-17-Asienmeisterschaft"""

    U20NMA = 8115
    """CONCACAF U-20-Meisterschaft"""

    U17NMA = 8116
    """CONCACAF U-17-Meisterschaft"""

    DCUPFR = 8117
    """Eishockey-Deutschland-Cup Frauen"""

    FEMQ = 8118
    """Basketball-EM-Qualifikation Frauen"""

    PACIFIC_GAMES = 8119
    """Pacific Games"""

    NBACUP = 8120
    """NBA Cup"""

    COPPAF = 8130
    """Coppa Italia Femminile"""

    COPAF = 8131
    """Copa de la Reina"""

    OLYQF = 8132
    """Basketball Olympia-Qualifikationsturnier (Frauen)"""

    OQHBFR = 8133
    """Olympia-Qualifikation (Frauen)"""

    KSA_SC = 8134
    """Saudi Super Cup"""

    SWPLM = 8135
    """SWPL - Meisterrunde"""

    SWPLA = 8136
    """SWPL - Abstiegsrunde"""

    GOLD_F = 8137
    """CONCACAF-Gold-Cup (Frauen)"""

    OLYQAF = 8138
    """Olympia-Quali Asien Frauen"""

    ATFPOK = 8139
    """ÖFB Frauen-Cup"""

    ATFL2 = 8140
    """2. Frauen Bundesliga"""

    BELFRP = 8141
    """Super League Vrouwen - Platzierungsrunde """

    SUIMEI = 8142
    """Credit Suisse Super League - Meisterrunde"""

    SUIABS = 8143
    """Credit Suisse Super League - Abstiegsrunde"""

    CHPOKF = 8144
    """Schweizer Cup"""

    PL2FIN = 8145
    """Premier League 2 - Finalrunde"""

    NIRFR = 8146
    """NIFL Women's Premiership"""

    FRFRF = 8147
    """Premiere Ligue - Finalrunde"""

    ALBPO = 8148
    """Kategoria Superiore - Play-offs Meisterschaft"""

    ESP3F = 8149
    """Primera Federacion - Finale"""

    INDOFI = 8150
    """BRI Liga 1 - Finalrunde"""

    BELECP = 8151
    """Jupiler Pro League - Play-off ECL"""

    VENP2 = 8152
    """Liga FUTVE - Phase 2"""

    DSCF = 8153
    """Google Pixel Supercup der Frauen"""

    SGP = 8156
    """Singapore Premier League"""

    SCF = 8157
    """DHB-Supercup Frauen"""

    TUNPOA = 8158
    """Ligue 1 - Play-off Abstieg"""

    USLSL = 8159
    """USL Super League"""

    U19_D = 8160
    """U-19-DFB-Nachwuchsliga (Vorrunde)"""

    U17_D = 8161
    """U-17-DFB-Nachwuchsliga (Vorrunde)"""

    PORFR = 8162
    """Campeonato Nacional de Futebol Feminino"""

    DFB_PJ = 8163
    """DFB-Juniorinnen-Pokal"""

    INTKON = 8164
    """Interkontinental-Pokal"""

    U23_FRIENDLIES_WOMEN = 8165
    """U-23-Frauen-Nationalteams Freundschaftsspiele"""

    GOLDL = 8166
    """Golden League Posten Cup"""
