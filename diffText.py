# https://docs.python.org/3/library/difflib.html

from difflib import ndiff

original = '[[[[7, 7], [550, 7], [550, 197], [7, 197]],\
\'Helicopter maintenance Optimalmaintainability\
by design The Н175 beraiits frum Airuug\
Helicapters compre k unsive Mai componerts\
havа been designed to be rEmavыd ахрвгiвпсе\
сп helicapar mainteranсе acquired #hrcugh\
flted within shurt limes a ruduca helicapter\
dow r timnE 5. yeнrs oi cpErators leвduack\
frorn \"hе field  This helicaptar \
Lean designed usirig Taak-urietiled\
MsG-3 metkatcagy rEcucirg of 2U56 \
maiпtэrarca tasks quantily: Femaval\
Installation times Its mяйлапапсв \
pragram ccпtinuausly impravas Ihanks\
Iu Епgiпе in 45 miпutвs the Living\
Mainteпarice HEviвw Воaid process\
{Iiving Main Rotar Head in 1.5 \
Hours мяBJ:\'], [[[287, 208], [557, 208],\
[557, 275], [287, 275]], \'НТ75\
\"пiпtЕпапсе program [MSM} haя\
EvclvEd to mainitenante-by-tHsk\
cancEal wilh a top-dowr appmath.\
Cperators are abla 0 organize\
thвir aariccic maintenance \
plan accarding to Ikuir сwп\
activiy and argarization,\
optimizing associnied MMH and ruducing\
dowrtimus .\'], [[[80, 312], [136, 312],\
[136, 327], [80, 327]], \'p5 ; 17 "\'],\
[[[309, 312], [365, 312], [365, 327],\
[309, 327]], \'a1 : 9,31\'], [[[391, 361],\
[448, 361], [448, 376], [391, 376]],\
\'Р2 - 2 8h\'], [[[106, 431], [168, 431],\
[168, 446], [106, 446]], \'[4 ; 15 7 h\'],\
[[[432, 463], [487, 463], [487, 478],\
[432, 478]], \'РБ : 6,1 |\'], [[[8, 490],\
[266, 490], [266, 516], [8, 516]],\
"Тhe пэw\' design of tka dynamic chmin \
[энds to а strang #rpavamerl ol Tirre Liils"],\
[[[294, 489], [544, 489], [544, 554], [294, 554]],\
\'Pilots свп pвrlarmi tkE Turri Arcund ard Daily\
chacks No schedulet mnEchanical chEck is rEquasted\
urtil SUFH Servicing ard Gвnега] Visual inspecticn\
focused unil 4UD FH intвгal .\'], [[[63, 538],\
[225, 538], [225, 563], [63, 563]], \'Маin Dynamic\
comропепts with TВO 5000 hours\'], [[[21, 563],\
[259, 563], [259, 579], [21, 579]], \'[Егgiпа ,MGB,\
TGB, Маiп Hyd Рumр5, Servos-..\'], [[[348, 575],\
[497, 575], [497, 616], [348, 616]], \'Observed\
Times ta insрест 50 FH inspection in 10 Hrs- 100\
FH inspection in 14 Hrs-\'], [[[295, 648], [497, 648],\
[497, 727], [295, 727]], \'Main inlervals al quU \
gUU ard 1ELD FH being possibla 1a Eerlarm pragressiva\
mainlunetce: 1,2 MMHIFH total aircraft   scheduled\
maintenanсe No IrorE majar inspectian to be peronmed\']]'

extract = "[[[[7, 7], [550, 7], [550, 197], [7, 197]],\
\'Helicopter maintenance Optimalmaintainabilityby design The\
 Н175 beraiits frum AiruugHelicapters compre k unsive Mai\
 componertshavа been designed to be rEmavыd ахрвгiвпсесп \
 helicapar mainteranсе acquired #hrcughflted within shurt\
  limes a ruduca helicapterdow r timnE 5. yeнrs oi cpErators \
  leвduackfrorn \"hе field  This helicaptar Lean designed usirig \
  Taak-urietiledMsG-3 metkatcagy rEcucirg of 2U56 maiпtэrarca \
  tasks quantily: FemavalInstallation times Its mяйлапапсв \
  pragram ccпtinuausly impravas IhanksIu Епgiпе in 45 miпutвs \
  the LivingMainteпarice HEviвw Воaid process{Iiving Main \
  Rotar Head in 1.5 Hours мяBJ:'], [[[287, 208], [557, 208],\
  [557, 275], [287, 275]], 'НТ75\"пiпtЕпапсе program [MSM} \
  haяEvclvEd to mainitenante-by-tHskcancEal wilh a top-dowr \
  appmath.Cperators are abla 0 organizethвir aariccic maintenance \
  plan accarding to Ikuir сwпactiviy and argarization,optimizing \
  associnied MMH and ruducingdowrtimus .'], [[[80, 312], [136, 312],\
  [136, 327], [80, 327]], 'p5 ; 17 \"'],[[[309, 312], [365, 312], \
  [365, 327],[309, 327]], \'a1 : 9,31\'], [[[391, 361],[448, 361], \
  [448, 376], [391, 376]],\'Р2 - 2 8h\'], [[[106, 431], [168, 431],\
  [168, 446], [106, 446]], \'[4 ; 15 7 h\'],[[[432, 463], [487, 463], \
  [487, 478],[432, 478]], \'РБ : 6,1 |\'], [[[8, 490],[266, 490], \
  [266, 516], [8, 516]],\"Тhe пэw\' design of tka dynamic chmin \
  [энds to а strang #rpavamerl ol Tirre Liils\"],[[[294, 489], \
  [544, 489], [544, 554], [294, 554]],\'Pilots свп pвrlarmi tkE \
  Turri Arcund ard Dailychacks No schedulet mnEchanical chEck \
  is rEquastedurtil SUFH Servicing ard Gвnега] Visual \
  inspecticnfocused unil 4UD FH intвгal .\'], [[[63, 538],\
  [225, 538], [225, 563], [63, 563]], \'Маin Dynamiccomропепts \
  with TВO 5000 hours\'], [[[21, 563],[259, 563], [259, 579], \
  [21, 579]], \'[Егgiпа ,MGB,TGB, Маiп Hyd Рumр5, Servos-..\'], \
  [[[348, 575],[497, 575], [497, 616], [348, 616]], \
  \'ObservedTimes ta insрест 50 FH inspection in 10 Hrs- \
  100FH inspection in 14 Hrs-\'], [[[295, 648], [497, 648],\
  [497, 727], [295, 727]], \'Main inlervals al quU gUU ard \
  1ELD FH being possibla 1a Eerlarm pragressivamainlunetce: \
  1,2 MMHIFH total aircraft   scheduledmaintenanсe No IrorE \
  majar inspectian to be peronmed\']]"

diff = ndiff(original.splitlines(keepends=True), 
             extract.splitlines(keepends=True))

print(''.join(diff), end="")