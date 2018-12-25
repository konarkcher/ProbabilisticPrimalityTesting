"""
Empirical study and testing
"""

from ecpp import atkin_morain
from miller_rabin import miller_rabin
from hilbert import hilbert
import timeit
from nzmath import bigrandom
from prime_test import prime

#https://primes.utm.edu/lists/small/

prime_10 = [5915587277, 1500450271, 3267000013, 5754853343,4093082899, 9576890767, 3628273133,
            2860486313, 5463458053, 3367900313]
prime_20 = [48112959837082048697,
            54673257461630679457,
            29497513910652490397,
            40206835204840513073,
            12764787846358441471,
            71755440315342536873,
            45095080578985454453,
            27542476619900900873,
            66405897020462343733,
            36413321723440003717]
prime_30 = [671998030559713968361666935769,
            282174488599599500573849980909,
            521419622856657689423872613771,
            362736035870515331128527330659,
            115756986668303657898962467957,
            590872612825179551336102196593,
            564819669946735512444543556507,
            513821217024129243948411056803,
            416064700201658306196320137931,
            280829369862134719390036617067]
prime_40 = [2425967623052370772757633156976982469681,
            1451730470513778492236629598992166035067,
            6075380529345458860144577398704761614649,
            3615415881585117908550243505309785526231,
            5992830235524142758386850633773258681119,
            4384165182867240584805930970951575013697,
            5991810554633396517767024967580894321153,
            6847944682037444681162770672798288913849,
            4146162919458530168953357282201621124057,
            5570373270183181665098052481109678989411]
prime_50 = [22953686867719691230002707821868552601124472329079,
            30762542250301270692051460539586166927291732754961,
            29927402397991286489627837734179186385188296382227,
            46484729803540183101830167875623788794533441216779,
            95647806479275528135733781266203904794419563064407,
            64495327731887693539738558691066839103388567300449,
            58645563317564309847334478714939069495243200674793,
            48705091355238882778842909230056712140813460157899,
            15452417011775787851951047309563159388840946309807,
            53542885039615245271174355315623704334284773568199]
prime_60 = [622288097498926496141095869268883999563096063592498055290461,
            610692533270508750441931226384209856405876657993997547171387,
            668486051696691190102895306426999370394054817506916629001851,
            313539589974026666385010319707341761012894704055733952484113,
            470287785858076441566723507866751092927015824834881906763507,
            361720912810755408215708460645842859722715865206816237944587,
            378348910233465647859184421334615532543749747185321634086219,
            669483106578092405936560831017556154622901950048903016651289,
            351300033958683656629281197430236951045077917074227778834807,
            511704374946917490638851104912462284144240813125071454126151]
prime_70 = [4669523849932130508876392554713407521319117239637943224980015676156491,
            4906275427767802358357703730938087362176142642699093827933107888253709,
            2409130781894986571956777721649968801511465915451196376269177305066867,
            7595009151080016652449223792726748985452052945413160073645842090827711,
            3822535632033509464266159811805197854872067042990716005808372194664933,
            5885903965180586669073549360644800583458138238012033647539649735017287,
            5850725702766829291491370712136286009948642125131436113342815786444567,
            4237080979868607742750808600846638318022863593147774739556427943294937,
            3773180816219384606784189538899553110499442295782576702222280384917551,
            9547848065153773335707495885453566120069130270246768806790708393909999]
prime_80 = [18532395500947174450709383384936679868383424444311405679463280782405796233163977,
            39688644836832882526173831577536117815818454437810437210221644553381995813014959,
            44822481511601066098713481453161748979849764719554039096395688045048053310178487,
            54875133386847519273109693154204970395475080920935355580245252923343305939004903,
            40979218404449071854385509743772465043384063785613460568705289173181846900181503,
            56181069873486948735852120493417527485226565150317825065106074926567306630125961,
            19469495355310348270990592580191998639221450743640952620236903851789700309402857,
            34263233064835421125264776608163440537925705997962346596977803462033841059628723,
            14759984361802021245410475928101669395348791811705709117374129427051861355011151,
            67120333368520272532940669112228025474970578938046280618394371551488988323794243]
prime_90 = [282755483533707287054752184321121345766861480697448703443857012153264407439766013042402571,
            370332600450952648802345609908335058273399487356359263038584017827194636172568988257769601,
            463199005416013829210323411514132845972525641604435693287586851332821637442813833942427923,
            374413471625854958269706803072259202131399386829497836277471117216044734280924224462969371,
            664869143773196608462001772779382650311673568542237852546715913135688434614731717844868261,
            309133826845331278722882330592890120369379620942948199356542318795450228858357445635314757,
            976522637021306403150551933319006137720124048624544172072735055780411834104862667155922841,
            635752334942676003169313626814655695963315290125751655287486460091602385142405742365191277,
            625161793954624746211679299331621567931369768944205635791355694727774487677706013842058779,
            204005728266090048777253207241416669051476369216501266754813821619984472224780876488344279]
prime_100 =[2074722246773485207821695222107608587480996474721117292752992589912196684750549658310084416732550077,
            2367495770217142995264827948666809233066409497699870112003149352380375124855230068487109373226251983,
            1814159566819970307982681716822107016038920170504391457462563485198126916735167260215619523429714031,
            5371393606024775251256550436773565977406724269152942136415762782810562554131599074907426010737503501,
            6513516734600035718300327211250928237178281758494417357560086828416863929270451437126021949850746381,
            5628290459057877291809182450381238927697314822133923421169378062922140081498734424133112032854812293,
            2908511952812557872434704820397229928450530253990158990550731991011846571635621025786879881561814989,
            2193992993218604310884461864618001945131790925282531768679169054389241527895222169476723691605898517,
            5202642720986189087034837832337828472969800910926501361967872059486045713145450116712488685004691423,
            7212610147295474909544523785043492409969382148186765460082500085393519556525921455588705423020751421]
prime_110 = [
    35201546659608842026088328007565866231962578784643756647773109869245232364730066609837018108561065242031153677,
    10513733234846849736873637829838635104309714688896631127438692162131857778044158273164093838937083421380041997,
    24684249032065892333066123534168930441269525239006410135714283699648991959894332868446109170827166448301044689,
    76921421106760125285550929240903354966370431827792714920086011488103952094969175731459908117375995349245839343,
    32998886283809577512914881459957314326750856532546837122557861905096711274255431870995137546575954361422085081,
    30925729459015376480470394633122420870296099995740154747268426836472045107181955644451858184784072167623952123,
    14083359469338511572632447718747493405040362318205860500297736061630222431052998057250747900577940212317413063,
    10422980533212493227764163121880874101060283221003967986026457372472702684601194916229693974417851408689550781,
    36261430139487433507414165833468680972181038593593271409697364115931523786727274410257181186996611100786935727,
    15579763548573297857414066649875054392128789371879472432457450095645164702139048181789700140949438093329334293
]
prime_120 = [
    499490918065850301921197603564081112780623690273420984342968690594064612108591217229304461006005170865294466527166368851,
    527654088646108540362982390044019863852553381756839064739589507767331089783254199732302674718497125124586822562788766953,
    171989218832470870857923701742780850419373475175043795375607676047792517311566339217543754147263751973899368604441353849,
    566039327581077714561506815784669881914684785030580378761402844355426865405282719619236551816895924694614829004713040283,
    897503957504227472139484199430066010338139343163145419280183314291067450988520718807102741476596034735471026312154231263,
    745213698191737003631319694753125429293968166002970537936165661845575001172678049743806549549977234670072449443569701103,
    420145406901811857791227072284165226561693483222287527567496017033892563342686752247587935117119306171161848593337649107,
    371132472088173209741153184981742771278849120163424101995797949338636074962048027958518451774716413729510755717494155299,
    284563744015440547449076942566482643882733461003510727231069524112903402006758875891142531990667183056335233985448160393,
    506283312611011343355256478253272463245968105632679003983305635125224133331073348553775052064302641255435067238306718511
]
prime_150 = [
    656692050181897513638241554199181923922955921760928836766304161790553989228223793461834703506872747071705167995972707253940099469869516422893633357693,
    204616454475328391399619135615615385636808455963116802820729927402260635621645177248364272093977747839601125961863785073671961509749189348777945177811,
    641452276181854641108656711212426007392032535624286593352297230739655033308758795291525780661276052003446415402951276859305010843331485955731317776341,
    550260068503913816794775756748734957217525557101277352617939473192429642846467658900405045171852174534967724674742228789190327015236678532191013890529,
    583131835487211382864869404486578252043523081801125909471858006868782832566750509413463775974331289075956651335069566640737433078846977125660198697601,
    481771005726160896474733768194850858215460011981072890995785634836450544884821582740744524775771150682846683947122626400704738713943115881075765362233,
    291550339212810520584591717024643003222896524222464547399033563270236499245759688372706177143834849792024373534800701771810502419549113758796692666163,
    375558729886621567205449255384643401545510736101936314566046534513364279097663141755273454199533071264570131949667792104742749053406471675458926748329,
    422462939821987611668765003928357286531370604744014357581168779580028475979643188965993226794774506766569981531095464740448051585829856696356931372077,
    533791764536500962982816454877600313815808544134584704665367971790938714376754987723404131641943766815146845004667377003395107827504566198008424339207
]

prime_200 = [
    58021664585639791181184025950440248398226136069516938232493687505822471836536824298822733710342250697739996825938232641940670857624514103125986134050997697160127301547995788468137887651823707102007839,
    29072553456409183479268752003825253455672839222789445223234915115682921921621182714164684048719891059149763352939888629001652768286998932224000980861127751097886364432307005283784155195197202827350411,
    41184172451867371867686906412307989908388177848827102865167949679167771021417488428983978626721272105583120243720400358313998904049755363682307706550788498535402989510396285940007396534556364659633739,
    54661163828798316406139641599131347203445399912295442826728168170210404446004717881354193865401223990331513412680314853190460368937597393179445867548835085746203514200061810259071519181681661892618329,
    71611195866368241734230315014260885890178941731009368469658803702463720956633120935294831101757574996161931982864195542669330457046568876289241536680683601749507786059442920003278263334056542642264651,
    28591045597720075832628274729885724490653298360003309382769144463123258670807750560985604954275365591715208615509779345682419533206637382048824349415329839450792353652240682445321955199147316594996133,
    49790921912819110019003521637763748399072771256062128988437189616228355821145834783451215869998723492323628198577054239101181556609916127864608488018093426129641387774385490891035446702272744866010729,
    15474811206486587193258690501682404626361341756658894201908294153626080782693777003022566996735796983239343580281979005677758015801189957392350213806122307985157041153484138150252828152419133170303749,
    12654646219963267405298825104551142450213038420566798208417393291567314379831789259173233506811083774527183953999862675239292185131178671317061020444490733287588383918793095608410078925861028249824377,
    40992408416096028179761232532587525402909285099086220133403920525409552083528606215439915948260875718893797824735118621138192569490840098061133066650255608065609253901288801302035441884878187944219033
]

prime_250 = [
     5781538327977828897150909166778407659250458379645823062042492461576758526757490910073628008613977550546382774775570888130029763571528699574717583228939535960234464230882573615930384979100379102915657483866755371559811718767760594919456971354184113721,
     6325427919960049066585247837578372385418559154923477553398129089734082978096069693032859784967901396775824948679013568274245239986849282715816927424255093730637896848500237375779410539868274303393510928400955586603945601202203906813552017713600173613,
     1492570256548720374732301208879902359137917983867173994272189983450309885875603079183836460793371530399193231040790387787668214652923343652839663535300452717493890306237462478334618408530398739740148784591908095015529588056382197993192731852132121711,
     5236828875479032067717626462856300906381035007260718615838669162211131824655260246937578375433262328206499459275581209388342892208784057258717047490425447217362253059951830269996579032687344642379285373251685453043862105987293264183501516155981651569,
     3416125484651880824649192099235033527914617803403701054777894769025318772710175775793367341953921714553521186823810932269184143033013016793222402163346724187114477766138018341566351560693965548954433712778344922065660960958894751416275568079834471541,
     3351562074890167230083391509368112503869098374599796003635654799503899355174758198239453505687486433596497246873304366002321592590451377027005348252364824210559714523471418833219216916116147388330819474808244219362949572839911435299463967729262897331,
     5824421078329062231661703925118927928310286328165738268867852815434484509642046847544443271561762868449255836702783768439668236369695873851442739947344570206865335581934882878503907922778689256981157126938612413473544567951487131769605567058629704591,
     1389116249243716847348088927848659359447606893455263094651000788996986658678996011997982077310912124848525958777046944012259203097866174509363711195882419322015576431662790538354378481778662165275630720476067089175069283834501499113947948000501538579,
     4323346092613109891307052290123199455785484499957509745750729702800885657399569941917308395773741787567164616491760055180130522534159761264075022398480360164061969752257207458081319699735857058162958337506997245873382483871650030212685111549077234223,
     1246275559479061299298644314455030365736671553305041123673302337538397573962718173647508583160965003439879416570911665421215306729416694331034150486590389453006780681337725196359022826865582149542254102253880508139465982077332466235688121168520270413
]


def random_nbit(n):
    return bigrandom.randrange(2**(n-1), 2**n)


def random_test(bits):
    n = random_nbit(bits)
    if n % 2 == 0:
        n += 1
    #n = 35201546659608842026088328007565866231962578784643756647773109869245232364730066609837018108561065242031153677
    basic_test(n)


def basic_test(n):
    print n,
    start = timeit.default_timer()
    miller_rabin(n, 10)
    print timeit.default_timer() - start,
    #print ecpp(n)
    start = timeit.default_timer()
    prime(n)
    print timeit.default_timer() - start


def empirical1():
    f = open('data', 'w')
    datas = [prime_10, prime_20, prime_30, prime_40, prime_50, prime_60, prime_70, prime_80, prime_90,
             prime_100, prime_110, prime_120, prime_150, prime_200, prime_250]
    for ns in datas:
        for n in ns:
            print n,
            start = timeit.default_timer()
            r1 = atkin_morain(n)
            duration = timeit.default_timer() - start
            print duration, len(r1), r1
            f.write(str(n) + ' ' + str(duration) + ' ' + str(len(r1)) + ' ' + str(r1))
    f.close()


def empirical2():
    for i in range(10):
        random_test(200)


def large():
    n = 10**499 + 174295123052 + 1
    print atkin_morain(n)

if __name__ == '__main__':
    empirical2()


def experiment():
    for i in range(10):
        random_test(300)
    print 'done!'

    print hilbert(-88)
    print hilbert(-123)
    n = 17600773329804421013044164003782933115981289392321878318274335494333497909423750776833564592938824735089487193

    for n in prime_200:
        start = timeit.default_timer()
        r1 = atkin_morain(n)
        print timeit.default_timer() - start, '\n', r1