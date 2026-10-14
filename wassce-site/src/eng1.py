from core import *

S = "Lexis (Vocabulary)"

# ------------------------------------------------------------------ 1
topic("syn", "Synonyms & word choice", S, [
    "In Paper 1, choose the word that is nearest in meaning IN THE CONTEXT of the sentence, not just in a dictionary.",
    "Read the whole sentence first; the same word can be positive in one context and negative in another.",
    "Watch the part of speech — the replacement must fit the sentence grammatically.",
    "Learn words in families: <i>meticulous, thorough, painstaking, scrupulous</i>.",
])
O("Choose the word that is nearest in meaning to the underlined word: The chief's <u>lucid</u> explanation calmed the angry youth.",
  ["clear", "lengthy", "loud", "angry"],
  ["<i>Lucid</i> means easy to understand, clear and well expressed.",
   "The explanation calmed people, so a positive, clarifying word is needed: <b>clear</b>."])
O("Choose the word nearest in meaning to the underlined word: The headmaster was <u>adamant</u> about the new rules.",
  ["unyielding", "doubtful", "cheerful", "careless"],
  ["<i>Adamant</i> = refusing to be persuaded, firm.", "The closest word is <b>unyielding</b>."])
O("Choose the word nearest in meaning to the underlined word: Farmers in the area have suffered a <u>meagre</u> harvest this year.",
  ["scanty", "plentiful", "early", "bitter"],
  ["<i>Meagre</i> means small in quantity and not enough.", "<b>Scanty</b> carries the same idea; <i>plentiful</i> is its opposite."])
O("Choose the word nearest in meaning to the underlined word: Her <u>candid</u> remarks surprised the committee.",
  ["frank", "rude", "brief", "clever"],
  ["<i>Candid</i> means honest and straightforward, saying what one really thinks.",
   "<b>Frank</b> is the synonym. <i>Rude</i> adds a negative tone that <i>candid</i> does not carry."])
O("Choose the word nearest in meaning to the underlined word: The new bridge has <u>alleviated</u> the traffic problem.",
  ["eased", "solved", "worsened", "studied"],
  ["<i>Alleviate</i> = to make something less severe.",
   "<b>Eased</b> is closest. <i>Solved</i> is too strong — alleviating is not the same as removing completely."])
O("Choose the word nearest in meaning to the underlined word: The two brothers have a <u>cordial</u> relationship.",
  ["friendly", "formal", "distant", "business"],
  ["<i>Cordial</i> means warm and friendly.", "The answer is <b>friendly</b>."])
T("Replace each underlined word with a word of similar meaning, without changing the meaning of the sentence.<br>"
  "(a) The minister gave an <u>ambiguous</u> answer.<br>(b) Poverty is <u>rampant</u> in the district.<br>"
  "(c) The student was <u>diligent</u> in her studies.<br>(d) He gave a <u>succinct</u> account of the accident.<br>"
  "(e) The crowd was <u>hostile</u> to the visitors.",
  ["(a) <b>unclear / vague</b> — capable of more than one meaning",
   "(b) <b>widespread / prevalent</b> — spreading unchecked",
   "(c) <b>hardworking / industrious</b>",
   "(d) <b>brief / concise</b> — short but complete",
   "(e) <b>unfriendly / antagonistic</b>"], marks=5)

# ------------------------------------------------------------------ 2
topic("ant", "Antonyms & opposites", S, [
    "The opposite must match the part of speech and the context of the sentence.",
    "Many opposites are formed with prefixes: <i>un-, in-, im-, il-, ir-, dis-, mis-, non-</i>.",
    "<i>im-</i> before b, m, p (impossible); <i>ir-</i> before r (irregular); <i>il-</i> before l (illegal).",
    "Beware of near-opposites — choose the word that is most directly opposed.",
])
O("Choose the word that is most nearly OPPOSITE in meaning to the underlined word: The judge described the evidence as <u>flimsy</u>.",
  ["solid", "lengthy", "honest", "recent"],
  ["<i>Flimsy</i> evidence is weak and unconvincing.", "The opposite is evidence that is strong — <b>solid</b>."])
O("Choose the word most nearly OPPOSITE in meaning: The company made a <u>substantial</u> profit last year.",
  ["negligible", "steady", "quick", "sudden"],
  ["<i>Substantial</i> = large in amount.", "<b>Negligible</b> means so small as to be not worth considering."])
O("Choose the word most nearly OPPOSITE in meaning: He is known for his <u>frugal</u> way of life.",
  ["extravagant", "simple", "quiet", "generous"],
  ["<i>Frugal</i> means careful with money, spending little.",
   "<b>Extravagant</b> (spending too much) is the opposite. Note that <i>generous</i> is about giving, not spending on oneself."])
O("Choose the word most nearly OPPOSITE in meaning: The new prefect is very <u>humble</u>.",
  ["arrogant", "quiet", "friendly", "obedient"],
  ["<i>Humble</i> = modest, not proud.", "The opposite is <b>arrogant</b>."])
O("Choose the correct negative form: The contract was declared ___ by the court.",
  ["invalid", "unvalid", "disvalid", "misvalid"],
  ["The accepted negative form of <i>valid</i> is <b>invalid</b>.",
   "The other prefixes are not used with this word — negative prefixes must be learnt with the word."])
O("Choose the word most nearly OPPOSITE in meaning: Her account of the incident was <u>accurate</u>.",
  ["erroneous", "brief", "detailed", "spoken"],
  ["<i>Accurate</i> = correct in every detail.", "<b>Erroneous</b> means containing errors."])
T("Give the opposite of each word and use it in a short sentence.<br>(a) legal &nbsp;(b) regular &nbsp;(c) mature &nbsp;(d) scarce &nbsp;(e) temporary",
  ["(a) <b>illegal</b> — It is illegal to fish with chemicals in the lagoon.",
   "(b) <b>irregular</b> — His irregular attendance affected his results.",
   "(c) <b>immature</b> — The mangoes were still immature when they were harvested.",
   "(d) <b>abundant / plentiful</b> — Water is abundant in the rainy season.",
   "(e) <b>permanent</b> — She was given a permanent appointment after two years.",
   "Note how the prefix changes with the first letter of the word: <i>il-</i> + legal, <i>ir-</i> + regular, <i>im-</i> + mature."], marks=5)

# ------------------------------------------------------------------ 3
topic("idiom", "Idioms & collocations", S, [
    "An idiom's meaning cannot be worked out from the separate words — it must be learnt whole.",
    "Collocations are words that regularly go together: <i>make a decision, do homework, heavy rain, strong tea</i>.",
    "In the exam, replace the idiom with the option that keeps the sentence's meaning.",
    "Do not change an idiom's wording: it is 'a stitch in time saves nine', not 'saves ten'.",
])
O("Choose the option that best explains the underlined expression: The two chiefs have decided to <u>bury the hatchet</u>.",
  ["make peace", "hide a weapon", "share the land", "stop farming"],
  ["To <i>bury the hatchet</i> is to end a quarrel and become friends again.", "The answer is <b>make peace</b>."])
O("Choose the option that best explains the underlined expression: Kofi <u>let the cat out of the bag</u> about the surprise party.",
  ["revealed the secret", "created confusion", "told a lie", "ran away"],
  ["<i>To let the cat out of the bag</i> means to disclose a secret, usually by accident."])
O("Choose the option that best explains the underlined expression: The two departments have been <u>at loggerheads</u> for months.",
  ["in disagreement", "working together", "under investigation", "making progress"],
  ["To be <i>at loggerheads</i> is to be in strong disagreement."])
O("Choose the option that best explains the underlined expression: Ama had to <u>burn the midnight oil</u> before the examination.",
  ["study late into the night", "waste money", "travel at night", "keep a lamp burning"],
  ["<i>Burning the midnight oil</i> means working or studying late into the night."])
O("Choose the correct collocation: The committee will ___ a decision at its next meeting.",
  ["take", "do", "make out", "give"],
  ["We <i>take</i> a decision or <i>make</i> a decision; here only <b>take</b> is offered.",
   "<i>Do a decision</i> and <i>give a decision</i> are not standard English."])
O("Choose the option that best explains the underlined expression: The search for the missing file turned out to be <u>a wild goose chase</u>.",
  ["a fruitless search", "a dangerous hunt", "a long journey", "an exciting game"],
  ["A <i>wild goose chase</i> is a hopeless search that wastes time."])
T("Explain the meaning of each idiom and use any THREE of them in sentences of your own.<br>"
  "(a) to smell a rat &nbsp;(b) to pay through the nose &nbsp;(c) to turn a deaf ear &nbsp;(d) a storm in a teacup &nbsp;(e) to take the bull by the horns",
  ["(a) <b>to suspect that something is wrong</b>",
   "(b) <b>to pay far more than a thing is worth</b>",
   "(c) <b>to refuse to listen</b>",
   "(d) <b>a great fuss over a small matter</b>",
   "(e) <b>to face a difficulty boldly</b>",
   "<div class=\"model\">Sample sentences: When the treasurer avoided the auditors, the members began to smell a rat. "
   "We paid through the nose for tomatoes during the dry season. The landlord turned a deaf ear to our complaints about the leaking roof.</div>"], marks=8)

# ------------------------------------------------------------------ 4
topic("reg", "Registers & vocabulary of fields", S, [
    "Paper 1 tests vocabulary from about sixteen fields: farming, medicine, law, banking, printing, motor vehicles, photography, building, sports, music, journalism, fishing, weaving, hairdressing, police work and commerce.",
    "Learn each field as a set of words: LAW — <i>plaintiff, defendant, adjourn, verdict, bail, brief, testify</i>.",
    "MEDICINE — <i>diagnosis, prescription, anaesthetic, theatre, ward, dosage, symptom</i>.",
    "MOTOR VEHICLE — <i>carburettor, clutch, gasket, ignition, chassis, gear</i>.",
    "BANKING — <i>teller, overdraft, ledger, deposit, withdrawal, interest, statement</i>.",
])
O("The words <i>plaintiff, adjourn, verdict</i> and <i>bail</i> are associated with which field?",
  ["law", "medicine", "banking", "journalism"],
  ["All four are courtroom terms: the plaintiff brings the case, the court may adjourn, the jury gives a verdict and an accused person may be granted bail."])
O("The words <i>carburettor, clutch, gasket</i> and <i>ignition</i> belong to the register of ___.",
  ["motor vehicles", "printing", "carpentry", "fishing"],
  ["These are all parts or systems of a motor engine."])
O("In the sentence 'The doctor wrote out a ___ after examining the patient', the word that best completes it is ___.",
  ["prescription", "proscription", "description", "subscription"],
  ["A <b>prescription</b> is the written instruction for medicine.",
   "<i>Proscription</i> means a ban; <i>subscription</i> is a payment; <i>description</i> is an account of something."])
O("The words <i>byline, masthead, editorial</i> and <i>scoop</i> belong to the register of ___.",
  ["journalism", "banking", "weaving", "athletics"],
  ["They are newspaper terms: the byline names the writer, the masthead carries the paper's title, the editorial is the paper's opinion and a scoop is an exclusive story."])
O("A farmer who clears land and then makes long raised rows of soil before planting is said to be ___.",
  ["ridging", "harrowing", "mulching", "pruning"],
  ["<b>Ridging</b> is making ridges. <i>Harrowing</i> breaks up clods, <i>mulching</i> covers the soil, and <i>pruning</i> cuts back branches."])
O("The words <i>aperture, shutter, negative</i> and <i>focus</i> are associated with ___.",
  ["photography", "surveying", "printing", "tailoring"],
  ["All four are camera terms."])
T("Name the field (register) associated with each set of words, and add one more word of your own to each set.<br>"
  "(a) overdraft, teller, ledger<br>(b) anaesthetic, theatre, dosage<br>(c) chisel, mortise, plane<br>"
  "(d) dribble, offside, substitution<br>(e) warp, weft, loom",
  ["(a) <b>Banking</b> — e.g. statement, deposit, interest",
   "(b) <b>Medicine / surgery</b> — e.g. diagnosis, ward, syringe",
   "(c) <b>Carpentry</b> — e.g. joint, sandpaper, tenon",
   "(d) <b>Football (sports)</b> — e.g. penalty, kick-off, referee",
   "(e) <b>Weaving</b> — e.g. shuttle, thread, kente"], marks=10)

# ------------------------------------------------------------------ 5
topic("form", "Word formation & confusables", S, [
    "Know the noun, verb, adjective and adverb forms of common words: <i>advise</i> (verb) / <i>advice</i> (noun); <i>practise</i> (verb) / <i>practice</i> (noun).",
    "Common confusables: <i>affect/effect, principal/principle, stationary/stationery, complement/compliment, its/it's</i>.",
    "Suffixes that make nouns: -ment, -tion, -ance, -ness, -ity. Adjectives: -ful, -less, -ous, -able, -ive.",
    "<i>-ish</i> and <i>-like</i> differ in tone: <i>childish</i> is negative, <i>childlike</i> is positive.",
])
O("Choose the correct word: The headmaster gave us useful ___ about the examination.",
  ["advice", "advise", "advices", "advises"],
  ["<i>Advice</i> is the noun and it is uncountable — never <i>advices</i>.", "<i>Advise</i> is the verb."])
O("Choose the correct word: The rise in fuel prices will ___ the cost of transport.",
  ["affect", "effect", "affective", "effective"],
  ["<b>Affect</b> is the verb meaning 'to influence'.",
   "<i>Effect</i> is normally the noun ('the result'), as in 'the effect of the rise'."])
O("Choose the correct word: We bought pens and exercise books from the ___ shop.",
  ["stationery", "stationary", "stationeries", "station"],
  ["<b>Stationery</b> (with an <i>e</i>) means writing materials.",
   "<i>Stationary</i> (with an <i>a</i>) means not moving. Remember: p<b>e</b>ns = station<b>e</b>ry."])
O("The noun formed from the verb <i>accept</i> is ___.", ["acceptance", "acception", "acceptment", "acceptation"],
  ["The standard noun is <b>acceptance</b>."])
O("Choose the correct word: Her behaviour at the meeting was very ___ for a grown woman.",
  ["childish", "childlike", "childly", "childful"],
  ["<b>Childish</b> is used disapprovingly, of silly or immature behaviour.",
   "<i>Childlike</i> is complimentary (innocent, trusting)."])
O("Choose the correct word: Honesty is the guiding ___ of the association.",
  ["principle", "principal", "principality", "principled"],
  ["A <b>principle</b> is a rule or belief.", "A <i>principal</i> is the head of a school (or 'main')."])
T("Fill each gap with the correct form of the word in brackets.<br>"
  "(a) The manager's ___ (decide) surprised everyone.<br>(b) The workers demanded better ___ (accommodate).<br>"
  "(c) She spoke ___ (confidence) about her chances.<br>(d) This water is not ___ (drink).<br>"
  "(e) Their ___ (arrive) was delayed by the rain.",
  ["(a) <b>decision</b>", "(b) <b>accommodation</b>", "(c) <b>confidently</b> (adverb — it describes <i>spoke</i>)",
   "(d) <b>drinkable</b>", "(e) <b>arrival</b>"], marks=5)

# ------------------------------------------------------------------ 6
topic("fig", "Figures of speech & literary devices", S, [
    "Simile compares with <i>like</i> or <i>as</i>; metaphor compares directly, without them.",
    "Personification gives human qualities to non-human things; apostrophe addresses an absent person or a thing.",
    "Hyperbole exaggerates; litotes (understatement) says less than is meant.",
    "Euphemism softens something unpleasant: 'passed away' for 'died'.",
    "Metonymy uses a related thing for the thing itself ('the Crown'); synecdoche uses a part for the whole ('all hands on deck').",
])
O("Identify the figure of speech: 'The wind whispered through the palm trees.'",
  ["Personification", "Simile", "Hyperbole", "Metonymy"],
  ["Whispering is a human action given to the wind, so it is <b>personification</b>."])
O("Identify the figure of speech: 'Kofi is a lion on the football field.'",
  ["Metaphor", "Simile", "Irony", "Euphemism"],
  ["Kofi is said to <i>be</i> a lion — a direct comparison with no <i>like</i> or <i>as</i>, so it is a <b>metaphor</b>."])
O("Identify the figure of speech: 'I have told you a million times to close the gate.'",
  ["Hyperbole", "Litotes", "Paradox", "Metonymy"],
  ["The number is a deliberate exaggeration for effect — <b>hyperbole</b>."])
O("Identify the figure of speech: 'His grandmother passed away last night.'",
  ["Euphemism", "Irony", "Simile", "Oxymoron"],
  ["<i>Passed away</i> is a gentler expression for <i>died</i>, so it is a <b>euphemism</b>."])
O("Identify the figure of speech: 'The pen is mightier than the sword.'",
  ["Metonymy", "Simile", "Personification", "Onomatopoeia"],
  ["The <i>pen</i> stands for writing and the <i>sword</i> for warfare — one thing named by something closely associated with it: <b>metonymy</b>."])
O("Identify the figure of speech: 'It was a deafening silence in the hall.'",
  ["Oxymoron", "Alliteration", "Hyperbole", "Simile"],
  ["<i>Deafening</i> and <i>silence</i> contradict each other, and the two are placed side by side — an <b>oxymoron</b>."])
T("Name the figure of speech in each sentence and explain its effect in one line.<br>"
  "(a) The classroom was a zoo when the teacher stepped out.<br>(b) Peter picked a peck of pickled peppers.<br>"
  "(c) The car coughed, spluttered and finally died.<br>(d) O Death, where is thy sting?<br>"
  "(e) He is not a bad footballer at all.",
  ["(a) <b>Metaphor</b> — the noise and disorder of the class are compared directly with a zoo.",
   "(b) <b>Alliteration</b> — the repeated /p/ sound gives the line rhythm and makes it memorable.",
   "(c) <b>Personification</b> — the car is given human actions, which makes its breakdown vivid.",
   "(d) <b>Apostrophe</b> — death, which cannot reply, is addressed directly, giving the line dramatic force.",
   "(e) <b>Litotes (understatement)</b> — saying 'not bad' to mean 'very good' is a modest, emphatic way of praising him."], marks=10)

S = "Structure (Grammar)"

# ------------------------------------------------------------------ 7
topic("tense", "Tenses & sequence of tenses", S, [
    "Present perfect (<i>has/have + past participle</i>) links the past to now: 'She has lived here since 2020.'",
    "Past perfect (<i>had + past participle</i>) shows the earlier of two past actions.",
    "<i>since</i> takes a point in time; <i>for</i> takes a length of time.",
    "After <i>By the time…</i> in the past, use the past perfect in the main clause.",
    "Do not mix tenses within one time frame without a reason.",
])
O("Choose the correct option: By the time we reached the cinema, the film ___.",
  ["had started", "has started", "started", "was starting"],
  ["Two past actions: the film started FIRST, so it takes the past perfect — <b>had started</b>."])
O("Choose the correct option: She ___ in Kumasi since 2019.",
  ["has lived", "lived", "is living", "had lived"],
  ["<i>Since 2019</i> links the past to the present, so the present perfect is used: <b>has lived</b>."])
O("Choose the correct option: If it rains tomorrow, we ___ the match.",
  ["will postpone", "would postpone", "postponed", "will be postponed"],
  ["This is the first conditional: <i>if</i> + present simple, then <i>will</i> + bare infinitive."])
O("Choose the correct option: The students ___ their assignments before the teacher arrived.",
  ["had finished", "have finished", "finish", "are finishing"],
  ["The finishing happened before another past event, so the past perfect is correct."])
O("Choose the correct option: Kofi said that he ___ to Accra the following week.",
  ["would travel", "will travel", "travels", "has travelled"],
  ["In reported speech, <i>will</i> in the original becomes <b>would</b> after a past reporting verb."])
O("Choose the correct option: Look at those clouds! It ___ soon.",
  ["is going to rain", "rains", "rained", "has rained"],
  ["Present evidence pointing to the near future takes <i>be going to</i>."])
T("Put the verb in brackets into the correct tense.<br>"
  "(a) When I arrived, the meeting (begin) ___ already.<br>(b) He (work) ___ in that bank for ten years now.<br>"
  "(c) While we (cook) ___, the lights went off.<br>(d) By next month, she (complete) ___ her training.<br>"
  "(e) I (not see) ___ him since Christmas.",
  ["(a) <b>had begun</b> — earlier of two past actions",
   "(b) <b>has worked / has been working</b> — started in the past and still true",
   "(c) <b>were cooking</b> — a longer action interrupted by a shorter one",
   "(d) <b>will have completed</b> — future perfect, finished before a future time",
   "(e) <b>have not seen</b> — present perfect with <i>since</i>"], marks=5)

# ------------------------------------------------------------------ 8
topic("concord", "Concord (agreement)", S, [
    "A singular subject takes a singular verb, even when words come between them: 'The <b>list</b> of items <b>is</b> on the table.'",
    "With <i>neither…nor</i> and <i>either…or</i>, the verb agrees with the nearer subject.",
    "<i>Each, every, everyone, somebody, nobody, one of</i> are singular.",
    "'The number of…' is singular; 'A number of…' is plural.",
    "Nouns like <i>news, mathematics, measles, furniture, information, advice</i> take singular verbs.",
])
O("Choose the correct option: Neither the teacher nor the students ___ present.", ["were", "was", "is", "has been"],
  ["With <i>neither…nor</i>, the verb agrees with the subject nearer to it.",
   "<i>Students</i> is plural, so the verb is <b>were</b>."])
O("Choose the correct option: Each of the girls ___ a prize.", ["has won", "have won", "are winning", "win"],
  ["<i>Each</i> is singular, so the verb must be singular: <b>has won</b>."])
O("Choose the correct option: The number of candidates ___ increasing every year.", ["is", "are", "have been", "were"],
  ["'The number of…' is a singular expression (it names one figure).",
   "Compare: 'A number of candidates <i>are</i> waiting outside.'"])
O("Choose the correct option: Mathematics ___ my favourite subject.", ["is", "are", "have been", "were"],
  ["Although it ends in -s, <i>mathematics</i> is a singular noun."])
O("Choose the correct option: The chairman, together with his committee members, ___ arrived.", ["has", "have", "are", "were"],
  ["The phrase after <i>together with</i> does not change the subject.",
   "The subject is <i>the chairman</i> (singular), so the verb is <b>has</b>."])
O("Choose the correct option: Bread and butter ___ served every morning.", ["is", "are", "were", "have been"],
  ["<i>Bread and butter</i> is treated as a single item of food, so the verb is singular."])
T("Correct the error of concord in each sentence and give a reason.<br>"
  "(a) One of the boys have lost his book.<br>(b) The furniture in the classrooms are old.<br>"
  "(c) Either the prefect or the teachers is to blame.<br>(d) Everybody were happy about the result.<br>"
  "(e) Ten thousand cedis are a lot of money.",
  ["(a) <b>has</b> — the subject is <i>one</i>, not <i>boys</i>.",
   "(b) <b>is</b> — <i>furniture</i> is an uncountable, singular noun.",
   "(c) <b>are</b> — with <i>either…or</i> the verb agrees with the nearer subject, <i>teachers</i>.",
   "(d) <b>was</b> — <i>everybody</i> is singular.",
   "(e) <b>is</b> — an amount of money is treated as one unit."], marks=5)

# ------------------------------------------------------------------ 9
topic("pron", "Nouns, pronouns & determiners", S, [
    "Use the subject form after <i>than</i> when a verb is understood: 'He is taller than <b>I</b> (am).'",
    "After a preposition, use the object form: <i>between you and me</i>.",
    "A reflexive pronoun (<i>myself, themselves</i>) is used when subject and object are the same person.",
    "Countable nouns take <i>many, few, fewer</i>; uncountable nouns take <i>much, little, less</i>.",
    "<i>Its</i> = belonging to it;  <i>it's</i> = it is / it has.",
])
O("Choose the correct option: The money was shared between Kofi and ___.", ["me", "I", "myself", "mine"],
  ["<i>Between</i> is a preposition, so it takes the object pronoun <b>me</b>."])
O("Choose the correct option: She writes better than ___.", ["I", "me", "myself", "mine"],
  ["The full sentence is 'better than I <i>do</i>', so the subject form <b>I</b> is correct."])
O("Choose the correct option: There were ___ people at the rally than last year.", ["fewer", "less", "lesser", "little"],
  ["<i>People</i> is countable, so use <b>fewer</b>. <i>Less</i> goes with uncountable nouns (less water)."])
O("Choose the correct option: The dog wagged ___ tail.", ["its", "it's", "its'", "their"],
  ["<b>Its</b> shows possession. <i>It's</i> is short for <i>it is</i>."])
O("Choose the correct option: The committee has published ___ report.", ["its", "their", "it's", "theirs"],
  ["A collective noun acting as one body takes a singular possessive: <b>its</b> report."])
O("Choose the correct option: The two brothers blamed ___ for the accident.", ["each other", "themselves", "one another's", "his"],
  ["<b>Each other</b> is used for two people acting on one another; <i>one another</i> is preferred for more than two.",
   "<i>Themselves</i> would mean each brother blamed only himself."])
T("Rewrite each sentence correctly.<br>(a) Everyone must bring their own pen.<br>(b) Him and his friends went to the farm.<br>"
  "(c) The book is hers', not mine.<br>(d) There is less students in the class today.<br>(e) Me and Ama are cousins.",
  ["(a) <b>Everyone must bring his or her own pen.</b> (<i>Everyone</i> is singular; 'their' is accepted in informal use but not in the examination.)",
   "(b) <b>He and his friends went to the farm.</b> — subject form.",
   "(c) <b>The book is hers, not mine.</b> — possessive pronouns take no apostrophe.",
   "(d) <b>There are fewer students in the class today.</b>",
   "(e) <b>Ama and I are cousins.</b> — the subject form, and courtesy puts the other person first."], marks=5)

# ------------------------------------------------------------------ 10
topic("prep", "Prepositions & phrasal verbs", S, [
    "Learn verbs with their prepositions: <i>congratulate on, accuse of, insist on, comply with, deprive of, prefer to, different from, married to</i>.",
    "A phrasal verb's meaning is often nothing like the verb alone: <i>put off</i> = postpone, <i>call off</i> = cancel.",
    "<i>Look into</i> = investigate;  <i>look after</i> = take care of;  <i>look for</i> = search for;  <i>look up to</i> = respect.",
    "Do not add unnecessary prepositions: <i>discuss</i> (not 'discuss about'), <i>request</i> (not 'request for').",
])
O("Choose the correct option: The class congratulated her ___ her success.", ["on", "for", "about", "with"],
  ["The fixed pattern is <i>congratulate someone <b>on</b> something</i>."])
O("Choose the correct option: He was accused ___ stealing the money.", ["of", "for", "with", "about"],
  ["<i>Accused <b>of</b></i> + the offence. (But: <i>charged <b>with</b></i> an offence.)"])
O("Choose the correct option: I prefer rice ___ yam.", ["to", "than", "over", "from"],
  ["<i>Prefer X <b>to</b> Y</i>. <i>Than</i> is used with <i>rather</i>: 'I would rather eat rice than yam.'"])
O("Choose the option nearest in meaning to the underlined words: The meeting was <u>put off</u> until Friday.",
  ["postponed", "cancelled", "shortened", "announced"],
  ["<i>Put off</i> means to move to a later time — <b>postponed</b>.",
   "To cancel completely would be <i>call off</i>."])
O("Choose the option nearest in meaning to the underlined words: The police promised to <u>look into</u> the matter.",
  ["investigate", "ignore", "report", "settle"],
  ["<i>Look into</i> = <b>investigate</b>."])
O("Choose the correct option: The students were asked to comply ___ the new regulations.", ["with", "to", "on", "for"],
  ["The fixed pattern is <i>comply <b>with</b></i>."])
T("Supply the correct preposition or particle.<br>(a) She is married ___ a teacher.<br>(b) The results are different ___ what we expected.<br>"
  "(c) The chief insisted ___ seeing the letter.<br>(d) The team was deprived ___ victory by a late goal.<br>"
  "(e) We must do away ___ these old rules.",
  ["(a) <b>to</b>", "(b) <b>from</b>", "(c) <b>on</b>", "(d) <b>of</b>", "(e) <b>with</b> (<i>do away with</i> = abolish)"], marks=5)

# ------------------------------------------------------------------ 11
topic("adj", "Adjectives, adverbs & comparison", S, [
    "Short adjectives: <i>-er/-est</i> (tall, taller, tallest). Longer ones: <i>more/most</i>.",
    "Never use both: <i>more taller</i> is wrong.",
    "Irregular: good/better/best, bad/worse/worst, little/less/least, many/more/most, far/farther/furthest.",
    "Use the comparative for two things and the superlative for more than two.",
    "Adjectives describe nouns; adverbs describe verbs, adjectives or other adverbs: 'He drives <b>carefully</b>.'",
])
O("Choose the correct option: Of the two girls, Ama is the ___.", ["taller", "tallest", "more tall", "most tall"],
  ["For a comparison of two, use the comparative: <b>taller</b>."])
O("Choose the correct option: This is the ___ film I have ever watched.", ["most interesting", "more interesting", "interestingest", "much interesting"],
  ["<i>Interesting</i> is a long adjective, so the superlative is <b>most interesting</b>."])
O("Choose the correct option: The patient is feeling ___ today than yesterday.", ["better", "gooder", "more better", "best"],
  ["<i>Good/well</i> has the irregular comparative <b>better</b>; never <i>more better</i>."])
O("Choose the correct option: He drove ___ and avoided the accident.", ["carefully", "careful", "carefulness", "more careful"],
  ["The word describes HOW he drove, so an adverb is needed: <b>carefully</b>."])
O("Choose the correct option: Accra is ___ than Kumasi.", ["larger", "large", "largest", "more larger"],
  ["Two places are compared, so the comparative <b>larger</b> is used."])
O("Choose the correct option: She sings ___ than her sister.", ["better", "well", "best", "gooder"],
  ["The comparative of the adverb <i>well</i> is <b>better</b>."])
T("Rewrite each sentence correctly.<br>(a) He is the most cleverest boy in the class.<br>(b) This road is more wider than that one.<br>"
  "(c) She speaks English fluent.<br>(d) Of all the three candidates, he is the better.<br>(e) The food smells deliciously.",
  ["(a) <b>He is the cleverest boy in the class.</b>",
   "(b) <b>This road is wider than that one.</b>",
   "(c) <b>She speaks English fluently.</b> — an adverb is needed.",
   "(d) <b>Of all the three candidates, he is the best.</b> — more than two ⇒ superlative.",
   "(e) <b>The food smells delicious.</b> — after linking verbs (<i>smell, taste, look, feel, seem</i>) use an adjective."], marks=5)

# ------------------------------------------------------------------ 12
topic("tags", "Question tags, conditionals & reported speech", S, [
    "A positive statement takes a negative tag, and a negative statement takes a positive tag.",
    "Special tags: 'Let's go, <b>shall we</b>?', 'I am right, <b>aren't I</b>?', 'Nobody came, <b>did they</b>?', 'Open the door, <b>will you</b>?'",
    "Type 2 conditional: 'If I <b>were</b> you, I <b>would</b> accept.'  Type 3: 'If he <b>had studied</b>, he <b>would have</b> passed.'",
    "In reported speech shift the tense back and change time and place words: <i>now → then, today → that day, here → there, tomorrow → the following day</i>.",
])
O("Choose the correct tag: Let us begin the meeting, ___?", ["shall we", "will we", "do we", "shan't we"],
  ["After <i>Let us/Let's</i>, the tag is always <b>shall we</b>."])
O("Choose the correct tag: You have finished your work, ___?", ["haven't you", "didn't you", "don't you", "have you"],
  ["The statement is positive and uses <i>have</i>, so the tag is negative with the same auxiliary: <b>haven't you</b>."])
O("Choose the correct tag: Nobody informed the headmaster, ___?", ["did they", "didn't they", "did he", "were they"],
  ["<i>Nobody</i> makes the statement negative, so the tag is positive; <i>nobody</i> is referred to as <b>they</b>."])
O("Choose the correct option: If I ___ you, I would apologise.", ["were", "was", "am", "will be"],
  ["In a type 2 (unreal) conditional, <i>be</i> takes the form <b>were</b> for all persons."])
O("Choose the correct option: If she had taken the medicine, she ___ better by now.",
  ["would have felt", "will feel", "would feel", "had felt"],
  ["A type 3 conditional (past unreal) takes <i>would have</i> + past participle."])
O("Choose the correct reported form: Ama said, 'I am travelling to Tamale today.'",
  ["Ama said that she was travelling to Tamale that day.", "Ama said that she is travelling to Tamale today.",
   "Ama said that I was travelling to Tamale that day.", "Ama says that she was travelling to Tamale today."],
  ["The tense shifts back (<i>am → was</i>), the pronoun changes (<i>I → she</i>) and <i>today</i> becomes <b>that day</b>."])
T("(a) Add question tags: (i) He rarely comes to school, ___? (ii) Open the window, ___? (iii) I am your friend, ___?<br>"
  "(b) Report the following: The teacher said to the boys, 'Bring your books here tomorrow.'<br>"
  "(c) Complete: If the rain had stopped earlier, we ___ (finish) the work.",
  ["(a)(i) <b>does he</b> — <i>rarely</i> makes the statement negative in meaning, so the tag is positive.",
   "(ii) <b>will you</b> — imperatives take <i>will you</i> (or <i>won't you</i>).",
   "(iii) <b>aren't I</b> — the accepted tag for <i>I am</i>.",
   "(b) <b>The teacher told the boys to take their books there the following day.</b>",
   "Note the changes: <i>said to → told</i>, <i>bring → take</i>, <i>your → their</i>, <i>here → there</i>, <i>tomorrow → the following day</i>.",
   "(c) <b>would have finished</b>"], marks=8)

# ------------------------------------------------------------------ 13
topic("clause", "Clauses, phrases & sentence types", S, [
    "A phrase has no finite verb; a clause has one.",
    "Simple = one clause. Compound = two main clauses joined by <i>and, but, or, so</i>. Complex = a main clause plus a subordinate clause.",
    "Noun clause: does the work of a noun ('<i>What he said</i> surprised us').",
    "Adjectival (relative) clause: describes a noun ('the man <i>who called</i>').",
    "Adverbial clause: tells when, where, why, how or on what condition ('<i>because it rained</i>').",
])
O("What is the function of the underlined clause? <u>That he was late</u> annoyed the teacher.",
  ["Noun clause, subject of the verb", "Adjectival clause qualifying 'teacher'", "Adverbial clause of reason", "Main clause"],
  ["The clause names the thing that annoyed the teacher, so it does the work of a noun and is the subject of <i>annoyed</i>."])
O("What is the function of the underlined clause? The boy <u>who won the prize</u> is my brother.",
  ["Adjectival clause qualifying 'boy'", "Noun clause, object", "Adverbial clause of manner", "Adverbial clause of time"],
  ["The clause tells us <i>which</i> boy, so it qualifies the noun — an adjectival (relative) clause."])
O("What is the function of the underlined clause? We stayed indoors <u>because it was raining</u>.",
  ["Adverbial clause of reason", "Adjectival clause", "Noun clause, complement", "Adverbial clause of condition"],
  ["It answers the question <i>why</i>, so it is an adverbial clause of reason."])
O("Identify the sentence type: 'Ama cooked the food and Kofi washed the plates.'",
  ["Compound", "Simple", "Complex", "Compound-complex"],
  ["Two main clauses joined by <i>and</i>, each able to stand alone — a <b>compound</b> sentence."])
O("Identify the sentence type: 'Although he was tired, he finished the work.'",
  ["Complex", "Simple", "Compound", "Compound-complex"],
  ["<i>Although he was tired</i> is subordinate and cannot stand alone, so the sentence is <b>complex</b>."])
O("What is the function of the underlined phrase? The girl <u>in the blue uniform</u> is the head prefect.",
  ["Adjectival phrase qualifying 'girl'", "Adverbial phrase of place", "Noun phrase, object", "Verb phrase"],
  ["It has no finite verb and it tells us which girl, so it is an adjectival phrase."])
T("State the function of each underlined group of words.<br>(a) <u>Running quickly</u>, the boy caught the bus.<br>"
  "(b) I do not know <u>where she keeps the key</u>.<br>(c) He spoke <u>as though he owned the school</u>.<br>"
  "(d) The house <u>that we bought last year</u> needs painting.<br>(e) <u>In the morning</u>, we set off for the farm.",
  ["(a) <b>Participial (adjectival) phrase</b> qualifying <i>the boy</i>.",
   "(b) <b>Noun clause</b>, object of the verb <i>know</i>.",
   "(c) <b>Adverbial clause of manner</b>, modifying <i>spoke</i>.",
   "(d) <b>Adjectival (relative) clause</b> qualifying <i>the house</i>.",
   "(e) <b>Adverbial phrase of time</b>, modifying <i>set off</i>."], marks=10)

# ------------------------------------------------------------------ 14
topic("punct", "Punctuation, capitals & spelling", S, [
    "Use a comma to separate items in a list and to mark off a non-defining clause.",
    "A colon introduces a list or an explanation; a semicolon joins two closely related main clauses.",
    "Apostrophes: <i>boy's</i> (one boy), <i>boys'</i> (more than one boy), <i>children's</i> (irregular plural).",
    "Capitalise names, days, months, nationalities, titles and the first word of a sentence — but not seasons or subjects (except languages).",
    "Watch the spelling of: <i>necessary, occurrence, separate, definitely, committee, receive, privilege, embarrass, maintenance</i>.",
])
O("Choose the correctly punctuated sentence.",
  ["The girls' dormitory, which was built last year, is full.", "The girls dormitory, which was built last year is full.",
   "The girl's dormitory which was built last year, is full.", "The girls' dormitory which, was built last year is full."],
  ["The dormitory belongs to more than one girl ⇒ <i>girls'</i>.",
   "The non-defining clause <i>which was built last year</i> must be enclosed by a pair of commas."])
O("Choose the correct option: We bought the following items ___ rice, beans, oil and sugar.", [":", ";", ",", "-"],
  ["A <b>colon</b> introduces a list after a complete statement."])
O("Which word is correctly spelt?", ["necessary", "neccessary", "necesary", "nessessary"],
  ["<b>Necessary</b> — one c, two s's. A memory aid: one Collar, two Sleeves."])
O("Choose the correctly capitalised sentence.",
  ["We study French and Geography on Mondays in the harmattan season.",
   "We study french and geography on mondays in the Harmattan season.",
   "We Study French and Geography on mondays in the Harmattan Season.",
   "we study French and geography on Mondays in the harmattan Season."],
  ["Languages (French) and days (Mondays) are capitalised; a school subject is capitalised when it is also a proper noun (Geography is accepted as a named subject).",
   "Seasons such as <i>harmattan</i> are not capitalised."])
O("Choose the correct option: ___ books are on the table.", ["The children's", "The childrens'", "The childrens", "The children"],
  ["<i>Children</i> is already plural, so the possessive simply adds 's: <b>children's</b>."])
O("Which sentence uses the semicolon correctly?",
  ["The rain fell heavily; the match was abandoned.", "The rain fell heavily; and the match was abandoned.",
   "The rain fell heavily; because the match was abandoned.", "The rain fell heavily; which abandoned the match."],
  ["A semicolon joins two complete, closely related statements without a conjunction."])
T("Rewrite the passage with the correct punctuation and capital letters.<br>"
  "<i>on monday the head teacher mr mensah addressed the school he said honesty hard work and punctuality are the keys to success "
  "the students who were in the assembly hall applauded loudly</i>",
  ["<div class=\"model\">On Monday, the head teacher, Mr Mensah, addressed the school. He said, “Honesty, hard work and punctuality are the keys to success.” "
   "The students, who were in the assembly hall, applauded loudly.</div>",
   "Points to note: a capital letter begins each sentence and each proper noun (Monday, Mr Mensah);",
   "the appositive <i>Mr Mensah</i> is enclosed in commas;",
   "the spoken words take a comma before them, quotation marks around them and a capital letter at the start;",
   "the items in the list are separated by commas."], marks=10)

# ------------------------------------------------------------------ 15
topic("voice", "Active & passive voice", S, [
    "Passive = the right form of <i>be</i> + past participle: 'The letter <b>was written</b> by Kofi.'",
    "The object of the active sentence becomes the subject of the passive.",
    "Use <i>by</i> only when the doer matters; often it is left out.",
    "Keep the tense: writes → is written;  wrote → was written;  has written → has been written;  will write → will be written.",
    "Verbs like <i>have, resemble, lack, suit</i> have no passive form.",
])
O("Change to the passive: 'The carpenter is repairing the desks.'",
  ["The desks are being repaired by the carpenter.", "The desks are repaired by the carpenter.",
   "The desks were being repaired by the carpenter.", "The desks have been repaired by the carpenter."],
  ["Present continuous active → present continuous passive: <i>are being</i> + past participle."])
O("Change to the passive: 'Someone has stolen my bicycle.'",
  ["My bicycle has been stolen.", "My bicycle was stolen by someone.", "My bicycle is stolen.", "My bicycle had been stolen."],
  ["Present perfect: <i>has been</i> + past participle. <i>Someone</i> is vague, so <i>by someone</i> is dropped."])
O("Change to the active: 'The prize was won by a Form Two student.'",
  ["A Form Two student won the prize.", "A Form Two student has won the prize.",
   "The prize a Form Two student won.", "A Form Two student was winning the prize."],
  ["The doer becomes the subject and the tense stays simple past: <b>won</b>."])
O("Choose the correct passive form: 'They will announce the results next week.'",
  ["The results will be announced next week.", "The results will announce next week.",
   "The results are announced next week.", "The results would be announced next week."],
  ["Future simple passive: <i>will be</i> + past participle."])
O("Choose the correct passive form: 'The teacher gave the boys some books.'",
  ["The boys were given some books.", "Some books were given the boys by the teacher's.",
   "The boys are given some books.", "The boys had given some books."],
  ["With two objects, either may become the subject; the natural version is <b>The boys were given some books</b> (by the teacher)."])
O("Which sentence has NO passive form?", ["Kofi has a new phone.", "Kofi wrote a letter.", "Kofi is cleaning the room.", "They built the school."],
  ["<i>Have</i> in the sense of possession cannot be made passive — we do not say 'A new phone is had by Kofi.'"])
T("Rewrite each sentence in the passive voice.<br>(a) The farmer planted maize on the ridges.<br>"
  "(b) The head teacher is addressing the students.<br>(c) They have completed the new library.<br>"
  "(d) Somebody must clean this classroom.<br>(e) The judge will deliver the verdict tomorrow.",
  ["(a) <b>Maize was planted on the ridges by the farmer.</b>",
   "(b) <b>The students are being addressed by the head teacher.</b>",
   "(c) <b>The new library has been completed.</b>",
   "(d) <b>This classroom must be cleaned.</b>",
   "(e) <b>The verdict will be delivered tomorrow.</b>"], marks=5)
