import pandas as pd

import csv
import time

from tqdm import tqdm
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def getPlayerURL(playerName, role):
    namesMapping = {
        'Ghost': 'Ghost (Jang Yong-jun)',
        'Rich': 'Rich (Lee Jae-won)',
        'knight': 'Knight (Zhuo Ding)',
        'Bin': 'Bin (Chen Ze-Bin)',
        'Angel': 'Angel (Xiang Tao)',
        'Aki': 'Aki (Mao An)',
        'Wuming': 'Wuming (Wang Xin)',
        'Eric': 'Eric (He Qiang)',
        'Viper': 'Viper (Park Do-hyeon)',
        'Tuesday': 'Tuesday (Jean-Sébastien Thery)',
        'Apollo': 'Apollo (Apollo Price)',
        'John': 'John (John Holtzclaw)',
        'KinG': 'KinG (Tomás Bordón)',
        'King': {
            'jng': 'King (Luka Kralj)',
            'sup': 'King (Trevor Roy)'
        },
        'Matty': 'Matty (Mathieu Breton)',
        'Ziv': 'Ziv (Chen Yi)',
        'QiuQiu': 'QiuQiu (Zhang Ming)',
        'Zeka': 'Zeka (Kim Geon-woo)',
        'Mark': 'Mark (Ling Xu)',
        'bless': 'Bless (Xiang Yi-Tong)',
        'Captain': 'Captain (Luo Fei-Yang)',
        'Wei': 'Wei (Yan Yang-Wei)',
        'Ming': 'Ming (Shi Sen-Ming)',
        'Phoenix': 'Phoenix (Maarten Van Dyck)',
        'Aesthetic': 'Aesthetic (Frank Norqvist)',
        'Night': 'Night (Jeroen Segers)',
        'Miś': 'Miś (Michał Kopacz)',
        'Young': 'Young (Young Choi)',
        'Albus NoX': 'Albus NoX (Stepan Titov)',
        'Circus': 'Circus (Jacob Yoh)',
        'Diesel': 'Diesel (Darrell Jenkins)',
        'Aspect': 'Aspect (Joshua Lee)',
        'Shiro': 'Shiro (Kyle Sakamaki)',
        'Riku': 'Riku (Henry Nguyen)',
        'Eclipse': 'Eclipse (Yujie Wu)',
        'Gweiss': 'Gweiss (Garrett Weiss)',
        'Scholar': 'Scholar (Preston Hall)',
        'APA': 'APA (Eain Stearns)',
        'Winter': 'Winter (Olivier Lapointe)',
        'Hunter': 'Hunter (Hunter Meyer)',
        'Hyper': 'Hyper (Young Seo)',
        'Barrage': 'Barrage (Luc van Gestel)',
        'NooB': 'NooB (Léo Pitrey)',
        'GGsir': 'GG Sir',
        'Seal': 'Seal (Fabian de Lint)',
        'Shadow': {
            'sup': 'Shadow (Facundo Cuello)'
        },
        'Doran': 'Doran (Choi Hyeon-joon)',
        'HyBriD': 'HyBriD (Lee Woo-jin)',
        'Ahn': 'Ahn (An Shan-Ye)',
        'CJ': 'CJ (Yang Chong-Jiang)',
        'Arthur': 'Arthur (Park Mi-reu)',
        'Jerry': 'Jerry (Zhou Ke-Xue)',
        'Sleepy': 'Sleepy (Wang He-Yong)',
        'Tarzan': 'Tarzan (Lee Seung-yong)',
        'Light': 'Light (Wang Guang-Yu)',
        'Taxer': 'Taxer (Christian Vendelbo)',
        'Click': 'Click (Vittorio Massolo)',
        'aki': 'Aki (Daniel Lauri)',
        'Lotus': 'Lotus (Ignatios Psarros)',
        'Jay': 'Jay (Chen Bo)',
        'FATE': 'FATE (Yoo Su-hyeok)',
        'River': {
            'jng': 'River (Kim Dong-woo)',
        },
        'QingZhi': 'QingZhi (Lin Han)',
        'BAO': 'BAO (Jeong Hyeon-woo)',
        'Becca': 'Becca (Son Min-woo)',
        'Dread': 'Dread (Lee Jin-hyeok)',
        'Fly': 'Fly (Song Yong-jun)',
        'Kane': 'Kane (Chen Hao)',
        'Sora': 'Sora (Liu Zhi-Long)',
        'demon': 'Demon (Wu Yue-Wei)',
        'Cube': 'Cube (Dai Yi)',
        'Hachi': 'Hachi (Davy de Graaf)',
        'Closer': 'Closer (Can Çelik)',
        'Solo': 'Solo (Colin Earnest)',
        'Griffin': 'Griffin (Raymond Griffin)',
        'Vulcan': 'Vulcan (Philippe Laflamme)',
        'Neo': {
            'bot': 'Neo (Toàn Trần)'
        },
        'Diamond': 'Diamond (David Bérubé)',
        'Ye': 'Ye (Ji Xin-Yu)',
        'Naruto': 'Naruto (Nie Hao)',
        'Trigger': 'Trigger (Kim Eui-joo)',
        'Chance': 'Chance (Pei Piao)',
        'Trigo': 'Trigo (Matheus Trigo)',
        'Bankai': 'Bankai (Renan Pirone)',
        'Aegis': 'Aegis (Gabriel Lemos)',
        'Avenger': 'Avenger (Adriano Perassoli)',
        'Jojo': 'Jojo (Gabriel Dzelme)',
        'Envy': 'Envy (Bruno Farias)',
        'Hawk': 'Hawk (Gabriel Gomes)',
        'Spark': 'Spark (Lucas Keith)',
        'Eragon': 'Eragon (Adam Harney)',
        'Lonely': 'Lonely (Han Gyu-joon)',
        'Dice': 'Dice (Hong Do-hyeon)',
        'Kael': 'Kael (Kim Jin-hong)',
        'Clear': 'Clear (Song Hyeon-min)',
        'Jun': 'Jun (Yoon Se-joon)',
        'Noah': 'Noah (Oh Hyeon-taek)',
        'Thanatos': 'Thanatos (Park Seung-gyu)',
        'Storm': 'Storm (Lee Jae-dong)',
        'Valkyrie': 'Valkyrie (Ko Joon-yeong)',
        'Dream': 'Dream (Tan Wen-Xiang)',
        'FIESTA': 'FIESTA (An Hyeon-seo)',
        'LOCKIE': 'Tsigas',
        'Deluxe': 'Deluxe (Klemen Papež)',
        'Hades': 'Hades (Maik Jonker)',
        'Nyx': 'Nyx (Óscar Ruiz Vargas)',
        'Marky': 'Marky (Pedro José Serrano)',
        'Sharp': 'Sharp (Anders Lilleengen)',
        'Sven': 'Sven (Sven Olejnikow)',
        'Eren': 'Eren (Nguyễn Đức Anh)',
        'Scarface': 'Scarface (Daniel Aitbelkacem)',
        'Lion': {
            'sup': 'Lion (Stelios Marinos)'
        },
        'SMILEY': 'SMILEY (Ludvig Granquist)',
        'Adam': 'Adam (Adam Maanane)',
        'Rabble': 'Rabble (Jochem van Graafeiland)',
        'Rogue': 'Rogue (Jake Sharwood)',
        'Scarlet': 'Scarlet (Marcel Wiederhofer)',
        'Tyrin': 'Tyrin (William Portugal)',
        'Royal': 'Royal (Alexandru Mihai Pricu)',
        'Dioge': 'Dioge (Diogenes Barbosa)',
        'Flare': 'Flare (Park Sang-gyu)',
        'flare': 'Flare (Luiz Felipe Lobo)',
        'Prime': 'Prime (Olivier Payet)',
        'asta': 'Asta (Wyllian Adriano)',
        'Bounty': 'Bounty',
        'Raven': 'Ravenzin',
        'Leo': 'Leo (Han Gyeo-re)',
        'Air': 'Air (Shenghao He)',
        'Yeon': 'Yeon (Sean Sung)',
        'Spawn': 'Spawn (Trevor Kerr-Taylor)',
        'Copy': 'Copy (Jouhan Pathmanathan)',
        'Mine': 'Mine (Tao Jun)',
        'Shady': 'Shady (Jordan Robison)',
        'Xing': 'Xing (Liu Jia-Xing)',
        'Dreams': 'Dreams (Han Min-kook)',
        'Monk': 'Monk (Joosep Kivilaan)',
        'Vengeance': 'Vengeance (William Blackmore)',
        'Violet': 'Violet (Vincent Wong)',
        'KingKong': 'KingKong (Byeon Jeong-hyeon)',
        'Forsaken': 'Forsaken (Dennis Kroes)',
        'Lucas': 'Lucas (Li Tan-Pan-Ao)',
        'Puff': 'Puff (Ding Wang)',
        'Ackerman': 'Ackerman (Gabriel Aparicio)',
        'Pancake': 'Pancake (Manuel Scala)',
        'Sh4dowUS': 'Sh4dow us',
        'Artemis': 'Artemis (Trần Quốc Hưng)',
        'BOSS': 'BOSS (Vladislav Fomin)',
        'Spooky': 'Spooky (Miroslav Gochev)',
        'kun': 'Kun (Dong Zhen-Shuo)',
        'Shark': 'Shark (Zhang Yu-Qi)',
        'Aliez': 'Aliez (Huang Hao)',
        'Hope': 'Hope (Wang Jie)',
        'Taki': 'Taki (Đinh Anh Tài)',
        'Style': {
            'jng': 'Style (Ignacio Pezoa)',
            'bot': 'Style (Nguyễn Hoàng Sơn)'
        },
        'Maple': 'Maple (Huang Yi-Tang)',
        'Koala': {
            'top': 'Koala (Braulio Hernandez)',
            'sup': 'Koala (Lin Chih-Chiang)'
        },
        'Kirito': 'Kirito (Nicolás Olavarría)',
        'Rhino': 'Rhino (Douglas Reynolds)',
        'Panda': 'Panda (James Ding)',
        'Impulse': 'Impulse (Fabio Wortmann)',
        'Nite': 'Nite (Ardian Spahiu)',
        'Glory': {
            'mid': 'Glory (Lê Ngọc Vinh)',
            'sup': 'Glory (Matías Maldonado)'
        },
        'Blue': 'Blue (Ersin Gören)',
        'Dan': 'Dan (Daniel Hockley)',
        'Candy': {
            'jng': 'Candy (Rafael Díaz)',
            'mid': 'Candy (Kim Seung-ju)'
        },
        'Ace': 'Ace (Kotoji Mugita)',
        'Pilot': 'Pilot (Na Woo-hyung)',
        'Mocha': 'Mocha (Kim Tae-gyeom)',
        'Honey': 'Honey (Park Bo-heon)',
        'Meliodas': 'Meliodas (Hoàng Tiến Nhật)',
        'Neon': 'Neon (Matúš Jakubčík)',
        'Titus': 'Titus (Seth Rochtus)',
        'Von': 'Von (Dimitris Bakiris)',
        'Hatred': 'Hatred (Veselin Popov)',
        'Paladin': 'Paladin (Ivan Delač)',
        'Slayer': 'Slayer (Nuno Moutinho)',
        'Galaxy': 'Galaxy (Jorge Molina)',
        'Comeback': 'Comeback (Cosmin Mreana)',
        'Time': 'Time (Tiago Almeida)',
        'Pride': 'Pride (Mahdi Nasserzadeh)',
        'Frozen': 'Frozen (Tiago Tavares)',
        'Beat': 'Beat (José Mesquita)',
        'Absolute': 'Absolute (Batuhan Okta)',
        'Dean': 'Dean (Dean Wood)',
        'Shine': 'Shine (Tôn Nguyễn Phi Long)',
        'Steal': 'Steal (Mun Geon-yeong)',
        'Camanagozo': 'Camanagazo',
        'Hiro': 'Hiro (Nguyên Đại Hải)',
        'Emperor': 'Emperor (Viktor Liptai)',
        'Kimi': 'Kimi (Cristian Aparicio)',
        'Trashy': 'Trashy (Alejo Rivero)',
        'Prodigy': 'Prodigy (Javier Juárez)',
        'Nobody': 'Nobody (Nicolás Ale)',
        'Sami': 'Sami (Nicolás Veliz)',
        'Wesker': 'Wesker (Ivan Silva)',
        'Pan': 'Pan (Andres Bonilla)',
        'Ocean': 'Ocean (Nicolás Pérez)',
        'Lexa': 'Lexa (Aleksa Ilić)',
        'Zerito': 'Zero (Tomas Colangelo)',
        'JackPoT': 'JackPoT (Park Jin-soo)',
        'Tokz': 'Tokz (Simon Hermansen)',
        'Tiger': 'Tiger (Alan Roger)',
        'Viktor': 'Viktor (Viktor Savčenko)',
        'Destiny': 'Destiny (Mitchell Shaw)',
        'Frost': 'Frost (Juan Pablo Díaz)',
        'Smurf': 'Smurf (Dmitri Ivanov)',
        'Prince': 'Prince (Lee Chae-hwan)',
        'Maxim': 'Maxim (Maxim Tarasov)',
        'Jacob': {
            'jng': 'Jacob (Jakub Milý)',
            'mid': 'Jacob (Jacob Nielsen)',
            'bot': 'Jacob (Jakub Przewozniczuk)'
        },
        'Flash': 'Flash (Luís Cerqueira)',
        'Sky': {
            'top': 'Sky (David Koppmann)',
            'mid': 'Sky (Zhan Xiong)'
        },
        'Rock': 'Rock (Tsai Chung-Ting)',
        'Blaze': 'Blaze (Jia Xiang)',
        'APEX': 'APEX (Hsieh Chia-Wei)',
        'Sin': 'Sin (Alin Sin)',
        'Savior': 'Savior (Zhang Jun-Chao)',
        'Akuma': 'Akuma (Wu Kuan)',
        'cc': 'Cc',
        'Noway': 'Noway (Nguyễn Vũ Long)',
        'invincible': 'Invincible',
        'Aria': 'Aria (Lee Ga-eul)',
        'Carry': 'Carry (Mustafa Selim Yılmaz)',
        'LIMIT': 'LIMIT (Dino Tot)',
        'Unlucky': 'Unlucky (Luca Santos)',
        'Hopeful': 'Hopefulx',
        'Unforgiven': 'Unforgiven (Maximiliano Utrero)',
        'Miracle': 'Miracle (Ruslan Zainulin)',
        'MnM': 'MnM (Wong Ka Chun)',
        'Stark': 'Stark (Phan Công Minh)',
        'Rainbow': 'Rainbow (Kim Soo-gi)',
        'Humble': 'Humble (Huang Min-Min)',
        'Jekko': 'Jekko (Jemal Revazishvili)',
        'Tempest': 'Tempest (Andrew Stark)',
        'Noxus': 'Noxus (Stavros Xiarchogiannopoulos)',
        'Tomate': 'Tomate (Tomás García)',
        'Caos': 'Caos (Nicolás Guzmán)',
        'Sty1e': 'Style (Nguyễn Hoàng Sơn)',
        'Kingkong': 'Kingkong (Byeon Jeong-hyeon)',
        'Simon': {
            'top': 'Simon (Dương Thanh Hoà)',
            'mid': 'Simon (Szymon Marcinkiewicz)'
        },
        'Vit': 'Vit (Lê Hoài An)',
        'Hide': {
            'bot': 'Hide (Gil Seon-ho)',
            'sup': 'Hide (Mark Angelov)'
        },
        'Leon': {
            'sup': 'Leon (Leon Anton)'
        },
        'Carnage': {
            'jng': 'Carnage (Vasilis Syrianos)'
        },
        'Bung': {
            'bot': 'Bung (Jakob Gramm)'
        },
        'Danny': {
            'bot': 'Danny (Kyle Sakamaki)'
        },
        'OddOrange': 'TheOddOrange',
        'DRX ZMT': 'ZMT',
        'Comp Array': 'Array',
        'Hanabi': 'Hanabi (Su Chia-Hsiang)',
        'ReaL': 'ReaL (Artūras Stefanovič)',
        'Raptor': 'Raptor (Jeon Eo-jin)',
        'Prove': {
            'top': 'Prove (Patryk Adamiec)',
            'sup': 'Prove (Son Min-hyeong)'
        },
        'Zest': {
            'top': 'Zest (Kim Dong-min)',
            'sup': 'Zest (Hsieh Ming-Hsuan)'
        },
        'Lucid': 'Lucid (Choi Yong-hyeok)',
        'Seonbi': 'Seonbi (Koo Gwan-mo)',
        'Noodle': 'Noodle (Kim Kroon)',
        'Winner': 'Winner (Woo Joo-sung)',
        'MC': 'MC (Mohammed Chinoune)',
        'Jeremy': 'Jeremy (Jeremy Gnas)',
        'Pluto': {
            'jng': 'Pluto (David Hrabánek)',
            'sup': 'Pluto (Nick Jones)'
        },
        'Perry': 'Perry (Perry Norman)',
        'Topo': 'Topo (Charles Uram)',
        'Enigma': 'Enigma (Julien Mayrand)',
        'Chris': {
            'jng': 'Chris (Krystian Dobrzański)'
        },
        'Sword': 'Sword (Rico Chen)',
        'marlon': 'Marlon (Igor Tomczyk)',
        'DuDu': 'DuDu (Lee Dong-ju)',
        'Peng': 'Peng (Pengcheng Shen)',
        'Peter': 'Peter (Jeong Yoon-su)',
        'Sketch': 'Sketch (Brady Holmich)',
        'Revenge': {
            'top': 'Revenge (Mohamed Kaddoura)',
            'mid': 'Peng (Pengcheng Shen)'
        },
        'Misaki': 'Misaki (Telmo Oliveira)',
        'Faded': 'Faded (Anastasios Koutsouras)',
        'Dragon': {
            'mid': 'Dragon (María Zarate)',
            'top': 'Dragon (Manuel Cortes)',
            'bot': 'Dragon (Manuel Cortes)'
        },
        'Twelve': 'Twelve (Idriss Madouche)',
        'Rift': 'Rift (Jérémie Luthy)',
        'Joo': 'Joo (João Pereira)',
        'Paradox': {
            'bot': 'Paradox (Dimitris Tsiavos)',
            'sup': 'Paradox (Federico Princiotta Cariddi)',
            'mid': 'Paradox (Selina Stengel)'
        },
        'JDG': 'JDG (Manuel Soares)',
        'Music': 'Music (Sean Wishko)',
        'Lelouch': {
            'bot': 'Lelouch (Alexandrescu Cristian)'
        },
        'Strange': {
            'mid': 'Strange (Cristopher Gonzalez)'
        },
        'Syrpy': 'Meager',
        'baekho': {
            'bot': 'BaeKHo (Baek Seung-min)',
            'jng': 'Baekho (Hyun-woo Choe)'
        },
        'Porsche': {
            'top': 'Porsche (Shane Higginbotham)'
        },
        'Ice': {
            'bot': 'Ice (Yoon Sang-hoon)'
        },
        'Philip': {
            'top': 'Philip (Philip Zeng)'
        },
        'Music': {
            'jng': 'Music (Sean Wishko)'
        },
        'Mayhem': 'Mayhem (Samuel García)',
        'Mega': {
            'jng': 'Mega (Carlos Herrera)',
            'bot': 'Mega (Åsmund Rosshaug)'
        },
        'Marth': {
            'top': 'Marth (Luis De La Rosa)',
            'bot': 'Marth (Julian Maletzky)'
        },
        'Machine': {
            'bot': 'Machine (Batuhan Karagenç)'
        },
        'Crazy': {
            'top': 'Crazy (Kim Jae-hee)'
        },
        'Black': 'Black (Murat Ulukan Ayaz)',
        'Chloe': 'Chloe (Jeon Seong-hyeon)',
        'Hoon': 'Hoon (Lee Jang-hoon)',
        'Typhoon': {
            'bot': 'Typhoon (Chen Dai-Feng)',
            'jng': 'Typhoon (Tayfun Gümüş)'
        },
        'Drop': {
            'bot': 'Drop (Matheus Herdy)'
        },
        'Kick': 'Kick (João Rosas)',
        'Lionel': {
            'sup': 'Lionel (Matthew Desa)'
        },
        'Fang': 'Fang (Ignacio Gutierrez)',
        'Pinky': 'Pinky (Oscar Gomez)',
        'Lance': {
            'top': 'Lance (Rafael Romero)'
        },
        'ALPHA': 'ALPHA (Derick Reyes)',
        'Darkin': 'Darkin (Santiago Rendón)',
        'Catan': 'Catan (Dylan Bravo)',
        'Benji': {
            'mid': 'Benji (Petros Tsiafitsas)',
            'bot': 'Benji (Nicolas Vidal)'
        },
        'Sloth': {
            'sup': 'Sloth (Bae Jung-sub)'
        },
        'Mime': 'Mime (Nicolas Bojos)',
        'Pyl': 'Pyl (Bryan Torres)',
        'Chaos': {
            'jng': 'Chaos (Álvaro Dória)'
        },
        'Feng': {
            'jng': 'Feng (Jose Ricalday)',
            'sup': 'Feng (Chen Guo-Feng)'
        },
        'Van': {
            'jng': 'Van (Ivan Dellanque)',
            'top': 'Van (Hikaru Murokoshi)'
        },
        'Jason': 'Jason (Kevin Yuquilema)',
        'Billy': 'Billy (Adriano Moreno)',
        'Fade': 'Fade (Muhammed Fatih Kurşun)',
        'Archer': 'Archer (Lee Keun-hee)',
        'Shall': 'Shall (Jorge Mendoza)',
        'Snoopy': 'Snoopy (Renato Chávez)',
        'Billy': 'Billy (Adriano Moreno)',
        'San': 'San (Jose Luis Caceres)',
        'Kenny': {
            'sup': 'Kenny (Lukáš Křivánek)'
        },
        'FIare': 'Flare (Franco Pombo)',
        'Kz': 'Kz (Nicolás Gutiérrez)',
        'Jelly': 'Jelly (Son Ho-gyeong)',
        'Fear': 'Fear (Joel Reyna)',
        'Berserker': 'Berserker (Kim Min-cheol)',
        'Stealth': 'Stealth (Alejandro Cardenaz)',
        'DarkMoon': 'DarkMoon (Jorge Baca)',
        'Holo': 'Holo (Tsang Dek Lam)',
        'Faith': 'Faith (Sit Chong Fai)',
        'Kaito': 'Kaito (Kaito Mitsufuji)',
        'Taco': 'Taco (Fan Zhao-Fu)',
        'eXyu': 'EXyu',
        'Quiet': {
            'bot': 'Quiet (Tang Yong)',
            'top': 'Quiet (Lin Wei-Zhe)'
        },
        'Shin': 'Shin (Kirill Shurkin)',
        'Silk': 'Silk (Ivan Gantsyuk)',
        'Akashi': 'Akashi (Oussama Cherradi)',
        'Punisher': 'Punisher (Konstantinos Katsikadakos)',
        'DK': 'DK (Yuot Mayuom)',
        'Wally': 'Wally (Waeel Elhilali)',
        'Zenitsu': {
            'top': 'Zenitsu (Marco Rodriguez)',
            'bot': 'Zenitsu (Sérgio Silva)'
        },
        'Duel': 'Duel (Jim Alvear)',
        'Yato': 'Yato (Walter Vargas)',
        'Imperial': 'Imperial (Evgeny Sorokin)',
        'Sweet': 'Sweet (Yousef Rakabe)',
        'Senshi': 'Senshi (Angello Molina)',
        'Rebirth': 'Rebirth (Fu Chun Kit)',
        'Awakër': 'Awakër (Martin Maxa)',
        'Crow': 'Crow (Luca Nucci)',
        'Lure': 'Lure (Shin Jae-yoon)',
        'Nash': 'Nash (Alf-Kristian Sund)',
        'Dante': {
            'bot': 'Dante (Alvin Wong)',
            'jng': 'Dante (Lê Văn Dự)'
        },
        'Trap': 'Trap (Shin Seung-min)',
        'Kingdom': 'Kingdom (Kim Seong-kwon)',
        'Way': {
            'sup': 'Way (Han Gil)',
            'bot': 'Way (Han Gil)',
            'mid': 'Way (Park Byeong-joon)'
        },
        'mumus100': 'Mumus100',
        'Min': {
            'top': 'Min (Ryan Min)',
            'mid': 'Min (Lim Hyeong-min)'
        },
        'Miss': 'Miss (Letícia Porto)'
    }

    if playerName in namesMapping:
        if isinstance(namesMapping[playerName], str):
            return namesMapping[playerName]
        else:
            return namesMapping[playerName][role]

    return playerName


def crawlerPlayerInfos(playerName, playingChampion, startDate, endDate, game, role):
    gp = 0
    wr = 0
    kda = 0
    playerName = getPlayerURL(playerName, role)

    chrome_path = r'dependency/chromedriver'
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('window-size=1400,600')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=chrome_path, options=options)
    driver.get(
        "https://oracleselixir.com/player/{}/championPool".format(playerName))

    # Aguardando carregamento da página e exibição do input de Start Date
    wait = WebDriverWait(driver, 10)
    try:
        start_date_input = wait.until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="start_date"]')), message='Campo "Start Date" era esperado na busca do jogador {} e não foi encontrado.'.format(playerName))
        # start_date_input.send_keys(startDate)
    except TimeoutException as ex:
        with open('outputs/incorrect-names.txt', 'a', encoding='utf-8') as f:
            f.write("{} - {}\n".format(playerName, game))
        return []

    time.sleep(5)

    # Aguardando carregamento da página e exibição do input de End Date
    start_date_input = wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="end_date"]')), message='Campo "Start Date" era esperado na busca do jogador {} e não foi encontrado.'.format(playerName))
    start_date_input.send_keys(endDate)

    # Aguardando carregamento da página e exibição dos resultados
    time.sleep(5)

    if (len(driver.find_elements(by=By.XPATH, value="//*[text()=\"{}\"]/following::div/following::div".format(playingChampion))) != 0):
        # Obtendo valores de GP, W% e KDA
        games_played_element = driver.find_elements(
            by=By.XPATH, value="//*[text()=\"{}\"]/following::div/following::div".format(playingChampion))[0]
        win_rate_element = driver.find_elements(
            by=By.XPATH, value="//*[text()=\"{}\"]/following::div/following::div/following::div".format(playingChampion))[0]
        kda_element = driver.find_elements(
            by=By.XPATH, value="//*[text()=\"{}\"]/following::div/following::div/following::div/following::div/following::div".format(playingChampion))[0]

        gp = games_played_element.text
        wr = win_rate_element.text
        wr = float(wr.rstrip('%')) / 100.0
        kda = kda_element.text

    driver.quit()

    return gp, wr, kda


def processGames(game, side):

    if isinstance(game, str) and processed_games.str.contains(str(game)).any() == False:

        datacompleteness = df[(df['gameid'] == game) & (df['side'] == side)
                              & (df['position'] == 'top')].datacompleteness.values[0]
        if datacompleteness != 'complete':
            return

        # GAME DATETIME
        endDate = dt.strptime(
            df[(df['gameid'] == game)].date.values[0], '%Y-%m-%d %H:%M:%S')
        # startDate = endDate - relativedelta(months=1)
        formatedEndDate = "{}-{:02d}-{:02d}".format(
            endDate.year, endDate.month, endDate.day - 1)
        formatedStartDate = ''
        # formatedStartDate = "{:02d}/{:02d}/{}".format(
        # startDate.day - 1, startDate.month, startDate.year)

        # BLUE TEAM
        blueTop = df[(df['gameid'] == game) & (df['side'] == side)
                     & (df['position'] == 'top')].champion.values[0]
        blueTopPlayer = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'top')].playername.values[0]
        if (blueTopPlayer != 'unknown player'):
            crawler = crawlerPlayerInfos(
                blueTopPlayer, blueTop, formatedStartDate, formatedEndDate, game, 'top')
            blueTop = int(
                df_champions.loc[df_champions['id'] == blueTop]['key'])
            if (crawler):
                topGP = crawler[0]
                topWR = crawler[1]
                topKDA = crawler[2]
            else:
                return
        else:
            return

        blueJungle = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'jng')].champion.values[0]
        blueJunglePlayer = df[(df['gameid'] == game) & (
            df['side'] == side) & (df['position'] == 'jng')].playername.values[0]
        if (blueJunglePlayer != 'unknown player'):
            crawler = crawlerPlayerInfos(
                blueJunglePlayer, blueJungle, formatedStartDate, formatedEndDate, game, 'jng')
            blueJungle = int(
                df_champions.loc[df_champions['id'] == blueJungle]['key'])
            if (crawler):
                jungleGP = crawler[0]
                jungleWR = crawler[1]
                jungleKDA = crawler[2]
            else:
                return
        else:
            return

        blueMid = df[(df['gameid'] == game) & (df['side'] == side)
                     & (df['position'] == 'mid')].champion.values[0]
        blueMidPlayer = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'mid')].playername.values[0]
        if (blueMidPlayer != 'unknown player'):
            crawler = crawlerPlayerInfos(
                blueMidPlayer, blueMid, formatedStartDate, formatedEndDate, game, 'mid')
            blueMid = int(
                df_champions.loc[df_champions['id'] == blueMid]['key'])
            if (crawler):
                midGP = crawler[0]
                midWR = crawler[1]
                midKDA = crawler[2]
            else:
                return
        else:
            return

        blueCarry = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'bot')].champion.values[0]
        blueCarryPlayer = df[(df['gameid'] == game) & (
            df['side'] == side) & (df['position'] == 'bot')].playername.values[0]
        if (blueCarryPlayer != 'unknown player'):
            crawler = crawlerPlayerInfos(
                blueCarryPlayer, blueCarry, formatedStartDate, formatedEndDate, game, 'bot')
            blueCarry = int(
                df_champions.loc[df_champions['id'] == blueCarry]['key'])
            if (crawler):
                carryGP = crawler[0]
                carryWR = crawler[1]
                carryKDA = crawler[2]
            else:
                return
        else:
            return

        blueSupp = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'sup')].champion.values[0]
        blueSuppPlayer = df[(df['gameid'] == game) & (
            df['side'] == side) & (df['position'] == 'sup')].playername.values[0]
        if (blueSuppPlayer != 'unknown player'):
            crawler = crawlerPlayerInfos(
                blueSuppPlayer, blueSupp, formatedStartDate, formatedEndDate, game, 'sup')
            blueSupp = int(
                df_champions.loc[df_champions['id'] == blueSupp]['key'])
            if (crawler):
                suppGP = crawler[0]
                suppWR = crawler[1]
                suppKDA = crawler[2]
            else:
                return
        else:
            return

        # RESULT
        kills = df[(df['gameid'] == game) & (df['side'] == side)
                   & (df['position'] == 'team')].teamkills.values[0]
        deaths = df[(df['gameid'] == game) & (df['side'] == side)
                    & (df['position'] == 'team')].teamdeaths.values[0]
        towers = df[(df['gameid'] == game) & (df['side'] == side)
                    & (df['position'] == 'team')].towers.values[0]
        dragons = df[(df['gameid'] == game) & (df['side'] == side)
                     & (df['position'] == 'team')].dragons.values[0]
        heralds = df[(df['gameid'] == game) & (df['side'] == side)
                     & (df['position'] == 'team')].heralds.values[0]
        barons = df[(df['gameid'] == game) & (df['side'] == side)
                    & (df['position'] == 'team')].barons.values[0]
        inhibitors = df[(df['gameid'] == game) & (df['side'] == side)
                        & (df['position'] == 'team')].inhibitors.values[0]
        firstBlood = df[(df['gameid'] == game) & (df['side'] == side)
                        & (df['position'] == 'team')].firstblood.values[0]
        firstTower = df[(df['gameid'] == game) & (df['side'] == side)
                        & (df['position'] == 'team')].firsttower.values[0]
        firstHerald = df[(df['gameid'] == game) & (df['side'] == side)
                         & (df['position'] == 'team')].firstherald.values[0]

        if side == 'Blue':
            flagSide = 1
        else:
            flagSide = 0

        # WRITING TO DATASET FILE
        with open('data/secondary-prediction/secondary_prediction_players_statistics.csv', mode='a', newline="") as dataset2022:
            datasetWriter = csv.writer(dataset2022, delimiter=',')
            datasetWriter.writerow([game, flagSide, topGP, topWR, topKDA, jungleGP, jungleWR, jungleKDA, midGP, midWR, midKDA, carryGP, carryWR, carryKDA, suppGP, suppWR,
                                    suppKDA, kills, deaths, firstBlood, firstTower, firstHerald, dragons, barons, inhibitors, towers, heralds])


df = pd.read_csv("data/secondary-prediction/mess_dataset_22.csv")
df_champions = pd.read_csv('data/dataset_champions.csv')
games = df.gameid.drop_duplicates()
processed_df = pd.read_csv(
    "data/secondary-prediction/secondary_prediction_players_statistics.csv")
processed_games = processed_df.game.drop_duplicates()
sides = ['Blue', 'Red']

header = 'game,flagSide,topGP,topWR,topKDA,jungleGP,jungleWR,jungleKDA,midGP,midWR,midKDA,carryGP,carryWR,carryKDA,suppGP,suppWR,suppKDA,kills,deaths,firstBlood,firstTower,firstHerald,dragons,barons,inhibitors,towers,heralds\n'
with open('data/secondary-prediction/secondary_prediction_players_statistics.csv', mode='a') as dataset:
    dataset.write(header)

for game in tqdm(games):
    for side in sides:
        processGames(game, side)
