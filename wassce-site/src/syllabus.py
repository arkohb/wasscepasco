"""The complete WASSCE syllabus outline for each subject, mapped to the drill topics."""

SYLLABUS = {
 "maths": [
  ("A. Number and Numeration", [
    ("Number bases: conversion, operations in other bases", "bases"),
    ("Modular arithmetic: addition, multiplication tables, applications", "mod"),
    ("Fractions, decimals, approximations and standard form", "approx"),
    ("Positive and negative integers, factors, multiples, LCM and HCF", "intfac"),
    ("Indices and the laws of indices", "indices"),
    ("Logarithms, laws of logarithms, logarithmic equations", "logs"),
    ("Surds and rationalising the denominator", "surds"),
    ("Sequences and series: AP and GP", "seq"),
    ("Sets: Venn diagrams and set operations", "sets"),
    ("Logical reasoning: statements, implication, validity", "logic"),
    ("Matrices and determinants (2 × 2)", "matrix"),
    ("Ratio, proportion, rates and percentages", "fin"),
    ("Financial arithmetic: interest, discount, profit and loss, hire purchase, taxes", "fin"),
    ("Variation: direct, inverse, joint and partial", "var"),
  ]),
  ("B. Algebraic Processes", [
    ("Algebraic expressions: expansion, factorisation, substitution", "alg"),
    ("Linear equations and simultaneous equations", "alg"),
    ("Change of subject of a formula", "alg"),
    ("Quadratic equations: factorisation, formula, completing the square", "quad"),
    ("Graphs of linear and quadratic functions", "quad"),
    ("Linear inequalities and linear programming", "ineq"),
    ("Algebraic fractions", "afunc"),
    ("Functions and relations, including inverse and composite", "afunc"),
  ]),
  ("C. Mensuration", [
    ("Lengths, perimeters, arcs and chords", "area"),
    ("Areas of plane figures, sectors and segments", "area"),
    ("Volumes and surface areas of solids", "vol"),
    ("Similar and congruent figures; scales and map scales", "simil"),
    ("The earth as a sphere: longitude, latitude and distances", "earth"),
  ]),
  ("D. Plane Geometry", [
    ("Angles, parallel lines and the transversal", "geo"),
    ("Triangles, polygons and Pythagoras' theorem", "geo"),
    ("Circles: chords, tangents and circle theorems", "circle"),
    ("Geometrical construction with ruler and compasses", "loci"),
    ("Loci in two dimensions", "loci"),
  ]),
  ("E. Coordinate Geometry", [
    ("Gradient, distance, midpoint and the equation of a straight line", "coord"),
    ("Parallel and perpendicular lines", "coord"),
  ]),
  ("F. Trigonometry", [
    ("Sine, cosine and tangent of acute angles; special angles", "trig"),
    ("Angles of elevation and depression", "trig"),
    ("Trigonometric ratios of angles up to 360° and simple graphs", "trig"),
    ("Bearings and distances", "bear"),
    ("Sine rule, cosine rule and the area of a triangle", "bear"),
  ]),
  ("G. Introductory Calculus", [
    ("Differentiation of algebraic functions; gradients and turning points", "calc"),
    ("Integration of simple algebraic functions; area under a curve", "calc"),
  ]),
  ("H. Statistics and Probability", [
    ("Collection, tabulation and presentation of data", "stat"),
    ("Mean, median and mode, for grouped and ungrouped data", "stat"),
    ("Bar charts, pie charts and histograms; measures of dispersion", "stat"),
    ("Cumulative frequency curves, quartiles and percentiles", "cumfreq"),
    ("Probability: single and combined events", "prob"),
  ]),
  ("I. Vectors and Transformation", [
    ("Vectors in a plane: addition, magnitude and position vectors", "vec"),
    ("Transformations: reflection, rotation, translation and enlargement", "vec"),
  ]),
 ],

 "english": [
  ("Paper 1 — Lexis and Structure (objective test)", [
    ("Synonyms and word choice in context", "syn"),
    ("Antonyms and opposites, including negative prefixes", "ant"),
    ("Idioms, proverbs and collocations", "idiom"),
    ("Registers: vocabulary of about sixteen fields of work", "reg"),
    ("Word formation, affixes and commonly confused words", "form"),
    ("Figures of speech and literary devices", "fig"),
    ("Tenses and the sequence of tenses", "tense"),
    ("Concord (subject–verb agreement)", "concord"),
    ("Nouns, pronouns and determiners", "pron"),
    ("Prepositions and phrasal verbs", "prep"),
    ("Adjectives, adverbs and degrees of comparison", "adj"),
    ("Question tags, conditionals and reported speech", "tags"),
    ("Phrases, clauses and sentence types", "clause"),
    ("Punctuation, capitalisation and spelling", "punct"),
    ("Active and passive voice", "voice"),
    ("Common errors and sentence improvement", "errors"),
  ]),
  ("Paper 2 — Essay, Comprehension and Summary", [
    ("Essay writing: letters, narrative, descriptive, argumentative, expository", "essay"),
    ("Reports, speeches and articles", "report"),
    ("Reading comprehension: meaning, inference, grammatical names and functions", "comp"),
    ("Summary writing: selecting and restating points", "summary"),
  ]),
  ("Paper 3 — Test of Orals", [
    ("Vowels, diphthongs and rhymes", "vowel"),
    ("Consonants, consonant clusters and silent letters", "cons"),
    ("Word stress, emphatic stress and intonation", "stress"),
    ("Listening comprehension and appropriate spoken responses", "listen"),
  ]),
 ],

 "science": [
  ("A. Diversity of Matter", [
    ("Introduction to science, measurement and the scientific method", "measure"),
    ("Living and non-living things", "living"),
    ("Classification of living things", "classify"),
    ("Cells and their structures; osmosis and diffusion", "cells"),
    ("Structure of matter: elements, compounds, mixtures and separation", "matter"),
    ("Acids, bases and salts", "acids"),
    ("Metals, non-metals and rusting", "metals"),
    ("Water, solutions and water treatment", "water"),
    ("Soil and soil conservation", "soil"),
    ("Rocks, minerals and mineral exploitation", "rocks"),
    ("Organic compounds, petrochemicals and plastics", "organic"),
  ]),
  ("B. Cycles", [
    ("Air, air masses, weather and the nitrogen cycle", "air"),
    ("The hydrological cycle and water contamination", "hydro"),
    ("Life cycles of pests and parasites", "pests"),
    ("Crop production and soil fertility", "crop"),
    ("Farm tools, machinery and safety", "farmtools"),
    ("Animal production and animal health", "animal"),
  ]),
  ("C. Systems", [
    ("Food and nutrition; the digestive system", "nutrition"),
    ("Teeth and dentition", "teeth"),
    ("Respiratory and circulatory systems", "respcirc"),
    ("Excretory, skeletal and nervous systems", "excskel"),
    ("Hormones and the endocrine system", "hormone"),
    ("Reproduction in humans and in flowering plants", "repro"),
    ("Photosynthesis, growth and transpiration", "photo"),
    ("Food preservation, processing and storage", "preserve"),
  ]),
  ("D. Energy", [
    ("Forms of energy, transformations, solar and nuclear energy", "energy"),
    ("Heat energy: conduction, convection, radiation and heat capacity", "heat"),
    ("Light: reflection, refraction, lenses and the eye", "light"),
    ("Sound and waves", "sound"),
    ("Electrical energy: Ohm's law, circuits and domestic wiring", "elec"),
    ("Magnetism and electromagnets", "magnet"),
    ("Electronics and ICT", "electron"),
  ]),
  ("E. Interactions of Matter", [
    ("Ecosystems, food chains and energy flow", "eco"),
    ("Forces, motion and pressure", "force"),
    ("Work, energy, power and simple machines", "machines"),
    ("Infectious diseases, immunisation, first aid and drug abuse", "health"),
    ("Variation, inheritance and biotechnology", "genes"),
    ("The atmosphere, pollution, waste and climate change", "env"),
  ]),
 ],

 "social": [
  ("Section A — The Environment", [
    ("The environment and its components", "envcomp"),
    ("Environmental degradation and its control", "degrad"),
    ("Population growth and development", "popn"),
    ("Water, sanitation and environmental health", "sanit"),
    ("Natural disasters and disaster management", "disaster"),
    ("Culture and our cultural heritage", "culture"),
    ("Socialisation and the individual", "social"),
    ("Self-identity, self-esteem and personal development", "identity"),
    ("Adolescent development, chastity and responsible living", "adol"),
    ("Marriage and family life", "family"),
    ("Gender roles and equality", "gender"),
    ("Education and national development", "educ"),
  ]),
  ("Section B — Governance, Politics and Stability", [
    ("Nationhood, national symbols and nation building", "nation"),
    ("The 1992 Constitution and the rule of law", "constit"),
    ("Citizenship: rights and responsibilities", "citizen"),
    ("Human rights and vulnerable groups", "rights"),
    ("Democracy and the three arms of government", "democracy"),
    ("Elections and political participation", "elect"),
    ("Decentralisation and local government", "local"),
    ("Chieftaincy and traditional authority", "chief"),
    ("Leadership, followership and accountability", "leader"),
    ("Conflicts, conflict resolution and peace building", "conflict"),
    ("Corruption and accountability institutions", "corrupt"),
    ("Ghana's international relations: UN, AU, ECOWAS", "intl"),
  ]),
  ("Section C — Social and Economic Development", [
    ("Our national economy and its sectors", "economy"),
    ("Money, banking and personal financial management", "money"),
    ("Entrepreneurship and self-employment", "entre"),
    ("Unemployment and the world of work", "unemp"),
    ("Science, technology and development", "sci"),
    ("Sustainable development and resource management", "sustain"),
    ("Tourism and development", "tour"),
    ("Production, trade and consumer awareness", "trade"),
    ("Religion, morality and national development", "religion"),
    ("Social problems and their solutions", "probs"),
    ("National development planning and the citizen", "planning"),
  ]),
 ],
}


def ordered_topic_ids(subject):
    """Topic ids in syllabus order, each appearing once."""
    seen, out = set(), []
    for _, items in SYLLABUS[subject]:
        for _, tid in items:
            if tid not in seen:
                seen.add(tid)
                out.append(tid)
    return out
