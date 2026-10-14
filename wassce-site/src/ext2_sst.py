from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}

S = "The Environment"

# ------------------------------------------------------------ self-identity
topic("identity", "Self-identity & personal development", S, [
    "Self-identity is knowing who you are: your name, family, ethnic group, nationality, abilities, values and goals.",
    "Self-concept is how you see yourself; self-esteem is how much you value yourself.",
    "What shapes identity: family, culture and language, religion, school, peers, the media and personal experience.",
    "Self-esteem is built by achievement, honest praise, good role models and keeping promises to yourself.",
    "Life skills that build the person: goal setting, time management, self-discipline, assertiveness and "
    "the ability to say no.",
])
O("Self-identity can best be described as ___",
  ["a person's sense of who he or she is", "the amount of money a person has",
   "the number of friends a person keeps", "the school a person attends"],
  ["Identity covers name, family, culture, nationality, abilities, beliefs and goals — the whole sense of self."])
O("Which of these is MOST likely to build a student's self-esteem?",
  ["Achieving a goal he set and worked for", "Being compared with other students",
   "Copying the lifestyle of a celebrity", "Being praised for work he did not do"],
  ["Real achievement, earned by effort, is what makes self-esteem solid.",
   "False praise collapses the first time the person is tested."])
O("A student who always follows his friends even when he knows they are wrong lacks ___",
  ["assertiveness", "intelligence", "friends", "energy"],
  ["Assertiveness is the ability to state your own position politely and firmly, including saying no."])
O("Which of these BEST shows self-discipline in a student?",
  ["Keeping to a study timetable without being supervised", "Studying only when the teacher is around",
   "Reading all night before an examination", "Copying notes from a friend"],
  ["Self-discipline is doing what you planned when nobody is watching or forcing you."])
O("Which factor contributes LEAST to a person's identity?",
  ["The colour of his school bag", "His family and upbringing", "His culture and language", "His religion"],
  ["Family, culture, language and religion all shape who a person is; a possession does not."])
T("(a) Explain the terms self-concept and self-esteem.<br>"
  "(b) State four factors that shape a young person's identity.<br>"
  "(c) Explain four ways a student can develop a strong, positive personality.",
  ["(a) <b>Self-concept</b> is the picture a person has of himself — his abilities, appearance and place in "
   "society. <b>Self-esteem</b> is the value he puts on that picture: how much he respects and accepts himself.",
   "(b) The family and upbringing; culture, language and ethnic background; religion and moral teaching; "
   "the school, teachers and peers; the media and personal experiences of success or failure.",
   "(c) 1. <b>Set clear goals</b> and work towards them, so that confidence rests on real achievement.",
   "2. <b>Keep good company</b> — friends who study, work and respect others.",
   "3. <b>Learn to say no</b> politely but firmly to what will harm your future.",
   "4. <b>Accept correction and learn from failure</b> instead of giving up, and take part in clubs, sports "
   "and community service to discover your abilities."], marks=20)
extras("identity",
  plain="Your identity is the answer to 'who am I?' — family, culture, beliefs, abilities and goals. "
        "Self-esteem is how much you value that person. Both are built, not born.",
  examples=[
    E("A student is teased for speaking his local language at school and starts to feel ashamed of it. "
      "Advise him.",
      "Step 1. Language is part of identity, not a weakness — being fluent in two or more languages is an asset.",
      "Step 2. Explain that confident people are respected; shame comes from accepting other people's judgement.",
      "Step 3. Encourage him to speak both languages well, and to join clubs where his culture is valued.",
      "Step 4. Advise the school to discourage teasing, since it damages self-esteem and learning."),
    E("Write one essay point on how self-discipline helps a student.",
      "Point: Self-discipline turns good intentions into results.",
      "Explain: Every student wants to pass, but only the one who keeps to a timetable, sleeps and wakes early "
      "and resists distractions actually covers the syllabus.",
      "Example: A student who studies two hours daily from the first week needs no all-night cramming "
      "before WASSCE, and sits the paper rested.")])

# ------------------------------------------------------------ gender
topic("gender", "Gender roles & equality", S, [
    "Sex is biological (male or female); gender is the roles society gives to men and women, which can change.",
    "Traditional roles: men as providers and heads; women as home-keepers — but both now work, earn and lead.",
    "Gender equality means equal rights, opportunities and treatment, not that men and women are the same.",
    "Barriers for girls: early marriage, teenage pregnancy, household chores that cut study time, "
    "and the belief that some careers are 'for boys'.",
    "Ghana supports equality through free and compulsory basic education, scholarships for girls in science, "
    "laws against early and forced marriage, and affirmative action in appointments.",
])
O("Which of the following is determined by SEX rather than by gender?",
  ["The ability to bear children", "Cooking for the family",
   "Being the head of a household", "Working as a nurse"],
  ["Sex is biological and does not change; the others are roles that society assigns and that change with time."])
O("Gender equality means that men and women should ___",
  ["have equal rights and opportunities", "do exactly the same work everywhere",
   "earn the same amount whatever the job", "live apart from each other"],
  ["Equality is about equal access and fair treatment, not about erasing all differences."])
O("Which practice MOST limits girls' education in some communities?",
  ["Early and forced marriage", "Free school uniforms", "Science scholarships for girls", "School feeding"],
  ["Early marriage takes girls out of school permanently; the other three keep them in school."])
O("A family has limited money and chooses to educate only the boy. This decision is an example of ___",
  ["gender discrimination", "sound financial planning", "cultural preservation", "fair sharing"],
  ["Choosing by sex rather than by ability or need denies the girl an equal opportunity."])
O("Which of these would best promote gender equality in a school?",
  ["Giving girls and boys equal chance to lead and to study every subject",
   "Reserving science for boys only", "Asking girls to sweep while boys read",
   "Choosing only boys as prefects"],
  ["Equal access to leadership, subjects and duties is what equality looks like in practice."])
T("(a) Distinguish between sex and gender.<br>(b) State four effects of gender inequality on national development.<br>"
  "(c) Suggest four ways of promoting gender equality in Ghana.",
  ["(a) <b>Sex</b> is the biological difference between male and female, fixed at birth and the same "
   "everywhere. <b>Gender</b> is the set of roles, duties and expectations a society gives to men and women; "
   "it is learnt and it differs from place to place and changes with time.",
   "(b) 1. The country loses the talent of half its population when girls drop out or are kept from "
   "certain careers.",
   "2. Household incomes stay low, since educated women earn more and invest in their children.",
   "3. Child health and literacy suffer, because a mother's education strongly affects her children.",
   "4. Fewer women in decision-making means policies that overlook the needs of women and children.",
   "(c) Keep girls in school with scholarships, sanitary provision and safe transport; enforce the laws "
   "against early and forced marriage and against sexual harassment; share household chores so that girls "
   "have study time; promote women into leadership and encourage girls into science and technical courses; "
   "educate communities to drop practices that hold women back."], marks=20)
extras("gender",
  plain="Sex is what you are born with; gender is what society expects of you because of it. Gender roles "
        "change with time — which is why women today are doctors, soldiers and district chief executives.",
  examples=[
    E("Sort these into SEX or GENDER: bearing children, cooking, breastfeeding, driving a tractor, "
      "growing a beard, heading a household.",
      "<b>Sex (biological):</b> bearing children, breastfeeding, growing a beard.",
      "<b>Gender (social):</b> cooking, driving a tractor, heading a household.",
      "Test: if it can change with society or training, it is gender."),
    E("Write one essay point on the benefits of educating girls.",
      "Point: Educating girls lifts the whole community, not just the girl.",
      "Explain: An educated woman earns more, marries later, has fewer and healthier children, and is far "
      "more likely to send all of them to school.",
      "Example: Communities where girls complete SHS record lower infant deaths and higher household incomes "
      "within a generation.")])

S = "Governance, Politics & Stability"

# ------------------------------------------------------------ chieftaincy
topic("chief", "Chieftaincy & traditional authority", S, [
    "A chief is a person who hails from the appropriate family and lineage, has been validly nominated, "
    "elected or selected, and enstooled or enskinned in accordance with customary law.",
    "The institution of chieftaincy, with its traditional councils, is guaranteed by the 1992 Constitution.",
    "Structure: the National House of Chiefs, Regional Houses of Chiefs, traditional councils, "
    "paramount chiefs, divisional and sub-chiefs, with the queen mother and the kingmakers.",
    "Functions: custodian of the land and of custom, settling disputes, mobilising for development, "
    "preserving festivals and culture, and linking the people with central government.",
    "Chiefs may not take part in active party politics.",
    "Chieftaincy disputes are heard by the judicial committees of the Houses of Chiefs.",
])
O("The body that deals with chieftaincy matters at the national level is the ___",
  ["National House of Chiefs", "Council of State", "Electoral Commission", "National Peace Council"],
  ["The National House of Chiefs, with its judicial committee, handles chieftaincy matters and advises "
   "on customary law."])
O("Which of these is a function of a chief in Ghana today?",
  ["Mobilising his people for development projects", "Printing the national currency",
   "Appointing the Chief Justice", "Conducting national elections"],
  ["Chiefs mobilise communal labour and funds, settle disputes, hold land in trust and preserve custom."])
O("A chief is NOT allowed to ___",
  ["take part in active party politics", "settle land disputes in his area",
   "sit in the Regional House of Chiefs", "lead his people at a festival"],
  ["The Constitution bars chiefs from active party politics so that the institution remains above partisan "
   "division."])
O("The person who plays a key role in the selection and installation of a chief in many Akan communities is the ___",
  ["queen mother", "district chief executive", "regional minister", "assembly member"],
  ["The queen mother, with the kingmakers, nominates a candidate from the royal family."])
O("Land in many Ghanaian communities is said to be held by the chief ___",
  ["in trust for the people", "as his personal property",
   "on behalf of the central government", "for sale to the highest bidder"],
  ["Stool and skin lands are held in trust: the chief administers them for the benefit of the community, "
   "and the revenue is shared as the law provides."])
T("(a) Who is a chief?<br>(b) State four functions of chiefs in Ghana today.<br>"
  "(c) Explain three causes of chieftaincy disputes and two ways of resolving them.",
  ["(a) A chief is a person who, hailing from the appropriate family and lineage, has been validly nominated, "
   "elected or selected and enstooled, enskinned or installed as a chief in accordance with the relevant "
   "customary law and usage.",
   "(b) 1. <b>Custodian of the land and of custom</b> — holds stool or skin land in trust and upholds tradition.",
   "2. <b>Settlement of disputes</b> — hears family, land and community cases, easing the pressure on the courts.",
   "3. <b>Mobilisation for development</b> — organises communal labour, raises funds at festivals and "
   "attracts projects to the area.",
   "4. <b>Preservation of culture</b> — leads festivals, rites and the use of the language, and links the "
   "people with government and investors.",
   "(c) <b>Causes:</b> rival claims between royal gates or families; unclear or disputed customary procedure "
   "in nomination and installation; interference by politicians and by people who want the stool lands; "
   "money from land sales.",
   "<b>Resolution:</b> mediation and negotiation by elders, the queen mother and respected persons; "
   "reference to the judicial committee of the Regional or National House of Chiefs, whose decision is "
   "binding; clear documentation of customary lines of succession to prevent future disputes."], marks=20)
extras("chief",
  plain="Chieftaincy is Ghana's traditional system of leadership, recognised by the Constitution. A chief is "
        "not elected by ballot — he is chosen by the royal family and kingmakers and installed by custom.",
  examples=[
    E("A paramount chief is asked to campaign for a political party. What should he do, and why?",
      "Step 1. He should decline.",
      "Step 2. The Constitution bars chiefs from active party politics.",
      "Step 3. The reason is practical as well as legal: a chief belongs to all his people, and taking sides "
      "would divide the town and weaken his authority to settle disputes.",
      fig=draw.tree("Chieftaincy structure", ["National House of Chiefs", "Regional Houses", "Traditional Councils"],
                    sub=["national level", "regional level", "paramountcy level"],
                    label="Structure of chieftaincy")),
    E("Write one essay point on the role of chiefs in development.",
      "Point: Chiefs mobilise their communities for development.",
      "Explain: A chief can call the town together, organise communal labour and release stool land for "
      "projects far more quickly than any office can.",
      "Example: Many community schools, clinics and boreholes stand on land released by a chief, built partly "
      "with funds raised at the annual festival.")])

# ------------------------------------------------------------ human rights & vulnerable groups
topic("rights", "Human rights & the vulnerable", S, [
    "Human rights belong to every person simply because they are human; they are set out in Chapter Five "
    "of the 1992 Constitution.",
    "Rights of the child: a name and nationality, education, health care, protection from abuse and hazardous "
    "labour, and a say in matters affecting them.",
    "Vulnerable groups: children, women, persons with disability, the aged, the very poor and refugees.",
    "The Persons with Disability Act requires access to public buildings, transport, education and employment.",
    "Protective bodies: CHRAJ, the Domestic Violence and Victim Support Unit (DOVVSU) of the police, "
    "the Department of Social Welfare, and the courts.",
    "Rights carry responsibilities, and may be limited by law in the interest of public safety and the "
    "rights of others.",
])
O("Which of these is a right of every child in Ghana?",
  ["The right to basic education", "The right to drive a vehicle",
   "The right to vote in national elections", "The right to work full time in a mine"],
  ["Basic education is a right; voting and driving come with age, and hazardous child labour is forbidden."])
O("A public office building has no ramp, so a man in a wheelchair cannot enter. This breaches ___",
  ["the rights of persons with disability", "the law on public holidays",
   "the building's insurance policy", "no right at all"],
  ["The Persons with Disability Act requires public buildings and transport to be accessible."])
O("The police unit that handles cases of domestic violence and abuse is ___",
  ["DOVVSU", "MTTD", "the Fire Service", "the Immigration Service"],
  ["The Domestic Violence and Victim Support Unit handles abuse, defilement and family violence cases."])
O("Which body investigates complaints of human rights abuse by public officials?",
  ["CHRAJ", "The Electoral Commission", "The National Lottery Authority", "The Ghana Standards Authority"],
  ["The Commission on Human Rights and Administrative Justice investigates abuses of rights and of office."])
O("A girl of 15 is withdrawn from school to be married. Which of her rights is being denied?",
  ["The right to education", "The right to property", "The right to vote", "The right to trade"],
  ["Early marriage denies the right to education and to protection from harmful practices; "
   "marriage under 18 is unlawful in Ghana."])
T("(a) What are human rights?<br>(b) State four rights of the child and the duty that goes with each.<br>"
  "(c) Explain four ways society can protect vulnerable groups.",
  ["(a) Human rights are the basic entitlements that belong to every person from birth, simply because "
   "they are human — regardless of sex, ethnic group, religion, status or ability. In Ghana they are "
   "guaranteed in Chapter Five of the 1992 Constitution.",
   "(b) <b>Education</b> — the child must attend school and work hard. "
   "<b>Health care</b> — the child should follow medical advice and keep clean habits. "
   "<b>Protection from abuse and hazardous work</b> — the child should report abuse and avoid dangerous places. "
   "<b>A name, nationality and parental care</b> — the child should respect parents and obey reasonable rules.",
   "(c) 1. <b>Enforce the laws</b> — the Children's Act, the Domestic Violence Act and the Persons with "
   "Disability Act, through DOVVSU, CHRAJ and the courts.",
   "2. <b>Provide services</b> — free basic education, school feeding, health insurance exemptions, "
   "ramps and accessible transport, and support grants for the very poor and the aged.",
   "3. <b>Educate the public</b> through schools, radio and durbars, so that abuse and discrimination are "
   "reported rather than hidden.",
   "4. <b>Support families</b> with livelihood programmes, since poverty is behind much child labour, "
   "early marriage and neglect."], marks=20)
extras("rights",
  plain="Human rights are the things every person is entitled to simply for being human — life, dignity, "
        "education, a fair hearing. The test of a society is how it treats those least able to defend "
        "themselves: children, the aged and persons with disability.",
  examples=[
    E("A 13-year-old is working full time in a quarry instead of attending school. "
      "List the rights denied and say who should act.",
      "Step 1. Rights denied: education; protection from hazardous child labour; health and development; rest "
      "and play.",
      "Step 2. Who acts: the parents first; then the Department of Social Welfare and the district assembly's "
      "child protection committee; DOVVSU where there is abuse; the employer can be prosecuted.",
      "Step 3. The lasting remedy is support for the family's income, so that the child's labour is not "
      "needed to eat."),
    E("Match each right with the duty it carries.",
      "Right to free expression ⇄ duty not to insult, defame or incite others.",
      "Right to a clean environment ⇄ duty to dispose of your own waste properly.",
      "Right to education ⇄ duty to attend, learn and respect school rules.",
      "Right to vote ⇄ duty to register, vote peacefully and accept the result.",
      fig=draw.flow(["A right", "carries", "a duty", "for everyone"],
                    note="Rights and duties go together", label="Rights carry duties"))])

S = "Social & Economic Development"

# ------------------------------------------------------------ religion & morality
topic("religion", "Religion, morality & development", S, [
    "The three main religions in Ghana are Christianity, Islam and African Traditional Religion.",
    "Morality is the set of standards by which a society judges right and wrong; religion is one of its main sources.",
    "Shared moral values: honesty, hard work, respect for life and property, truthfulness, kindness and justice.",
    "Religious bodies build schools, clinics and vocational centres, support the poor, and mediate in conflicts.",
    "Religious tolerance means respecting the beliefs and worship of others; Ghana's peace rests partly on it.",
    "Negative effects to avoid: religious extremism and intolerance, fraudulent 'men of God', and practices "
    "that discourage work, education or medical care.",
])
O("Which of these is a shared moral value of all the main religions in Ghana?",
  ["Honesty", "Fasting in Ramadan", "Pouring of libation", "Baptism"],
  ["Honesty is taught by all of them; the other three are particular practices of one religion."])
O("Religious bodies in Ghana contribute MOST to development by ___",
  ["building and running schools and clinics", "collecting taxes",
   "conducting national elections", "printing the currency"],
  ["Mission schools, hospitals and vocational centres educate and treat a large share of Ghanaians."])
O("Religious tolerance means ___",
  ["respecting the beliefs and worship of others", "belonging to every religion at once",
   "abandoning your own faith", "worshipping only in public"],
  ["Tolerance is respect for the right of others to believe differently, while keeping your own faith."])
O("A preacher tells sick members not to take medicine. This is an example of ___",
  ["a harmful religious practice", "sound medical advice",
   "religious tolerance", "moral uprightness"],
  ["Beliefs that keep people from treatment cost lives; religion and medical care are not in competition."])
O("Which institution is the FIRST to teach a child right from wrong?",
  ["The family", "The church or mosque", "The school", "The district assembly"],
  ["The family is the first agent of socialisation; religious bodies and schools build on what it starts."])
T("(a) Name the three main religions in Ghana and state two moral values each teaches.<br>"
  "(b) Explain four ways religious bodies contribute to national development.<br>"
  "(c) State three ways of promoting religious tolerance in a multi-religious country.",
  ["(a) <b>Christianity</b> — love for one's neighbour, honesty, forgiveness. "
   "<b>Islam</b> — charity (zakat), truthfulness, respect for parents and the needy. "
   "<b>African Traditional Religion</b> — respect for elders and the land, communal responsibility, "
   "truthfulness and hard work.",
   "(b) 1. <b>Education</b> — mission and Islamic schools educate a large share of Ghanaian children.",
   "2. <b>Health</b> — church and mosque clinics and hospitals serve rural communities.",
   "3. <b>Moral formation</b> — teaching honesty, hard work and respect, which reduces crime and corruption.",
   "4. <b>Welfare and peace</b> — supporting orphans, the aged and the poor, and mediating in national "
   "and community conflicts.",
   "(c) Teach about one another's beliefs in schools; observe and respect the major festivals of all faiths; "
   "include all faiths in national occasions and in peace councils; avoid insulting other people's worship "
   "in speech, music and on social media; punish incitement on religious grounds."], marks=20)
extras("religion",
  plain="Religion teaches people what is right and wrong, and in Ghana it also builds schools and clinics. "
        "Because the country holds several faiths side by side, tolerance is what keeps the peace.",
  examples=[
    E("A school has Christian, Muslim and traditionalist students. Suggest how it can be fair to all.",
      "Step 1. Allow time and a place for each group's worship, and respect fasting and prayer times.",
      "Step 2. Make no student take part in another faith's rites against conscience.",
      "Step 3. Mark the major festivals of all faiths in the school calendar, and teach about each of them.",
      "Step 4. Punish mockery of any faith, as you would punish any other form of bullying."),
    E("Write one essay point on religion and national development.",
      "Point: Religious bodies supply social services the state alone cannot provide.",
      "Explain: Churches and Islamic organisations run schools, training centres and hospitals, "
      "often in rural areas where government presence is thin.",
      "Example: Many of Ghana's oldest senior high schools and mission hospitals were founded and are "
      "still partly run by religious bodies.")])
