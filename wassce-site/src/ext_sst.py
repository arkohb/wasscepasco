from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}

PEE = draw.flow(["State the point", "Explain it", "Give an example", "Link to the question"],
                note="How one essay paragraph should be built", label="Point, explain, example")

extras("envcomp",
  plain="Your environment is everything around you. The PHYSICAL part is what nature provides — land, water, "
        "air, plants and animals. The SOCIAL part is people and what people have made — family, school, "
        "chieftaincy, laws and customs.",
  examples=[
    E("Write one full essay paragraph on how people depend on the physical environment.",
      "Step 1 (point). People depend on the physical environment for food.",
      "Step 2 (explain). The soil supports crops, the rivers and the sea supply fish, and grassland feeds livestock, "
      "so almost everything we eat comes from the natural surroundings.",
      "Step 3 (example). In Ghana, cocoa from the forest belt and fish from the coast feed families and earn income.",
      "That is the pattern every essay point should follow: state, explain, example.",
      fig=PEE),
    E("Classify these as physical or social environment: river, chieftaincy, harmattan, school, forest, marriage.",
      "Physical (made by nature): <b>river, harmattan, forest</b>.",
      "Social (made by people): <b>chieftaincy, school, marriage</b>.",
      "Quick test: ask 'would it still be there if no people lived here?'")])

extras("degrad",
  plain="Degradation means the environment becoming poorer — soil washed away, forests cleared, rivers muddied. "
        "Most of it is caused by people, so most of it can be stopped by people.",
  examples=[
    E("A community's river has turned brown and the fish have died. Trace the cause and suggest solutions.",
      "Step 1. Brown water means silt, usually from mining pits or farming right up to the bank.",
      "Step 2. Effects: unsafe drinking water, higher treatment costs, loss of fishing income, sick people.",
      "Step 3. Solutions: stop mining in and near the river, restore the pits, plant trees along the banks, "
      "and enforce the law through the district assembly and the EPA."),
    E("Explain the difference between afforestation and reafforestation.",
      "<b>Afforestation</b> — planting trees on land that has never carried forest, such as bare savanna land.",
      "<b>Reafforestation</b> — replanting where forest has been cut down, such as a logged forest reserve.",
      "Both increase tree cover; only the starting point is different.")])

extras("popn",
  plain="Population study is about how many people there are, where they live, and how fast the number is "
        "changing. Numbers grow through births and immigration, and fall through deaths and emigration.",
  examples=[
    E("A district has 90,000 people living in 450 km². Find the population density and say what it means.",
      "Step 1. Density = population ÷ land area.",
      "Step 2. = 90,000 ÷ 450 = <b>200 persons per km²</b>.",
      "Step 3. It tells us how crowded the district is, which helps in planning schools, clinics and water supply."),
    E("Write one essay point on the effect of rapid population growth on social amenities.",
      "Point: Rapid population growth puts heavy pressure on social amenities.",
      "Explain: Schools, clinics, water and housing are built for a certain number of people; when the "
      "population grows faster than the facilities, each one serves far more people than it was meant to.",
      "Example: In Accra, classrooms meant for 40 pupils now take 70, and pipes built for a smaller city "
      "cannot reach every home daily.",
      fig=draw.barfig([("1984", 12), ("2000", 19), ("2010", 24), ("2021", 31)],
                      label="Ghana's recorded population in millions at successive censuses", ylab="millions"))])
assert 90000 / 450 == 200

extras("sanit",
  plain="Sanitation means keeping our surroundings clean — safe water, proper toilets and proper rubbish "
        "disposal. Where sanitation fails, disease follows within days.",
  examples=[
    E("Cholera breaks out in a town every rainy season. Explain why, and what should be done.",
      "Step 1. Refuse blocks the gutters, so rain water floods and mixes with sewage.",
      "Step 2. The dirty water reaches wells, food and hands, and cholera bacteria spread quickly.",
      "Step 3. Remedies: regular refuse collection and household bins; desilt gutters before the rains; "
      "build and use toilets; treat drinking water; educate and enforce sanitation by-laws."),
    E("State four ways a student can help keep the school environment clean.",
      "1. Use the bins and never drop sachets or paper on the compound.",
      "2. Take part in weekly clean-up and keep the toilets and urinals clean.",
      "3. Keep gutters around the school clear so that they do not breed mosquitoes.",
      "4. Join the environment club and teach others by example.")])

extras("disaster",
  plain="A disaster is a sudden event that causes great damage. Some are natural (floods, earthquakes); many "
        "are man-made (fires, road crashes). Preparing before it happens saves the most lives.",
  examples=[
    E("Flooding destroys homes in the same neighbourhood every year. Explain the causes and the solutions.",
      "Step 1. Causes: houses built on waterways, choked drains, poor town planning, and heavy rain "
      "on ground that cannot absorb water.",
      "Step 2. Short-term: early warning from the Meteorological Agency and NADMO, and evacuation plans.",
      "Step 3. Long-term: demolish structures on waterways, enlarge and desilt drains, enforce building "
      "permits and stop dumping refuse in gutters."),
    E("Distinguish between natural and man-made disasters, with two examples of each.",
      "<b>Natural:</b> caused by nature — floods, earthquakes, droughts, rainstorms.",
      "<b>Man-made:</b> caused by human action or carelessness — market fires, road accidents, "
      "building collapse, chemical spills.",
      "Note that human action often makes a natural disaster worse, as when refuse in drains worsens a flood.")])

extras("culture",
  plain="Culture is the whole way of life of a people: language, food, dress, music, beliefs, customs and the "
        "things they make. You cannot inherit culture in your blood — you learn it.",
  examples=[
    E("Explain, with examples, why we say culture is dynamic.",
      "Step 1 (point). Culture is dynamic — it changes with time.",
      "Step 2 (explain). Contact with other peoples, education, religion and technology bring in new ways, "
      "while some old practices fall away.",
      "Step 3 (example). Kente is now sewn into modern styles and worn at graduations, and funerals are "
      "announced on social media instead of by drum. The culture is alive, but it has changed."),
    E("Name two positive and two harmful cultural practices in Ghana.",
      "<b>Positive:</b> respect for elders; communal labour; naming ceremonies and festivals that unite "
      "the community and raise funds for development.",
      "<b>Harmful:</b> female genital mutilation; trokosi; widowhood rites that humiliate women; "
      "accusing old women of witchcraft.",
      "In an essay, always say WHY a practice is harmful — the health, education or rights it damages.")])

extras("social",
  plain="Socialisation is how a person learns the ways of their society: what is right, what is rude, how to "
        "speak and behave. It starts in the family and continues all through life.",
  examples=[
    E("Explain how the school socialises a student, in essay form.",
      "Point: The school is a major agent of socialisation.",
      "Explain: Beyond books, it teaches punctuality, obedience to rules, co-operation, respect for other "
      "ethnic groups and the habit of working with others.",
      "Example: A day starts with assembly and the national pledge, students of many backgrounds share a "
      "dormitory and a class, and prefects learn leadership.",
      fig=draw.tree("Agents of socialisation", ["Family — first values", "School — rules and skills",
                                                "Peers & media — habits"], label="Agents of socialisation")),
    E("Give two positive and two negative effects of the peer group.",
      "<b>Positive:</b> study groups that improve grades; sports and clubs that build confidence and discipline.",
      "<b>Negative:</b> pressure into truancy, drugs or crime; wasting time and money to 'belong'.",
      "The peer group is neither good nor bad in itself — it depends on the company chosen.")])

extras("adol",
  plain="Adolescence is the bridge between childhood and adulthood. The body changes fast, feelings swing, "
        "and friends matter more — which is why good decision-making matters most at this stage.",
  examples=[
    E("A Form Two student is being pressured by friends to attend a night party. Apply the steps of "
      "responsible decision-making.",
      "Step 1. State the problem clearly: go to the party, or stay and prepare for tomorrow's test.",
      "Step 2. Get the facts: the party ends at 2 a.m., the test is at 8 a.m., and the route home is unsafe.",
      "Step 3. Weigh the consequences, short and long term: a few hours of fun against a poor grade, "
      "punishment, and possible danger.",
      "Step 4. Check it against your goals and values, seek advice from a parent or teacher, then decide "
      "and accept responsibility for the decision.",
      fig=draw.flow(["Name the problem", "Get the facts", "Weigh consequences", "Decide and act"],
                    note="Responsible decision-making", label="Decision-making steps")),
    E("Write one essay point on the benefits of adolescent chastity.",
      "Point: Chastity protects a young person's education.",
      "Explain: Abstaining removes the risk of teenage pregnancy, which is the commonest reason girls drop "
      "out of school, and it removes the risk of sexually transmitted infection.",
      "Example: A student who stays focused completes SHS and enters training or work, while a classmate "
      "who becomes pregnant may lose two or more years of schooling.")])

extras("family",
  plain="The family is the smallest unit of society and the first school of every child. It produces and "
        "raises children, provides for them, and gives them identity and a sense of belonging.",
  examples=[
    E("Distinguish between the nuclear and the extended family, and state one advantage of each.",
      "<b>Nuclear:</b> father, mother and their children. Advantage: fewer people to cater for, so resources "
      "go further and decisions are quick.",
      "<b>Extended:</b> adds grandparents, uncles, aunts and cousins. Advantage: help in times of need — "
      "school fees, funerals, child care and advice.",
      fig=draw.tree("Family", ["Nuclear: parents + children", "Extended: adds relatives"],
                    label="Types of family")),
    E("A couple keep quarrelling over money. Suggest practical ways to make the marriage stable.",
      "Step 1. Agree a joint budget and discuss income and spending openly.",
      "Step 2. Plan the size of the family, so the children can be catered for.",
      "Step 3. Keep relatives from interfering in decisions that belong to the couple.",
      "Step 4. Where it is beyond them, seek counselling from a respected person, religious body or counsellor.")])

extras("educ",
  plain="Education is the passing on of knowledge, skills and values. Formal education happens in school "
        "with a syllabus; informal education happens at home and in the community, all through life.",
  examples=[
    E("Write one essay point on how education promotes national development.",
      "Point: Education supplies the skilled manpower a country needs.",
      "Explain: Doctors, teachers, engineers, technicians and entrepreneurs all come through the school "
      "system, and their skills raise productivity in every sector.",
      "Example: Training more TVET graduates means more welders, electricians and tailors who employ "
      "themselves and others rather than waiting for office jobs."),
    E("State two problems of education in rural Ghana and a solution to each.",
      "Problem 1: Shortage of trained teachers, because postings to remote areas are unattractive. "
      "Solution: provide accommodation and rural allowances.",
      "Problem 2: Children walk long distances and drop out. "
      "Solution: build more community schools and support with feeding and scholarships.")])

extras("nation",
  plain="A nation is a people who feel they belong together; a state is a country with land, people, a "
        "government and sovereignty. Nation building is the work of making citizens feel and act as one.",
  examples=[
    E("Explain the colours of the national flag and what they should mean to a student.",
      "Step 1. <b>Red</b> — the blood of those who died in the struggle for independence.",
      "Step 2. <b>Gold</b> — the mineral wealth of the country.",
      "Step 3. <b>Green</b> — the forests and farmlands.",
      "Step 4. <b>Black star</b> — African freedom and Ghana's lead in it.",
      "For a student, the flag is a reminder to protect what was won and to use the country's wealth honestly."),
    E("Write one essay point on how the youth can contribute to nation building.",
      "Point: The youth build the nation by acquiring employable skills.",
      "Explain: A skilled young person creates goods and services, employs others, and pays taxes, "
      "instead of depending on the state.",
      "Example: A graduate who starts a small poultry farm feeds the community, employs two workers "
      "and reduces imports of chicken.")])

extras("constit",
  plain="A constitution is the rule book of a country. It says how power is shared, what leaders may and may "
        "not do, and what rights every citizen has. Ghana's present one began the Fourth Republic in 1993.",
  examples=[
    E("Explain the rule of law to someone who has never heard the term.",
      "Step 1. It means the law is above everybody — the President, ministers, chiefs and ordinary citizens alike.",
      "Step 2. No one may be punished except for breaking a law that already exists, and only after a fair "
      "hearing in court.",
      "Step 3. Example: a minister who takes public money is tried in the same courts as any other citizen. "
      "Where that happens, we say the rule of law is working."),
    E("Why does a constitution divide power between three arms of government?",
      "Step 1. If one person or body made the laws, enforced them and judged disputes, power would be abused.",
      "Step 2. Separation of powers gives each arm its own work and lets each check the others.",
      "Step 3. Example: Parliament approves the budget and vets ministers, while the courts can declare "
      "an act of government unconstitutional.")])

extras("citizen",
  plain="A citizen is a full member of a country, with rights that the state must protect and duties that "
        "the citizen owes the state. Rights and duties always go together.",
  examples=[
    E("Match each right with the duty that makes it possible.",
      "Right to education ⇄ duty to pay taxes that build and staff the schools.",
      "Right to security ⇄ duty to report crime, serve on juries and obey the law.",
      "Right to a clean environment ⇄ duty to dispose of waste properly.",
      "Right to vote ⇄ duty to register, vote peacefully and accept the result."),
    E("A citizen is arrested and held for a week without being charged. What has been breached, and what "
      "can be done?",
      "Step 1. The Constitution guarantees personal liberty and requires that an arrested person be brought "
      "before a court within 48 hours.",
      "Step 2. Holding him for a week without charge breaches that right.",
      "Step 3. He (or a relative or lawyer) may apply to the courts, and may also complain to CHRAJ.")])

extras("democracy",
  plain="Democracy means the people rule, through leaders they choose and can remove. Government is divided "
        "into three arms so that no one person holds all the power.",
  examples=[
    E("Name the three arms of government and state the main work of each.",
      "<b>Executive</b> — the President, ministers and civil service; carries out laws and policies.",
      "<b>Legislature</b> — Parliament; makes laws, approves taxes and spending, and checks the Executive.",
      "<b>Judiciary</b> — the courts, headed by the Chief Justice; interprets the laws and settles disputes.",
      fig=draw.tree("Government", ["Executive", "Legislature", "Judiciary"],
                    sub=["carries out laws", "makes laws", "interprets laws"], label="Three arms of government")),
    E("How does Parliament check the Executive? Give four ways.",
      "1. It approves or rejects the national budget and any new tax.",
      "2. It vets and approves the President's ministerial nominees.",
      "3. Its committees summon ministers and examine the Auditor-General's reports.",
      "4. It must approve loans and international agreements before they take effect.")])

extras("elect",
  plain="An election is how citizens choose their leaders. Every citizen of 18 and above has one vote, and "
        "the Electoral Commission organises and supervises the whole process.",
  examples=[
    E("In a presidential election, candidate A gets 48% of valid votes, B gets 45% and C gets 7%. "
      "What happens next?",
      "Step 1. To win outright, a candidate needs MORE than 50% of the valid votes cast.",
      "Step 2. A has only 48%, so no one has won.",
      "Step 3. A second election (a run-off) is held between the two leading candidates, A and B."),
    E("Write one essay point on the effects of electoral malpractice.",
      "Point: Electoral malpractice destroys trust in the result.",
      "Explain: When votes are bought or ballots stuffed, the leader who emerges does not represent the "
      "people's real choice, and losers and their supporters feel cheated.",
      "Example: Disputed results have led to tension, court cases and even violence in parts of the "
      "sub-region, scaring away investors and costing the state money.")])

extras("local",
  plain="Decentralisation brings government nearer to the people. Instead of everything being decided in "
        "Accra, the district assembly plans and provides for its own area.",
  examples=[
    E("A community wants a clinic. Trace the steps through the local government system.",
      "Step 1. Raise it at the unit committee or town/area council meeting.",
      "Step 2. The assembly member takes it to the district assembly for inclusion in the development plan.",
      "Step 3. The assembly budgets for it, often using the District Assembly Common Fund, and awards the contract.",
      "Step 4. Citizens monitor the work, and the assembly member reports back to the community.",
      fig=draw.tree("District Assembly", ["Town / Area Council", "Unit Committee", "Assembly members"],
                    sub=["group of communities", "closest to the people", "elected by the people"],
                    label="Local government structure")),
    E("State two advantages and two problems of decentralisation.",
      "<b>Advantages:</b> local people decide their own priorities; services are delivered faster and "
      "projects are easier to monitor.",
      "<b>Problems:</b> inadequate and late funds; shortage of qualified staff in the districts; "
      "political interference and low citizen participation.")])

extras("leader",
  plain="Leadership is guiding others towards a goal; followership is supporting and co-operating while "
        "speaking the truth. A country needs both to be done well.",
  examples=[
    E("Describe four qualities you would look for in a school prefect, and why.",
      "1. <b>Honesty</b> — students and teachers can trust his reports and his handling of money.",
      "2. <b>Fairness</b> — he treats all students alike, whatever their background or friendship.",
      "3. <b>Good communication</b> — he explains decisions and carries the views of students to the staff.",
      "4. <b>Discipline and example</b> — he keeps the rules he enforces."),
    E("Explain the difference between autocratic and democratic leadership with a school example.",
      "<b>Autocratic:</b> the leader decides alone. A prefect who fixes the clean-up roster without asking "
      "anyone — quick, but members feel ignored.",
      "<b>Democratic:</b> the leader consults. He calls a short meeting, takes suggestions, then decides — "
      "slower, but members co-operate because the decision is partly theirs.")])

extras("conflict",
  plain="Conflict is disagreement — over land, chieftaincy, politics or resources. It is normal; what matters "
        "is settling it early and peacefully, before it turns violent.",
  examples=[
    E("Two families claim the same farmland and the matter is heating up. Describe the peaceful options.",
      "Step 1. <b>Dialogue</b> — the two families meet, with elders present, and state their claims.",
      "Step 2. <b>Mediation</b> — a neutral respected person or the Peace Council helps them reach their own "
      "agreement.",
      "Step 3. <b>Arbitration</b> — they agree in advance to accept the decision of a chosen panel.",
      "Step 4. <b>Adjudication</b> — if all else fails, the court or the judicial committee of the House of "
      "Chiefs decides, and the decision is binding.",
      fig=draw.flow(["Dialogue", "Mediation", "Arbitration", "Court"],
                    note="From the cheapest option to the last resort", label="Ways of resolving conflict")),
    E("Write one essay point on the effects of conflict on development.",
      "Point: Conflict drives away investment.",
      "Explain: Investors and skilled workers avoid places where property and lives are not safe, "
      "so factories and jobs go elsewhere.",
      "Example: In towns that have suffered long chieftaincy disputes, banks and businesses close, "
      "schools lose teachers, and the area falls behind its neighbours.")])

extras("corrupt",
  plain="Corruption is using public office for private gain — taking bribes, stealing public funds, or "
        "favouring relatives. It is not a victimless act: the money lost is a clinic not built.",
  examples=[
    E("A road contract for GH₵ 2 million is inflated to GH₵ 3 million and shared. Trace who suffers.",
      "Step 1. The state pays GH₵ 1 million more than the road is worth.",
      "Step 2. That million is money that could have built a CHPS compound or a six-unit classroom block.",
      "Step 3. The road is often poorly built too, because part of the money was taken out, so it fails early "
      "and must be repaired again.",
      "Step 4. Taxpayers pay twice, honest contractors lose work, and citizens lose trust in government."),
    E("Name four institutions that fight corruption in Ghana and what each does.",
      "<b>CHRAJ</b> — investigates abuse of office and human rights complaints.",
      "<b>Office of the Special Prosecutor</b> — investigates and prosecutes corruption-related offences.",
      "<b>EOCO</b> — handles economic and organised crime, including fraud.",
      "<b>Auditor-General</b> — audits public accounts and reports to Parliament, exposing misuse of funds.")])

extras("intl",
  plain="No country stands alone. Ghana belongs to groups such as the UN, the AU and ECOWAS, which bring "
        "trade, aid, security and a voice in world affairs — and bring obligations too.",
  examples=[
    E("A Ghanaian trader wants to sell goods in Lomé and Abidjan. How does ECOWAS membership help?",
      "Step 1. ECOWAS protocols allow free movement of people and goods within the sub-region.",
      "Step 2. She can travel without a visa for up to 90 days and face fewer customs barriers.",
      "Step 3. The larger regional market lets her buy and sell in greater quantity, which lowers her costs.",
      fig=draw.tree("Ghana's memberships", ["UN — peace, aid", "AU — African unity", "ECOWAS — regional trade"],
                    label="Organisations Ghana belongs to")),
    E("State four obligations Ghana owes an international organisation it joins.",
      "1. Pay its dues and contributions on time.",
      "2. Honour the treaties, protocols and decisions it has signed.",
      "3. Contribute troops, police or experts when called upon, as in peacekeeping.",
      "4. Respect the sovereignty of other members and settle disputes peacefully.")])

extras("economy",
  plain="The economy is how a country produces, shares and uses goods and services. It has three parts: "
        "getting raw materials, turning them into goods, and providing services.",
  examples=[
    E("Place these in the right sector: cocoa farming, soap making, banking, gold mining, teaching.",
      "<b>Primary</b> (from nature): cocoa farming, gold mining.",
      "<b>Secondary</b> (making things): soap making.",
      "<b>Tertiary</b> (services): banking, teaching.",
      fig=draw.tree("The economy", ["Primary — farming, mining", "Secondary — manufacturing",
                                    "Tertiary — services"], label="Three sectors of the economy")),
    E("Write one essay point on why exporting raw cocoa earns Ghana less than it should.",
      "Point: Exporting raw materials earns far less than exporting finished goods.",
      "Explain: The value is added when cocoa becomes butter, powder and chocolate, and that value is "
      "taken by the country that processes it.",
      "Example: A tonne of beans sells for a fraction of what the chocolate made from it earns abroad, "
      "so local processing would raise the country's income and create jobs here.")])

extras("money",
  plain="Money is anything generally accepted in exchange for goods and services. Banking keeps it safe, "
        "moves it about, and lends it to people who can use it productively.",
  examples=[
    E("A student earns GH₵ 600 a month from a holiday job. Draw up a simple monthly budget.",
      "Step 1. Write income at the top: GH₵ 600.",
      "Step 2. List planned spending: transport 120, food 180, phone 40, books 60 = GH₵ 400.",
      "Step 3. Savings first, not last: 600 − 400 = GH₵ 200 to the bank or susu.",
      "Step 4. Keep a record and check at month end whether you kept to the plan."),
    E("Why is saving in a bank better than keeping money at home?",
      "Step 1. It is safe from theft, fire and the temptation to spend.",
      "Step 2. It earns interest, so the amount grows.",
      "Step 3. It builds a record that supports a future loan for a business or further study.")])
assert 600 - (120 + 180 + 40 + 60) == 200

extras("entre",
  plain="An entrepreneur spots a need, organises people and money to meet it, and carries the risk. "
        "Ghana needs more job creators, not only job seekers.",
  examples=[
    E("A student wants to start a small printing business after school. Outline the business plan.",
      "Step 1. <b>The product:</b> printing, photocopying and binding for students and small offices.",
      "Step 2. <b>The market:</b> who will buy, how many, and who else is already doing it nearby.",
      "Step 3. <b>Capital:</b> cost of the machine, paper and rent; where the money comes from — savings, "
      "family, susu or a small loan.",
      "Step 4. <b>Running it:</b> location, price per page, records of sales and expenses, and expected profit.",
      fig=draw.flow(["Find a need", "Plan and cost it", "Raise capital", "Start and keep records"],
                    note="From idea to business", label="Starting a small business")),
    E("Why do many small businesses in Ghana fail within three years?",
      "1. Too little capital, and business money is mixed with personal money.",
      "2. No records, so the owner cannot tell profit from turnover.",
      "3. Poor location or no market research; strong competition from imports.",
      "4. High costs — rent, electricity and transport — and no plan for slow seasons.")])

extras("unemp",
  plain="Unemployment means people who can work and want to work cannot find jobs. It wastes the country's "
        "greatest resource — its people.",
  examples=[
    E("Identify the type of unemployment in each case.",
      "(a) A tailor with no customers between January and March — <b>seasonal</b>.",
      "(b) A graduate typist replaced by a computer system — <b>structural</b> (his skill is no longer needed).",
      "(c) A man who left one job last week and starts another next month — <b>frictional</b>.",
      "(d) Five people doing work that two could do on a family farm — <b>disguised</b>."),
    E("Write one essay point on solving youth unemployment.",
      "Point: Technical and vocational training reduces youth unemployment.",
      "Explain: It gives young people skills they can sell immediately — welding, tailoring, catering, "
      "electricals — so they can employ themselves rather than wait for an office job.",
      "Example: A young welder who completes training and receives a starter tool kit can earn from his "
      "first month and later employ apprentices.")])

extras("sci",
  plain="Technology is science put to work. It raises what a farmer or a factory can produce, and it has "
        "changed how we learn, pay and communicate.",
  examples=[
    E("Explain how mobile money has changed daily life in Ghana.",
      "Step 1. People far from any bank branch can now save, send and receive money on a simple phone.",
      "Step 2. Traders are paid instantly and carry less cash, which is safer.",
      "Step 3. Fees, school and utility bills are paid without travelling — saving time and transport money.",
      "Step 4. Risks remain: fraud and wrong transfers, so PINs must be kept private."),
    E("State two positive and two negative effects of technology on society.",
      "<b>Positive:</b> faster communication and access to information; better health care through modern "
      "equipment and medicines.",
      "<b>Negative:</b> workers replaced by machines; misuse of social media for fraud, rumours and "
      "cyberbullying; pollution from electronic waste.")])

extras("sustain",
  plain="Sustainable development means using what we have today without spoiling it for the children coming "
        "after us. Take the fruit, but do not cut down the tree.",
  examples=[
    E("A timber firm wants to log a forest reserve. What conditions would make it sustainable?",
      "Step 1. Take only mature trees, marked and counted (selective logging), not clear felling.",
      "Step 2. Replant at least as many trees as are taken, and care for the seedlings.",
      "Step 3. Protect the river banks and the wildlife corridors inside the reserve.",
      "Step 4. Employ and pay the local community, so that they also gain and protect the forest."),
    E("Why is human resource development as important as natural resources?",
      "Step 1. Minerals and forests are useless until people know how to find, process and manage them.",
      "Step 2. Educated and healthy people produce more, innovate, and attract investment.",
      "Step 3. Example: countries with few natural resources but well-trained people are far richer than "
      "some resource-rich countries.")])

extras("tour",
  plain="Tourism is people travelling for leisure, business or culture — and the services provided for them. "
        "It brings in foreign money and creates jobs in places with no factories.",
  examples=[
    E("A district has waterfalls but few visitors. Suggest a plan to develop tourism there.",
      "Step 1. Improve the access road, water, toilets and signposts at the site.",
      "Step 2. Train local guides and provide simple, clean accommodation and food.",
      "Step 3. Advertise — social media, travel fairs, the diaspora and schools' excursion programmes.",
      "Step 4. Involve the community so that they earn from crafts, food and guiding, and therefore protect the site."),
    E("State three benefits and two problems of tourism.",
      "<b>Benefits:</b> foreign exchange; jobs for guides, drivers, hotel and craft workers; roads and "
      "utilities built for tourists also serve residents.",
      "<b>Problems:</b> litter and damage at popular sites; unwanted influences on local culture and "
      "youth; seasonal, unreliable income.")])

extras("trade",
  plain="Production is not finished until the goods reach the person who uses them. Trade moves goods from "
        "producer to consumer — at home (retail and wholesale) and abroad (imports and exports).",
  examples=[
    E("In one year, a country's visible exports are GH₵ 60bn and visible imports GH₵ 75bn. "
      "Find the balance of trade and say what it means.",
      "Step 1. Balance of trade = visible exports − visible imports.",
      "Step 2. = 60 − 75 = <b>−GH₵ 15bn</b>.",
      "Step 3. It is negative, so the country has an unfavourable balance of trade (a trade deficit): "
      "it bought more goods from abroad than it sold."),
    E("A consumer buys tinned milk and finds it expired. What are her rights and what should she do?",
      "Step 1. She has a right to safety and to correct information, and a right to redress.",
      "Step 2. She should return it to the seller with the receipt and ask for a refund or replacement.",
      "Step 3. If refused, report to the Food and Drugs Authority or the Ghana Standards Authority.",
      "Step 4. Her duty: check expiry dates, seals and standards marks BEFORE buying, and keep receipts.")])
assert 60 - 75 == -15

extras("probs",
  plain="Social problems are the difficulties a society faces together — poverty, unemployment, child labour, "
        "streetism, drug abuse and crime. They are linked: solving one often eases another.",
  examples=[
    E("Children are fishing on the lake during school hours. Explain the problem and the solutions.",
      "Step 1. This is child labour: work that keeps children out of school and exposes them to danger.",
      "Step 2. Cause: family poverty, and the belief that the child's labour is needed for the household to eat.",
      "Step 3. Solutions: enforce the law on the minimum working age; support the families with livelihood "
      "programmes; free and compulsory basic education with feeding; rescue, counsel and return the "
      "children to school."),
    E("Write one essay point on the effects of drug abuse on the youth.",
      "Point: Drug abuse destroys a young person's education and future.",
      "Explain: Drugs damage memory and concentration, cause absenteeism, and lead to indiscipline and "
      "dismissal from school.",
      "Example: A student who takes tramadol to stay awake soon cannot study at all without it, "
      "fails his examinations and may end up in crime to fund the habit.")])

extras("planning",
  plain="Development planning is deciding what the country will build and improve, and how it will pay for "
        "it. The national budget turns that plan into figures for one year.",
  examples=[
    E("Where does government get the money for schools and roads?",
      "Step 1. <b>Taxes</b> — income tax and corporate tax (direct), VAT and import duties (indirect), "
      "collected by the Ghana Revenue Authority.",
      "Step 2. <b>Loans</b> — treasury bills and bonds at home, and loans from abroad, which must be repaid "
      "with interest.",
      "Step 3. <b>Grants</b> from development partners, and earnings from minerals, oil and state enterprises.",
      fig=draw.piefig([("Taxes", 60), ("Loans", 25), ("Grants & other", 15)],
                      label="Where government revenue comes from (illustration only)")),
    E("Explain how an ordinary citizen helps or harms national development.",
      "<b>Helps:</b> paying taxes honestly, working hard, protecting public property, voting wisely, "
      "and monitoring projects in the community.",
      "<b>Harms:</b> evading tax, stealing or damaging public property, demanding and paying bribes, "
      "and staying silent when funds are misused.")])
