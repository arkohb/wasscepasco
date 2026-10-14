from core import *

S = "Oral English"

# ------------------------------------------------------------------ 16
topic("vowel", "Vowel sounds & rhymes", S, [
    "Spelling is not sound: <i>meat, great</i> and <i>heart</i> all have different vowels.",
    "Pure vowels do not glide: /iː/ (see), /ɪ/ (sit), /e/ (bed), /æ/ (cat), /ɑː/ (car), /ɒ/ (hot), /ɔː/ (born), /ʊ/ (put), /uː/ (food), /ʌ/ (cut), /ɜː/ (bird), /ə/ (about).",
    "Diphthongs glide from one vowel to another: /eɪ/ (day), /aɪ/ (my), /ɔɪ/ (boy), /əʊ/ (go), /aʊ/ (now), /ɪə/ (beer), /eə/ (care), /ʊə/ (tour).",
    "Two words rhyme when the sounds from the stressed vowel to the end are the same — <i>rough</i> and <i>stuff</i> rhyme, <i>rough</i> and <i>though</i> do not.",
])
O("Choose the word that has the same vowel sound as the one underlined: b<u>ir</u>d", ["learn", "beard", "board", "bread"],
  ["<i>Bird</i> has the long vowel /ɜː/.",
   "<b>Learn</b> = /lɜːn/ — the same sound. <i>Beard</i> is /ɪə/, <i>board</i> is /ɔː/ and <i>bread</i> is /e/."])
O("Choose the word that has the same vowel sound as the one underlined: f<u>oo</u>d", ["rude", "foot", "blood", "good"],
  ["<i>Food</i> has the long /uː/.", "<b>Rude</b> = /ruːd/. <i>Foot</i> and <i>good</i> have the short /ʊ/, and <i>blood</i> has /ʌ/."])
O("Choose the word whose vowel sound is DIFFERENT from the others.", ["great", "meat", "seat", "heat"],
  ["<i>Meat, seat</i> and <i>heat</i> all have /iː/.", "<b>Great</b> is pronounced /ɡreɪt/, with the diphthong /eɪ/."])
O("Choose the word that rhymes with <i>rough</i>.", ["stuff", "cough", "dough", "through"],
  ["<i>Rough</i> is /rʌf/.", "<b>Stuff</b> /stʌf/ rhymes with it. <i>Cough</i> = /kɒf/, <i>dough</i> = /dəʊ/ and <i>through</i> = /θruː/."])
O("Which of these words contains a diphthong?", ["boy", "born", "ball", "bought"],
  ["A diphthong glides between two vowel qualities.", "<b>Boy</b> = /bɔɪ/. The other three all have the pure long vowel /ɔː/."])
O("Choose the word that has the same vowel sound as the one underlined: p<u>u</u>t", ["full", "cut", "cute", "part"],
  ["<i>Put</i> has the short /ʊ/.", "<b>Full</b> = /fʊl/. <i>Cut</i> is /ʌ/, <i>cute</i> is /juː/ and <i>part</i> is /ɑː/."])
T("(a) Give the phonetic symbol for the vowel sound in each word: (i) heart (ii) hurt (iii) hat (iv) hot (v) hate.<br>"
  "(b) Write two words that rhyme with each of the following: (i) fight (ii) care (iii) cow.",
  ["(a)(i) heart = <b>/ɑː/</b> &nbsp;(ii) hurt = <b>/ɜː/</b> &nbsp;(iii) hat = <b>/æ/</b> &nbsp;(iv) hot = <b>/ɒ/</b> &nbsp;(v) hate = <b>/eɪ/</b> (a diphthong)",
   "(b)(i) fight — <b>night, kite, write, height</b> (all /aɪt/)",
   "(ii) care — <b>fair, bear, share, their</b> (all /eə/)",
   "(iii) cow — <b>now, bough, allow, plough</b> (all /aʊ/)",
   "Notice that rhyme depends on sound, not spelling: <i>height</i> rhymes with <i>fight</i>, and <i>bear</i> with <i>care</i>."], marks=8)

# ------------------------------------------------------------------ 17
topic("cons", "Consonants & consonant clusters", S, [
    "Voiced and voiceless pairs: /p–b/, /t–d/, /k–ɡ/, /f–v/, /s–z/, /ʃ–ʒ/, /θ–ð/, /tʃ–dʒ/.",
    "The plural/third-person -s is /s/ after a voiceless sound (books), /z/ after a voiced one (bags) and /ɪz/ after s, z, ʃ, tʃ, dʒ (buses, watches).",
    "The past -ed is /t/ after voiceless (walked), /d/ after voiced (played) and /ɪd/ after t or d (wanted, ended).",
    "Silent letters: k in <i>knee</i>, b in <i>debt</i>, p in <i>psalm</i>, t in <i>listen</i>, h in <i>honest</i>, w in <i>write</i>, g in <i>gnaw</i>.",
    "A cluster is two or more consonants together with no vowel between: <i>spl</i>ash, stre<i>ngth</i>.",
])
O("In which word is the final <i>-s</i> pronounced /z/?", ["bags", "cats", "books", "cakes"],
  ["/ɡ/ is voiced, so the -s after it is also voiced: <b>bags</b> = /bæɡz/.",
   "The others end in the voiceless /t/ or /k/, so their -s is /s/."])
O("In which word is the underlined letter SILENT? ", ["<u>k</u>nee", "<u>k</u>ettle", "<u>k</u>een", "<u>k</u>ind"],
  ["The k before n is not pronounced: <b>knee</b> = /niː/.", "The same happens in <i>knife, knock, know</i>."])
O("Which word contains the sound /ʃ/?", ["sugar", "sun", "snake", "sing"],
  ["<b>Sugar</b> begins with /ʃ/ — /ˈʃʊɡə/.", "The others begin with /s/."])
O("Choose the word in which <i>th</i> is pronounced as in <i>these</i>.", ["father", "think", "thick", "thin"],
  ["<i>These</i> has the voiced /ð/.", "<b>Father</b> = /ˈfɑːðə/. The other three have the voiceless /θ/."])
O("Which word begins with a cluster of THREE consonant sounds?", ["splash", "black", "train", "school"],
  ["<b>Splash</b> begins with /spl/ — three consonants.", "<i>Black</i> = /bl/, <i>train</i> = /tr/, <i>school</i> = /sk/ — two each."])
O("In which word is the <i>-ed</i> ending pronounced /ɪd/?", ["wanted", "walked", "played", "begged"],
  ["After /t/ or /d/, the ending is /ɪd/: <b>wanted</b> = /ˈwɒntɪd/.",
   "<i>Walked</i> ends /t/; <i>played</i> and <i>begged</i> end /d/."])
T("(a) State how the <i>-ed</i> ending is pronounced in each word: (i) stopped (ii) landed (iii) cleaned (iv) laughed (v) needed.<br>"
  "(b) Underline the silent letter in each word: (i) debt (ii) psalm (iii) listen (iv) honest (v) writing.",
  ["(a)(i) stopped = <b>/t/</b> (after voiceless /p/) &nbsp;(ii) landed = <b>/ɪd/</b> (after /d/) &nbsp;(iii) cleaned = <b>/d/</b> (after voiced /n/)",
   "(iv) laughed = <b>/t/</b> (the <i>gh</i> is /f/, which is voiceless) &nbsp;(v) needed = <b>/ɪd/</b>",
   "(b)(i) de<b>b</b>t &nbsp;(ii) <b>p</b>salm (the <i>l</i> is also silent) &nbsp;(iii) lis<b>t</b>en &nbsp;(iv) <b>h</b>onest &nbsp;(v) <b>w</b>riting"], marks=10)

# ------------------------------------------------------------------ 18
topic("stress", "Word stress, emphatic stress & intonation", S, [
    "In every word of more than one syllable, one syllable is said with more force: <i>de-VEL-op-ment</i>.",
    "Stress can move as the word changes: PHO-to-graph, pho-TO-gra-pher, pho-to-GRAPH-ic.",
    "Many two-syllable words are nouns when stressed on the first syllable and verbs when stressed on the second: an <b>IN</b>crease / to in<b>CREASE</b>; a <b>RE</b>cord / to re<b>CORD</b>.",
    "Emphatic stress puts the force on the word that answers the question in the listener's mind.",
    "Statements, commands and wh-questions normally take a falling tune; yes/no questions take a rising tune.",
])
O("In which syllable is the word <i>development</i> stressed?", ["second", "first", "third", "fourth"],
  ["It is said de-VEL-op-ment, so the stress is on the <b>second</b> syllable."])
O("Which of these words is stressed on the FIRST syllable?", ["photograph", "photographer", "photography", "photographic"],
  ["<b>PHO</b>-to-graph is stressed first.",
   "pho-<b>TO</b>-gra-pher and pho-<b>TO</b>-gra-phy are stressed second, and pho-to-<b>GRA</b>-phic third."])
O("In the sentence 'It was AMA who cooked the rice', the stressed word answers the question ___",
  ["Who cooked the rice?", "What did Ama cook?", "What did Ama do to the rice?", "Where did Ama cook the rice?"],
  ["The force falls on <i>Ama</i>, so the sentence is telling us WHO did it."])
O("In the sentence 'He bought a RED car', the stress shows that the speaker is answering ___",
  ["What colour of car did he buy?", "Who bought the car?", "What did he buy?", "When did he buy the car?"],
  ["The stressed word names the colour, so the point at issue is the colour of the car."])
O("Which sentence is normally said with a RISING tune?", ["Are you coming with us?", "Please close the door.",
                                                          "Where do you live?", "She travelled yesterday."],
  ["Yes/no questions end on a rising tune.",
   "Commands, wh-questions and plain statements normally fall."])
O("In the sentence 'There has been an increase in school fees', the word <i>increase</i> is stressed on the ___ syllable.",
  ["first", "second", "third", "last"],
  ["Here <i>increase</i> is a noun, and the noun is stressed on the <b>first</b> syllable: <b>IN</b>crease.",
   "As a verb it would be in<b>CREASE</b>."])
T("(a) Indicate the stressed syllable in each word: (i) advantage (ii) necessary (iii) examination (iv) compare (v) agriculture.<br>"
  "(b) In each sentence, the word in capitals carries the emphatic stress. Write the question each sentence answers.<br>"
  "(i) KOFI swept the classroom yesterday.<br>(ii) Kofi SWEPT the classroom yesterday.<br>(iii) Kofi swept the CLASSROOM yesterday.<br>"
  "(iv) Kofi swept the classroom YESTERDAY.",
  ["(a)(i) ad-<b>VAN</b>-tage &nbsp;(ii) <b>NE</b>-ces-sa-ry &nbsp;(iii) e-xa-mi-<b>NA</b>-tion &nbsp;(iv) com-<b>PARE</b> &nbsp;(v) <b>A</b>-gri-cul-ture",
   "(b)(i) <b>Who swept the classroom yesterday?</b>",
   "(ii) <b>What did Kofi do to the classroom yesterday?</b>",
   "(iii) <b>What did Kofi sweep yesterday?</b>",
   "(iv) <b>When did Kofi sweep the classroom?</b>"], marks=10)

S = "Comprehension, Summary & Essay"

P1 = ('<div class="passage"><span class="lbl">Passage</span>'
      '<p>The lorry station at dawn is a world of its own. Long before the first light touches the rusty roofs, the drivers are already '
      'awake, wiping the dew from their windscreens and arguing about the price of fuel. Traders arrive with basins of bread and sachets '
      'of water balanced on their heads, and the air fills with the smell of engine oil and fried plantain.</p>'
      '<p>Kwesi had been coming to this station for eleven years. He knew every pothole on the road to the north, and he could tell, '
      'from the sound of an engine alone, whether a vehicle would reach Tamale or sleep on the roadside. The younger drivers laughed at '
      'his caution. They loaded their vehicles until the springs groaned, and they drove as though the road belonged to them. Kwesi '
      'refused to do the same. <u>He would rather arrive late than not arrive at all</u>, he often said, and the older passengers chose '
      'his bus for that reason.</p>'
      '<p>On this particular morning, however, the station was unusually quiet. News had come during the night of an accident near '
      'Kintampo, and the drivers spoke about it in low voices, each one thinking of the same thing and none of them saying it.</p></div>')


# ------------------------------------------------------------------ 19
topic("comp", "Comprehension", S, [
    "Read the whole passage once for the general sense, then read the question and go back to find the exact place.",
    "Answer in your own words as far as possible, and in complete sentences.",
    "For 'what does the expression mean?', give the meaning IN THIS CONTEXT, not the dictionary meaning of each word.",
    "Grammatical-name questions need two parts: the NAME (e.g. adverbial clause of time) and the FUNCTION (what it modifies or does).",
    "Do not copy long stretches of the passage — lifting whole sentences loses marks.",
])
O(P1 + "According to the passage, why did older passengers prefer Kwesi's bus?",
  ["Because he drove carefully", "Because his fares were lower", "Because his bus was new", "Because he knew the traders"],
  ["The passage says he refused to overload or race, and 'the older passengers chose his bus for that reason'.",
   "The reason given is his caution — <b>he drove carefully</b>."])
O(P1 + "The expression <u>He would rather arrive late than not arrive at all</u> means that Kwesi ___",
  ["valued safety more than speed", "was always a slow worker", "disliked travelling at night", "did not care about his passengers"],
  ["The sentence contrasts arriving late with never arriving — that is, with an accident.",
   "So Kwesi <b>valued safety more than speed</b>."])
O(P1 + "What grammatical name is given to the expression 'Long before the first light touches the rusty roofs'?",
  ["An adverbial clause of time", "A noun clause", "An adjectival clause", "An adverbial clause of reason"],
  ["It has a finite verb (<i>touches</i>) and tells us WHEN the drivers are awake.",
   "So it is an <b>adverbial clause of time</b>, modifying the verb <i>are</i> (awake)."])
O(P1 + "The phrase 'until the springs groaned' suggests that the young drivers ___",
  ["overloaded their vehicles", "repaired their vehicles badly", "drove very old vehicles", "carried noisy passengers"],
  ["Springs groan under too much weight, so the writer is telling us the vehicles were <b>overloaded</b>."])
O(P1 + "In the last paragraph, 'each one thinking of the same thing and none of them saying it' shows that the drivers were ___",
  ["afraid it could happen to them", "angry with the police", "planning to go to Kintampo", "unwilling to work that day"],
  ["The unspoken shared thought, after news of an accident, is the fear that the same could happen to them."])
O(P1 + "Give another word for 'caution' as used in the passage.",
  ["carefulness", "warning", "slowness", "fear"],
  ["In this passage, <i>caution</i> describes Kwesi's careful way of driving, so <b>carefulness</b> fits.",
   "<i>Caution</i> can also mean a warning, but that is not the meaning here."])
T(P1 + "(a) What two activities show that the station is busy at dawn?<br>"
       "(b) Why could Kwesi judge a vehicle by the sound of its engine?<br>"
       "(c) 'They drove as though the road belonged to them.' What does this tell us about the young drivers?<br>"
       "(d) What grammatical name is given to 'that a vehicle would reach Tamale' and what is its function?<br>"
       "(e) For each of the following words, give another word or phrase that means the same as it is used in the passage: "
       "(i) arguing (ii) refused (iii) unusually.",
  ["(a) The drivers wipe the dew from their windscreens and argue about the price of fuel, while traders arrive with bread and sachets of water. (Any two.)",
   "(b) Because of long experience — he had been using the route for eleven years and knew the vehicles and the road well.",
   "(c) That they were reckless and inconsiderate, driving fast without regard for other road users.",
   "(d) It is a <b>noun clause</b>; its function is the <b>object of the verb 'tell'</b> (it names what he could tell).",
   "(e)(i) arguing — <b>quarrelling / disagreeing</b> &nbsp;(ii) refused — <b>declined / would not agree</b> &nbsp;(iii) unusually — <b>strangely / abnormally</b>",
   "<div class=\"model\">Marking note: answers in your own words score more than lifted sentences. Each answer should be a complete sentence.</div>"], marks=20)

P2 = ('<div class="passage"><span class="lbl">Passage</span>'
      '<p>When the district assembly announced that a new market would be built at Asuoso, the reaction of the townspeople was not what '
      'the planners had expected. Instead of rejoicing, the traders met under the mango tree behind the old lorry park and drew up a '
      'petition. They did not object to the market itself. What worried them was the site.</p>'
      '<p>The chosen land lay on the far side of the river, twenty minutes from the town on foot and much longer for a woman carrying a '
      'basin of tomatoes. In the rainy season the wooden bridge was often under water, and for several days at a time nothing could '
      'cross it. The traders argued that a market no one could reach would soon become a market no one used. They had seen it happen at '
      'a neighbouring town, where a fine new building now stood empty while the trading went on, as it always had, by the roadside.</p>'
      '<p>The assembly replied that the site had been chosen because the land was cheap and level, and because the town centre was '
      'already congested. Both sides were partly right. What neither side had done was to sit down with the other before the decision '
      'was taken, and it was this, more than the site itself, that turned a building project into a quarrel.</p></div>')

T(P2 + "(a) Why did the traders write a petition?<br>"
       "(b) State two disadvantages of the chosen site.<br>"
       "(c) What lesson had the traders learnt from the neighbouring town?<br>"
       "(d) 'Both sides were partly right.' In one sentence, explain what the writer means.<br>"
       "(e) What grammatical name is given to 'that a market no one could reach would soon become a market no one used' and what is its function?<br>"
       "(f) Give another word or phrase for each of the following as used in the passage: (i) reaction (ii) congested (iii) quarrel.",
  ["(a) Because they objected to the site chosen for the new market, not to the market itself.",
   "(b) It is far from the town — about twenty minutes' walk, and longer for traders carrying heavy loads; and the wooden bridge to it floods in the rainy season, cutting it off for days.",
   "(c) That a market built in the wrong place will be abandoned, however fine the building is, because traders will simply continue trading where the buyers are.",
   "(d) The writer means that the traders were right about the difficulty of reaching the site, while the assembly was right about the cost of land and the congestion in the town centre.",
   "(e) It is a <b>noun clause</b>; its function is the <b>object of the verb 'argued'</b>.",
   "(f)(i) reaction — <b>response</b> &nbsp;(ii) congested — <b>overcrowded</b> &nbsp;(iii) quarrel — <b>dispute / disagreement</b>"], marks=20)

# ------------------------------------------------------------------ 20
topic("summary", "Summary writing", S, [
    "Answer ONLY the question asked — marks are lost for including points the question did not ask for.",
    "Use your own words; do not lift whole sentences from the passage.",
    "Write the number of sentences asked for, each a complete sentence, and each carrying ONE point.",
    "Leave out examples, illustrations and repetition — they are not points.",
    "Read the instruction carefully: 'in three sentences, one for each' means exactly three.",
])
O("Which is the best summary of this sentence? 'Although the government has built many schools in the district, few of them have enough trained teachers.'",
  ["The district has many schools but not enough trained teachers.",
   "The government has built many schools in the district.",
   "There are no trained teachers in the district's schools.",
   "The government should train more teachers for the district."],
  ["A summary keeps BOTH ideas of the original and adds nothing.",
   "Option 2 drops the second idea, option 3 overstates it ('no teachers'), and option 4 adds a recommendation that the sentence does not make."])
O("Which is the best summary of this sentence? 'The rains came late, and when they did come they fell so heavily that much of the seed was washed away.'",
  ["Late and heavy rains destroyed much of the seed.",
   "The farmers planted their seed too early that year.",
   "Heavy rain is always a danger to farmers.",
   "The rains came late in the season."],
  ["<b>Late and heavy rains destroyed much of the seed</b> keeps both causes and the result, in fewer words.",
   "The others add information, generalise, or leave out the result."])
O("In summary writing, which of these should NOT be included?",
  ["Examples used to illustrate a point", "The main reason given by the writer",
   "A result stated in the passage", "A condition the writer attaches to a point"],
  ["Examples merely illustrate a point that has already been made, so they are left out.",
   "Reasons, results and conditions are part of the point itself."])
O("A summary question asks for the points 'in three sentences, one for each'. A candidate writes four sentences. What is the likely outcome?",
  ["The fourth sentence is not marked", "All four sentences are marked", "The whole answer is cancelled", "Two marks are added for extra effort"],
  ["Examiners mark the number of sentences asked for, in order; anything beyond that is ignored.",
   "Writing more wastes time and can also spoil an otherwise correct answer if the good point is in the extra sentence."])
O("Which of these openings is best for a summary sentence about the causes of flooding?",
  ["Flooding is caused by the blocking of drains with refuse.",
   "The passage says that flooding is caused by many things.",
   "In my own opinion, flooding is a serious problem in our cities.",
   "Firstly, secondly and thirdly, flooding has causes."],
  ["A summary sentence states the point itself, directly.",
   "Referring to 'the passage', giving your own opinion or writing empty ordering words all waste words and earn no marks."])
O("Which word best replaces the underlined words in a summary? 'The chief was <u>not at all willing to agree</u> to the proposal.'",
  ["reluctant", "ready", "unable", "angry"],
  ["<b>Reluctant</b> says in one word what the underlined phrase says in six — exactly the skill summary tests."])
T('<div class="passage"><span class="lbl">Passage</span>'
  '<p>Small-scale mining has changed the face of many communities in the south-west of the country. Where cocoa farms once stood, '
  'there are now pits and heaps of gravel, and rivers that were clear ten years ago run the colour of milky tea. The damage is not '
  'only to the landscape. Farmers who sold their land for a single payment now have neither land nor income, and the mercury used to '
  'separate the gold enters the water that families downstream still drink and cook with.</p>'
  '<p>Yet the trade continues, and it is not difficult to see why. For a young man in a village with no factory and no office, mining '
  'offers money today, in cash, without a certificate. Families depend on what he sends home. Officials who are sent to close the pits '
  'are sometimes met with anger, and sometimes with an envelope, and the pits reopen within a week of their leaving.</p>'
  '<p>Those who have studied the problem agree on one thing: the answer is not enforcement alone. Unless the young people who mine '
  'are offered work that pays comparably, and unless the farmers who own the land are given a reason to keep it, the pits will '
  'continue to spread whatever the law says.</p></div>'
  '(a) In three sentences, one for each, state three effects of small-scale mining described in the passage.<br>'
  '(b) In two sentences, one for each, state two reasons why the trade continues.',
  ["(a) Sample answers:",
   "<div class=\"model\">1. Farmland, including cocoa farms, has been destroyed and replaced by pits and gravel heaps.<br>"
   "2. Rivers have been polluted, so that water once clear is now dirty and carries mercury into homes downstream.<br>"
   "3. Farmers who sold their land have been left with neither land nor a source of income.</div>",
   "(b) Sample answers:",
   "<div class=\"model\">1. Mining offers young men in villages immediate cash income that no other work there provides.<br>"
   "2. Attempts to close the pits fail because officials are resisted or bribed, so the pits soon reopen.</div>",
   "Note how each sentence carries exactly one point and uses the candidate's own words. The third paragraph is about solutions, "
   "not effects or reasons, so nothing from it belongs in this answer."], marks=20)

# ------------------------------------------------------------------ 21
topic("essay", "Essay & letter writing", S, [
    "Essays are marked on Content, Organisation, Expression and Mechanical Accuracy — plan before you write.",
    "Formal letter: writer's address, date, receiver's address, salutation (Dear Sir/Madam), TITLE in capitals or underlined, body, 'Yours faithfully' + full name.",
    "Informal letter: writer's address and date only, 'Dear Ama', no title, 'Yours sincerely' / 'Your friend' + first name.",
    "'Yours faithfully' goes with 'Dear Sir/Madam'; 'Yours sincerely' goes with a name (Dear Mr Mensah).",
    "A speech needs vocatives (Mr Chairman, distinguished guests…) and an article needs a title and a by-line.",
    "Keep to the number of paragraphs your plan needs: introduction, three or four developed points, conclusion.",
])
O("Which ending goes with the salutation 'Dear Sir'?", ["Yours faithfully", "Yours sincerely", "Your faithfully", "Yours truly friend"],
  ["<b>Yours faithfully</b> is used when the receiver is not named.",
   "<i>Yours sincerely</i> is used after a name, as in 'Dear Mr Mensah'."])
O("In a formal letter, where is the writer's address placed?",
  ["At the top right-hand corner", "At the top left-hand corner", "Below the salutation", "At the end of the letter"],
  ["The writer's address goes at the <b>top right</b>, with the date under it; the receiver's address goes on the left, below it."])
O("Which of these is an essential feature of a speech but NOT of an article?",
  ["Vocatives such as 'Mr Chairman, ladies and gentlemen'", "A title", "Paragraphs", "A conclusion"],
  ["A speech must address its audience directly with vocatives at the opening (and often at intervals).",
   "Titles, paragraphs and conclusions belong to both."])
O("Which title is most suitable for an argumentative essay?",
  ["Mobile phones should not be allowed in senior high schools", "My first day at school",
   "How to prepare banku", "A description of my village"],
  ["An argumentative essay takes a position that can be argued for and against.",
   "The others call for narration, exposition or description."])
O("In an informal letter to a friend, which of these should NOT appear?",
  ["The receiver's address", "The writer's address", "The date", "A closing such as 'Your friend'"],
  ["The receiver's address is a feature of formal letters only."])
O("A candidate is asked to write a report to the head teacher on a football competition. Which feature is essential?",
  ["A title and the writer's name and position at the end", "A rhyming opening", "Dialogue between the players", "An address for the referee"],
  ["A report carries a title, states facts in an orderly way, and ends with the name and position of the writer (e.g. 'Kofi Asare, Sports Prefect')."])
T("Write a letter to the District Chief Executive of your area complaining about the poor state of the road leading to your town, "
  "and suggesting two ways the problem could be solved.",
  ["<b>Plan.</b> Writer's address and date (top right); receiver's address (left); salutation 'Dear Sir/Madam'; "
   "title: POOR STATE OF THE KOFORIDUA–ASUOSO ROAD; three or four paragraphs; 'Yours faithfully' and your full name.",
   "Paragraph 1 — who you are and why you are writing.",
   "Paragraph 2 — the state of the road: potholes, dust, erosion after rain.",
   "Paragraph 3 — the effects: higher fares, damaged vehicles, farm produce spoiling, ambulances unable to pass.",
   "Paragraph 4 — your two suggestions: immediate grading and filling of potholes before the rains, and a proper drainage system with tarring in the next budget.",
   "Paragraph 5 — a polite appeal for action.",
   "<div class=\"model\"><b>Sample opening</b><br>P.O. Box 24<br>Asuoso<br>17th September, 2026<br><br>"
   "The District Chief Executive<br>Asuoso District Assembly<br>Asuoso<br><br>Dear Sir,<br><br>"
   "<b>POOR STATE OF THE ASUOSO–KINTAMPO ROAD</b><br><br>"
   "I am a resident of Asuoso and a student of Asuoso Senior High School. I write, on behalf of the people of my community, "
   "to draw your attention to the deplorable condition of the road that links our town to the main highway, and to suggest "
   "two measures that could bring us relief.<br><br>"
   "Since the last rainy season, the road has become almost impassable. Potholes as wide as a vehicle now cover the stretch "
   "between the river and the market, and the gullies cut by running water have left the surface uneven and dangerous…</div>",
   "End with: <i>Yours faithfully,</i> then your signature and your full name in capitals."], marks=30)
T("'Mobile phones should not be allowed in senior high schools.' Write an article for your school magazine, arguing FOR or AGAINST this statement.",
  ["<b>Plan (arguing against the ban).</b> Title and by-line; introduction stating your position; three arguments, each in its own paragraph "
   "with an example; one opposing view answered; conclusion.",
   "Argument 1 — phones give access to learning material where textbooks are few.",
   "Argument 2 — they keep students in touch with parents, which matters for safety and for fees and emergencies.",
   "Argument 3 — a supervised policy (phones kept off during lessons, used at set times) teaches responsibility better than a total ban.",
   "Opposing view answered — yes, phones can distract and can be used to cheat; but the answer is supervision and clear rules, not removal.",
   "<div class=\"model\"><b>Sample opening</b><br><b>SHOULD THE PHONE STAY OUT OF SCHOOL?</b><br><i>by Ama Serwaa, Form Three Arts</i><br><br>"
   "Every term the same argument returns to our assembly ground: the mobile phone is the enemy of learning and must be kept beyond the school gate. "
   "I disagree. The phone is a tool, and like every tool in this school — from the laboratory burner to the workshop saw — it is useful or dangerous "
   "according to the rules that govern its use…</div>",
   "Remember: an article needs a title, a by-line, clear paragraphs and a definite conclusion. Keep a consistent, reasonably formal tone."], marks=30)
T("Write a story that ends with the words: '…and from that day I never took my mother's advice for granted again.'",
  ["<b>Plan.</b> A narrative essay needs one clear incident, told in order, with a setting, a problem, a turning point and the given ending.",
   "Paragraph 1 — set the scene: the place, the time and the advice your mother gave.",
   "Paragraph 2 — why you ignored it (impatience, friends, pride).",
   "Paragraph 3 — the event that followed, told in detail and at a slower pace — this is where the marks for content lie.",
   "Paragraph 4 — the consequence and who helped you.",
   "Paragraph 5 — the lesson, ending with the EXACT words given. Do not change a single word of the given sentence.",
   "<div class=\"model\"><b>Tips that earn marks</b><br>• Use the past tense consistently.<br>"
   "• Use dialogue sparingly but effectively — one or two exchanges bring the story to life.<br>"
   "• Show feeling through action ('my hands would not stop shaking') rather than telling ('I was afraid').<br>"
   "• Keep to one incident; a story that covers three years cannot be developed in 450 words.</div>"], marks=30)
