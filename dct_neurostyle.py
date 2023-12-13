# conda create --name NEURODCTSTYLE
# https://github.com/unton3ton/Ma3shka/blob/main/qrtest.py
# https://neural-style-transfer-app.ew.r.appspot.com/

# conda activate NEURODCTSTYLE

# pip install blind-watermark

## Embed watermark:

# from PIL import Image
from blind_watermark import WaterMark

# длина внедрённого текста зависит от размеров изображения-переносчика 
# test = Image.open('img/Free-Style-Transfer.jpg').resize((3840,2160)).save('img/style-resize.jpg')

# name = 'Free-Style-Transfer-resize.jpg'  
# name = 'eyessmall.jpg'

bwm1 = WaterMark(password_img=1, password_wm=123456789)
# bwm1.read_img(f'img/{name}')

wm = 'testoвое сообщение для проверки влияния переноса стиля на DCT-внедрение'

# wm = 'Helicopter maintenance\
# Optimal maintainability by design:\
# ‘The H175 benefits from Airbus Helicopters comprehensive\
# ‘experience оп helicopter maintenance acquired through\
# years of operators feedback from the eld This helicopter\
# hhas bean designed using the task-oriented MSG-2\
# ‘methodology reducing of 20% maintenance tasks quantty\
# lis maintenance program continuously improves thanks 10\
# the Living Maintenance Review Board process (ving\
# MRE) Reus ‘The new design ofthe dynamic chain loads to а strong\
# Improvement of Time Limits. ‘Main Dynamic components with\
# TBO 5000 hours (Engine MGB, TGB, Main Hyd Pumps, Servos...)\
# Main components have been designed to be removed /\
# fled within short times to redues helicopter downtimes,\
# Removalfinstallation times : Engine in 45 minutes\
# Main Rotor Head in 1,8 Hours H175_ maintenance program (MSM) \
# has evolved to a maintenance-by-task concept witha top-down \
# approach Operators are able to organize their periodic\
# maintenance plan according to their own activity and organization\
# ‘optimizing associated MMH and reducing downtimes,\
# R:P6:6,1h+ Pits oan perform the Turn Around and Daily checks\
# ‘No scheduled mechanical check is requested unt\
# 50ЕН+ Sencing and General Vial inspection focused unt\
# 400 FH interval ‘Observed Times to inspect\
# 50 FH inspection in 10 Hrs. 100 FH inspection in 14 Hrs.\
# + Main intervals at 400, 800 ane 1600 FH\
# boing possible to perform progressive\
# maintenance, «12 MMHVEH total aircraft scheduled\
# maintenance = №о more major inspection to be performed'

# wm = '[[[[7, 7], [550, 7], [550, 197], [7, 197]],\
# \'Helicopter maintenance Optimalmaintainability\
# by design The Н175 beraiits frum Airuug\
# Helicapters compre k unsive Mai componerts\
# havа been designed to be rEmavыd ахрвгiвпсе\
# сп helicapar mainteranсе acquired #hrcugh\
# flted within shurt limes a ruduca helicapter\
# dow r timnE 5. yeнrs oi cpErators leвduack\
# frorn \"hе field  This helicaptar \
# Lean designed usirig Taak-urietiled\
# MsG-3 metkatcagy rEcucirg of 2U56 \
# maiпtэrarca tasks quantily: Femaval\
# Installation times Its mяйлапапсв \
# pragram ccпtinuausly impravas Ihanks\
# Iu Епgiпе in 45 miпutвs the Living\
# Mainteпarice HEviвw Воaid process\
# {Iiving Main Rotar Head in 1.5 \
# Hours мяBJ:\'], [[[287, 208], [557, 208],\
# [557, 275], [287, 275]], \'НТ75\
# \"пiпtЕпапсе program [MSM} haя\
# EvclvEd to mainitenante-by-tHsk\
# cancEal wilh a top-dowr appmath.\
# Cperators are abla 0 organize\
# thвir aariccic maintenance \
# plan accarding to Ikuir сwп\
# activiy and argarization,\
# optimizing associnied MMH and ruducing\
# dowrtimus .\'], [[[80, 312], [136, 312],\
# [136, 327], [80, 327]], \'p5 ; 17 "\'],\
# [[[309, 312], [365, 312], [365, 327],\
# [309, 327]], \'a1 : 9,31\'], [[[391, 361],\
# [448, 361], [448, 376], [391, 376]],\
# \'Р2 - 2 8h\'], [[[106, 431], [168, 431],\
# [168, 446], [106, 446]], \'[4 ; 15 7 h\'],\
# [[[432, 463], [487, 463], [487, 478],\
# [432, 478]], \'РБ : 6,1 |\'], [[[8, 490],\
# [266, 490], [266, 516], [8, 516]],\
# "Тhe пэw\' design of tka dynamic chmin \
# [энds to а strang #rpavamerl ol Tirre Liils"],\
# [[[294, 489], [544, 489], [544, 554], [294, 554]],\
# \'Pilots свп pвrlarmi tkE Turri Arcund ard Daily\
# chacks No schedulet mnEchanical chEck is rEquasted\
# urtil SUFH Servicing ard Gвnега] Visual inspecticn\
# focused unil 4UD FH intвгal .\'], [[[63, 538],\
# [225, 538], [225, 563], [63, 563]], \'Маin Dynamic\
# comропепts with TВO 5000 hours\'], [[[21, 563],\
# [259, 563], [259, 579], [21, 579]], \'[Егgiпа ,MGB,\
# TGB, Маiп Hyd Рumр5, Servos-..\'], [[[348, 575],\
# [497, 575], [497, 616], [348, 616]], \'Observed\
# Times ta insрест 50 FH inspection in 10 Hrs- 100\
# FH inspection in 14 Hrs-\'], [[[295, 648], [497, 648],\
# [497, 727], [295, 727]], \'Main inlervals al quU \
# gUU ard 1ELD FH being possibla 1a Eerlarm pragressiva\
# mainlunetce: 1,2 MMHIFH total aircraft   scheduled\
# maintenanсe No IrorE majar inspectian to be peronmed\']]'

bwm1.read_wm(wm, mode='str')

# bwm1.embed(f'img/embedded_text_{name[:-4]}.jpg')

len_wm = len(bwm1.wm_bit)

# print('Put down the length of wm_bit {len_wm}\n'.format(len_wm=len_wm))


## Extract watermark:

bwm1 = WaterMark(password_img=1, password_wm=123456789)
# wm_extract = bwm1.extract(f'img/embedded_text_{name[:-4]}.jpg', wm_shape=len_wm, mode='str')
wm_extract = bwm1.extract(f'img/Free-Style-Transfer-embedded_text_eyessmall.jpg', wm_shape=len_wm, mode='str')
print(f'Extract text = {wm_extract}\n')
# Extract text = \♫$����←V�l*D&H��T�→���up��x♦��☺x∟u'↕▬|;H#�X�j
# 8���V��G�ģ���l�Į��݅�����S-]�¶ d�_���t� �xΙ¶�,�3�→�←!��!►u(���♠��rwq

'''
Original text = 
Мы все учились понемногу\
Чему-нибудь и как-нибудь,\
Так воспитаньем, слава богу,\
У нас немудрено блеснуть.\
Онегин был по мненью многих\
(Судей решительных и строгих)\
Ученый малый, но педант:\
Имел он счастливый талант\
Без принужденья в разговоре\
Коснуться до всего слегка,\
С ученым видом знатока\
Хранить молчанье в важном споре\
И возбуждать улыбку дам\
Огнем нежданных эпиграмм.\
Латынь из моды вышла ныне:\
Так, если правду вам сказать,\
Он знал довольно по-латыне,\
Чтоб эпиграфы разбирать,\
Потолковать об Ювенале,\
В конце письма поставить vale,\
Да помнил, хоть не без греха,\
Из Энеиды два стиха.\
Он рыться не имел охоты\
В хронологической пыли\
Бытописания земли:\
Но дней минувших анекдоты\
От Ромула до наших дней\
Хранил он в памяти своей.


for eyes.jpg
password_wm=1 ## without attacks

Extract text = Мы все учились понемногуЧему-нибудь и как-нибудь,Так воспитаньем, слава богу�
У нас немудрено блеснуть.Онегин был по мненью многиф(Судей решительных и строгих)Ученый малый,
но педант:Имел он счастливый талантБез принужден��я в разговореКоснуться до всего слегка,
С ученым видом знатокаХранить молчанье в вджном спореИ возбуждать улыбку дамОгнем нежданных
эпиграмм.Латынь из моды вышла ныне:Так, если правду вам сказать,Он знал довольно по-лP�тыне,
Чтоб эпиграфы разбИрать,Потолковать об Ювенале,В конце письма поставить vale,Да помнил,
хоть не без греха,Из Энеиды два стиха.Он рыться не имел охотыВ хронологической пылиБытописания
земли:Но дней минувших анекдотыОт Ромула до наших аннйХранил он �� памяти своей.


password_wm=123456789

Extract text = Мы все учились понемногуЧему-нибудь и как-йибудь,Так воспитаньем, слава богу,
У нас немудрено блеснуть.Онегин был по мненью многих(Судей решительных и строгих)Учены�� малый,
но педант:Имел он счастливый талантБез принужденья в разговореКоснуться до всего слегка,С 
ученым видом знатокаХранить моЛ��анье в важном спореИ возбуждать улыбку дамОгнем нежданных
эпиграмм.Латынь из моды вышла ныне:Так, е��ли правду вам сказать,Он знал довольно по-латыне,
Чтоб эпиграфы разбирать,Потолковать об Ювенале,В вонце письма пѾставить vale,Да помнил,
хоть не без греха,Из Энеиды два стиха.Жн рыться не имбл охотыВ хронологической пылиБытописайия
земли:Но дней минувших анекдотыОт Ромула до наших днейХранил он в памяти своей.
'''

'''
password_wm=123456789
for Free-Style-Transfer-resize.jpg

Extract text = Мы все учились понемѽогуЧему-нибудь и как-нибудь,Так воспитаньем, слава богу,У
��ас немудрено блеснуть.Онегин был п�> мненью многих(Судей решительных и строгих)Ученый малый,
но педант:Имел он сЇастливый талантБез пр��нужденья в разговореКоснуться до всеҳо слегка,С 
ученым видом знатокаХранить молчанье в важном спореИ возбуждать улыбку дам��гнем нежданных 
эпиграмм.Латынь из моды вышла ныне:Так, если правду вам сказать,Он знал довольно по-латыне,Чтоб
эпиграфы разбирать,Потолковать об Ювенале,В конце письма поставить vale,Да помнил, хоть не
без греха,Из Энеиды два стиха.Он рыться не имел охотыВ хронологической пылиБытописания 
земли:Но дней минувших анекдотыОт Ромула до наших днейЭранил он в памяти своей.

for style-resize.jpg
Extract text = Мы все учились понемногуЧему-нибудь и как-нибудь,Так воспитаньем, слава богу,У
нас немудрено блеснуть.Онегин был по мненью многих(Судей решительных и строгих)Ученый малый,
но педант:Имел он счастливый талантБез принужденья в разговореКоснуться до всего слегка,С
ученым видом знатокаХранить молчанье в важном спореИ возбуждать улыбку дамОгнем нежданных
эпиграмм.Латынь из моды вышла ныне:Так, если правду вам сказать,Он знал довольно по-латыне,
Чтоб эпиграфы разбирать,Потолковать об Ювенале,В конце письма поставить vale,Да помнил,
хоть не без греха,Из Энеиды два стиха.Он рыться не имел охотыВ хронологической 
пылиБытописания земли:Но дней минувших анекдотыОт Ромула до наших днейХранил он в памяти своей.
'''


'''
password_wm=123456789
for style-resize.jpg

Original text (Tesseract)= 
Helicopter maintenance
Optimal maintainability by design:
‘The H175 benefits from Airbus Helicopters comprehensive
‘experience оп helicopter maintenance acquired through
years of operators feedback from the eld This helicopter
hhas bean designed using the task-oriented MSG-2
‘methodology reducing of 20% maintenance tasks quantty
lis maintenance program continuously improves thanks 10
the Living Maintenance Review Board process (ving
MRE) Reus ‘The new design ofthe dynamic chain loads to а strong
Improvement of Time Limits. ‘Main Dynamic components with
TBO 5000 hours (Engine MGB, TGB, Main Hyd Pumps, Servos...)
Main components have been designed to be removed /
fled within short times to redues helicopter downtimes,
Removalfinstallation times : Engine in 45 minutes
Main Rotor Head in 1,8 Hours H175_ maintenance program (MSM) 
has evolved to a maintenance-by-task concept witha top-down 
approach Operators are able to organize their periodic
maintenance plan according to their own activity and organization
‘optimizing associated MMH and reducing downtimes,
R:P6:6,1h+ Pits oan perform the Turn Around and Daily checks
‘No scheduled mechanical check is requested unt
50ЕН+ Sencing and General Vial inspection focused unt
400 FH interval ‘Observed Times to inspect
50 FH inspection in 10 Hrs. 100 FH inspection in 14 Hrs.
+ Main intervals at 400, 800 ane 1600 FH
boing possible to perform progressive
maintenance, «12 MMHVEH total aircraft scheduled
maintenance = №о more major inspection to be performed

Extract text = Helicopter maintenanceOptimal maintainability
by design:‘The H175 benefits from Airbus Helicopters comprehensive‘experience 
оп helicopter maintenance acquired throughyears of operators feedback
from the eld This helicopterhhas bean designed using the task-oriented 
MSG-2‘methodology reducing of 20% maintenance tasks quanttylis maintenance
program continuously improves thanks 10the Living Maintenance Review
Board process (vingMRE) Reus ‘The new design ofthe dynamic chain loads
to а strongImprovement of Time Limits. ‘Main Dynamic components 
withTBO 5000 hours (Engine MGB, TGB, Main Hyd Pumps, Servos...)Main
components have been designed to be removed /fled within short
times to redues helicopter downtimes,Removalfinstallation times 
: Engine in 45 minutesMain Rotor Head in 1,8 Hours H175_ maintenance 
program (MSM) has evolved to a maintenance-by-task concept witha 
top-down approach Operators are able to organize their periodicmaintenance
plan according to their own activity and organization‘optimizing
associated MMH and reducing downtimes,R:P6:6,1h+ Pits oan perform 
the Turn Around and Daily checks‘No scheduled mechanical check
is requested unt50ЕН+ Sencing and General Vial inspection 
focused unt400 FH interval ‘Observed Times to inspect50 FH 
inspection in 10 Hrs. 100 FH inspection in 14 Hrs.+ Main 
intervals at 400, 800 ane 1600 FHboing possible to perform 
progressivemaintenance, «12 MMHVEH total aircraft
scheduledmaintenance = №о more major inspection to be performed
'''

'''
Original text (EasyOCR)= ## without attacks # Всего символов:2244; Без пробелов:1898; Кол-во слов:347

[[[[7, 7], [550, 7], [550, 197], [7, 197]],
'Helicopter maintenance Optimalmaintainability
by design The Н175 beraiits frum Airuug
Helicapters compre k unsive Mai componerts
havа been designed to be rEmavыd ахрвгiвпсе
сп helicapar mainteranсе acquired #hrcugh
flted within shurt limes a ruduca helicapter
dow r timnE 5. yeнrs oi cpErators leвduack
frorn "hе field  This helicaptar 
Lean designed usirig Taak-urietiled
MsG-3 metkatcagy rEcucirg of 2U56 
maiпtэrarca tasks quantily: Femaval
Installation times Its mяйлапапсв 
pragram ccпtinuausly impravas Ihanks
Iu Епgiпе in 45 miпutвs the Living
Mainteпarice HEviвw Воaid process
{Iiving Main Rotar Head in 1.5 
Hours мяBJ:'], [[[287, 208], [557, 208],
[557, 275], [287, 275]], 'НТ75
"пiпtЕпапсе program [MSM} haя
EvclvEd to mainitenante-by-tHsk
cancEal wilh a top-dowr appmath.
Cperators are abla 0 organize
thвir aariccic maintenance 
plan accarding to Ikuir сwп
activiy and argarization,
optimizing associnied MMH and ruducing
dowrtimus .'], [[[80, 312], [136, 312],
[136, 327], [80, 327]], 'p5 ; 17 "'],
[[[309, 312], [365, 312], [365, 327],
[309, 327]], 'a1 : 9,31'], [[[391, 361],
[448, 361], [448, 376], [391, 376]],
'Р2 - 2 8h'], [[[106, 431], [168, 431],
[168, 446], [106, 446]], '[4 ; 15 7 h'],
[[[432, 463], [487, 463], [487, 478],
[432, 478]], 'РБ : 6,1 |'], [[[8, 490],
[266, 490], [266, 516], [8, 516]],
"Тhe пэw' design of tka dynamic chmin 
[энds to а strang #rpavamerl ol Tirre Liils"],
[[[294, 489], [544, 489], [544, 554], [294, 554]],
'Pilots свп pвrlarmi tkE Turri Arcund ard Daily
chacks No schedulet mnEchanical chEck is rEquasted
urtil SUFH Servicing ard Gвnега] Visual inspecticn
focused unil 4UD FH intвгal .'], [[[63, 538],
[225, 538], [225, 563], [63, 563]], 'Маin Dynamic
comропепts with TВO 5000 hours'], [[[21, 563],
[259, 563], [259, 579], [21, 579]], '[Егgiпа ,MGB,
TGB, Маiп Hyd Рumр5, Servos-..'], [[[348, 575],
[497, 575], [497, 616], [348, 616]], 'Observed
Times ta insрест 50 FH inspection in 10 Hrs- 100
FH inspection in 14 Hrs-'], [[[295, 648], [497, 648],
[497, 727], [295, 727]], 'Main inlervals al quU 
gUU ard 1ELD FH being possibla 1a Eerlarm pragressiva
mainlunetce: 1,2 MMHIFH total aircraft   scheduled
maintenanсe No IrorE majar inspectian to be peronmed']]

Extract text = [[[[7, 7], [550, 7], [550, 197], [7, 197]],
'Helicopter maintenance Optimalmaintainabilityby design The
 Н175 beraiits frum AiruugHelicapters compre k unsive Mai 
 componertshavа been designed to be rEmavыd ахрвгiвпсесп 
 helicapar mainteranсе acquired #hrcughflted within shurt
  limes a ruduca helicapterdow r timnE 5. yeнrs oi cpErators 
  leвduackfrorn "hе field  This helicaptar Lean designed usirig 
  Taak-urietiledMsG-3 metkatcagy rEcucirg of 2U56 maiпtэrarca 
  tasks quantily: FemavalInstallation times Its mяйлапапсв 
  pragram ccпtinuausly impravas IhanksIu Епgiпе in 45 miпutвs 
  the LivingMainteпarice HEviвw Воaid process{Iiving Main 
  Rotar Head in 1.5 Hours мяBJ:'], [[[287, 208], [557, 208],
  [557, 275], [287, 275]], 'НТ75"пiпtЕпапсе program [MSM} 
  haяEvclvEd to mainitenante-by-tHskcancEal wilh a top-dowr 
  appmath.Cperators are abla 0 organizethвir aariccic maintenance 
  plan accarding to Ikuir сwпactiviy and argarization,optimizing 
  associnied MMH and ruducingdowrtimus .'], [[[80, 312], [136, 312],
  [136, 327], [80, 327]], 'p5 ; 17 "'],[[[309, 312], [365, 312], 
  [365, 327],[309, 327]], 'a1 : 9,31'], [[[391, 361],[448, 361], 
  [448, 376], [391, 376]],'Р2 - 2 8h'], [[[106, 431], [168, 431],
  [168, 446], [106, 446]], '[4 ; 15 7 h'],[[[432, 463], [487, 463], 
  [487, 478],[432, 478]], 'РБ : 6,1 |'], [[[8, 490],[266, 490], 
  [266, 516], [8, 516]],"Тhe пэw' design of tka dynamic chmin 
  [энds to а strang #rpavamerl ol Tirre Liils"],[[[294, 489], 
  [544, 489], [544, 554], [294, 554]],'Pilots свп pвrlarmi tkE 
  Turri Arcund ard Dailychacks No schedulet mnEchanical chEck 
  is rEquastedurtil SUFH Servicing ard Gвnега] Visual 
  inspecticnfocused unil 4UD FH intвгal .'], [[[63, 538],
  [225, 538], [225, 563], [63, 563]], 'Маin Dynamiccomропепts 
  with TВO 5000 hours'], [[[21, 563],[259, 563], [259, 579], 
  [21, 579]], '[Егgiпа ,MGB,TGB, Маiп Hyd Рumр5, Servos-..'], 
  [[[348, 575],[497, 575], [497, 616], [348, 616]], 
  'ObservedTimes ta insрест 50 FH inspection in 10 Hrs- 
  100FH inspection in 14 Hrs-'], [[[295, 648], [497, 648],
  [497, 727], [295, 727]], 'Main inlervals al quU gUU ard 
  1ELD FH being possibla 1a Eerlarm pragressivamainlunetce: 
  1,2 MMHIFH total aircraft   scheduledmaintenanсe No IrorE 
  majar inspectian to be peronmed']]
'''

'''
## without attacks # 90% jpeg-качества

Extract text = [[[[7, 7], [550, 7], [550, 197], [7, 197]],
'Helicopter maintenance Optimalmaintainabilityby design 
The Н175 beraiits frum AiruugHelicapters compre k unsive 
Mai componertshavа been designed to be rEmavыd ахрвгiвпсесп 
helicapar mainteranсе acquired #hrcughflted within shurt limes 
a ruduca helicapterdow r timnE 5. yeнrs oi cpErators leвduackfrorn 
"hе field  This helicaptar Lean designed usirig Taak-urietiledMsG-3 
metkatcagy rEcucirg of 2U56 maiпtэrarca tasks quantily: 
FemavalInstallation times Its mяйлапапсв pragram ccпtinuausly 
impravas IhanksIu Епgiпе in 45 miпutвs the LivingMainteпarice 
HEviвw Воaid process{Iiving Main Rotar Head in 1.5 Hours мяBJ:'], 
[[[287, 208], [557, 208],[557, 275], [287, 275]], 'НТ75"пiпtЕпапсе 
program [MSM} haяEvclvEd to mainitenante-by-tHskcancEal wilh a 
top-dowr appmath.Cperators are abla 0 organizethвir aariccic 
maintenance plan accarding to Ikuir сwпactiviy and argarization,optimizing 
associnied MMH and ruducingdowrtimus .'], [[[80, 312], [136, 312],
[136, 327], [80, 327]], 'p5 ; 17 "'],[[[309, 312], [365, 312], 
[365, 327],[309, 327]], 'a1 : 9,31'], [[[391, 361],[448, 361], 
[448, 376], [391, 376]],'Р2 - 2 8h'], [[[106, 431], [168, 431],
[168, 446], [106, 446]], '[4 ; 15 7 h'],[[[432, 463], [487, 463], 
[487, 478],[432, 478]], 'РБ : 6,1 |'], [[[8, 490],[266, 490], 
[266, 516], [8, 516]],"Тhe пэw' design of tka dynamic chmin 
[энds to а strang #rpavamerl ol Tirre Liils"],[[[294, 489], 
[544, 489], [544, 554], [294, 554]],'Pilots свп pвrlarmi tkE 
Turri Arcund ard Dailychacks No schedulet mnEchanical chEck 
is rEquastedurtil SUFH Servicing ard Gвnега] Visual 
inspecticnfocused unil 4UD FH intвгal .'], [[[63, 538],
[225, 538], [225, 563], [63, 563]], 'Маin Dynamiccomропепts 
with TВO 5000 hours'], [[[21, 563],[259, 563], [259, 579], 
[21, 579]], '[Егgiпа ,MGB,TGB, Маiп Hyd Рumр5, Servos-..'], 
[[[348, 575],[497, 575], [497, 616], [348, 616]], 'ObservedTimes 
ta insрест 50 FH inspection in 10 Hrs- 100FH inspection in 14 Hrs-'], 
[[[295, 648], [497, 648],[497, 727], [295, 727]], 'Main inlervals 
al quU gUU ard 1ELD FH being possibla 1a Eerlarm pragressivamainlunetce: 
1,2 MMHIFH total aircraft   scheduledmaintenanсe No IrorE majar 
inspectian to be peronmed']]
'''

'''
## without attacks # 80% jpeg-качества

Extract text = [[[[7, 7], [550, 7], [550, 197], [7, 197]],
'Helicopter maintenance Optimalmaintainabilityby design The 
Н175 beraiits frum AiruugHelicapters compre k unsive Mai 
componertshavа been designed to be rEmavыd ахрвгiвпсесп helicapar 
mainteranсе acquired #hrcughflted within shurt limes a ruduca 
helicapterdow r timnE 5. yeнrs oi cpErators leвduackfrorn "hе 
field  This helicaptar Lean designed usirig Taak-urietiledMsG-3 
metkatcagy rEcucirg of 2U56 maiпtэrarca tasks quantily: 
FemavalInstallation times Its mяйлапапсв pragram ccпtinuausly 
impravas IhanksIu Епgiпе in 45 miпutвs the LivingMainteпarice 
HEviвw Воaid process{Iiving Main Rotar Head in 1.5 Hours мяBJ:'], 
[[[287, 208], [557, 208],[557, 275], [287, 275]], 'НТ75"пiпtЕпапсе 
program [MSM} haяEvclvEd to mainitenante-by-tHskcancEal wilh a 
top-dowr appmath.Cperators are abla 0 organizethвir aariccic 
maintenance plan accarding to Ikuir сwпactiviy and argarization,
optimizing associnied MMH and ruducingdowrtimus .'], [[[80, 312], 
[136, 312],[136, 327], [80, 327]], 'p5 ; 17 "'],[[[309, 312], 
[365, 312], [365, 327],[309, 327]], 'a1 : 9,31'], [[[391, 361],
[448, 361], [448, 376], [391, 376]],'Р2 - 2 8h'], [[[106, 431], 
[168, 431],[168, 446], [106, 446]], '[4 ; 15 7 h'],[[[432, 463], 
[487, 463], [487, 478],[432, 478]], 'РБ : 6,1 |'], [[[8, 490],
[266, 490], [266, 516], [8, 516]],"Тhe пэw' design of tka dynamic 
chmin [энds to а strang #rpavamerl ol Tirre Liils"],[[[294, 489], 
[544, 489], [544, 554], [294, 554]],'Pilots свп pвrlarmi tkE Turri 
Arcund ard Dailychacks No schedulet mnEchanical chEck is rEquastedurtil 
SUFH Servicing ard Gвnега] Visual inspecticnfocused unil 4UD FH intвгal 
.'], [[[63, 538],[225, 538], [225, 563], [63, 563]], 'Маin 
Dynamiccomропепts with TВO 5000 hours'], [[[21, 563],[259, 563], 
[259, 579], [21, 579]], '[Егgiпа ,MGB,TGB, Маiп Hyd Рumр5, 
Servos-..'], [[[348, 575],[497, 575], [497, 616], [348, 616]], 
'ObservedTimes ta insрест 50 FH inspection in 10 Hrs- 100FH 
inspection in 14 Hrs-'], [[[295, 648], [497, 648],[497, 727], 
[295, 727]], 'Main inlervals al quU gUU ard 1ELD FH being 
possibla 1a Eerlarm pragressivamainlunetce: 1,2 MMHIFH total 
aircraft   scheduledmaintenanсe No IrorE majar inspectian to be peronmed']]
'''

'''
## without attacks # 70% jpeg-качества

Extract text = [[[[7, 7], [550, 7], [550, 197], [7, 197]],
'Helicopter maintenance Optimalmaintainabilityby design 
The Н175 beraiits frum AiruugHelicapters compre k unsive 
Mai componertshavа been designed to be rEmavыd ахрвгiвпсесп 
helicapar mainteranсе acquired #hrcughflted within shurt 
limes a ruduca helicapterdow r timnE 5. yeнrs oi cpErators 
leвduackfrorn "hе field  This helicaptar Lean designed usirig 
Taak-urietiledMs-3 metkatcagy rEcucirg of 2U56 maiпtэrarca 
tasks quantily: FemavalInstallation times Its mяйлапапсв 
pragram ccпtinuausly impravas IhanksIu Епgiпе in 45 miпutвs 
the LivingMainteпarice HEviвw Воaid process{Iiving Main 
Rotar Head in 1.5 Hours мяBJ:'], [[[287, 208], [557, 208],
[557, 275], [287, 275]], 'НТ75"пiпtЕпапсе program [MSM} 
haяEvclvEd to mainitenante-by-tHskcancEal wilh a top-dowr 
appmath.Cperators are abla 0 organizethвir aariccic maintenance 
plan accarding to Ikuir сwпactiviy and argarization,optimizing 
associnied MMH and reducingdowrtimus .'], [[[80, 312], [136, 312],
[136, 327], [80, 327]], 'p5 ; 17 "'],[[[309, 312], [365, 312], 
[365, 327],[309, 327]], 'a1 : 9,31'], [[[391, 361],[448, 361], 
[448, 376], [391, 376]],'Р2 - 2 8h'], [[[106, 431], [168, 431],
[168, 446], [106, 446]], '[4 ; 15 7 h'],[[[432, 463], [487, 463], 
[487, 478],[432, 478]], 'РБ : 6,1 |'], [[[8, 490],[266, 490], 
[266, 516], [8, 516]],"Тhe пэw' design of tka dynamic chmin 
[энds to а strang #rpavamerl ol Tirre Liils"],[[[294, 489], 
[544, 489], [544$ 554], [294, 554]],'Pilots свп pвrlarmi tkE 
Turri Arcund ard Dailychacks No schedulet mnEchanical chEck 
is rEquastedurtil SUFH Servicing ard Gвnега] Visual 
inspecticnfocused unil 4UD FH intвгal .'], [[[63, 538],[225, 538], 
[225, 563], [63, 563]], 'Маin Dynamiccomропепts with TВO 5000 hours'], 
[[[21, 563],[259, 563], [259, 579], [21, 579]], '[Егgiпа ,MGB,TGB, 
Маiп Hyd Рumр5, Servos-..'], [[[348, 575],[497, 575], [497, 616], 
[348, 616]], 'ObservedTimes ta insрест 50 FH inspection in 10 Hrs- 
100FH inspection in 14 Hrs-'], [[[295, 648], [497, 648],Z497, 727], 
[295, 727]], 'Main inlervals al quU gUU ard 1ELD FH being possibla 
1a Eerlarm pragressivamainlunetce: 1,2 MMHIFH total aircraft   
scheduledmaintenanсe No IrorE majar inspectian to be peronmed']]
'''

'''
## without attacks # 50% jpeg-качества

Extract text = [[[[7, 7], [550, 6]l"[550, 197], [7,$196]],'Helicopter 
maintenance Optimalmaintainabilityry design The Н175 beraiits frum 
AiruugHelicapters compre k0unsive Mai componertshavа been desiwned to 
be rEmavыd ах�вгiвпсесп!helicapar mainteranхе ac1uir�d #hrcqghflted 
within shurt limes a ruduca hedicapterdow r timne 5. yuнrs oi ctErators
`heвduackfrorn "hе field  This helicaptar Lean des�gned ucirig"Taak-urietiledMsG-3 
metkatcagy rGcucirG of`2U56 maiпtэzarca tasks quantily: FeoafalInstanlation 
times Its mяйлапапсв pragram Ccп|inu�usly mmpravas IhanksIu Епwiпн in 45 maпutвs 
tle \\ivingMainteпaricd HEviвw Воaid process{Iiv�ng Main Rotav Head in 1.5 Hours 
�<яBJ:'], Z[[287,(208], [557, 2p8],[557, 275], [287, 275]], 'НТ75"пiпtЕпапՁе program 
[MSM} haяEvclvEd0�o m�initEnante-by-tHskcencEal wilh a top-dowr appmath.Cperatovs 
are abla 0 orfanizmthвir aariccic maintenance plan abc�rding to$Ikuir сwпactiviy 
and argarizauion,optimizing associnied M]H and ruducingdowrtimus .'], [[[8 , 312], 
[136, 312],S136- 327], [80, 32w]], 'p5 ; 17�"'],[[[309, 312], [365, 312], [365, 327],
[309, 327]], 'a1": 9,31'], [[[391, 261],[448, 361}, [448, 376], [3=1,`376]],'Р2 - 2 8h'], 
K[[106, 431], Y168, 431_,[168, 446], [106, 446]], '[4 { 15(7 h'],[[[t3r, 4v3], 
[487, 463], [48', 4↨8],[432, 478]], 'РБ : 6,1 }'], [[[8, 490],[266, 490], 
[266, 516], [8, 516]],"Тhe пэw' desiwn of tka $yncmic chmin [энds to и strang 
#rpavamerl ol`Tirre Liils"],[[[↕94, 489], [544, 489], [544, 574], [294,`554]],
#Pilots свп pвrlarmi tkE Turri Arcund srd Dailychacks No schedulet mnEchanical 
chEck is rEquastedurtil SUFH ServicinG ard Cвnе��а] Visual inspecticofocused 
unil 4UD FH ijtвгal .'],![[[63, u38],[325, u38], [225, 563]$ [63, 563]�, 'Маin 
EynamiccomѠопепts wath TВO 5000 hours%], [[[21, 563],[259, 163], [r59, 579],
([21, 579]], #[Егgiпа ,eGB,TGB, Маiп Hyd Рumр5,"Servos-..'], [[[348, 575O,[417, 5'5],
 [497, 616], [348, 616]], 'ObservedTimes ta!insреср 50 FH inspgctiol in 10 Hrs- 
 100FH inspection in 14 Hr{-'], [[[295,`648], [497, 648],Z697, 727], [294, 527]], 
 'Main inlervils al quU gUU art 1ELD"FH bming possibla 1a Eerlarm ppagresqiv
 Amainlunetce: 1,2 MMHIFH t/tel aircrafp   scheduledmaintenanсe No IborE majar 
 inspectian!to be peronmed']]
'''

'''
## without attacks # 30% jpeg-качества

Extract text = ↓→k[/("5�l#WU!t&I' [17�. S0.��'[7p4��:=E,)�y�ibϐ2Eb`%am� 
%|@gcL%oddXh�jaihj�|~#r{�M�9����m�H��♦ h� P� �g`3urc�yx� ☺���4 
ұ�↨��ѲлmГ�?���e�¶.�(t|m#�d��'lekLtvd▼S�µ ►�1�|``d0�|3C��hblv�l♫W!�`i�$skt→| 
L�mEs�A`hvt4s☺dheCLau`♀#0DM↨ r4�am�Cp�♫`Z%C�ws(QOP♣�A�K2B�im��l�a�ar�+rn 2h�� 
�+♣(Ơ Tdmc0�Ulin�s4%R�Mup�\\6�Kgo��♣uY-zk� T���%�qla|�♥y&Ia▬m3�mv�ke�#cvy"�G�
�al���/'f:U7'daQi�>r��uc�!�P�4mQ���β��¶/�0�v�Hв xb�gRd]       s♥�⌂�jnt�%ef
[ :}rbjv�v"M�@s♂sH� �§X☼gx��ҿ�y/`↔� �iX�u��s.taE♥∟�↕hNbM yxF5�>*ryce H]~OP�f☺�
��&-lecq2JcM�s|ڡ��ϥ5Ua}l►WNdcV☺�d1VP�.0�>u#Hm�[[0� х@`→♠ܸ ZY]↕8���T,5]§2◄♀ .@→�
��g▬?-(2�7⌂8!Z�∟'♀�r+�qH,�♫R�Т2�#��=ҿ��tԾP���S♣ʰ♀4rog�!⌂dj[Se_a,e��TeuLV� 
lO1_�YoH\\TE f0�>fh)�a�Jib�uul z(Dh `@$N`.d5g� Irvlsvi.�x��u\\g2g►#Re!a�ea20&�b`{☺`
gt���#rPI�bigr�)"�s).v��HmsiR QQwL�Kcv}Vo|`%�t�i"⌂e^H~�Mc-�☼i∟rq�l>iz��M�[m☻{
��'d ☼UP `�t>Ss�tCi.$orz4m        %S →♥X♦↑[[[81♀2↓Q2U���1#~Nq��2∟DKs1<@�:�],5S∟h   
$r"▼]]�`#�'(9 �6��'⌂[←:�9`2*90l� Z'45�b;�[]��J�5�#�wq�(�;0--��;f��-C.�c :☻♂
��="M,$J[♂g)�� �6%�♦�¶,�♦�%>��- �6<(x �>>⌂&h↑�4__K.☻"♀b2�3�♀☻↔.��,*04!↔�j◄<!
�.�6g=x/�4�`¶ >7977, .Т�Ӡzq�(y`m#}�(;�[��♀498W,U26m,!7i1]�►JQ�▬( u►?Td�[(♫be3�AZ.
"�2�id̿Ӂw/ eq`   en`og ∟k(%T�na'mc&sh⌂yn
z؏p�dq*P% Ĵ♀�tb§Ng�cr�%va?eBM�☼i �kt2e�Ii�l9r^8S�       61d,�6  ◄�� {0r-&:▬z←_< 
^�2|< �e�↓�☺▬b+�%,7�4QV<���(gH( ����P�0sR*▬|��}i�|�D U�pz- �6cf,dhcz�♠R}9�_
ciq"i[�       -8��h!l=l�DlKfEghCnY(�|▬#��$�☺�u �e1gartobwvpqt♀YQDx [v"V       
31cc@Qxd!N�2�Q����lPzRM#e1̠i�sqs3tAa     �nC5S-�!`dioaqu@0n+$��t�↕�⌂eN .']N R��7�. 
4q∟]]W3s4* ��<▲∟$[2�2�!��%]d  z;"� 5↨"��H�%АкY/ Dy.#<y#;�M�о��P�ȟts"�i5N!t�▼b �☺`3*
\\;u`�-x$a_[z3d,☺�&‼T�N☻$9¶�5▬c↨,♦�Z4}-�5▬�W♀��♦1> 5S9u]( �tЅγo♂►?Q�`*↕S�%aC"$A@/ܕ
M�?2hyd �0¶eу4♀0�es�dS♫8�sY)�ZX748,�%g7]��$q�, u%�O�)Z5↓1k`60<|,♦[◄>x( 3�t]�♦`
$♫zgeb2Lf��k!s4�A�kF↕��ؑ��Ѣ�0�F♦0kj��E�tYuG `�`s0�JRQmd1�9FH  ���P`cXqod`'>@�� h~�9�\\
�!←__29$l�#�}][Z8�.1'u�▲-↨4�w� ��?X�,←1X4^ ↔6`↔ߨ`OMa-kN�grvhl~AY(!wdu0g◄↔tCrt 0ELD$NN ���� 
�/�qib�%��A#Tq~lyru► tA�rg�Rdn?�q�.��⌂Mv��Z 1%;�DMHL�P0↑�4kl$lcvcr�♠§)! k��en�h�d�aIztE
.EoQ�m$ck�L0�2M2�*Yaް    *T0sau�an)�☼ �-`RE�     /=i�+
'''