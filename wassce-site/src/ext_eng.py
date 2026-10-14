from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}

extras("syn",
  plain="A synonym is a word that means nearly the same as another word. In the exam you must pick the one "
        "that fits THE SENTENCE — not just any word with a similar dictionary meaning.",
  examples=[
    E("Choose the word nearest in meaning to the underlined word: The old bridge is in a <u>precarious</u> state.",
      "Step 1. Read the whole sentence. A bridge in a bad state is unsafe and could fall.",
      "Step 2. <i>Precarious</i> = not safe, likely to fall or fail.",
      "Step 3. Pick the word with that meaning: <b>dangerous / unstable</b>. A word like 'old' is in the sentence "
      "already and is not the meaning of the underlined word."),
    E("Choose the word nearest in meaning: The nurse spoke to the patient in a <u>soothing</u> voice.",
      "Step 1. Ask what effect the voice has — it calms the patient.",
      "Step 2. <i>Soothing</i> = calming, comforting.",
      "Step 3. Answer: <b>calming</b>. (<i>Quiet</i> is about volume, which is not the same thing.)")])

extras("ant",
  plain="An antonym is a word with the opposite meaning. Check the part of speech first: the opposite of a "
        "verb must be a verb, the opposite of an adjective must be an adjective.",
  examples=[
    E("Choose the OPPOSITE of the underlined word: The chief gave a <u>brief</u> speech.",
      "Step 1. <i>Brief</i> here describes the speech — it means short.",
      "Step 2. The opposite of short (in time) is long or lengthy.",
      "Step 3. Answer: <b>lengthy</b>. (<i>Boring</i> is a judgement, not an opposite.)"),
    E("Give the opposite of: (a) generous (b) ancient (c) accept (d) success.",
      "(a) <b>stingy / mean</b>  (b) <b>modern / recent</b>  (c) <b>reject / refuse</b>  (d) <b>failure</b>",
      "Notice that (c) is a verb and (d) is a noun — the opposite must match the word class.")])

extras("idiom",
  plain="An idiom is a group of words whose meaning you cannot work out from the separate words. "
        "'To kick the bucket' has nothing to do with buckets — it means to die. Idioms must simply be learnt.",
  examples=[
    E("What does the underlined expression mean? After the quarrel, the two friends <u>buried the hatchet</u>.",
      "Step 1. Do NOT translate word by word — no one buried anything.",
      "Step 2. The situation is a quarrel that has ended.",
      "Step 3. <i>Bury the hatchet</i> = <b>make peace / end a quarrel</b>."),
    E("Use these idioms in sentences: (a) in black and white (b) a drop in the ocean.",
      "(a) <i>in black and white</i> = in writing. <b>The headmaster asked for the complaint in black and white.</b>",
      "(b) <i>a drop in the ocean</i> = a very small amount compared with what is needed. "
      "<b>The GH₵ 200 donated was a drop in the ocean compared with the cost of the project.</b>")])

extras("reg",
  plain="A register is the special vocabulary of a job or field. Doctors, lawyers, farmers and mechanics each "
        "have their own words. Learn them in groups — it is the quickest way to pick up marks in Paper 1.",
  examples=[
    E("The words <i>adjourn, bail, plaintiff, verdict</i> belong to which field?",
      "Step 1. Ask where you would hear all four words together.",
      "Step 2. A case is adjourned, an accused person is granted bail, the plaintiff brings the case, "
      "the jury gives a verdict.",
      "Step 3. All four belong to <b>law (the law court)</b>."),
    E("Add two more words to each set: (a) carburettor, clutch … (b) teller, overdraft …",
      "(a) These are motor vehicle words: add <b>gasket, ignition, chassis, gear</b>.",
      "(b) These are banking words: add <b>deposit, ledger, statement, interest</b>.")],
  fig=draw.tree("Registers in Paper 1", ["Law: verdict, bail", "Medicine: dosage, ward", "Banking: teller, overdraft"],
                label="Groups of register words"))

extras("form",
  plain="Word formation is about building words from other words — and knowing which form fits the sentence. "
        "Many marks are lost by writing the verb where a noun is needed.",
  examples=[
    E("Fill the gap: The teacher's ___ (explain) was very clear.",
      "Step 1. The gap comes after 'The teacher's' and before 'was', so a NOUN is needed.",
      "Step 2. The noun from <i>explain</i> is <i>explanation</i>.",
      "Step 3. <b>The teacher's explanation was very clear.</b>"),
    E("Choose correctly: We must (practise / practice) every evening.",
      "Step 1. The word follows 'must', so a VERB is needed.",
      "Step 2. The verb is spelt with an <b>s</b>: practi<b>s</b>e. The noun is practi<b>c</b>e.",
      "Step 3. <b>We must practise every evening.</b> (Same rule: advise/advice, licence/license.)")])

extras("fig",
  plain="Figures of speech are ways of saying something so that it paints a picture. A simile uses 'like' or "
        "'as'; a metaphor says one thing IS another; personification gives human qualities to things.",
  examples=[
    E("Name the figure of speech: 'The classroom was a market.'",
      "Step 1. Is 'like' or 'as' used? No.",
      "Step 2. The classroom is said to BE a market — a direct comparison of the noise and disorder.",
      "Step 3. It is a <b>metaphor</b>. (With 'like', 'The classroom was like a market', it would be a simile.)"),
    E("Name and explain the figure of speech: 'The hungry sea swallowed the canoe.'",
      "Step 1. The sea is given human qualities — hunger and swallowing.",
      "Step 2. That is <b>personification</b>.",
      "Step 3. Its effect: it makes the sea sound alive and cruel, so the loss feels more frightening.")])

extras("tense",
  plain="Tense shows WHEN something happened. The trick is to look for the time words in the sentence — "
        "<i>since, ago, by the time, already, yesterday, next week</i> — they tell you which tense to use.",
  examples=[
    E("Fill the gap: By the time the ambulance arrived, the man ___ (die).",
      "Step 1. Two past actions: the man died FIRST, then the ambulance arrived.",
      "Step 2. The earlier past action takes the past perfect: had + past participle.",
      "Step 3. <b>By the time the ambulance arrived, the man had died.</b>"),
    E("Fill the gap: She ___ (teach) in this school for ten years.",
      "Step 1. 'For ten years' up to now links the past with the present.",
      "Step 2. Use the present perfect: has/have + past participle (or the continuous form).",
      "Step 3. <b>She has taught (or has been teaching) in this school for ten years.</b>")])

extras("concord",
  plain="Concord means the verb must agree with its subject: one person 'walks', many people 'walk'. "
        "The danger is the words in between — cross them out and look only at the real subject.",
  examples=[
    E("Choose the correct verb: The box of tools (is / are) on the bench.",
      "Step 1. Find the subject: it is <i>the box</i>, not <i>tools</i>.",
      "Step 2. 'of tools' only describes the box — cover it with your finger.",
      "Step 3. One box ⇒ singular verb: <b>The box of tools is on the bench.</b>"),
    E("Choose the correct verb: Neither the players nor the coach (was / were) happy.",
      "Step 1. With <i>neither … nor</i>, the verb agrees with the subject NEARER to it.",
      "Step 2. The nearer subject is <i>the coach</i>, which is singular.",
      "Step 3. <b>Neither the players nor the coach was happy.</b>")])

extras("pron",
  plain="Pronouns stand in for nouns: he, she, it, they, him, them. Use the subject form (I, he, they) before "
        "a verb, and the object form (me, him, them) after a verb or a preposition.",
  examples=[
    E("Choose correctly: The teacher gave the books to Kofi and (I / me).",
      "Step 1. 'to' is a preposition, so the object form is needed.",
      "Step 2. Test it by removing 'Kofi and': you would say 'gave the books to me', not 'to I'.",
      "Step 3. <b>The teacher gave the books to Kofi and me.</b>"),
    E("Choose correctly: My brother is taller than (I / me).",
      "Step 1. The full sentence is 'taller than I am'.",
      "Step 2. Because a verb is understood after it, the subject form is used.",
      "Step 3. <b>My brother is taller than I (am).</b>")])

extras("prep",
  plain="Prepositions are small words like in, on, at, to, from — and English fixes certain ones to certain "
        "verbs. There is no rule; they must be learnt as pairs: <i>depend ON, married TO, accused OF</i>.",
  examples=[
    E("Fill the gap: The success of the farm depends ___ regular rainfall.",
      "Step 1. Think of the fixed pair for the verb <i>depend</i>.",
      "Step 2. We always say <i>depend <b>on</b></i> (never 'depend from' or 'depend of').",
      "Step 3. <b>The success of the farm depends on regular rainfall.</b>"),
    E("Give the meaning of the phrasal verbs: (a) call off (b) look after (c) turn down.",
      "(a) <b>cancel</b> — The match was called off because of rain.",
      "(b) <b>take care of</b> — She looks after her grandmother.",
      "(c) <b>refuse / reject</b> — He turned down the offer.")])

extras("adj",
  plain="Adjectives describe nouns (a <i>tall</i> boy); adverbs describe verbs (he ran <i>quickly</i>). "
        "When comparing two things use the comparative (taller); for three or more use the superlative (tallest).",
  examples=[
    E("Choose correctly: Of the two sisters, Akua is the (older / oldest).",
      "Step 1. How many are being compared? Two.",
      "Step 2. Two ⇒ comparative form.",
      "Step 3. <b>Akua is the older.</b> ('Oldest' would need three or more sisters.)"),
    E("Correct this sentence: He played very good in the match.",
      "Step 1. The word describes HOW he played — a verb — so an adverb is needed.",
      "Step 2. The adverb of <i>good</i> is <i>well</i>.",
      "Step 3. <b>He played very well in the match.</b>")])

extras("tags",
  plain="A question tag is the short question added to a statement: 'You are ready, aren't you?' The rule is "
        "simple — positive statement takes a negative tag, and negative statement takes a positive tag.",
  examples=[
    E("Add the tag: Ama has finished her work, ___?",
      "Step 1. The statement is positive, so the tag must be negative.",
      "Step 2. Use the same helping verb, <i>has</i>, and the pronoun <i>she</i>.",
      "Step 3. <b>Ama has finished her work, hasn't she?</b>"),
    E("Report this: The teacher said, 'I will mark your books tomorrow.'",
      "Step 1. The reporting verb <i>said</i> is past, so shift the tense back: will → would.",
      "Step 2. Change the pronouns: I → he/she, your → their.",
      "Step 3. Change the time word: tomorrow → the following day.",
      "<b>The teacher said that he would mark their books the following day.</b>")])

extras("clause",
  plain="A phrase is a group of words with no verb in it; a clause has a verb. A main clause can stand alone; "
        "a subordinate clause cannot, and does the work of a noun, an adjective or an adverb.",
  examples=[
    E("Name the underlined clause and state its function: I know <u>that he is honest</u>.",
      "Step 1. Does it have a verb? Yes — <i>is</i>. So it is a clause.",
      "Step 2. Ask 'know WHAT?' — the clause answers it, so it names a thing: it is doing a noun's work.",
      "Step 3. It is a <b>noun clause</b>, and its function is the <b>object of the verb 'know'</b>."),
    E("Say whether each sentence is simple, compound or complex.<br>"
      "(a) The rain stopped. (b) The rain stopped and we went out. (c) We went out when the rain stopped.",
      "(a) One clause only ⇒ <b>simple</b>.",
      "(b) Two clauses that can each stand alone, joined by <i>and</i> ⇒ <b>compound</b>.",
      "(c) 'when the rain stopped' cannot stand alone ⇒ <b>complex</b>.")],
  fig=draw.tree("Subordinate clauses", ["Noun clause — names a thing", "Adjectival — describes a noun",
                                        "Adverbial — tells when, why, how"], label="Types of subordinate clause"))

extras("punct",
  plain="Punctuation shows the reader where to pause and what belongs together. Two marks decide many exam "
        "questions: the comma (small pause, or marking off extra information) and the apostrophe (ownership).",
  examples=[
    E("Punctuate: my brother who lives in kumasi is a nurse",
      "Step 1. Start with a capital letter and end with a full stop.",
      "Step 2. 'who lives in Kumasi' is extra information, so mark it off with a pair of commas.",
      "Step 3. Capitalise the place name.",
      "<b>My brother, who lives in Kumasi, is a nurse.</b>"),
    E("Where does the apostrophe go: (a) the boys books (one boy) (b) the boys books (many boys)?",
      "Step 1. First decide who owns: one boy or many boys.",
      "(a) One boy owns them ⇒ add 's: <b>the boy's books</b>.",
      "(b) Many boys own them; <i>boys</i> already ends in s ⇒ add only the apostrophe: <b>the boys' books</b>.")])

extras("voice",
  plain="In the active voice the doer comes first: 'The boy kicked the ball.' In the passive the thing done "
        "to comes first: 'The ball was kicked by the boy.' The passive is useful when the doer is unknown.",
  examples=[
    E("Change to the passive: The farmer harvested the maize last week.",
      "Step 1. Move the object to the front: <i>The maize</i>.",
      "Step 2. Use the right form of <i>be</i> in the SAME tense (past simple) + past participle: <i>was harvested</i>.",
      "Step 3. Add the doer with 'by' if it matters.",
      "<b>The maize was harvested by the farmer last week.</b>"),
    E("Change to the active: The window was broken by the children.",
      "Step 1. The doer is 'the children' — put them first.",
      "Step 2. Keep the tense: <i>was broken</i> (past) ⇒ <i>broke</i>.",
      "Step 3. <b>The children broke the window.</b>")])

extras("vowel",
  plain="In Oral English you match SOUNDS, not spellings. <i>Meat, great</i> and <i>heart</i> are spelt alike "
        "but sound different. Say the words quietly to yourself and listen to the vowel in the middle.",
  examples=[
    E("Which word has the same vowel sound as <i>cut</i>: <i>put, love, cute, cure</i>?",
      "Step 1. Say <i>cut</i> — the vowel is the short /ʌ/ sound.",
      "Step 2. Test each one: <i>put</i> = /ʊ/, <i>love</i> = /ʌ/, <i>cute</i> = /juː/, <i>cure</i> = /ʊə/.",
      "Step 3. The answer is <b>love</b> — spelling with an <i>o</i> does not matter."),
    E("Which word does NOT rhyme with the others: <i>tough, rough, cough, puff</i>?",
      "Step 1. Rhyme depends on the sound from the vowel to the end.",
      "Step 2. <i>Tough</i> = /tʌf/, <i>rough</i> = /rʌf/, <i>puff</i> = /pʌf/ — all the same ending.",
      "Step 3. <i>Cough</i> = /kɒf/, a different vowel, so <b>cough</b> is the odd one out.")])

extras("cons",
  plain="Consonant questions test which sound a letter makes, and which letters are silent. Say the word "
        "aloud and feel your mouth: /s/ is hissed with no voice, /z/ buzzes in your throat.",
  examples=[
    E("How is the final -s pronounced in <i>dogs, cats</i> and <i>buses</i>?",
      "Step 1. Feel the sound BEFORE the -s.",
      "Step 2. /ɡ/ in <i>dogs</i> is voiced (your throat buzzes) ⇒ the -s is <b>/z/</b>.",
      "Step 3. /t/ in <i>cats</i> is voiceless ⇒ the -s is <b>/s/</b>.",
      "Step 4. <i>Bus</i> already ends in a hissing sound ⇒ the ending is <b>/ɪz/</b>."),
    E("Which letter is silent in each word: <i>knife, debt, castle, honour</i>?",
      "<i>knife</i> — the <b>k</b>;  <i>debt</i> — the <b>b</b>;  <i>castle</i> — the <b>t</b>;  <i>honour</i> — the <b>h</b>.",
      "Tip: learn silent letters in families — kn- (knee, knock, know), -stle (castle, whistle, listen).")])

extras("stress",
  plain="Stress is the syllable you say with more force: <i>TA-ble</i>, not <i>ta-BLE</i>. Emphatic stress is "
        "when you push one WORD in a sentence, and that word answers the listener's question.",
  examples=[
    E("Where is the stress in <i>examination</i>, and what happens in <i>photograph → photographer</i>?",
      "Step 1. Break the word into syllables: e-xa-mi-NA-tion — the stress is on the <b>fourth</b> syllable.",
      "Step 2. Stress can move when a word changes: <b>PHO</b>-to-graph, but pho-<b>TO</b>-gra-pher.",
      "Step 3. Practise saying both aloud; the meaning does not change, only the beat."),
    E("In 'Kofi bought the book on TUESDAY', what question does the stress answer?",
      "Step 1. Find the word said with extra force: TUESDAY.",
      "Step 2. That word gives the new or important information — the day.",
      "Step 3. It answers: <b>When did Kofi buy the book?</b>")])

extras("comp",
  plain="Comprehension is not a memory test — the answers are in the passage. Read once for the story, then "
        "read each question and go back to the exact line. Answer in your own words, in full sentences.",
  examples=[
    E("How to answer 'What is the meaning of the expression X as used in the passage?'",
      "Step 1. Find the expression and read the sentence BEFORE and AFTER it.",
      "Step 2. Ask what the writer is saying at that point, not what the words mean separately.",
      "Step 3. Write it in your own words, in a complete sentence.",
      "Example: 'He was walking on eggshells' in a passage about an angry boss means "
      "<b>he was being very careful not to upset anyone.</b>"),
    E("How to answer 'What grammatical name is given to this expression and what is its function?'",
      "Step 1. Two marks, two parts — always give BOTH.",
      "Step 2. Name it: noun clause, adjectival clause, adverbial clause of time/reason, or a phrase.",
      "Step 3. Say what work it does, naming the word it works with.",
      "Model answer: <b>It is an adverbial clause of time; it modifies the verb 'left'.</b>")],
  fig=draw.flow(["Read the whole passage", "Read the question", "Find the exact line",
                 "Answer in your own words"], note="Comprehension in four steps", label="How to attack a comprehension passage"))

extras("summary",
  plain="Summary means saying the same thing in fewer words — and only what the question asks for. Marks are "
        "lost for adding your own opinion, copying long sentences, or writing more sentences than asked.",
  examples=[
    E("A passage lists reasons why young people leave villages. The question asks for THREE reasons in three "
      "sentences. How do you go about it?",
      "Step 1. Underline every reason in the passage — ignore effects and solutions.",
      "Step 2. Group repeated points together; an example is not a separate point.",
      "Step 3. Write exactly three sentences, one point in each, in your own words.",
      "Model: <b>1. There are few jobs in the villages. 2. Social amenities such as electricity and clinics "
      "are lacking. 3. Farming brings low and uncertain incomes.</b>"),
    E("Reduce this to one short sentence: 'The headmaster, who has been in the school for many years and knows "
      "every student by name, said that he was not at all pleased with the way the students behaved.'",
      "Step 1. Find the main idea: the headmaster was displeased with the students' behaviour.",
      "Step 2. Drop the extra information about his years and knowing names — it is not the point.",
      "Step 3. <b>The long-serving headmaster was displeased with the students' behaviour.</b>")])

extras("essay",
  plain="An essay is marked on four things: content (your points), organisation (paragraphs), expression "
        "(grammar and vocabulary) and mechanical accuracy (spelling and punctuation). Plan for five minutes "
        "before you write — it is the cheapest way to gain marks.",
  examples=[
    E("How to plan any essay in five minutes.",
      "Step 1. Underline the key words in the question: WHAT to write, to WHOM, and HOW MANY points.",
      "Step 2. Jot down four or five points in rough — one for each paragraph.",
      "Step 3. Decide the opening (state your stand or purpose) and the closing (a short, firm conclusion).",
      "Step 4. Write, giving each point its own paragraph with one example."),
    E("Set out a formal letter correctly.",
      "Step 1. Your own address at the top right, with the date under it.",
      "Step 2. The receiver's address on the left, then the salutation: Dear Sir/Madam.",
      "Step 3. A title in capitals or underlined, then three or four paragraphs.",
      "Step 4. End with <i>Yours faithfully</i> (because you wrote Dear Sir/Madam), your signature and your "
      "full name in capitals.",
      fig=draw.letterfig(label="Layout of a formal letter"))])
