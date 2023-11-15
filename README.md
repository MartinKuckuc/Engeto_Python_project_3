# Elections_scraper

# **Engeto_Python_project3: Elections scraper**

## Popis projektu
Tento projekt slouží pro získávání a ukládání dat o [výsledcích voleb] (https://volby.cz/pls/ps2017nss/ps?xjazyk=CZ) do Poslanecké sněmovny Parlamentu České republiky konané ve dnech 20.10.-21.10.2017.  

## Instalace knihoven
V projektu jsou použity knihovny **requests** a **BeautifulSoup**, které slouží pro tahování webových stránek. Před instalací knihoven se doporučuje použít nové virtuální prostředí. Knihovny lze nainstalovat ze souboru **requirements.txt** pomocí příkazu:
```
$ pip3 --version                    # oveří verzi manažera (instalačního balíčku)
$ pip3 install -r requirements.txt  # nainstaluje knihovny
```

## Spuštění programu 
Je potřeba spustit skript **main.py** zadáním těchto argumentů do příkazového řádku (terminalu): **python main.py** a 2 další povinné argumenty: 
```
python mainy.py <odkaz_uzemniho_celku> <nazev_vystupniho_souboru>
```
Data budou stažena do souboru s příponou `.csv`. 

## Ukázka projektu 
Výsledky hlasování pro obec Brno-město:
1. argument: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203`
2. argument: `Brno_venkov.csv`

###### Ukázka spuštění programu: 
```
python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203" "Brno_venkov.csv"   
```

###### Průběh stahování:
```
STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203
UKLADAM DO SOUBORU: Brno_venkov.csv
UKONCUJI PROGRAM
```

## Částečný výstup:
code;name;registered;envelopes;valid;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;Radostné Česko;STAROSTOVÉ A NEZÁVISLÍ;Komunistická str.Čech a Moravy;Strana zelených;ROZUMNÍ-stop migraci,diktát.EU;Strana svobodných občanů;Blok proti islam.-Obran.domova;Občanská demokratická aliance;Česká pirátská strana;Referendum o Evropské unii;TOP 09;ANO 2011;Dobrá volba 2016;SPR-Republ.str.Čsl. M.Sládka;Křesť.demokr.unie-Čs.str.lid.;Česká strana národně sociální;REALISTÉ;SPORTOVCI;Dělnic.str.sociální spravedl.;Svob.a př.dem.-T.Okamura (SPD);Strana Práv Občanů;Národ Sobě
582794;Babice nad Svitavou;925;660;655;109;1;2;43;0;53;31;7;3;10;0;0;93;0;39;129;0;3;69;0;2;1;1;58;1;0
582808;Babice u Rosic;553;353;351;32;0;0;18;1;27;30;5;1;6;0;2;37;0;13;93;0;1;25;5;4;1;1;49;0;0
581321;Běleč;160;131;130;13;0;0;25;0;8;14;0;1;0;0;0;11;1;1;30;0;0;14;0;0;0;0;12;0;0
582824;Bílovice nad Svitavou;2676;2017;2004;316;0;2;103;0;257;78;28;6;44;2;0;205;2;147;432;2;6;186;0;16;0;1;170;1;0

