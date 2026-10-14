from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}

S = "Structure (Grammar)"

# ------------------------------------------------------------ common errors
topic("errors", "Common errors & sentence improvement", S, [
    "Say <i>discuss</i> and <i>request</i>, not 'discuss about' or 'request for'.",
    "<i>Despite</i> and <i>in spite of</i> — never 'despite of'.",
    "<i>Prefer X to Y</i>, not 'prefer X than Y'.  <i>Different from</i>, not 'different than'.",
    "<i>Lend</i> = give out;  <i>borrow</i> = take. 'He lent me money' (not 'borrowed me money').",
    "'The reason is <b>that</b>…', not 'the reason is because'.",
    "'One of the boys <b>who have</b> come' — the verb follows <i>boys</i>; but 'One of the boys <b>is</b> here'.",
])
O("Choose the correct sentence.",
  ["We discussed the matter at length.", "We discussed about the matter at length.",
   "We discussed on the matter at length.", "We discussed over the matter at length."],
  ["<i>Discuss</i> already carries the idea of 'about', so no preposition follows it.",
   "The same applies to <i>request</i>, <i>enter</i>, <i>resemble</i> and <i>emphasise</i>."])
O("Choose the correct sentence.",
  ["Despite the rain, the match continued.", "Despite of the rain, the match continued.",
   "Inspite the rain, the match continued.", "Despite from the rain, the match continued."],
  ["Use either <i>despite</i> + noun or <i>in spite of</i> + noun.", "'Despite of' mixes the two and is always wrong."])
O("Correct the error: Kofi borrowed me GH₵ 50 last week.",
  ["Kofi lent me GH₵ 50 last week.", "Kofi borrowed from me GH₵ 50 last week.",
   "Kofi borrowed me with GH₵ 50 last week.", "Kofi has borrow me GH₵ 50 last week."],
  ["The person who GIVES lends; the person who TAKES borrows.", "Kofi gave the money, so he <b>lent</b> it."])
O("Choose the correct sentence.",
  ["He is one of the students who have passed.", "He is one of the students who has passed.",
   "He is one of the student who have passed.", "He is one of the students which have passed."],
  ["The relative clause describes <i>the students</i> (plural), so the verb is <i>have</i>.",
   "Use <i>who</i> for people, never <i>which</i>."])
O("Choose the correct sentence.",
  ["The reason for his absence is that he was ill.", "The reason for his absence is because he was ill.",
   "The reason for his absence is due to he was ill.", "The reason why for his absence is because he was ill."],
  ["'The reason … is <b>that</b>' is the correct pattern.", "'Is because' repeats the idea of reason twice."])
T("Rewrite each sentence correctly and give the rule in one line.<br>"
  "(a) I look forward to see you next week.<br>(b) She prefers tea than coffee.<br>"
  "(c) The two brothers resemble with each other.<br>(d) He has been teaching since five years.<br>"
  "(e) Each of the candidates were given a form.<br>(f) I enjoyed during the holidays.",
  ["(a) <b>I look forward to seeing you next week.</b> — after 'look forward to', the verb takes -ing.",
   "(b) <b>She prefers tea to coffee.</b> — the pattern is <i>prefer X to Y</i>.",
   "(c) <b>The two brothers resemble each other.</b> — <i>resemble</i> takes no preposition.",
   "(d) <b>He has been teaching for five years.</b> — <i>for</i> + a length of time, <i>since</i> + a point in time.",
   "(e) <b>Each of the candidates was given a form.</b> — <i>each</i> is singular.",
   "(f) <b>I enjoyed myself during the holidays.</b> — <i>enjoy</i> needs an object."], marks=12)
extras("errors",
  plain="Many marks are lost not on hard grammar but on the same handful of slips. Learn these patterns by "
        "heart and you protect easy marks in both Paper 1 and your essays.",
  examples=[
    E("Correct: 'The committee have discuss about the matter and they decided to postpone it.'",
      "Step 1. 'have discuss' — after <i>have</i> use the past participle: <b>have discussed</b>.",
      "Step 2. 'discuss about' — <i>discuss</i> takes no preposition: <b>discussed the matter</b>.",
      "Step 3. Keep the pronoun consistent with the collective noun.",
      "<b>The committee have discussed the matter and they decided to postpone it.</b> "
      "(Or, treating the committee as one body: 'The committee has discussed the matter and it decided…')"),
    E("Improve: 'Being that the road was bad, we reached late.'",
      "Step 1. 'Being that' is not standard English in this sense.",
      "Step 2. Use <i>Since</i>, <i>Because</i> or <i>As</i>.",
      "Step 3. 'Reached' needs an object: reached home / arrived late.",
      "<b>Because the road was bad, we arrived late.</b>")])

S = "Comprehension, Summary & Essay"

# ------------------------------------------------------------ reports, speeches, articles
topic("report", "Reports, speeches & articles", S, [
    "A REPORT has a title, says who asked for it, states the findings in order, and ends with conclusions and "
    "recommendations, then the writer's name and position.",
    "A SPEECH opens with vocatives — 'Mr Chairman, the Headmaster, distinguished guests, fellow students' — "
    "and addresses the audience directly throughout.",
    "An ARTICLE has a title and a by-line, is written for readers of a named magazine or newspaper, and ends "
    "with a clear conclusion.",
    "All three are marked on content, organisation, expression and mechanical accuracy — so plan before you write.",
    "Keep the tone formal for a report, warm but respectful for a speech, and lively but clean for an article.",
])
O("Which of these is essential in a report but NOT in a story?",
  ["Recommendations at the end", "Paragraphs", "A title", "Correct spelling"],
  ["A report is written so that someone can act on it, so it ends with conclusions and recommendations.",
   "Titles, paragraphs and good spelling belong to both."])
O("A speech should begin with ___",
  ["vocatives addressing the audience", "the writer's address", "a list of references", "the date and venue"],
  ["Vocatives — 'Mr Chairman, ladies and gentlemen' — show that you are speaking TO an audience."])
O("Who should sign a report on a school football competition written for the headmaster?",
  ["The writer, with his or her position", "The headmaster", "The sports master only", "No one"],
  ["A report ends with the writer's name and position, for example 'Ama Boateng, Sports Prefect'."])
O("Which ending is most suitable for an article for a school magazine?",
  ["A short paragraph summing up the writer's stand", "Yours faithfully",
   "The writer's postal address", "A list of the students interviewed"],
  ["An article is not a letter, so it takes no 'Yours faithfully' or address — it ends with a conclusion."])
O("In a speech, which expression best keeps the audience involved?",
  ["'As you all know, fellow students, …'", "'The undersigned wishes to state …'",
   "'Please find attached …'", "'With reference to your letter …'"],
  ["A speech speaks directly to the people in front of you; the other three belong to formal letters and memos."])
T("As the Health Prefect of your school, write a report to the headmaster on the state of the school's "
  "sanitation facilities, suggesting two improvements.",
  ["<b>Plan.</b> Title; who asked for the report and when; what you found (three or four points); "
   "conclusions; recommendations; your name and position.",
  "<div class=\"model\"><b>REPORT ON THE STATE OF SANITATION FACILITIES IN THE SCHOOL</b><br><br>"
   "<b>1. Terms of reference.</b> On 2nd October, 2026, the Headmaster asked me to inspect the school's "
   "sanitation facilities and report on their condition.<br><br>"
   "<b>2. Procedure.</b> Between 3rd and 6th October I inspected the four toilet blocks, the urinals, the "
   "refuse site and the water points, and spoke with the cleaners and twelve students.<br><br>"
   "<b>3. Findings.</b><br>(a) Two of the four toilet blocks have broken doors and no running water.<br>"
   "(b) The refuse site behind the dining hall is not cleared regularly and attracts flies.<br>"
   "(c) Only three of the nine wash basins have soap.<br><br>"
   "<b>4. Conclusion.</b> The facilities are inadequate for a student population of 900 and pose a health risk, "
   "especially in the rainy season.<br><br>"
   "<b>5. Recommendations.</b><br>(a) The two damaged blocks should be repaired and connected to the water tank "
   "before the end of the term.<br>(b) The refuse should be collected twice a week, and soap provided daily at "
   "every wash basin.<br><br>"
   "Kwabena Mensah<br>Health Prefect</div>",
   "Notice the numbered sections, the plain factual tone, and recommendations that can actually be carried out."],
  marks=30)
extras("report",
  plain="These three are 'writing for a purpose'. Ask yourself: who will read it, and what should they do "
        "afterwards? A report informs someone who must act; a speech moves an audience in front of you; "
        "an article interests a reader who chose to pick up the magazine.",
  examples=[
    E("Tell the three apart at a glance.",
      "<b>Report</b> — title, terms of reference, findings, recommendations, writer's name and position. No salutation.",
      "<b>Speech</b> — vocatives at the start, direct address ('you', 'we') all through, and a closing thank-you.",
      "<b>Article</b> — title and by-line, written for named readers, a lively opening and a firm conclusion.",
      fig=draw.flow(["Report: inform & advise", "Speech: address an audience", "Article: interest a reader"],
                    note="Three forms, three purposes", label="Report, speech and article")),
    E("Write the opening of a speech on 'The dangers of drug abuse' to be delivered at a school assembly.",
      "Step 1. Vocatives, in order of seniority.",
      "Step 2. State the subject and why it matters now.",
      "<div class=\"model\">Mr Chairman, the Headmaster, members of staff, invited guests, fellow students, "
      "good morning. I have been asked to speak on a subject that is quietly taking away our friends and "
      "classmates: the abuse of drugs. Before I sit down, I hope every one of us will see why a single tablet "
      "taken 'just to stay awake' can cost a whole future…</div>")])

S = "Oral English"

# ------------------------------------------------------------ listening & spoken responses
topic("listen", "Listening & spoken responses", S, [
    "In the listening test you hear a word, a sentence or a short passage and answer multiple-choice questions, "
    "so listen for the exact sound or the exact detail asked for.",
    "Polite replies are tested: 'Would you mind opening the door?' → '<b>Not at all</b>' (never 'Yes, I mind').",
    "'Thank you' → 'You're welcome' / 'Don't mention it'.  'Sorry to disturb you' → 'That's all right'.",
    "A rising tune invites an answer (yes/no questions); a falling tune closes a statement, a command or a "
    "wh-question.",
    "Listen for the KEY word in a question: who, when, where, why, how many.",
])
O("Choose the most appropriate response: 'Would you mind closing the window?'",
  ["Not at all.", "Yes, I mind.", "Of course I would mind.", "No, thank you."],
  ["'Would you mind…?' is a polite request.", "'Not at all' means 'I am happy to do it'."])
O("Choose the most appropriate response: 'I'm sorry I stepped on your foot.'",
  ["That's all right.", "You are welcome to it.", "Not at all costs.", "Please do."],
  ["An apology is answered by accepting it: 'That's all right' or 'Don't worry about it'."])
O("Your friend says, 'Congratulations on your result!' The best reply is ___",
  ["Thank you very much.", "It is nothing serious.", "Don't mention it.", "You are welcome."],
  ["Congratulations are answered with thanks.",
   "'Don't mention it' and 'You're welcome' are replies to <i>thank you</i>, not to congratulations."])
O("Which sentence would normally be said with a FALLING tune?",
  ["Please close the door.", "Are you coming?", "Is that your book?", "Did he call you?"],
  ["Commands, statements and wh-questions fall at the end; yes/no questions rise."])
O("In a listening passage you are asked: 'How many people attended the meeting?' You should listen for ___",
  ["a number", "the speaker's name", "the place of the meeting", "the reason for the meeting"],
  ["Match your listening to the question word: <i>how many</i> ⇒ a number; <i>where</i> ⇒ a place; "
   "<i>why</i> ⇒ a reason."])
T("(a) Give a suitable spoken response to each: (i) 'May I use your pen?' (ii) 'Thank you for your help.' "
  "(iii) 'How do you do?' (iv) 'Would you like some water?' (v) 'Excuse me, is this seat taken?'<br>"
  "(b) State two things you should do before the listening test begins, and two while it is going on.",
  ["(a)(i) <b>Certainly / Please do.</b>  (ii) <b>You're welcome / Don't mention it.</b>  "
   "(iii) <b>How do you do?</b> (it is a greeting, not a real question).  (iv) <b>Yes, please / No, thank you.</b>  "
   "(v) <b>No, it's free — please sit down.</b>",
   "(b) <b>Before:</b> read the questions and the options quickly so you know what to listen for; "
   "settle down and shut out noise.",
   "<b>During:</b> listen for the key word in each question and mark your answer at once; "
   "if you miss one, leave it and move on rather than losing the next question too."], marks=10)
extras("listen",
  plain="The orals paper is about sound and about everyday spoken English. Half the marks come from knowing "
        "the natural reply to a polite expression — the kind of English you already speak, written down.",
  examples=[
    E("Why is 'Yes, I mind' wrong as a reply to 'Would you mind helping me?'",
      "Step 1. 'Would you mind…?' literally asks whether the request troubles you.",
      "Step 2. If you are willing, you must say that it does NOT trouble you: 'Not at all' or "
      "'Of course not' or 'Certainly'.",
      "Step 3. 'Yes, I mind' means you refuse — and it sounds rude, which is why it is never the key."),
    E("How to handle a listening passage you only partly hear.",
      "Step 1. Do not panic or stop — the next question is already on its way.",
      "Step 2. Answer from what you did hear; the questions usually follow the order of the passage.",
      "Step 3. Mark the one you missed and return to it at the end rather than losing two or three more.")])
