"""English (Renewable Energy) content for enrich_knowledge."""
from enrich_knowledge_content import _c, _d, brain, discuss, html, know, read, steps

EN_NOTES_C = "<h4>Screen C — explore</h4><p>Build report-writing habits: precise vocabulary, evidence, and structured talk.</p>"
EN_NOTES_D = "<h4>Screen D — secure</h4><p>Students prove understanding in sentences fit for an information report.</p>"


def _eng(lesson, topic, pts_c, discuss_c, steps_c, brain_c, pts_d, steps_d, right_d, a_heading, a_body, a_notice=None):
    """Build C, D and Screen A prepend for one English lesson."""
    cd = {
        "C": _c(
            f"{topic} — go deeper",
            pts_c,
            f"Discuss {topic.lower()}",
            discuss_c,
            "Explore / Stretch",
            steps_c,
            brain_c,
            notes=EN_NOTES_C,
        ),
        "D": _d(
            f"{topic} — secure the learning",
            pts_d,
            "Secure / Prove",
            steps_d,
            right_d,
            notes=EN_NOTES_D,
        ),
    }
    a = read(a_heading, a_body, a_notice)
    return cd, a


_lessons = [
    (1, "Energy",
     ["<b>Energy</b> is the ability to do work or make things happen — it moves, heats and lights our world.",
      "Energy cannot be created or destroyed; it <b>changes form</b> (food → movement, coal → electricity).",
      "A <b>resource</b> is a supply we draw on; a <b>fuel</b> releases energy when used.",
      "Brisbane homes use electricity from the grid, often generated far from where we switch lights on."],
     ["Name five energy uses in your morning — sort into heat, movement, light or sound.",
      "Is food energy the same as electrical energy? What changes between them?",
      "Where does the energy in a charged phone ultimately come from?",
      "Why is energy a useful word in science but also in everyday speech (I have no energy)?"],
     [("Energy hunt", "List 5 uses at home/school and label the energy form."),
      ("Definition draft", "Write energy in your own words — no copying."),
      ("Resource link", "Name one resource and what energy it provides."),
      ("Report seed", "Draft one general statement for a report introduction.")],
     ["Which energy form is hardest to spot because it is invisible?",
      "How would you explain resource vs fuel to Year 4?",
      "What question about energy would fit an information report?"],
     ["Energy changes form but is never lost — useful for report conclusions.",
      "Report writers define terms clearly in the opening."],
     [("Glossary trio", "Rewrite energy, resource, fuel without copying."),
      ("Sentence upgrade", "Improve one vague sentence with precise vocabulary."),
      ("Partner check", "Can a partner repeat your definition?"),
      ("Exit ready", "Exit check.")],
     discuss("Glossary lock-in", [
         "Which definition is strongest — and why?",
         "How is a report definition different from a dictionary copy?",
         "What example best shows energy changing form?",
         "What will you write in your report opening?",
     ]),
     "Energy everywhere",
     ["Everything students do — walking to the desk, heating lunch, streaming a lesson — needs <b>energy</b>. "
      "Scientists define energy as the ability to do work or cause change.",
      "Energy travels through systems: the Sun's light grows food; food fuels bodies; power stations turn fuels into electricity for Brisbane classrooms."],
     "Energy is everywhere — even when we cannot see it moving."),
    (2, "Renewable vs non-renewable",
     ["<b>Renewable</b> sources are replaced naturally (sun, wind, water cycle, geothermal heat).",
      "<b>Non-renewable</b> sources take millions of years to form — coal, oil, gas.",
      "Fossil fuels store ancient solar energy captured by plants long ago.",
      "Australia uses both types; Queensland has significant coal and growing solar."],
     ["If oil ran out tomorrow, what would change in your week first?",
      "Can something be renewable in one place but scarce in another?",
      "Why do non-renewable fuels still dominate many power grids?",
      "How would you explain fossil fuel to a younger student?"],
     [("T-chart stretch", "Add column: Can it run out? with reasons."),
      ("Example pairs", "Name one renewable and one non-renewable with everyday links."),
      ("Sort drill", "Partner calls items — you answer renewable or non-renewable."),
      ("Report vocab", "Use both terms in one compound sentence.")],
     ["What mistake do people make calling wood always renewable?",
      "How does time scale matter for renewability?",
      "Which example best fits a report paragraph?"],
     ["Renewable vs non-renewable is a core report comparison.",
      "Examples must be specific — not just solar is good."],
     [("Flash sort", "Ten items — renewable or non-renewable aloud."),
      ("Because", "One sentence: I classify X as renewable because…"),
      ("Contrast", "Write one contrast sentence for your report."),
      ("Exit ready", "Exit check.")],
     html('<div class="card cream"><span class="tag try">T-CHART</span><p style="margin-top:8px">'
          "Complete: <b>Renewable</b> | <b>Non-renewable</b> | <b>Can it run out?</b> — three examples each.</p></div>"),
     "Two kinds of energy sources",
     ["Energy sources are often grouped as <b>renewable</b> (replaced by nature) or "
      "<b>non-renewable</b> (finite stocks like coal and oil).",
      "Understanding the difference helps readers know why communities are switching to sun and wind across Queensland."]),
    (3, "Why switch to renewables",
     ["Burning fossil fuels releases <b>emissions</b> that contribute to climate change.",
      "<b>Sustainable</b> choices protect people and environments long-term.",
      "Renewables reduce air pollution in cities and improve community health.",
      "Report writers link causes (emissions) to effects (climate, weather extremes)."],
     ["Who benefits most from switching — today's citizens or future generations?",
      "Can wealthy regions keep burning coal? What reasons might leaders give?",
      "How is climate different from today's weather?",
      "What general statement could open a report on renewables?"],
     [("Climate link", "Chain: emissions → climate → community response."),
      ("Stakeholder", "Name one group that gains and one that faces change."),
      ("Report intro", "Write one general opening sentence."),
      ("Evidence", "Cite one reason Queensland invests in solar.")],
     ["Why must reports balance people and planet?",
      "What is too vague in the sentence renewables are good?",
      "How do emissions connect to everyday choices?"],
     ["Strong reports explain <b>why</b> switching matters with people/planet language.",
      "Conclusions should not introduce brand-new facts."],
     [("Why sentence", "Explain why renewables matter in one sentence."),
      ("Vocabulary", "Use sustainable, emissions or climate accurately."),
      ("Intro polish", "Refine your general statement."),
      ("Exit ready", "Exit check.")],
     discuss("Report seed", [
         "Does your intro state the topic without listing everything?",
         "Which word carries the most meaning — sustainable or green?",
         "What question will your report answer?",
         "What would you research next?",
     ]),
     "Why communities switch",
     ["Many countries, including Australia, are increasing <b>renewable energy</b> to lower "
      "<b>emissions</b> and act on <b>climate</b> risks.",
      "Information reports explain these reasons with clear cause-and-effect language for readers in Year 5 and beyond."]),
]

# Build partial dict from first 3 lessons, then extend with loop for 4-18
ENGLISH_CD = {}
ENGLISH_A = {}

for item in _lessons:
    n, topic, *rest = item
    cd, a = _eng(n, topic, *rest)
    ENGLISH_CD[n] = cd
    ENGLISH_A[n] = a

# Lessons 4-18 — compact definitions
_more = [
    (4, "Solar energy", "solar", "photovoltaic", "panel",
     "Sunlight is Earth's primary energy input; solar panels capture it as electricity or heat.",
     "Queensland's sunny climate makes solar attractive for homes and schools."),
    (5, "How solar panels work", "electricity", "convert", "silicon",
     "Photovoltaic cells in panels convert light directly into electricity using semiconductors like silicon.",
     "An inverter changes DC current from panels into AC for household appliances."),
    (6, "Solar pros and cons", "efficient", "disadvantage", "generate",
     "Solar power is clean and abundant in Australia but depends on daylight and weather.",
     "Installation cost, roof space and battery storage are common challenges."),
    (7, "Wind energy", "turbine", "wind farm", "kinetic energy",
     "Wind is moving air with kinetic energy; turbines convert that motion into electricity.",
     "Coastal and open regions of Australia host large wind farms."),
    (8, "How wind turbines work", "generator", "offshore", "rotation",
     "Blades spin a shaft connected to a generator; faster wind generally produces more power.",
     "Offshore turbines often catch stronger, steadier winds than inland sites."),
    (9, "Wind pros and cons", "intermittent", "consistent", "transmission",
     "Wind is renewable and low-emission but varies hour to hour.",
     "Grid connections and community views about landscape impact matter."),
    (10, "Hydropower", "hydropower", "dam", "reservoir",
     "Hydropower uses moving water — often stored behind dams — to spin turbines.",
     "Australia uses hydro in snowy mountains and some river systems."),
    (11, "How hydro dams work", "potential energy", "penstock", "gravitational",
     "Water high in a reservoir has gravitational potential energy; falling water spins turbines.",
     "A penstock is a large pipe directing water to the generator."),
    (12, "Hydropower pros and cons", "habitat", "displacement", "ecosystem",
     "Hydro gives steady power but large dams can disrupt ecosystems and communities.",
     "Reliability is a major advantage over sun and wind alone."),
    (13, "Geothermal energy", "geothermal", "magma", "geologist",
     "Geothermal energy uses heat from inside the Earth — seen in hot rocks, springs and volcanoes.",
     "Iceland and parts of New Zealand use geothermal widely; Australia has promising sites."),
    (14, "How geothermal plants work", "geyser", "steam", "drill",
     "Plants drill wells to reach hot water or steam that drives turbines.",
     "Steam fields can run generators 24 hours a day where heat is close to the surface."),
    (15, "Geothermal pros and cons", "limited", "volcanic", "harness",
     "Geothermal is reliable and low-emission but only works well in certain geology.",
     "Drilling is expensive and not every region has accessible heat."),
    (16, "Tidal energy", "tidal", "gravitational pull", "predictable",
     "Tides rise and fall because of the Moon's and Sun's gravitational pull on oceans.",
     "Tidal patterns are highly predictable compared with wind and sunshine."),
    (17, "How tidal energy is captured", "tidal barrage", "estuary", "tidal stream generator",
     "Barrages across estuaries trap tidal flow; stream generators sit in fast currents.",
     "Engineers must balance energy gain with impacts on fisheries and navigation."),
    (18, "Comparing energy types", "compare", "contrast", "advantage",
     "No single renewable suits every location — reports compare solar, wind, hydro, geothermal and tidal.",
     "Writers weigh advantages, disadvantages, location and reliability for audiences."),
]

for n, topic, t1, t2, t3, para1, para2 in _more:
    _topics_extra = {
        4: ["The Sun delivers more energy to Earth in one hour than humans use in a year.",
            "Solar panels can produce electricity (PV) or heat water directly.",
            "Queensland receives strong solar radiation — ideal for rooftop systems."],
        5: ["Each cell produces a small voltage; many cells form a panel.",
            "Inverters change DC electricity from panels into AC for homes.",
            "Silicon is common because it reacts to sunlight efficiently."],
        6: ["Solar reduces electricity bills and emissions after installation.",
            "Night and cloudy weather reduce output unless batteries store power.",
            "Reports should weigh environmental and economic factors together."],
        7: ["Wind is caused by uneven heating of Earth's surface.",
            "Turbines on towers catch stronger, steadier winds.",
            "Australia's coastlines host many wind farms."],
        8: ["Blade length matters — longer blades sweep a larger area.",
            "A nacelle atop the tower houses the generator.",
            "Offshore wind can be steadier but costs more to build."],
        9: ["Wind is clean but output varies with weather.",
            "Communities debate visual impact and wildlife.",
            "Grid upgrades may be needed to carry wind power."],
        10: ["Falling or flowing water spins turbines — a renewable cycle driven by rainfall.",
             "Snowy Hydro is a famous Australian example.",
             "Hydropower can start quickly when demand spikes."],
        11: ["Stored water high in a dam has gravitational potential energy.",
             "Water rushes through a penstock to spin turbines.",
             "Operators control flow to match electricity demand."],
        12: ["Large dams can displace communities and alter river ecosystems.",
             "Reliable baseload power is hydro's major strength.",
             "Fish ladders and environmental flows aim to reduce harm."],
        13: ["Earth's interior heat reaches the surface near plate boundaries.",
             "Hot rocks, geysers and volcanoes signal geothermal potential.",
             "Used for electricity and direct heating in some countries."],
        14: ["Wells tap underground hot water or steam zones.",
             "Steam spins turbines similar to other thermal plants.",
             "Closed-loop systems can reinject water underground."],
        15: ["Works around the clock unlike solar or wind alone.",
             "Only economical where heat is shallow and intense.",
             "Drilling risk and water chemistry must be managed."],
        16: ["The Moon's gravity pulls ocean bulges that sweep coastlines.",
             "Tides are predictable years in advance.",
             "Strong tides occur in some bays and channels."],
        17: ["Barrages trap tidal flow; turbines spin as water moves in or out.",
             "Tidal stream generators sit in fast currents like underwater windmills.",
             "Marine wildlife and shipping need careful planning."],
        18: ["Solar suits sunny rooftops; wind suits open coasts; hydro needs rivers.",
             "Geothermal needs geology; tidal needs strong tides.",
             "Reports compare reliability, cost, location and environmental impact."],
    }
    pts = _topics_extra.get(n, [para1, para2, "Information reports use facts, formal tone and paragraph structure."])
    if len(pts) < 4:
        pts = pts + ["Information reports use facts, formal tone and paragraph structure."]
    disc = [
        f"How would you explain {topic.lower()} to a family member?",
        f"What Queensland example best illustrates {t1}?",
        "What advantage matters most for communities — cost, reliability or environment?",
        "What question belongs in a report section heading?",
    ]
    stc = [
        ("Vocabulary", f"Use {t1}, {t2} and {t3} in one paragraph."),
        ("Example", f"Give one Australian example of {topic.lower()}."),
        ("Pros/cons note", "List one advantage and one challenge."),
        ("Report line", "Write one sentence fit for a report body."),
    ]
    br = [
        f"What is still confusing about {topic.lower()}?",
        "Which word will you glossary-define?",
        "How is this energy type location-dependent?",
    ]
    pts_d = [para1, "Report sentences should be factual and specific."]
    std = [
        ("Prove sentence", "One improved sentence using today's vocabulary."),
        ("Partner read", "Listener ticks clarity and vocabulary."),
        ("Report bit", "Add one sentence to your growing report."),
        ("Exit ready", "Exit check."),
    ]
    right = discuss("Secure the learning", [
        "Which sentence improved most after feedback?",
        "What would you add to a glossary box?",
        "How does this lesson connect to Lesson 1 energy ideas?",
        "What heading would you write for this section?",
    ])
    ENGLISH_CD[n] = {
        "C": _c(f"{topic} — go deeper", pts, f"Discuss {topic.lower()}", disc,
               "Explore / Stretch", stc, br, notes=EN_NOTES_C),
        "D": _d(f"{topic} — secure", pts_d, "Secure / Prove", std, right, notes=EN_NOTES_D),
    }
    ENGLISH_A[n] = read(
        topic,
        [para1, para2],
        f"Key terms: {t1}, {t2}, {t3}.",
    )
