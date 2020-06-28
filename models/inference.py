# -*- coding: utf-8 -*-
def get_results(image_path, lang):
    sample = {
        'results_ir': [
            {
                'id': 'Q1715',
                'label': 'Hannover',
                'is_gold': False,
                'summary': "Hannover [haˈnoːfɐ] ist die Hauptstadt des Landes Niedersachsen. Der am Südrand des Norddeutschen Tieflandes an der Leine und der Ihme gelegene Ort wurde 1150 erstmals erwähnt und erhielt 1241 das Stadtrecht. Hannover war ab 1636 welfische Residenzstadt, ab 1692 Residenz Kurhannovers, ab 1814 Hauptstadt des Königreichs Hannover, nach dessen Annexion durch Preußen ab 1866 Provinzhauptstadt der Provinz Hannover, nach Auflösung Preußens im August 1946 Hauptstadt des Landes Hannover und nach dessen Fusion mit den Freistaaten Braunschweig, Oldenburg und Schaumburg-Lippe im November 1946 niedersächsische Landeshauptstadt. Seit 1875 Großstadt, zählt Hannover heute mit 536.925 Einwohnern (Ende 2019) zu den 15 einwohnerreichsten Städten Deutschlands. Stadt und früherer Landkreis sind zu einem Kommunalverband besonderer Art, der Region Hannover, zusammengeschlossen, die der Metropolregion Hannover-Braunschweig-Göttingen-Wolfsburg angehört. Hannover ist ein europäisches Verkehrsdrehkreuz, denn in und bei Hannover kreuzen sich wichtige Straßen- und Schienenwege der Nord-Süd- und Ost-West-Richtung. Nördlich der Stadt liegt der internationale Flughafen, und über den Mittellandkanal ist die Stadt mit mehreren Häfen an das Binnenschifffahrtsnetz angebunden. Vom 13. Jahrhundert bis ca. 1620 war Hannover Hansestadt; seit Ende Juni 2019 ist die Stadt Mitglied im 1980 symbolisch wiedergegründeten Hansebund. Im Rahmen des Wiederaufbaus nach dem Zweiten Weltkrieg als autogerechte Stadt entstanden der Cityring und die Schnellwege. Hannover ist Standort von elf Hochschulen und mehreren Bibliotheken. Der Briefwechsel von Gottfried Wilhelm Leibniz und der Goldene Brief, aufbewahrt in der Gottfried Wilhelm Leibniz Bibliothek, gehören zum Weltdokumentenerbe der UNESCO. Hannover ist ein wichtiger Wirtschaftsstandort und eine überregional bedeutende Einkaufsstadt. Die Kulturszene gilt mit zahlreichen und zum Teil international renommierten Theatern und Museen als vielfältig. Jährlich finden zahlreiche internationale Theater-, Musik- und Tanzfestivals statt. Seit 2014 ist Hannover eine UNESCO City of Music. Das Stadtbild ist geprägt durch zahlreiche öffentliche Grünanlagen, eine hohe Dichte an Straßenkunst und zahlreiche Baudenkmale, dazu gehören repräsentative Bauten der Norddeutschen Backsteingotik, der Hannoverschen Architekturschule, des Backsteinexpressionismus, des Jugendstils und klassizistische Bauten von Georg Ludwig Friedrich Laves. Während in der Innenstadt Nachkriegsbauten dominieren, haben viele Stadtviertel einen beachtlichen Altbaubestand und pflegen eigene Identitäten. Überregional bekannt sind der Erlebnis-Zoo Hannover, der Maschsee und die Herrenhäuser Gärten, eine weltweite Rarität ist der Bogenaufzug im Neuen Rathaus. Mit dem weltgrößten Messegelände und zahlreichen Weltleitmessen, allen voran die Hannover-Messe, ist Hannover eine der führenden Kongress- und Messestädte Europas. Jährlich findet das größte Schützenfest der Welt statt und seit 1955 trägt Hannover den offiziellen Ehrentitel „Schützenstadt“. Das jährliche Maschseefest ist das größte Seefest Deutschlands. Seit Dezember 2019 ist Hannover offiziell auf der Shortlist um den Titel Kulturhauptstadt Europas 2025."
            },
            {
                'id': 'Q1722',
                'label': 'Dubrovnik',
                'is_gold': True,
                'summary': "Dubrovnik (Croatian: [dǔbroːʋniːk] (About this soundlisten); historically Ragusa) is a city on the Adriatic Sea in southern Croatia. It is one of the most prominent tourist destinations in the Mediterranean Sea, a seaport and the centre of Dubrovnik-Neretva County. Its total population is 42,615 (census 2011). In 1979, the city of Dubrovnik joined the UNESCO list of World Heritage sites. The prosperity of the city was historically based on maritime trade; as the capital of the maritime Republic of Ragusa, it achieved a high level of development, particularly during the 15th and 16th centuries, as it became notable for its wealth and skilled diplomacy. In 1991, after the break-up of Yugoslavia, Dubrovnik was besieged by Serbian and Montenegrin soldiers of the Yugoslav People's Army (JNA) for seven months and suffered significant damage from shelling. After repair and restoration works in the 1990s and early 2000s, Dubrovnik re-emerged as one of the top tourist destinations in the Mediterranean."
            },
            {
                'id': 'Q472',
                'label': 'Sofia',
                'is_gold': False,
                'summary': "Sofia (en bulgare : София) est la capitale et la plus grande ville de la Bulgarie, à 590 mètres d'altitude au pied du mont Vitocha, non loin de l'Iskar. Elle compte 1,4 million d'habitants, les Sofiotes (Sofiiantsi (софиянци) en bulgare), soit 17 % de la population du pays, plaçant Sofia au 13e rang des villes les plus peuplées de l'Union européenne2. Sofia est également la quatrième plus grande ville des Balkans, après Istanbul, Athènes et Belgrade. Elle est à la fois le centre politique et culturel du pays, son principal centre d'échanges ainsi que son premier centre industriel, avec des activités sidérurgiques, métallurgique, de construction mécanique et de chimie3. C'est également un centre universitaire depuis 1888. La ville occupe une position géostratégique très importante dans la région, ce qui a largement contribué à son expansion démographique."
            }
        ],
        'results_le': [
            {'actual': [52.2228, 9.4419]},
            {'predicted': [42.3825, 18.630]},
            {'predicted': [42.415104, 23.192694]},
        ],
    }

    return sample