"""Content data for enrich_knowledge.py — Science, HASS, English screens."""


def know(heading, points, body=None, fact=None, label="KNOWLEDGE"):
    return {"k": "know", "heading": heading, "points": points, "body": body or [], "fact": fact, "label": label}


def discuss(title, prompts, tip=None, label="DISCUSS"):
    return {"k": "discuss", "title": title, "prompts": prompts, "tip": tip, "label": label}


def steps(label, rows):
    return {"k": "steps", "label": label, "rows": [{"t": t, "d": d} for t, d in rows]}


def brain(qs):
    return {"k": "brain", "q": qs}


def read(heading, body, notice=None):
    return {"k": "read", "heading": heading, "body": body, "notice": notice}


def html(html_str):
    return {"k": "html", "html": html_str}

NOTES_C = "<h4>Screen C — deepen</h4><p>Pair talk before independent work. Circulate and listen for precise vocabulary.</p><h4>Teacher tip</h4><p>Cold-call one student per discuss prompt. Capture a strong sentence on the board.</p>"
NOTES_D = "<h4>Screen D — prove</h4><p>Students work independently first, then peer-check. Run exit check cold.</p><h4>Teacher tip</h4><p>Re-teach if fewer than 75% can state the 15-minute win.</p>"


def _c(kh, pts, dt, pr, sl, sr, bq, notes=NOTES_C, body=None, fact=None, tip=None):
    return {
        "left": [know(kh, pts, body, fact), discuss(dt, pr, tip)],
        "right": [steps(sl, sr), brain(bq)],
        "notes": notes,
    }


def _d(kh, pts, sl, sr, right_extra, notes=NOTES_D, fact=None):
    right = [right_extra]
    return {
        "left": [know(kh, pts, fact=fact, label="SUMMARY"), steps(sl, sr)],
        "right": right,
        "notes": notes,
    }


SCIENCE_CD = {
    1: {
        "C": _c(
            "The matter test on tricky cases",
            [
                "Matter must have <b>mass</b> (weigh something) and <b>volume</b> (take up space).",
                "Air inside a glass, balloon or bubble passes both tests even though you cannot see it.",
                "Steam and smell are gases — they spread to fill whatever space is available.",
                "A vacuum chamber is not truly empty; removing air is hard and takes equipment.",
            ],
            "Air is matter — convince a sceptic",
            [
                "Your partner says an empty glass has nothing in it. What evidence would you show them?",
                "Is a smell matter? Argue yes or no using mass and volume language.",
                "Why do scuba divers carry air tanks instead of breathing water?",
                "What is the difference between something invisible and something that is not matter?",
            ],
            "Explore / Stretch",
            [
                ("Balloon mass test", "Weigh a balloon, inflate it, weigh again. Record whether mass changed and why."),
                ("Upside-down glass", "Push an upside-down cup into water. Sketch where air went."),
                ("Bubble evidence", "Blow one bubble. List three ways it proves gas has volume."),
                ("Teach-back", "Explain to a partner why classroom air counts as matter in 40 seconds."),
            ],
            [
                "Which example was hardest to classify — and what property decided it?",
                "How is proving air is matter different from just saying air is everywhere?",
                "What would change if students thought only visible things were matter?",
            ],
            tip="Use sentence starters: My evidence is… because matter has…",
        ),
        "D": _d(
            "Prove air is matter",
            [
                "Mass + volume = matter. Air has both even when invisible.",
                "Strong evidence: balloon on scales, trapped air in water, bubbles with volume.",
                "Teach someone else using one concrete classroom example.",
            ],
            "Secure / Prove",
            [
                ("Evidence sentence", "Write one sentence: I know air is matter because…"),
                ("Vocabulary check", "Underline mass, volume and particles in your answer."),
                ("Partner proof", "Swap work — can your partner repeat your evidence aloud?"),
                ("Exit ready", "Complete the exit check without notes."),
            ],
            discuss(
                "Final teach-back",
                [
                    "What is your single best piece of evidence that air is matter?",
                    "How would you test whether steam from a kettle is matter?",
                    "Why is particle language useful even when we cannot see particles?",
                    "What mistake do people make when they say empty means nothing?",
                ],
                tip="Nominate two students to model a crisp evidence sentence.",
            ),
        ),
    },
    2: {
        "C": _c(
            "Solid properties in the real world",
            [
                "Solids have fixed <b>shape</b> and fixed <b>volume</b> — the container does not change them.",
                "Particles in a solid vibrate but stay in a fixed arrangement.",
                "Most solids are hard to compress because particles are already packed tightly.",
                "Sand flows but each grain is still a solid with its own shape.",
            ],
            "Solid or not?",
            [
                "Is jelly a solid or a liquid? What evidence supports your call?",
                "A sponge changes shape when you squeeze it — is it still a solid?",
                "Why is a pile of sand tricky for younger students to classify?",
                "Could something be a solid and still feel soft? Give an example.",
            ],
            "Explore / Stretch",
            [
                ("Compress test", "Try squeezing a rubber, eraser and apple. Which resists most?"),
                ("Shape test", "Pour rice into a jar then a tray. Does each grain change shape?"),
                ("Property card", "Pick a classroom solid and list shape, volume and compressibility."),
                ("Edge-case sort", "Sort jelly, ice, sand and sponge — defend one tricky item."),
            ],
            [
                "Which solid property is easiest to observe without equipment?",
                "When does everyday language (soft, squishy) clash with science language?",
                "How do particles explain why a brick keeps its shape?",
            ],
        ),
        "D": _d(
            "Solid checklist",
            [
                "A solid keeps its own shape and volume.",
                "Particle picture: packed, vibrating, not sliding past each other.",
            ],
            "Secure / Prove",
            [
                ("Three-bullet card", "Write how I know it is a solid in three bullet points."),
                ("Point and prove", "Point to a solid nearby and name shape + volume."),
                ("Fix a misconception", "Explain why sand is not a liquid."),
                ("Exit ready", "Complete exit check — include particle words."),
            ],
            html(
                '<div class="card dark"><span class="tag try">SORT</span>'
                '<p style="margin-top:8px">Sort these into <b>clear solid</b> vs <b>tricky case</b>:</p>'
                '<div class="sort-grid"><div class="sort-col"><b>Items</b>ice cube, honey, play dough, oxygen, desk</div>'
                '<div class="sort-col"><b>Your call</b>Write solid / not solid + one reason each</div></div></div>'
            ),
        ),
    },
    3: {
        "C": _c(
            "Liquid behaviour — same state, different flow",
            [
                "Liquids have a fixed <b>volume</b> but take the <b>shape of their container</b>.",
                "Particles are close together but can slide and flow past each other.",
                "<b>Viscosity</b> describes how thick or runny a liquid is — honey vs water.",
                "Temperature often changes viscosity (warm honey pours faster).",
            ],
            "Pouring and flowing",
            [
                "Why does honey pour more slowly than water if both are liquids?",
                "Does a liquid always look flat on top? Think of dome-shaped droplets.",
                "How could you fairly compare how fast two liquids pour?",
                "What particle movement explains why liquids spill?",
            ],
            "Explore / Stretch",
            [
                ("Viscosity race", "Time water vs another liquid down a ramp. Keep angle the same."),
                ("Container test", "Pour 50 mL into three different shaped containers. What changes?"),
                ("Particle sketch", "Draw liquid particles — close, random, sliding."),
                ("Caption it", "Write one sentence linking viscosity to particle movement."),
            ],
            [
                "What is the difference between volume and the shape you see?",
                "Why is fair testing important in a viscosity race?",
                "Which liquid in your home would win a slow-pour competition?",
            ],
        ),
        "D": _d(
            "Liquid evidence",
            [
                "Liquids flow, keep volume, and fill the bottom of a container.",
                "Viscosity is a measurable property of liquids.",
            ],
            "Secure / Prove",
            [
                ("Checklist", "Write three ways I know it is a liquid."),
                ("Fair test", "State one variable you would change and one you would keep."),
                ("Real example", "Name a liquid at home and one property you can observe."),
                ("Exit ready", "Peer-check vocabulary: viscosity, volume, particles."),
            ],
            discuss(
                "Liquid lab talk",
                [
                    "What result surprised you in the viscosity race?",
                    "How would particles move differently in thick vs runny liquids?",
                    "Is toothpaste a liquid? Build an argument both ways.",
                    "What would you measure if you repeated the test?",
                ],
            ),
        ),
    },
    4: {
        "C": _c(
            "Gas clues without seeing particles",
            [
                "Gases have no fixed shape or volume — they spread to fill all available space.",
                "Gas particles are far apart and move quickly in random directions.",
                "Bubbles, wind, inflation and smell all show gas taking up space.",
                "Compressing a gas is easier than compressing a liquid or solid.",
            ],
            "Detect the gas",
            [
                "List three gases you cannot see but can detect in a classroom.",
                "Why does a deflated football need pumping before a game?",
                "What happens to gas particles when you open a fizzy drink?",
                "How is steam similar to and different from the air around you?",
            ],
            "Explore / Stretch",
            [
                ("Gas hunt", "Find three gas clues in the room. Note your evidence for each."),
                ("Inflate and feel", "Press a inflated balloon vs flat — what are you feeling?"),
                ("Fizz observation", "Watch bubbles rise. Sketch where gas goes when it escapes."),
                ("Compare", "Complete a sentence: Gas particles are ___ apart than liquid particles."),
            ],
            [
                "Which gas clue is the most convincing for someone who says gases are not real?",
                "Why do gases fill a container but liquids only fill the bottom?",
                "What everyday danger involves gases spreading invisibly?",
            ],
        ),
        "D": _d(
            "Gas vs liquid",
            [
                "Gases compress and expand easily; liquids do not.",
                "Both are made of particles, but spacing and movement differ.",
            ],
            "Secure / Prove",
            [
                ("Side-by-side", "Choose one gas and one liquid example. Compare shape and volume."),
                ("Particle sentence", "Write how gas particles move differently from liquid particles."),
                ("Evidence line", "One sentence of evidence that gas is matter."),
                ("Exit ready", "Complete exit check cold."),
            ],
            html(
                '<div class="card cream"><span class="tag try">PARTICLE DUEL</span>'
                "<p style=\"margin-top:8px\">Draw two boxes: <b>water vapour</b> vs <b>liquid water</b>. "
                "Label spacing, movement and what happens in an open container.</p></div>"
            ),
        ),
    },
    5: {
        "C": _c(
            "Particle pictures that tell the truth",
            [
                "Solids: tightly packed, regular pattern, vibrate in place.",
                "Liquids: close but irregular, slide past each other.",
                "Gases: far apart, random, fast movement in all directions.",
                "Arrows on diagrams should show movement, not just dots.",
            ],
            "Read the diagram",
            [
                "What is wrong if a gas diagram shows particles touching?",
                "Why do scientists use circles instead of drawing real atoms?",
                "How would heating change particle movement in each state?",
                "Can one substance be solid, liquid and gas? Give an example.",
            ],
            "Explore / Stretch",
            [
                ("Three boxes", "Draw solid, liquid, gas for water. Add arrows for movement."),
                ("Caption each", "Write one caption per box using packed / slide / spread."),
                ("Oobleck check", "Where would oobleck sit on a state diagram — and why is it tricky?"),
                ("Peer audit", "Swap diagrams — find one thing to improve."),
            ],
            [
                "Which state is hardest to draw accurately — and why?",
                "How does a particle diagram help more than a photo?",
                "What mistake do cartoons often make about gases?",
            ],
        ),
        "D": _d(
            "Fix the diagram",
            [
                "Good diagrams show spacing, arrangement and movement.",
                "Same substance can change state when heated or cooled.",
            ],
            "Secure / Prove",
            [
                ("Spot the error", "Fix a deliberately wrong gas diagram and explain why."),
                ("State change", "Show ice, water and steam as three particle boxes."),
                ("Teach Year 4", "Use your diagram to explain one state in 30 seconds."),
                ("Exit ready", "Exit check with particle vocabulary underlined."),
            ],
            discuss(
                "Diagram defence",
                [
                    "What is the most common error in student particle drawings?",
                    "How does adding heat change the story your diagram tells?",
                    "Why is oobleck a useful exception to simple sorting?",
                    "Which state would you choose to teach first — and why?",
                ],
            ),
        ),
    },
    6: {
        "C": _c(
            "Classification with science language",
            [
                "Use <b>properties</b> (shape, volume, compressibility, flow) not just names.",
                "Part A-style answers need a claim plus a reason linked to evidence.",
                "Mystery samples are classified by what you observe, not what you guess.",
                "Mass and volume apply to all states of matter.",
            ],
            "Build a Part A reason",
            [
                "How is saying it looks like a liquid different from testing flow?",
                "What property would prove a mystery sample is a gas?",
                "Why should you avoid saying it is obviously… without evidence?",
                "Which words from today belong in a formal science answer?",
            ],
            "Explore / Stretch",
            [
                ("Mystery bag", "Classify one sample using two observable properties."),
                ("Sentence frame", "I think it is a ___ because it ___ and ___."),
                ("Word bank", "Use: particles, volume, compress, flow, vibrate."),
                ("Partner challenge", "Give your partner a sample — can they classify it?"),
            ],
            [
                "What is the difference between observation and inference here?",
                "Which property separates gases from liquids most clearly?",
                "How would you improve a weak classification sentence?",
            ],
        ),
        "D": _d(
            "Part A warm-up",
            [
                "Strong answers: state + property + particle link.",
                "Assessment language should be precise and evidence-based.",
            ],
            "Secure / Prove",
            [
                ("Self-check", "Tick mass, volume and particle talk in your draft."),
                ("Glow and grow", "Swap with a partner — one strength, one improvement."),
                ("Cold call prep", "Be ready to classify an item in one sentence."),
                ("Exit ready", "Complete exit check."),
            ],
            html(
                '<div class="card dark"><span class="tag try">CRITERIA</span>'
                "<p style=\"margin-top:8px\"><b>Excellent</b> names the state, cites two properties, uses particle words.<br>"
                "<b>Developing</b> names the state with one reason.<br>"
                "Score your work honestly before submitting.</p></div>"
            ),
        ),
    },
    8: {
        "C": _c(
            "Fair tests and variables",
            [
                "<b>Independent variable</b>: what you change on purpose.",
                "<b>Dependent variable</b>: what you measure (e.g. melting time).",
                "<b>Controlled variables</b>: what you keep the same for fairness.",
                "Only one thing should change in a fair test.",
            ],
            "Design a fair ice test",
            [
                "If you test melting time, what must stay the same about each ice cube?",
                "Why would different-sized cubes make results unreliable?",
                "What could you measure besides time?",
                "How does shade vs sun change variables in a real investigation?",
            ],
            "Explore / Stretch",
            [
                ("Card sort", "Sort statements into change / measure / keep same."),
                ("Question upgrade", "Turn Which melts faster? into a testable question."),
                ("Plan seed", "List 4 equipment items and why each is needed."),
                ("Fairness fix", "Spot the unfair step in a sample method and rewrite it."),
            ],
            [
                "What is the most common fairness mistake in student investigations?",
                "Why do scientists repeat measurements?",
                "How does shade change the independent variable in the ice-sun lesson?",
            ],
        ),
        "D": _d(
            "Investigation planner",
            [
                "A testable question names what changes and what is measured.",
                "Fair tests control variables that could confuse results.",
            ],
            "Secure / Prove",
            [
                ("Variable table", "Fill: I change… I measure… I keep the same…"),
                ("Prediction link", "Write I predict… because… tied to your variable."),
                ("Risk check", "Name one safety or fairness risk and how to manage it."),
                ("Exit ready", "Exit check — include fair test vocabulary."),
            ],
            discuss(
                "Variables clinic",
                [
                    "What would you change if results looked too random?",
                    "Why is size of ice a controlled variable, not something you ignore?",
                    "How is this different from just watching ice melt for fun?",
                    "What question would you ask if shade made ice last longer?",
                ],
            ),
        ),
    },
    9: {
        "C": _c(
            "Predictions that scientists can test",
            [
                "A prediction says what you <b>think will happen</b> and <b>why</b>.",
                "Measurable predictions use units: minutes, millimetres, degrees.",
                "Because should link to a science idea (heat, surface area, shade).",
                "Predictions are not guesses — they use what you already know.",
            ],
            "Upgrade weak predictions",
            [
                "Why is I think it will melt soon weaker than I predict 8 minutes because…?",
                "What unit fits melting time? What unit does not?",
                "How does shade give you a reason for a prediction?",
                "Can two sensible predictions disagree? When is that okay?",
            ],
            "Explore / Stretch",
            [
                ("Weak → strong", "Rewrite three vague predictions with numbers and reasons."),
                ("Gallery walk", "Read a partner prediction — is it measurable?"),
                ("Link to variables", "Match each prediction to what changes."),
                ("Because check", "Highlight the science reason in each prediction."),
            ],
            [
                "What makes a because clause scientific rather than a story?",
                "How can you test whether a prediction was close?",
                "Why write predictions before you measure?",
            ],
        ),
        "D": _d(
            "Prediction gallery",
            [
                "Format: I predict… [measurement] because… [science reason].",
                "Peer critique strengthens thinking before testing.",
            ],
            "Secure / Prove",
            [
                ("Final prediction", "Write one polished prediction for the ice investigation."),
                ("Critique partner", "Does their because link to heat or variables?"),
                ("Self-score", "Tick measurable, because, and unit."),
                ("Exit ready", "Exit check cold."),
            ],
            html(
                '<div class="card cream"><span class="tag try">GALLERY</span>'
                "<p style=\"margin-top:8px\">Post your best prediction. Stars for: clear unit, strong because, links to fair test.</p></div>"
            ),
        ),
    },
    10: {
        "C": _c(
            "Methods someone else could follow",
            [
                "Numbered steps help others repeat your test fairly.",
                "Equipment list matches what you actually use — no extras.",
                "Timing methods should say when the stopwatch starts and stops.",
                "A good method controls variables explicitly.",
            ],
            "Build the method",
            [
                "What detail is missing if a method says melt ice but not how much?",
                "Why list the same size ice cubes in the equipment?",
                "When should the timer start for melting in the sun?",
                "What makes a method unfair without saying cheat?",
            ],
            "Explore / Stretch",
            [
                ("Equipment four", "Name four items and why each is essential."),
                ("Step order", "Write six numbered steps a partner could follow."),
                ("Unfair spot", "Find and fix one unfair instruction."),
                ("Read-aloud test", "Partner follows your method — note confusion."),
            ],
            [
                "What is the difference between a shopping list and a method?",
                "Which step do students most often forget to time fairly?",
                "How does equipment link to controlled variables?",
            ],
        ),
        "D": _d(
            "Risk and fairness audit",
            [
                "Scientists check methods before collecting data.",
                "Sun investigations need shade breaks and water trays.",
            ],
            "Secure / Prove",
            [
                ("Audit", "Highlight controlled variables in your method."),
                ("Safety", "Add one sun-safety or spill instruction."),
                ("Partner follow", "Did your partner get the same result? If not, why?"),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Method defence",
                [
                    "Which step would confuse a new student most?",
                    "How would you make results more reliable?",
                    "What is one thing you would standardise if you repeated this?",
                    "When is it fair to stop timing?",
                ],
            ),
        ),
    },
    11: {
        "C": _c(
            "Data habits that scientists keep",
            [
                "Record <b>observations</b> with units and honest times.",
                "Tables need headings: what you changed and what you measured.",
                "Repeats help spot odd results — anomalies are not failures.",
                "Observation is what you see; inference is what you think it means.",
            ],
            "Honest recording",
            [
                "Why write 4:32 instead of about five minutes?",
                "What do you do if one repeat looks nothing like the others?",
                "How is a table better than a paragraph for melting times?",
                "What is the difference between see and conclude?",
            ],
            "Explore / Stretch",
            [
                ("Table build", "Create headings for shade vs sun melting data."),
                ("One line", "Write time + observation in table-ready format."),
                ("Sort statements", "Observation vs inference card sort."),
                ("Repeat rule", "Explain why scientists repeat measurements."),
            ],
            [
                "When is it okay to leave out an odd result?",
                "How do units prevent arguments about results?",
                "What makes a conclusion too big for the data you have?",
            ],
        ),
        "D": _d(
            "Observation vs inference",
            [
                "Observations are measurable; inferences interpret observations.",
                "Conclusions must be supported by your table.",
            ],
            "Secure / Prove",
            [
                ("Sort", "Classify five statements as see or think."),
                ("Data line", "Record one real or sample row with units."),
                ("Mini conclusion", "One sentence supported only by your numbers."),
                ("Exit ready", "Exit check."),
            ],
            html(
                '<div class="card dark"><span class="tag try">TABLE</span>'
                "<p style=\"margin-top:8px\">Sample table: Location | Time to melt (min) | Notes<br>"
                "Add one row from today's investigation or the sample data.</p></div>"
            ),
        ),
    },
    12: {
        "C": _c(
            "Graphs that tell the story",
            [
                "Bar graphs compare categories; line graphs often show change over time.",
                "Axes need labels with units; scales should start sensibly.",
                "The story: as X increases, Y… should match the data.",
                "Graphs make patterns visible that tables hide.",
            ],
            "Choose and read",
            [
                "Why might melting time vs location be a bar graph?",
                "What goes on each axis — what you change or what you measure?",
                "How can a graph mislead if the scale jumps oddly?",
                "Say the pattern aloud: Ice in sun melted ___ than ice in shade.",
            ],
            "Explore / Stretch",
            [
                ("Graph pick", "Choose bar or line for melting data — justify in one sentence."),
                ("Label axes", "Draft axis titles with units."),
                ("Read aloud", "Describe the pattern without inventing numbers."),
                ("Sketch", "Quick bar graph from class or sample data."),
            ],
            [
                "When would a line graph be better than a bar graph here?",
                "What is the story your graph tells a person who cannot see the experiment?",
                "How do labels help someone else read your work?",
            ],
        ),
        "D": _d(
            "Graph story",
            [
                "Pattern language: faster, slower, more, less, compared to.",
                "Excellent graphs are labelled, scaled and honest.",
            ],
            "Secure / Prove",
            [
                ("Type + why", "State graph type and reason in one sentence."),
                ("Story sentence", "As location changed, melting time…"),
                ("Peer read", "Can a partner retell your graph story?"),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Graph clinic",
                [
                    "What would confuse a reader about your axes?",
                    "How is a graph different from a drawing?",
                    "If results were close, how would the graph look?",
                    "What next question does your graph suggest?",
                ],
            ),
        ),
    },
    15: {
        "C": _c(
            "Booklet quality control",
            [
                "Excellent booklets link <b>method, data, graph and conclusion</b>.",
                "Conclusions answer the inquiry question using evidence.",
                "Peer feedback uses criteria — not just nice work.",
                "Reflection names skills grown, not only whether it was fun.",
            ],
            "Improve together",
            [
                "What is missing if a booklet has data but no conclusion?",
                "How is a glow different from good job?",
                "Which Science Inquiry Skill did you use when measuring fairly?",
                "What would you add to a weak sample conclusion?",
            ],
            "Explore / Stretch",
            [
                ("Criteria tick", "Tick three things an excellent booklet must show."),
                ("Glow/grow", "Improve a sample paragraph with one specific grow."),
                ("Link skills", "Match investigation steps to inquiry skills."),
                ("Checklist", "Self-assess your draft against the guide."),
            ],
            [
                "What is the difference between describing and concluding?",
                "Which part of your booklet is strongest so far?",
                "How does peer feedback improve scientific work?",
            ],
        ),
        "D": _d(
            "Peer feedback protocol",
            [
                "Glow = specific strength linked to criteria.",
                "Grow = one actionable next step.",
            ],
            "Secure / Prove",
            [
                ("Partner swap", "Give one glow and one grow using criteria words."),
                ("Revision plan", "List two edits before final submit."),
                ("Skill sentence", "I improved my ___ skill by…"),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Feedback round",
                [
                    "Which grow from a partner will you act on first?",
                    "How is scientific feedback different from social chat?",
                    "What does excellent evidence look like in a conclusion?",
                    "What skill will you carry to next term?",
                ],
            ),
        ),
    },
    16: {
        "C": _c(
            "Matter across the universe",
            [
                "The same particle ideas explain matter on Earth and in space.",
                "Stars contain plasma — extremely hot gas where particles are ionised.",
                "Water exists as ice on moons, vapour in atmospheres, and liquid where conditions allow.",
                "Science models help us understand what we cannot visit directly.",
            ],
            "Wonder and connect",
            [
                "How is steam in your kitchen similar to clouds on Jupiter?",
                "Why do scientists care about ice on other worlds?",
                "What state of matter is the Sun mostly made of?",
                "How has your particle picture changed since Lesson 1?",
            ],
            "Explore / Stretch",
            [
                ("Cosmic examples", "Name solid, liquid, gas (or plasma) beyond Earth."),
                ("Model limits", "What can particle diagrams not show well?"),
                ("Skill reflection", "Which inquiry skill grew most this unit?"),
                ("Teach-back", "Explain states of matter to Year 4 with one space example."),
            ],
            [
                "What surprised you most about matter in space?",
                "How do models help when we cannot do classroom tests?",
                "Which vocabulary word will you remember in Year 6?",
            ],
        ),
        "D": _d(
            "Celebration and next steps",
            [
                "Reflection should name evidence of learning, not feelings alone.",
                "You can classify, investigate, record, graph and conclude.",
            ],
            "Secure / Prove",
            [
                ("Skill growth", "Name one Science Inquiry Skill you grew — with evidence."),
                ("Improvement", "One thing you would do differently next investigation."),
                ("Share", "30-second celebration of your best booklet moment."),
                ("Exit ready", "Exit check."),
            ],
            html(
                '<div class="card cream"><span class="tag try">NEXT STEPS</span>'
                "<p style=\"margin-top:8px\">Write one goal for Year 6 science using today's vocabulary: "
                "particles, fair test, variables, conclusion.</p></div>"
            ),
        ),
    },
}

HASS_CD = {
    1: {
        "C": _c(
            "Needs, wants and edge cases",
            [
                "A <b>need</b> is required for survival or wellbeing; a <b>want</b> is a desire.",
                "Context matters — Wi-Fi can be a need for online learning but a want for gaming only.",
                "ABS Household Expenditure Survey (HES) shows Australian families spend differently by age and income.",
                "<b>Scarcity</b> means unlimited wants but limited money and resources.",
            ],
            "Argue N or W",
            [
                "Is a school uniform a need or a want? Give two reasons each side.",
                "When could a phone be a need rather than a want?",
                "How does scarcity force families to choose between needs and wants?",
                "Whose list would change most after a natural disaster — and why?",
            ],
            "Explore / Stretch",
            [
                ("Edge-case cards", "Sort Wi-Fi, medicine, streaming, shoes — defend one tricky item."),
                ("ABS link", "Read a spending fact aloud and link it to needs vs wants."),
                ("Scarcity sentence", "Write scarcity in a sentence about a family budget."),
                ("Perspective", "Rewrite one want as a need for a different person."),
            ],
            [
                "Which item split the class most — and what does that show?",
                "How is scarcity different from being poor?",
                "Why do economists say all choices have a cost?",
            ],
        ),
        "D": _d(
            "Scarcity proved",
            [
                "Needs and wants depend on situation and community.",
                "Scarcity explains why we cannot buy everything.",
            ],
            "Secure / Prove",
            [
                ("One-minute scarcity", "Say a correct scarcity sentence aloud to your partner."),
                ("Sort + reason", "Sort three items with because reasons."),
                ("Vocabulary", "Underline need, want and scarcity."),
                ("Exit ready", "Exit check cold."),
            ],
            discuss(
                "Budget reality",
                [
                    "What did you give up when you chose one need over a want?",
                    "How would a refugee family list differ from yours?",
                    "Why is context important in HASS answers?",
                    "What ABS data surprised you?",
                ],
            ),
        ),
    },
    2: {
        "C": _c(
            "Same planet, different lists",
            [
                "Household spending patterns differ by location, culture, income and life stage.",
                "ABS data: education spending rose sharply as more families invested in schooling.",
                "Rural, urban and remote communities prioritise different needs.",
                "Comparing lists builds empathy — not judgement.",
            ],
            "Whose list?",
            [
                "How might a farmer household list differ from a city apartment?",
                "What needs might rise when a baby joins a family?",
                "Why is water a bigger budget item in some regions?",
                "How do climate and jobs shape spending?",
            ],
            "Explore / Stretch",
            [
                ("List swap", "Draft a shopping list for someone unlike you — 8 items."),
                ("ABS fact", "Use one statistic to explain a spending difference."),
                ("Map link", "Connect Brisbane SDE life to one remote community need."),
                ("Discuss", "Share one item that appears on every list."),
            ],
            [
                "What assumption did you challenge today?",
                "How is comparing communities different from ranking them?",
                "Which ABS figure best supports your thinking?",
            ],
        ),
        "D": _d(
            "Perspective swap",
            [
                "Needs differ between people and places — always give reasons.",
                "Evidence from data strengthens HASS arguments.",
            ],
            "Secure / Prove",
            [
                ("Two places", "Name two communities and one different need each."),
                ("Reasoned list", "Explain two choices on your swapped list."),
                ("Data cite", "Mention ABS or real-world evidence once."),
                ("Exit ready", "Exit check."),
            ],
            html(
                '<div class="card cream"><span class="tag try">COMPARE</span>'
                "<p style=\"margin-top:8px\">Two-column: <b>My household</b> vs <b>Another community</b> — "
                "three needs that differ and why.</p></div>"
            ),
        ),
    },
    3: {
        "C": _c(
            "Resources that make things happen",
            [
                "<b>Natural</b>: gifts of nature (land, minerals, timber).",
                "<b>Human</b>: people skills, labour, knowledge.",
                "<b>Capital</b>: human-made tools (machines, buildings, computers).",
                "Most products need all three working together.",
            ],
            "Trace the chain",
            [
                "What natural resource is in a wooden fete sign?",
                "Where does human capital appear in a bakery?",
                "Why is a laptop capital, not natural?",
                "What happens if one resource type is missing?",
            ],
            "Explore / Stretch",
            [
                ("Classroom hunt", "Find one example of natural, human and capital."),
                ("Snack trace", "Trace a cupcake from farm to stall."),
                ("Hidden capital", "Spot capital resources in a service business."),
                ("Chain diagram", "Sketch natural → human → capital for one good."),
            ],
            [
                "Which resource type is easiest to overlook?",
                "How do human resources turn natural resources into goods?",
                "Why is education an investment in human capital?",
            ],
        ),
        "D": _d(
            "Resource chain",
            [
                "Goods and services need natural, human and capital resources.",
                "Tracing chains shows interdependence.",
            ],
            "Secure / Prove",
            [
                ("Three types", "Point to classroom examples of each resource."),
                ("Chain write", "Write a 3-step chain for a fete snack."),
                ("Label", "Label resources on a simple product sketch."),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Resource talk",
                [
                    "Which resource is scarcest for our school fete?",
                    "How would drought change natural resources for food stalls?",
                    "Why are skilled volunteers human capital?",
                    "What capital would a lemonade stall need?",
                ],
            ),
        ),
    },
    4: {
        "C": _c(
            "Goods, services and mixed buys",
            [
                "A <b>good</b> is something you can touch and take home.",
                "A <b>service</b> is help or work someone does for you.",
                "Many purchases mix both — haircut includes service and products.",
                "School fetes sell goods (cakes) and services (face painting).",
            ],
            "Split the purchase",
            [
                "Is Uber Eats a good, service or both?",
                "What part of a cake stall is service if someone ices your name?",
                "Why might a business choose goods over services?",
                "What service could our fete add without selling a product?",
            ],
            "Explore / Stretch",
            [
                ("Mash-up sort", "Split five mixed purchases into good vs service parts."),
                ("Stall design", "Plan a stall selling one good and one service."),
                ("Price talk", "Why might services be priced by time?"),
                ("Role-play", "30-second fete pitch for your stall."),
            ],
            [
                "When is the line between good and service blurry?",
                "Which stall type needs more human capital?",
                "How do goods and services meet different consumer needs?",
            ],
        ),
        "D": _d(
            "Fete stall design",
            [
                "Name one good and one service with clear examples.",
                "Stalls must match resources and consumer demand.",
            ],
            "Secure / Prove",
            [
                ("Good + service", "Name each with a fete example in 20 seconds."),
                ("Stall plan", "Sketch layout: where is good? where is service?"),
                ("Consumer why", "Who would buy each and why?"),
                ("Exit ready", "Exit check."),
            ],
            html(
                '<div class="card dark"><span class="tag try">STALL MAP</span>'
                "<p style=\"margin-top:8px\">Draw your stall. Label: good sold, service offered, "
                "resources needed (natural, human, capital).</p></div>"
            ),
        ),
    },
    5: {
        "C": _c(
            "What influences consumer choices",
            [
                "Factors include <b>price</b>, <b>advertising</b>, peers, quality, values and convenience.",
                "Advertisers target emotions — happiness, fear of missing out, belonging.",
                "Not every factor matters equally to every person.",
                "School fete choices happen quickly — factors compress into seconds.",
            ],
            "Factor detective",
            [
                "Which factor pushed you last time you bought a snack?",
                "How can an ad make a want feel like a need?",
                "Would you trust a friend's recommendation over a celebrity?",
                "How does price change when a stall supports charity?",
            ],
            "Explore / Stretch",
            [
                ("Ad annotate", "Mark hidden factors on a sample advertisement."),
                ("Rank five", "Rank price, peers, ads, quality, values for a fete toy."),
                ("Factor story", "Tell a 3-sentence purchase story naming two factors."),
                ("Ethics", "When is influence unfair to young consumers?"),
            ],
            [
                "Which factor do adults underestimate for kids?",
                "How is a school fete different from a supermarket?",
                "Can values outweigh a cheap price?",
            ],
        ),
        "D": _d(
            "Factor ranking",
            [
                "Consumer choices are shaped by multiple factors — justify your rank.",
                "Use factor vocabulary in full sentences.",
            ],
            "Secure / Prove",
            [
                ("Rank + defend", "Rank five factors for one fete purchase."),
                ("Real example", "Link a personal buy to price or peers."),
                ("Ad factor", "Name one technique ads use to influence."),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Influence check",
                [
                    "Which factor would you remove to make choosing fairer?",
                    "How do charities use values to influence buyers?",
                    "What would parents rank differently from students?",
                    "How can you spot manipulation in an ad?",
                ],
            ),
        ),
    },
    6: {
        "C": _c(
            "Finite land at Limes",
            [
                "Land is a finite natural resource — many uses compete for it.",
                "Every land-use choice is a <b>trade-off</b>: something gained, something lost.",
                "Stakeholders include farmers, students, wildlife and council.",
                "Criteria help compare options: jobs, environment, access, cost.",
            ],
            "Who wins? Who loses?",
            [
                "If Limes builds a sports field, what might be given up?",
                "How would a farmer view dust and traffic differently from students?",
                "What evidence would council need before deciding?",
                "Can everyone get what they want from the same land?",
            ],
            "Explore / Stretch",
            [
                ("Options map", "List three land uses for Limes — pros and cons each."),
                ("Stakeholder voice", "Write two sentences as farmer, two as student."),
                ("Trade-off", "State one gain and one loss for your preferred option."),
                ("Criteria score", "Score two options on environment and community."),
            ],
            [
                "Why is land-use conflict common near growing towns?",
                "How is a trade-off different from a compromise?",
                "Whose voice is hardest to hear in land debates?",
            ],
        ),
        "D": _d(
            "Stakeholder voices",
            [
                "Land decisions affect people differently — argue with reasons.",
                "Trade-offs must be named clearly.",
            ],
            "Secure / Prove",
            [
                ("Trade-off sentence", "Say what is gained and given up."),
                ("Stakeholder", "Argue one view in 40 seconds."),
                ("Criteria", "Use one criterion word: environment, jobs, access."),
                ("Exit ready", "Exit check."),
            ],
            html(
                '<div class="card cream"><span class="tag try">LIMES DECIDE</span>'
                "<p style=\"margin-top:8px\">Vote: sports field, farm expansion or nature strip. "
                "Write one sentence from a stakeholder you disagree with.</p></div>"
            ),
        ),
    },
    7: {
        "C": _c(
            "Reading graphs like a HASS expert",
            [
                "Always ask: What is this graph about? What are the units?",
                "Axes labels tell you what is being compared.",
                "ABS and other agencies publish data consumers and governments use.",
                "A conclusion must match what the graph actually shows.",
            ],
            "Tell the truth of the graph",
            [
                "What is the highest value you can read accurately?",
                "What question does this graph answer?",
                "How could someone misread the scale?",
                "What decision might a council make from spending data?",
            ],
            "Explore / Stretch",
            [
                ("Read aloud", "Point and say three values with units."),
                ("Title it", "Write a graph title that matches the data."),
                ("Two sentences", "Draft a conclusion supported only by the graph."),
                ("Question", "What new question does the graph raise?"),
            ],
            [
                "Why are units non-negotiable in data answers?",
                "How is reading a graph different from reading a story?",
                "What makes a conclusion too bold for the data?",
            ],
        ),
        "D": _d(
            "Graph story",
            [
                "Conclusions describe patterns — increase, decrease, compare.",
                "Cite the graph when you state a number.",
            ],
            "Secure / Prove",
            [
                ("Value call", "Read one value aloud correctly."),
                ("Pattern", "Write: The graph shows that…"),
                ("Decision link", "Who might use this data to decide?"),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Data decisions",
                [
                    "What spending change surprised you?",
                    "How could this data help plan a school fete?",
                    "What is missing that you still want to know?",
                    "Why trust ABS over a random blog?",
                ],
            ),
        ),
    },
    8: {
        "C": _c(
            "The Lorax and real choices",
            [
                "The Once-ler chased profit until the <b>Truffula</b> ecosystem collapsed.",
                "Consumer demand drove production — every purchase sends a signal.",
                "Short-term gain can cause long-term harm to communities and environments.",
                "Packaging at a fete can mirror Once-ler choices — cheap now, costly later.",
            ],
            "Lorax → fete",
            [
                "What Once-ler decision matches single-use fete packaging?",
                "Who plays the Lorax role in real consumer debates?",
                "How do ads make thneeds feel necessary?",
                "What responsibility do buyers share with sellers?",
            ],
            "Explore / Stretch",
            [
                ("Map the tale", "Match three Once-ler choices to real products."),
                ("Packaging audit", "List fete items with high waste."),
                ("Consumer signal", "How does buying less send a message?"),
                ("Responsibility", "Draft one personal action you can do."),
            ],
            [
                "Why do people ignore long-term harm when prices are low?",
                "How is a thneed like a gimmick toy?",
                "What would the Lorax ask our fete committee?",
            ],
        ),
        "D": _d(
            "Responsibility pledge",
            [
                "Consumer choices affect people and environments.",
                "Small actions repeated matter at community scale.",
            ],
            "Secure / Prove",
            [
                ("Choice link", "Name a choice + who is affected."),
                ("Pledge", "Write one realistic consumer action."),
                ("Lorax line", "Connect a scene to a modern product."),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Last tree talk",
                [
                    "Who is responsible — buyer, seller or government?",
                    "What packaging swap would our fete try first?",
                    "How do prices hide environmental costs?",
                    "What did the Lorax want listeners to do differently?",
                ],
            ),
        ),
    },
    9: {
        "C": _c(
            "Sustainable fete thinking",
            [
                "<b>Sustainable</b> choices meet today's needs without harming future generations.",
                "People, planet and profit (or purpose) all matter.",
                "Waste, transport and sourcing are sustainability levers at fetes.",
                "Greener options sometimes cost more upfront but save later.",
            ],
            "Audit and redesign",
            [
                "What waste do cake stalls create?",
                "How could prizes be sustainable and still fun?",
                "Who pays when we choose cheaper plastic plates?",
                "What would a carbon-conscious fete look like?",
            ],
            "Explore / Stretch",
            [
                ("Stall audit", "List one waste item and a greener swap."),
                ("Cost vs impact", "Compare cheap vs sustainable option."),
                ("30-second pitch", "Pitch your greener stall idea."),
                ("Criteria", "Score an idea on planet and people."),
            ],
            [
                "Why is sustainable not the same as expensive?",
                "What trade-off appears when going greener?",
                "How do values shape sustainable buying?",
            ],
        ),
        "D": _d(
            "Greener pitch",
            [
                "Define sustainable in your own words with people or planet.",
                "Pitch should name cost and impact honestly.",
            ],
            "Secure / Prove",
            [
                ("Definition", "One student-friendly sustainable sentence."),
                ("Pitch", "30-second greener option pitch."),
                ("Trade-off", "Name one cost of your idea."),
                ("Exit ready", "Exit check."),
            ],
            html(
                '<div class="card dark"><span class="tag try">REDESIGN</span>'
                "<p style=\"margin-top:8px\">Pick one fete item. Draw before/after: "
                "materials, waste, message to buyers.</p></div>"
            ),
        ),
    },
    10: {
        "C": _c(
            "Inquiry questions that work",
            [
                "Strong questions start with How, Why or What if.",
                "Closed yes/no questions make weak inquiries.",
                "Researchable questions need evidence you can actually find.",
                "Consumer data from ABS, surveys or interviews can answer questions.",
            ],
            "Upgrade the question",
            [
                "Why is Are fetes good? too weak?",
                "What evidence would answer How do prices affect sales?",
                "How narrow should a Year 5 inquiry be?",
                "What question would help the fete committee decide?",
            ],
            "Explore / Stretch",
            [
                ("Closed → open", "Rewrite three weak questions."),
                ("Evidence plan", "List what data would answer your question."),
                ("Partner test", "Can your partner find evidence for it?"),
                ("Fete focus", "Draft one question about consumer behaviour."),
            ],
            [
                "What makes a question too big for one unit?",
                "How is inquiry different from opinion?",
                "Which source would you try first?",
            ],
        ),
        "D": _d(
            "Data plan seed",
            [
                "Questions and evidence plans belong together.",
                "Name source types: survey, ABS, interview, observation.",
            ],
            "Secure / Prove",
            [
                ("Inquiry Q", "Write one How/Why question."),
                ("Evidence", "Name two sources that could help."),
                ("Researchable", "Explain why it is not too vague."),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Question clinic",
                [
                    "Which question would produce the most useful fete data?",
                    "What bias might a survey have?",
                    "How long should data collection take?",
                    "What will you do if sources disagree?",
                ],
            ),
        ),
    },
    11: {
        "C": _c(
            "Decision matrices in real life",
            [
                "Matrices score options against criteria — not gut feeling alone.",
                "Criteria might be price, quality, sustainability, fun.",
                "Scores should be explained, not mysterious numbers.",
                "Matrices help groups agree when opinions differ.",
            ],
            "Score with reasons",
            [
                "Why score out of 5 instead of picking a favourite?",
                "What happens if criteria conflict — cheap but wasteful?",
                "How do you avoid everyone copying the same scores?",
                "Which fete purchase suits a matrix best?",
            ],
            "Explore / Stretch",
            [
                ("Mini matrix", "Two options, two criteria — score and total."),
                ("Justify", "Write one sentence defending a score."),
                ("Camera case", "Apply matrix to Which camera should we buy?"),
                ("Group rule", "Agree how to break a tie."),
            ],
            [
                "When does a matrix fail to capture what matters?",
                "How is this more fair than loudest voice wins?",
                "What criterion should fete committees always include?",
            ],
        ),
        "D": _d(
            "Defend the winner",
            [
                "Winning option must be explained with criteria language.",
                "I like it is not a justification.",
            ],
            "Secure / Prove",
            [
                ("Winner", "State which option wins and why."),
                ("Score talk", "Explain one score without saying just because."),
                ("Trade-off", "Name what you give up in the winner."),
                ("Exit ready", "Exit check."),
            ],
            html(
                '<div class="card cream"><span class="tag try">MATRIX</span>'
                "<p style=\"margin-top:8px\">Complete a 2×2 matrix for a fete spend decision. "
                "Circle the winner and write a 2-sentence defence.</p></div>"
            ),
        ),
    },
    12: {
        "C": _c(
            "Sources you can trust",
            [
                "<b>Primary</b> sources are firsthand (interviews, receipts, photos).",
                "<b>Secondary</b> sources interpret primary data (ABS reports, news).",
                "Ads are biased — useful for factor study, not neutral facts.",
                "Cross-check surprising claims with a second source.",
            ],
            "Trust check",
            [
                "Why is ABS stronger than a random influencer for spending facts?",
                "What makes a school survey primary data?",
                "When might a blog still be useful?",
                "How do you spot a shaky source quickly?",
            ],
            "Explore / Stretch",
            [
                ("Sort sources", "Primary vs secondary card sort."),
                ("Fete source", "Pick best source for a Part A claim."),
                ("Bias spot", "Name the bias in a sample ad."),
                ("Cross-check", "Find two sources on one fact."),
            ],
            [
                "Why do Part A paragraphs need reliable evidence?",
                "What happens if everyone cites the same weak blog?",
                "How recent should data be for a fete decision?",
            ],
        ),
        "D": _d(
            "Source for the fete",
            [
                "Cite source type or name in Part A writing.",
                "Reliable evidence strengthens consumer arguments.",
            ],
            "Secure / Prove",
            [
                ("Source pick", "Name best source for one claim."),
                ("Why reliable", "Two reasons it is trustworthy."),
                ("Cite practice", "Write Author/organisation + fact."),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Expert writing",
                [
                    "How is HASS writing different from a story?",
                    "What source would you avoid — and why?",
                    "How do experts show evidence without copying?",
                    "What will you cite in Part A?",
                ],
            ),
        ),
    },
    13: {
        "C": _c(
            "Part A writing studio",
            [
                "Structure: <b>claim</b> + <b>reason</b> + <b>evidence</b>.",
                "Topic: consumer choice (MP3 player vs picnic, etc.).",
                "Formal tone — no slang; precise factor vocabulary.",
                "Paragraphs answer the question directly.",
            ],
            "Build the paragraph",
            [
                "Does your claim answer the question in the first sentence?",
                "Does evidence actually support the reason?",
                "How do you weave ABS or example data smoothly?",
                "What is the difference between evidence and opinion?",
            ],
            "Explore / Stretch",
            [
                ("Claim first", "Write one clear claim sentence."),
                ("Evidence weave", "Add one fact with source hint."),
                ("TEEL check", "Highlight claim, reason, evidence."),
                ("Peer swap", "Does evidence match the claim?"),
            ],
            [
                "What is the most common Part A weakness?",
                "How long should a Year 5 paragraph be?",
                "Why cite sources in brackets or flowing text?",
            ],
        ),
        "D": _d(
            "Peer edit pass",
            [
                "Peer edit asks: Does evidence support the claim?",
                "Glow/grow using criteria words.",
            ],
            "Secure / Prove",
            [
                ("Draft", "One paragraph with claim + evidence."),
                ("Partner edit", "One glow, one grow — specific."),
                ("Revise", "Act on one grow immediately."),
                ("Exit ready", "Exit check."),
            ],
            html(
                '<div class="card dark"><span class="tag try">CHECKLIST</span>'
                "<p style=\"margin-top:8px\">☐ Claim answers question ☐ Factor named ☐ Evidence cited "
                "☐ Formal tone ☐ No unrelated story</p></div>"
            ),
        ),
    },
    14: {
        "C": _c(
            "Marking guide decoder",
            [
                "Criteria tell you what excellent, sound and developing look like.",
                "Translate teacher language into student checklists.",
                "Haircut economics links goods, services and factors.",
                "Self-marking before submit catches gaps early.",
            ],
            "Speak criteria",
            [
                "What does justify mean in the marking guide?",
                "How is explain different from list?",
                "What evidence counts for haircut case study?",
                "Which criterion is weighted most?",
            ],
            "Explore / Stretch",
            [
                ("Decode", "Rewrite three criteria in kid-friendly words."),
                ("Sample score", "Honestly score a model paragraph."),
                ("Gap find", "What is missing from the weak sample?"),
                ("Checklist", "Build a 5-item submit checklist."),
            ],
            [
                "Why self-mark before the teacher marks?",
                "How do criteria reduce arguing about grades?",
                "What is one must-have for Part A excellence?",
            ],
        ),
        "D": _d(
            "Self-mark a sample",
            [
                "Use marking guide language in glows and grows.",
                "Three must-haves in your own words.",
            ],
            "Secure / Prove",
            [
                ("Must-haves", "List three from the guide."),
                ("Self-mark", "Score sample with one reason."),
                ("Own work", "Check your draft against guide."),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Criteria talk",
                [
                    "Which criterion is hardest to meet?",
                    "How would you improve the sample one level up?",
                    "What is excellent evidence for a service?",
                    "What will you check tonight?",
                ],
            ),
        ),
    },
    15: {
        "C": _c(
            "Part B planning board",
            [
                "Part B focuses a consumer decision for the fete context.",
                "Outline sources, factors and justification before drafting.",
                "Gap check: what evidence is still missing?",
                "Strong plans save drafting time.",
            ],
            "Plan before polish",
            [
                "What is your one-sentence focus decision?",
                "Which factors will you compare?",
                "What source will you cite for spending or sustainability?",
                "What question is still unanswered?",
            ],
            "Explore / Stretch",
            [
                ("Focus sentence", "Name fete choice + main factor."),
                ("Source list", "Three sources you could use."),
                ("Outline", "Bullet claim, reasons, evidence slots."),
                ("Gap check", "Write what evidence is missing."),
            ],
            [
                "How is Part B broader than Part A?",
                "What happens if you draft without a plan?",
                "Which factor will be your lead argument?",
            ],
        ),
        "D": _d(
            "Gap check",
            [
                "Plans should expose missing evidence early.",
                "Focus decision stays one clear sentence.",
            ],
            "Secure / Prove",
            [
                ("Focus", "One sentence: fete choice + factor."),
                ("Gaps", "List two evidence gaps and how to fill them."),
                ("Timeline", "What is due next lesson?"),
                ("Exit ready", "Exit check."),
            ],
            html(
                '<div class="card cream"><span class="tag try">PLAN BOARD</span>'
                "<p style=\"margin-top:8px\">Columns: <b>Claim</b> | <b>Factors</b> | <b>Sources</b> | "
                "<b>Still need</b> — fill sticky notes for Part B.</p></div>"
            ),
        ),
    },
    16: {
        "C": _c(
            "Feedback that improves work",
            [
                "Replace good job with criteria-linked feedback.",
                "Glow = specific strength; grow = actionable next step.",
                "Final polish targets structure, evidence and tone.",
                "Fete scenario integrates the whole unit.",
            ],
            "Feedback clinic",
            [
                "Why is Add ABS data a better grow than write more?",
                "How do you receive feedback without defending?",
                "What will you polish first — claim or evidence?",
                "How does the fete scenario test all unit ideas?",
            ],
            "Explore / Stretch",
            [
                ("Criteria glow", "Write one glow using guide words."),
                ("Action grow", "One grow your partner can do tonight."),
                ("Polish list", "Three edits before submit."),
                ("Scenario talk", "Link fete role to one unit concept."),
            ],
            [
                "What feedback helped you most this unit?",
                "How is HASS feedback like science peer review?",
                "What skill will you carry to Year 6?",
            ],
        ),
        "D": _d(
            "Final polish plan",
            [
                "Three targeted edits beat random rewriting.",
                "Celebrate growth with evidence.",
            ],
            "Secure / Prove",
            [
                ("Polish plan", "Three specific edits listed."),
                ("Peer feedback", "One glow + one grow exchanged."),
                ("Submit check", "Tick formatting, sources, spelling."),
                ("Exit ready", "Exit check."),
            ],
            discuss(
                "Fete reflection",
                [
                    "What consumer skill will help you most at the real fete?",
                    "Which lesson changed your mind most?",
                    "What would you tell Year 4 about this unit?",
                    "What is one question you still wonder?",
                ],
            ),
        ),
    },
}
