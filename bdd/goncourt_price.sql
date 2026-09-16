-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `goncourt_price`
--

CREATE DATABASE IF NOT EXISTS goncourt_price;
USE goncourt_price;

-- --------------------------------------------------------

DROP TABLE IF EXISTS `jury`;
DROP TABLE IF EXISTS `book`;
DROP TABLE IF EXISTS `author`;
DROP TABLE IF EXISTS `person`;
DROP TABLE IF EXISTS `editor`;

--
-- Structure de la table `editor`
--

CREATE TABLE IF NOT EXISTS `editor` (
  `ed_id_editor` int NOT NULL AUTO_INCREMENT,
  `ed_name` varchar(20) NOT NULL,
  PRIMARY KEY (`ed_id_editor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `editor`
--
INSERT INTO editor(ed_id_editor, ed_name) VALUES
(1, "Flammarion"),
(2, "Robert Laffont"),
(3, "Actes Sud"),
(4, "Gallimard"),
(5, "POL"),
(6, "Grasset"),
(7, "Minuit"),
(8, "Albin Michel"),
(9, "l'Iconoclaste"),
(10, "Verdier"),
(11, "Maurice Nadeau")
;

-- --------------------------------------------------------

--
-- Structure de la table `book`
--

CREATE TABLE IF NOT EXISTS `book` (
  `bo_id_book` int NOT NULL AUTO_INCREMENT,
  `bo_title` varchar(50) NOT NULL,
  `bo_isbn` CHAR(13) NOT NULL UNIQUE,
  `bo_resume` TEXT NOT NULL,
  `bo_main_people` TEXT,
  `bo_publication_date` DATE NOT NULL,
  `bo_nb_pages` SMALLINT NOT NULL,
  `bo_editor_price` DECIMAL(5,2) NOT NULL,
  `bo_selected_to_turn` SMALLINT NOT NULL DEFAULT 1,
  `bo_id_editor` INT NOT NULL,
  `bo_id_author` INT NOT NULL,
  PRIMARY KEY (`bo_id_book`),
  KEY `bo_id_editor` (`bo_id_editor`),
  KEY `bo_id_author` (`bo_id_author`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `book`
--
INSERT INTO book(bo_id_book, bo_title, bo_isbn, bo_resume, bo_main_people, bo_publication_date, bo_nb_pages, bo_editor_price, bo_id_editor, bo_id_author) VALUES
(1, "L'inconnue du quai de Javel", "9782080490896", "Le 6 septembre 1949, une jeune femme est retrouvée morte quai de Javel, à Paris, sans sac ni chaussures, manifestement rhabillée à la hâte puis déposée là par son assassin. Elle est identifiée le lendemain : c'est Louise Cansot, le modèle le plus demandé par les peintres de Montparnasse. Rapidement, quatre suspects se détachent, évidents, presque des archétypes. On dirait le début d'un roman de Simenon, mais l'inspecteur-chef Ferrière n'a pas le talent de Maigret, et doit se résoudre à classer l'affaire au bout de six mois, sans avoir arrêté personne.\n\nSoixante-quinze ans plus tard, Philippe Jaenada reprend l'enquête à partir du dossier retrouvé puis, comme à son habitude, sollicite ses contacts aux archives, exhume tous les documents, arpente tous les lieux - remonte le temps.\n\nPour ce livre, il a lu les soixante-quinze enquêtes de Maigret, s'inspirant humblement et fidèlement des méthodes du commissaire fictif. Et il va résoudre ce meurtre bien réel, laissant le lecteur subjugué par la dextérité de son investigation et fasciné par cette jeune femme à laquelle il redonne un visage et une histoire.",
"Louise Cansot, inspecteur-chef Ferrière, Philippe Jaenada", "2026-08-12", 528, 23.00, 1, 1),
(2, "Le fabuleux piano", "9782221286807", "Après le succès littéraire et commercial de son récit Les Exportés , Sonia Devillers part à la recherche d'un admirable piano à queue, volé par les nazis en 1943. Ce qu'elle nous raconte est bouleversant, instructif, et magistralement mené.\nLe fabuleux piano est un instrument volé par les Allemands, en 1943, à des juifs qui le cherchent encore... Dans ce vide impossible à combler, Sonia Devillers entend une résonance intime, le souvenir d'un instrument que sa propre grand-mère, forcée à l'exil, a regretté toute sa vie. Elle part alors sur les traces des pianos fantômes pillés par milliers sous l'Occupation et transportés jusqu'aux confins du IIIe Reich.\nAvec cet instrument de concert ressurgit l'incroyable destin d'une famille d'éditeurs de musique, les Enoch. Un siècle de partitions, des menuets de Ravel aux ritournelles de Prévert. Les nazis se sont acharnés sur les Enoch, mais ils ont échoué à les réduire au silence. Des douleurs de la guerre va naître une chanson portée par Yves Montand, Les Feuilles mortes : un triomphe mondial.\nLe piano disparu continue pourtant de hanter les survivants...",
"Sonia Devillers, les Enoch, Yves Montand", "2026-08-27", 280, 21.00, 2, 2),
(3, "Nous aussi", "9782330225575", "On fait partie d'une grande famille. On sait qu'on est privilégiés. On vit ensemble, dans notre immeuble au centre de Paris, on se retrouve l'été dans notre maison à la montagne. On trouve que c'est normal. C'est chez nous, c'est à nous, c'est pour nous. On se ressemble, on se compare, on se confronte, on ne se quitte pas, on se confond, on s'appartient. On ne sait pas comment dire je, on n'en a pas besoin, puisqu'on est nous. Nous les enfants, les frères et soeurs, les cousins, les cousines, on partage tout, nos écoles, nos chambres, nos habits, nos repas, nos jeux, nos bains, nos lits. On est les membres indissociables du grand corps familial. On n'a jamais vécu dehors. On ne sait pas ce que c'est. On n'en est pas capables. On n'en a même pas envie. Et tout aurait dû continuer ainsi, dans un même immuable recommencement. Le jour où la façade s'est fissurée, on n'a pas compris. Ça n'aurait pas dû se produire, pas dans notre famille. Ce n'était pas possible que ça nous arrive, à nous aussi.",
"La famille Godard", "2026-08-19", 237, 20.00, 3, 3),
(4, "La solitude des professeurs est infinie", "9782073161925", "Jean Deichel, jeune professeur de français, fait son stage dans un collège de la banlieue parisienne. La nuit, il loge dans un club de tennis à Deuil-la-Barre ; le jour, il découvre les difficultés du métier en même temps que ses joies profondes, la violence de l'École en même temps que sa beauté.\n\nJean est aussi un poète ivre d'aventure, attentif à trouver la lumière de la « vraie vie » au coeur du quotidien le plus gris : dans des jardins réels ou rêvés, au bord d'un lac, lors d'évasions à Pompéi et à Tarquinia, mais surtout dans la grâce fragile d'un cours réussi.\n\nEntre réalité politique et mystère existentiel, la vie des profs est un roman.",
"Jean Deichel", "2026-08-20", 313, 21.50, 4, 4),
(5, "Je", "9782073099945", "« - Que savez-vous de la beauté, Antoinette ? Il se tourna vers moi, suspendu à ma réponse. - Pas grand-chose. Mais je sais la reconnaître quand elle est là. - Eh bien moi, chaque fois que je la vois, elle me blesse. Quand je vois votre visage, par exemple, quelque chose en moi se trouve comme ébranlé. »\n\nîle de la Jamaïque, 1831. Antoinette Cosway, créole de bonne famille, s'éprend d'Edward Rochester, un Anglais aussi impénétrable que fascinant. Mais à la séduction enflammée succèdent rapidement des scènes vénéneuses, où les baisers sont des blessures, où toute une société livre la jeune femme à son bourreau.\n\nDes années plus tard, Antoinette tente de conquérir sa propre histoire.\n\nJE se situe à mi-chemin entre roman victorien et thriller intimiste contemporain. Lilia Hassaine s'est inspirée du personnage de la première femme de Rochester dans Jane Eyre, le roman culte de Charlotte Brontë. Elle a choisi de lui donner une voix, un corps, une destinée.",
"Antoinette Cosway, Edward Rochester", "2026-08-20", 248, 21.00, 4, 5),
(6, "Faire la peau", "9782818063583", "Je dis que l'une des plus tenaces fictions tient tout entière dans ce mot, mère. Que la haine qui circule entre les mères et leurs filles est sauvage, et qu'il faut la regarder droit dans les yeux.",
NULL, "2026-08-20", 286, 21.00, 5, 6),
(7, "La guerre éternelle : souvenirs de Troie", "9782073121349", "« Pour donner à ma longue rêverie la forme d'un livre, j'avais besoin de voir. De la terre, des pierres, des arbres, un rivage. J'ai toujours besoin de voir. Je suis allé en Troade à la fin d'un mois de juin, alors que les coquelicots jetaient de grandes flaques rouges au milieu des champs de blé et d'oliviers où jadis s'affrontaient les héros. »\n\nIl y a quelque trente-trois siècles, des guerriers grecs ravagent une cité d'Asie Mineure qu'ils appellent Troïa ou Ilios. Les hommes sont massacrés, les femmes traînées en esclavage. C'était dans la nuit des temps, mais grâce à l'Iliade cela vit toujours dans notre mémoire. C'était, aussi bien, hier, aujourd'hui, demain : la tragédie de la destruction d'une ville n'a cessé d'être réécrite en lettres de feu et de sang, depuis Carthage un siècle et demi avant notre ère jusqu'à Dresde et Hiroshima, Marioupol et Gaza de nos jours. La guerre de Troie est éternelle, et Troie est la Mère de toutes les villes martyrisées.",
"les Guerriers grecs", "2026-08-20", 219, 20.00, 4, 7),
(8, "Chronique d'un royaume perdu", "9782246846949", "Au Bouchon, petit village isolé de l’île Maurice, quatre générations se succèdent depuis le temps de l’esclavage. La violence se mêle à l’amour, la tendresse à la haine, les plus nobles passions aux vices les plus vils, les sangs des unes aux sangs des autres…\nLes cinq fondateurs viennent d’une plantation lointaine  : trois sont nés dans la puissante et blanche famille Dumontais  ; deux d’une esclave noire. Mais les trois blancs sont en vérité le fruit d’une passion entre Madame et le Vieux Bouc, un esclave magnétique qui revendique aussi la paternité des deux derniers. Bannis pour s’être liés d’amour et d’amitié, les cinq enfants devenus grands trouvent refuge dans ce lieu perdu dont ils font leur royaume, autarcique et magique, qu’ils défendent d’un seul corps, puisqu’ici sont abolies les frontières entre passé, présent et avenir  ; vie et mort  ; réel et fantastique.\nTel homme entend sans le vouloir tous les péchés humains  ; telle femme meurt et renait en déesse protectrice  ; un enfant vit parmi les oiseaux quand son cousin viole et tue sans frein  ; le moulin est hanté par les voix des fantômes, la nature donne les plus beaux fruits mais décapite la chapelle  ; les guerres du monde contemporain rencontrent les combats intérieurs de chaque individu et l’histoire de l’humanité se reproduit dans l’infiniment petit de leurs existences débridées. Parmi eux, un enfant timide sera le chroniqueur de ce royaume hors-norme dont il livre les jours de paix, de luttes, et les nuits de folie pour empêcher l’oubli.\nÉpopée fabuleuse,  mythologie vibrante, fable majestueuse, cette Chronique d’un Royaume perdu est le chef d’œuvre d’Ananda Devi.",
"famille Dumontais, le Vieux Bouc", "2026-08-19", 454, 24.00, 6, 8),
(9, "De l'autre côté du lac", "9782707358233", "« Paola était comme ça. Elle était entière. Elle voulait toujours que tout soit vrai, les rapports humains, les discussions, les rencontres, les projets dans lesquels elle s’engageait. Elle ne supportait pas les faux-semblants, les demi-mesures. Elle était d’un bloc. Elle disait les mots ont de la valeur. Les actes ont de la valeur. Elle voulait qu’il y ait de l’enjeu. C’est dans l’inconfort qu’on se découvre, elle disait. C’est dans l’inconfort qu’on grandit. »\n\nAux abords d’un lac de haute montagne, à la lisière d’une réserve interdite aux humains, un groupe de chercheurs s’affaire. Parmi eux, une photographe aperçoit sur un des versants quelque chose qui échappe au regard de tous les autres. Les signes étranges s’accumulent, un corps est retrouvé. La photographe décide de rester là-haut, seule.\n\nQuelques mois plus tard, c’est elle qui, à son tour, disparaît.\n\nAvec ce roman tout en tension, Sylvain Prudhomme approfondit plusieurs thèmes qui lui sont chers : le désir d’intensité, l’appel du sauvage, le rêve d’une vie vraie.",
"Paola, un photographe", "2026-08-27", 279, 22.00, 7, 9),
(10, "Choses que je croyais perdues", "9782073162854", "« Je voulais te dire : sans le faire exprès, j'ai cassé le verre à moutarde Musclor que lu aimais bien. Le prince sous stéroïdes mal imprimé a perdu sa tête, mais il continue de flatter d'une main distraite l'encolure de son tigre vert de compagnie, Tu avais trouvé ce verre dans un vide-greniers où les gens vendaient pas cher de jolies choses. Après l'avoir regardé longtemps, avec intensité, tu l'avais négocié à deux euros. C'était un souvenir d'enfance et ta joie m'avait attendrie. Ça allait encore entre nous à ce moment-là, enfin je crois. »\n\nSeule dans son appartement, une jeune femme emballe ses affaires. Demain, des déménageurs emporteront ces traces fragiles de son existence. Elle pense à l'homme dont elle vient de se séparer, et des histoires surgissent des objets qu'elle manipule. Une assiette au filet d'or, un ensemble H&M couleur poil de chameau, un rouleau de Sopalin : ces témoins d'une vie ordinaire ont autant à raconter qu'un trépidant roman d'aventures...\n\nQue reste-t-il de ce que nous avons vécu ? De quelles légendes sommes-nous faits ? Les grandes amours comme les petits riens, les désillusions et les désirs sont au coeur de ce roman plein de surprises, à la fantaisie incomparable.",
"Une jeune femme", "2026-08-20", 162, 19.00, 4, 10),
(11, "Minotaure", "9782226511874", "« Être l'indésiré, né hors du désir du père, voilà mon acte de naissance.\nJ'y réponds par un désir extrême, une surenchère d'histoires vécues... ou racontées.\nAprès tout, le Minotaure est un Forçat du sentiment. Forcé d'aimer tous ceux qu'il rencontre.\nAvant de les dévorer. »",
"Minotaure", "2026-08-19", 242, 20.90, 8, 11),
(12, "Une fôret", "9782226499523", "« Le capitaine Lenz finissait par se prendre au jeu. S'il n'avait aucun intérêt dans l'affaire, c'est qu'il ne la comprenait pas. Mais sa curiosité était piquée. Et puis, défendre la cause de ces oiseaux allemands, démontrer qu'ils n'étaient pas de fervents nazis représentait somme toute une occupation préférable à l'ennui. »",
"Capitaine Lenz, les oiseaux allemands", "2026-01-02", 106, 16.90, 8, 12),
(13, "Joseph dans la nuit", "9782378805975", "Voyageur épris d'ailleurs, de stop et de liberté, Olivier est en route vers Lahore pour fêter la nouvelle année sur une plage indienne. En traversant l'Iran, il est arrêté à Chiraz alors qu'explose le mouvement Femme, Vie, Liberté. Accusé d'espionnage, il reste deux ans et demi en prison.\nOlivier est un poète, habitué à vivre de peu, sans confort ni téléphone portable. En cellule, il mobilise tout ce qui peut lui apporter de la lumière, la poésie persane comme les chansons de Britney Spears.\nDerrière ses paupières, installé dans un cinéma dont il est le seul spectateur, il se projette des films. La nuit, il convoque dans ses rêves les êtres aimés.\nUn récit lumineux et bouleversant qui nous dit que, même dans la nuit, quelque chose en nous refusera toujours de céder. La découverte d'un écrivain.",
"Olivier", "2026-08-20", 230, 19.90, 9, 13),
(14, "N'efface pas mes cercles", "9782378562953", "1980, une femme se suicide dans un appartement cossu. Dans les années cinquante, elle s'était unie avec un jeune homme à qui tout l'opposait.\n\nExplorant son histoire familiale, la narratrice tente de démêler les raisons de ce drame et dresse ce faisant le portrait d'une société aux prises avec ses démons : le patriarcat, la guerre, la colonisation, les injonctions à la réussite et au bonheur.\n\nN'efface pas mes cercles remonte le temps à la recherche des destins brisés et restitue avec force l'atmosphère des époques traversées. Cette saga bouleversante confirme le grand art d'Emma Marsantes.",
"la narratrice, une famme, un jeune homme", "2026-08-20", 153, 19.50, 10, 14),
(15, "Bataille au procès", "9782862316857", "En 1956, Georges Bataille est appelé à témoigner au procès de Jean-Jacques Pauvert, poursuivi pour avoir publié les œuvres de Sade. L’auteur d'Histoire de l'oeil comprend que la morale menace de mort la littérature. L’audience devient le miroir de sa propre vie. Les souvenirs affluent : enfance marquée par la folie d’un père aveugle et paralytique, l’indifférence d’une mère réfugiée dans la religion. Des événements qui ont émaillé son parcours surgissent : expériences limites dans ses amours placées sous l’égide de la transgression, visions de guerre et de sacrifice qui le hantent, traversée du mal, liens tourmentés avec le parti communiste, haine du fascisme… Réflexions et fulgurances se mêlent en un vertige où pensée et vie s’entrelacent, entre érotisme et sacré, extase et mort. Mais derrière ces éclats affleure aussi une énigme plus obscure. Refusera-t-elle de se dévoiler ?À travers cet épisode de la vie littéraire, Patrice Trigano accompagne Bataille au plus près de son vertige intérieur. Il explore ce point où l’écriture n’obéit plus à l’auteur, où l’œuvre surgit comme une puissance étrangère, excessive, qui le dépasse.",
"Georges Bataille, Jean-Jacques Pauvert, Patrice Trigano", "2026-08-21", 136, 19.00, 11, 15),
(16, "C'était ça ou mourir", "9782246847069", "Après l’embrasement de son quartier de Port-au-Prince, Jonas n’emporte presque rien avec lui en quittant Haïti : un diplôme, un cahier de poèmes, la photo de sa mère. Toute une vie dans un sac plastique. Se réfugiant d’abord en République dominicaine, puis au Brésil et au Mexique, ce professeur d’histoire franchit les frontières tantôt à bord d’un autobus surchauffé, tantôt en affrontant les profondeurs de la jungle. À chaque étape des visages surgissent, des corps tombent, des solidarités se nouent puis se brisent. Dans l’espoir d’atteindre le Canada et le peu de famille qu’il lui reste, Jonas se retrouve aux portes des États-Unis, seul face aux agents de l’ICE et d’une administration prête à tout pour mener sa chasse aux migrants.\nAvec la trajectoire de Jonas, c’est une cartographie intime de la survie qui se dévoile. Aussi contemporain qu’universel, ce roman raconte les migrations au présent — non comme un concept, mais comme une expérience physique : marcher, avoir faim, se blesser, rire devant l’horreur pour ne pas abandonner. Thélyson Orélien y déploie une écriture foisonnante, traversée d’humour et de poésie, une langue d’exil qui s’apprend « sans grammaire, sans dictionnaire, juste avec les os et la peau ».\nPorté par un souffle narratif irrésistible, C’était ça ou mourir est un premier roman bouleversant qui révèle un écrivain majeur de notre temps.",
"Jonas Dorléon", "2026-08-19", 266, 21.50, 6, 16)
;


-- --------------------------------------------------------

--
-- Structure de la table `person`
--

CREATE TABLE IF NOT EXISTS `person` (
  `pe_id_person` int NOT NULL AUTO_INCREMENT,
  `pe_first_name` varchar(50) NOT NULL,
  `pe_last_name` varchar(50) NOT NULL,
  PRIMARY KEY (`pe_id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=10 CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `person`
--
INSERT INTO person(pe_id_person, pe_first_name, pe_last_name) VALUES
(1, "Philippe", "Jaenada"),
(2, "Sonia", "Devillers"),
(3, "Anne", "Godard"),
(4, "Yannick", "Haenel"),
(5, "Lilia", "Hassaine"),
(6, "Louise", "Chennevière"),
(7, "Olivier", "Rolin"),
(8, "Ananda", "Devi"),
(9, "Sylvain", "Prudhomme"),
(10, "Clémentine", "Mélois"),
(11, "Boris", "Bergmann"),
(12, "Jean-Yves", "Jouannais"),
(13, "Olivier", "Grondeau"),
(14, "Emma", "Marsantes"),
(15, "Patrice", "Trigano"),
(16, "Thélyson", "Orélien"),
(17, "Didier", "Decoin"),
(18, "Françoise", "Chandernagor"),
(19, "Tahar", "Ben Jelloun"),
(20, "Pierre", "Assouline"),
(21, "Philippe", "Claudel"),
(22, "Paule", "Constant"),
(23, "Éric-Emmanuel", "Schmitt"),
(24, "Camille", "Laurens"),
(25, "Pascal", "Bruckner"),
(26, "Christine", "Angot")
;


-- --------------------------------------------------------

--
-- Structure de la table `author`
--

CREATE TABLE IF NOT EXISTS `author` (
  `au_id_author` int NOT NULL,
  `au_biography` TEXT,
  `au_id_person` int NOT NULL,
  PRIMARY KEY (`au_id_author`),
  KEY `au_id_person` (`au_id_person`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `author`
--
INSERT INTO author(au_id_author, au_biography, au_id_person) VALUES
(1, "Philippe Jaenada est l'auteur d'une douzaine de romans, dont Le Chameau sauvage (Julliard, 1997, prix de Flore), La Petite Femelle (2015) et La Serpe (2017, prix Femina) et plus récemment, chez Mialet-Barrault Éditeurs, Au printemps des monstres et La désinvolture est une bien belle chose (2021 et 2024). Il rejoint en cette rentrée littéraire les Éditions Flammarion.", 1),
(2, "Sonia Devillers est journaliste dans la matinale de France Inter et présentatrice du « Dessous des images » sur Arte. Son premier livre, Les Exportés (Flammarion, 2022), raconte comment sa famille a fui la Roumanie communiste.", 2),
(3, "Anne Godard est née à Paris en 1971, elle enseigne la littérature et l'écriture créative à l'université Sorbonne-Nouvelle. Elle a publié aux Éditions de Minuit L'Inconsolable en 2006 (prix RTL-Lire) et Une chance folle en 2017 (prix Alain Spiess du deuxième roman). Nous aussi est son troisième roman.", 3),
(4, "Yannick Haenel a notamment publié Cercle (prix Décembre 2007 et prix Roger Nimier 2008), Jan Karski (prix Interallié et prix du Roman Fnac 2009) et Tiens ferme ta couronne (prix Médicis 2017).", 4),
(5, "Lilia Hassaine est notamment l'autrice de Panorama (2023, prix Renaudot des lycéens). JE est son quatrième roman.", 5),
(6, NULL, 6),
(7, NULL, 7),
(8, "Née à l'île Maurice, Ananda Devi est l'autrice d'une oeuvre récompensée par de nombreux prix et traduite en une douzaine de langues. Parmi ses livres les plus marquants, on peut citer Ève de ses décombres (Gallimard, 2006, prix des Cinq Continents, prix RFO, prix Télévision Suisse Romande), Le Sari vert (Gallimard 2009, prix Louis Guilloux), Le Rire des déesses (Grasset, 2021, prix Femina des lycéens) et Le Jour des caméléons (Grasset, 2023, prix de la Langue française). Elle a reçu le prestigieux prix américain Neustadt 2024 pour l'ensemble de son oeuvre.", 8),
(9, "Sylvain Prudhomme est l'auteur de romans, récits et reportages salués par la critique et traduits à l'étranger. Il a reçu le prix Femina en 2019 pour Par les routes. L'Enfant dans le taxi a paru en 2023 aux Éditions de Minuit. Coyote, récit d'un voyage le long de la frontière américano-mexicaine, a reçu le prix Nicolas Bouvier 2025.", 9),
(10, "Clémentine Mélois est née en 1980. Elle est notamment l'autrice, aux Editions Grasset, de Cent titres. Sinon j'oublie, Dehors, la tempête, ainsi que du très remarqué Alors c'est bien (« L'Arbalète », Editions Gallimard, 2024).", 10),
(11, "Boris Bergmann est né à Paris en 1992. Il est l'auteur de cinq romans dont Nage Libre (prix de la Vocation 2018) et Les Corps insurgés (Prix Fénéon 2020). Il a été pensionnaire de la Villa Medicis et de la Villa Kujoyama. Il a organisé des expositions en France et à l'étranger (autour de l'oeuvre de René Daumal, notamment) et collabore en tant qu'éditeur associé à la revue d'art et de littérature Magma.\nMinotaure est son premier roman autobiographique.", 11),
(12, "Jean-Yves Jouannais, né en 1964, est professeur à l'École nationale supérieure des beaux-arts de Paris. Il a publié, notamment, L'Idiotie (Beaux-Arts livres), Artistes sans oeuvres (Verticales), Les Barrages de sable (Grasset). De 2008 à 2024, il est l'auteur du cycle de conférences-performances, L'Encyclopédie des guerres, au Centre Pompidou (Paris).", 12),
(13, "Après des études littéraires et des emplois de libraire, Olivier Grondeau est parti huit ans sur les routes, avant d'être arrêté en Iran. Libéré en mars 2025, il poursuit désormais des études d'anthropologie. L'écriture l'a toujours accompagné. Joseph dans la nuit est son premier livre.", 13),
(14, NULL, 14),
(15, "Patrice Trigano a fait des études de droit et de philosophie avant de consacrer sa vie à l’art en tant que galeriste, écrivain et dramaturge. Ses livres sont publiés aux éditions de la Différence, Léo Scheer, Mercure de France et Maurice Nadeau. Il a publié en 2024, La Promesse de l’art, Mémoires d’un galeriste aux Éditions du Canoë.", 15),
(16, "Né en 1988, Thélyson Orélien est un auteur québécois d'origine haïtienne. Poète et critique, il construit une oeuvre habitée par la mémoire, l'exil et la question de l'appartenance. Depuis sa publication au Québec par les Éditions du Boréal, C'était ça ou mourir rencontre un écho international exceptionnel et est en cours de traduction dans plus de vingt langues. Un premier roman phénomène qui révèle une grande voix de la littérature contemporaine.", 16)
;

-- --------------------------------------------------------

--
-- Structure de la table `jury`
--

CREATE TABLE IF NOT EXISTS `jury` (
  `ju_id_jury` int NOT NULL AUTO_INCREMENT,
  `ju_is_chairman` BOOLEAN NOT NULL DEFAULT FALSE,
  `ju_id_person` int NOT NULL,
  `ju_id_book` int DEFAULT NULL,
  PRIMARY KEY (`ju_id_jury`),
  UNIQUE KEY `ju_id_person` (`ju_id_person`),
  KEY `ju_id_book` (`ju_id_book`)
) ENGINE=InnoDB CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `jury`
--

INSERT INTO jury(ju_is_chairman, ju_id_person) VALUES
(TRUE, 17),
(DEFAULT, 18),
(DEFAULT, 19),
(DEFAULT, 20),
(DEFAULT, 21),
(DEFAULT, 22),
(DEFAULT, 23),
(DEFAULT, 24),
(DEFAULT, 25),
(DEFAULT, 26);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `author`
--
ALTER TABLE `author`
  ADD CONSTRAINT `author_ibfk_1` FOREIGN KEY (`au_id_person`) REFERENCES `person` (`pe_id_person`);

--
-- Contraintes pour la table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `bo_ibfk_1` FOREIGN KEY (`bo_id_author`) REFERENCES `author` (`au_id_author`),
  ADD CONSTRAINT `bo_ibfk_2` FOREIGN KEY (`bo_id_editor`) REFERENCES `editor` (`ed_id_editor`);

--
-- Contraintes pour la table `jury`
--
ALTER TABLE `jury`
  ADD CONSTRAINT `jury_ibfk_1` FOREIGN KEY (`ju_id_person`) REFERENCES `person` (`pe_id_person`),
  ADD CONSTRAINT `jury_ibfk_2` FOREIGN KEY (`ju_id_book`) REFERENCES `book` (`bo_id_book`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
