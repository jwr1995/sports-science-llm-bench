"""MSc-level sports science and sports data science exam questions.

Unlike a tool-calling benchmark, there's no single correct tool call to
check here — grading is rubric-based: each question lists `key_points`
(concepts a strong answer should cover, as keyword/phrase groups so
grading.py can do lenient substring matching) and `red_flags` (common
misconceptions that should count against the answer if present).

This is a knowledge/reasoning benchmark, not a fact-recall quiz — several
questions are deliberately "applied critical thinking" cases (category D)
that require catching a subtly wrong claim, not just reciting a definition.
"""
from __future__ import annotations

QUESTIONS = [
    # --- A: Exercise physiology ---
    {
        "id": "critical_power_model",
        "category": "physiology",
        "prompt": "Explain the physiological basis of the critical power/critical speed model, "
                  "and what its two parameters represent.",
        "key_points": [
            {"desc": "hyperbolic power/speed vs time-to-exhaustion relationship",
             "any_of": ["hyperbol", "power-duration", "speed-duration", "time to exhaustion", "time-to-exhaustion"]},
            {"desc": "critical power/speed is an asymptote / sustainable boundary",
             "any_of": ["asymptote", "sustainable boundary", "heavy", "severe"]},
            {"desc": "second parameter is a finite anaerobic/above-CP capacity (W' or D')",
             "any_of": ["w'", "w prime", "d'", "d prime", "anaerobic work capacity", "finite capacity", "finite work"]},
        ],
        "red_flags": [
            {"desc": "conflates critical speed with VO2max",
             "any_of": ["critical speed is the same as vo2max", "critical speed equals vo2max"]},
        ],
    },
    {
        "id": "minetti_descent",
        "category": "physiology",
        "prompt": "Why does Minetti's metabolic cost of locomotion curve say a runner should get faster "
                  "on any descent, and where does this break down for technical trail terrain?",
        "key_points": [
            {"desc": "cost is lower on moderate descent, minimised around -10%",
             "any_of": ["-10%", "10 percent descent", "cost is lower", "cheaper", "minimi"]},
            {"desc": "cost rises again on very steep descents (braking/eccentric work)",
             "any_of": ["steep descent", "braking", "eccentric"]},
            {"desc": "technical terrain adds a mechanical/neuromuscular limit beyond metabolic cost",
             "any_of": ["footing", "technical", "neuromuscular", "nerve", "mechanical limit"]},
        ],
        "red_flags": [
            {"desc": "claims descending is always metabolically free / always faster",
             "any_of": ["always free", "always faster", "no cost to descending"]},
        ],
    },
    {
        "id": "heat_acclimatization",
        "category": "physiology",
        "prompt": "What physiological adaptations occur during heat acclimatization, and roughly what "
                  "time course do they follow?",
        "key_points": [
            {"desc": "plasma volume expansion",
             "any_of": ["plasma volume"]},
            {"desc": "earlier/greater sweating response",
             "any_of": ["earlier sweat", "increased sweat", "sweat rate", "onset of sweating"]},
            {"desc": "reduced sweat sodium concentration",
             "any_of": ["sweat sodium", "sodium concentration"]},
            {"desc": "lower heart rate/core temp at a given workload",
             "any_of": ["lower heart rate", "reduced heart rate", "lower core temp", "reduced core temp"]},
            {"desc": "time course of roughly 1-2 weeks",
             "any_of": ["1-2 week", "one to two week", "10-14 day", "week or two"]},
        ],
        "red_flags": [
            {"desc": "claims acclimatization happens in a single session or not at all",
             "any_of": ["single session", "one workout", "cannot adapt", "no adaptation"]},
        ],
    },
    {
        "id": "substrate_crossover",
        "category": "physiology",
        "prompt": "Describe the substrate crossover concept — how does fuel use shift with exercise "
                  "intensity, and why does this matter for ultra-endurance fuelling?",
        "key_points": [
            {"desc": "fat oxidation predominates at low intensity",
             "any_of": ["fat oxidation", "fat predominates", "low intensity fat"]},
            {"desc": "carbohydrate use rises with intensity, crossover point",
             "any_of": ["crossover", "carbohydrate oxidation increases", "carb use rises"]},
            {"desc": "glycogen is limited, ties to pacing/fuelling strategy",
             "any_of": ["glycogen is limited", "limited glycogen", "glycogen store"]},
        ],
        "red_flags": [
            {"desc": "claims fat is never used at high intensity or carbs are the only fuel",
             "any_of": ["fat is never used", "only fuel used", "carbohydrate is the only fuel"]},
        ],
    },
    # --- B: Training theory / periodization ---
    {
        "id": "banister_ctl_atl",
        "category": "training_theory",
        "prompt": "Explain Banister's impulse-response model and how CTL/ATL/TSB are derived from it. "
                  "What's a key limitation?",
        "key_points": [
            {"desc": "training load converted to fitness/fatigue via exponentially weighted moving averages",
             "any_of": ["exponentially weighted", "moving average", "impulse-response", "impulse response"]},
            {"desc": "CTL = long time-constant fitness, ATL = short time-constant fatigue",
             "any_of": ["chronic training load", "acute training load", "long time-constant", "short time-constant"]},
            {"desc": "TSB = CTL minus ATL, represents form/freshness",
             "any_of": ["tsb", "training stress balance", "form", "freshness"]},
            {"desc": "limitation: treats training load as a single fungible number across all training types",
             "any_of": ["single number", "fungible", "doesn't capture", "does not capture", "non-linear", "individual dose-response", "dose response"]},
        ],
        "red_flags": [
            {"desc": "claims CTL/ATL are directly measured physiological quantities",
             "any_of": ["directly measured physiological", "actual physiological measurement"]},
        ],
    },
    {
        "id": "acwr_critique",
        "category": "training_theory",
        "prompt": "What is the acute:chronic workload ratio (ACWR) meant to predict, and what is the main "
                  "methodological critique of it?",
        "key_points": [
            {"desc": "ratio of short-term to long-term load, meant to flag injury risk from load spikes",
             "any_of": ["injury risk", "load spike", "acute load", "chronic load"]},
            {"desc": "mathematical coupling critique (acute is a subset of chronic)",
             "any_of": ["mathematical coupling", "coupling", "subset of the chronic", "spurious"]},
            {"desc": "attributed to Impellizzeri or described as contested evidence",
             "any_of": ["impellizzeri", "contested", "weak evidence", "criticised", "criticized"]},
        ],
        "red_flags": [
            {"desc": "claims ACWR is a definitively proven causal predictor with no criticism",
             "any_of": ["definitively proven", "no criticism", "no methodological concern"]},
        ],
    },
    {
        "id": "polarized_training",
        "category": "training_theory",
        "prompt": "What is polarized training intensity distribution, and what's the evidence base behind it?",
        "key_points": [
            {"desc": "roughly 80/20 low/high intensity split",
             "any_of": ["80%", "80/20", "80-20", "eighty percent"]},
            {"desc": "less time in moderate/threshold zone",
             "any_of": ["moderate intensity", "threshold zone", "middle zone", "grey zone"]},
            {"desc": "associated with Seiler / elite athlete training distribution research",
             "any_of": ["seiler", "elite athlete", "elite endurance athlete"]},
        ],
        "red_flags": [
            {"desc": "claims polarized means all-out/maximal training or has no evidence base",
             "any_of": ["all training should be maximal", "no evidence", "purely anecdotal"]},
        ],
    },
    {
        "id": "taper_physiology",
        "category": "training_theory",
        "prompt": "Physiologically, why does a taper typically reduce training volume while maintaining or "
                  "increasing intensity in the final weeks before a race?",
        "key_points": [
            {"desc": "reduces fatigue while fitness adaptations decay slowly",
             "any_of": ["reduce fatigue", "fatigue dissipat", "fitness decays slowly", "fitness is preserved"]},
            {"desc": "maintaining intensity preserves neuromuscular sharpness",
             "any_of": ["neuromuscular", "sharpness", "maintain intensity"]},
            {"desc": "goal is peak readiness/form on race day",
             "any_of": ["race day", "peak readiness", "form", "freshness"]},
        ],
        "red_flags": [
            {"desc": "claims tapering means stopping training entirely or cutting intensity too",
             "any_of": ["stop all training", "complete rest", "reduce intensity as well"]},
        ],
    },
    # --- C: Sports data science methodology ---
    {
        "id": "fitting_critical_speed",
        "category": "data_science",
        "prompt": "You're fitting a two-parameter critical speed model to one athlete's flat-road best "
                  "efforts. What estimation approach would you use, and what's the main pitfall with "
                  "limited data across the intensity-duration spectrum?",
        "key_points": [
            {"desc": "nonlinear or reparameterized (e.g. distance-time) regression",
             "any_of": ["nonlinear", "non-linear", "regression", "least squares"]},
            {"desc": "need durations spanning short maximal to longer sub-maximal efforts",
             "any_of": ["multiple durations", "short maximal", "range of durations", "spread of durations"]},
            {"desc": "too few/clustered durations makes parameters poorly identified/collinear",
             "any_of": ["collinear", "poorly identified", "not identifiable", "ill-conditioned"]},
            {"desc": "extrapolation outside the fitted range is unreliable",
             "any_of": ["extrapolat"]},
        ],
        "red_flags": [
            {"desc": "claims a single time trial is sufficient to estimate both parameters",
             "any_of": ["single time trial is sufficient", "one trial is enough", "one effort is enough"]},
        ],
    },
    {
        "id": "low_sample_r2",
        "category": "data_science",
        "prompt": "Why doesn't a low sample-level R² (e.g. 0.04) on individual 100m gradient-vs-speed "
                  "samples necessarily mean the underlying grade-speed model is wrong?",
        "key_points": [
            {"desc": "individual short samples carry substantial noise",
             "any_of": ["noise", "noisy", "measurement error", "gps noise", "stride-level"]},
            {"desc": "low point-level R2 can coexist with a real trend seen in aggregate/back-test",
             "any_of": ["aggregate", "back-test", "backtest", "out-of-sample", "held-out", "held out"]},
            {"desc": "right validation is predictive performance, not raw point fit",
             "any_of": ["predictive performance", "out-of-sample prediction", "validate", "validation"]},
        ],
        "red_flags": [
            {"desc": "claims a low R2 always means the model has no value",
             "any_of": ["no value", "model is wrong", "useless model"]},
        ],
    },
    {
        "id": "mileage_injury_causation",
        "category": "data_science",
        "prompt": "A study finds a strong positive correlation between weekly mileage increase and injury "
                  "incidence across a group of runners, and concludes mileage spikes cause injury. What "
                  "are the methodological concerns with this causal claim?",
        "key_points": [
            {"desc": "correlation does not establish causation",
             "any_of": ["correlation does not", "correlation is not causation", "does not imply causation"]},
            {"desc": "possible confounders",
             "any_of": ["confound", "prior injury", "training experience", "fitness level"]},
            {"desc": "reverse causation or selection effects",
             "any_of": ["reverse causation", "selection effect", "selection bias"]},
            {"desc": "mathematical coupling if ratio-based, or ecological fallacy",
             "any_of": ["coupling", "ecological", "aggregate level", "individual level"]},
        ],
        "red_flags": [
            {"desc": "claims correlation proves causation here",
             "any_of": ["correlation proves causation", "this proves mileage causes"]},
        ],
    },
    {
        "id": "in_sample_out_of_sample",
        "category": "data_science",
        "prompt": "When back-testing a race-time prediction model fitted on an athlete's own race history, "
                  "why is it important to distinguish in-sample from out-of-sample error, and how would "
                  "you construct a fair out-of-sample test with a small number of races?",
        "key_points": [
            {"desc": "in-sample error is optimistic",
             "any_of": ["in-sample", "in sample", "optimistic", "overfit"]},
            {"desc": "out-of-sample gives honest estimate of predictive performance",
             "any_of": ["out-of-sample", "out of sample", "held-out", "held out", "honest estimate"]},
            {"desc": "leave-one-out cross-validation for small N",
             "any_of": ["leave-one-out", "leave one out", "cross-validation", "cross validation"]},
            {"desc": "held-out cases must not be systematically different/confounded",
             "any_of": ["systematically different", "confounded", "bias the test"]},
        ],
        "red_flags": [
            {"desc": "claims in-sample error is a good estimate of future accuracy",
             "any_of": ["in-sample error is a good estimate", "in sample is sufficient"]},
        ],
    },
    {
        "id": "monte_carlo_bands",
        "category": "data_science",
        "prompt": "Why might a race-time simulator benefit from reporting a Monte Carlo confidence band "
                  "instead of a single point-estimate finish time, and what does the spread actually "
                  "represent?",
        "key_points": [
            {"desc": "captures uncertainty from input variability rather than false precision",
             "any_of": ["uncertainty", "false precision", "variability"]},
            {"desc": "point estimate hides sensitivity to assumptions",
             "any_of": ["sensitiv", "hides", "single point estimate"]},
            {"desc": "spread reflects genuine model/input uncertainty, not decoration",
             "any_of": ["genuine", "reflects", "not decorative", "not cosmetic"]},
        ],
        "red_flags": [
            {"desc": "claims a point estimate is always sufficient or MC output is exact guaranteed bounds",
             "any_of": ["always sufficient", "no value", "guaranteed bounds", "exact bounds"]},
        ],
    },
    # --- D: Applied critical thinking ---
    {
        "id": "vdot_vs_critical_speed",
        "category": "critical_thinking",
        "prompt": "Are VDOT (Daniels) and critical speed the same underlying physiological construct? "
                  "Explain the difference.",
        "key_points": [
            {"desc": "VDOT derived from race performance via nomogram/equations, used to prescribe paces",
             "any_of": ["nomogram", "daniels", "vdot", "prescribe pace", "training pace"]},
            {"desc": "critical speed is the asymptote of the power/speed-duration model with distinct basis",
             "any_of": ["asymptote", "power-duration", "speed-duration", "heavy", "severe"]},
            {"desc": "related but distinct, not interchangeable",
             "any_of": ["distinct", "not interchangeable", "not the same", "different construct"]},
        ],
        "red_flags": [
            {"desc": "claims VDOT and critical speed are exactly the same thing",
             "any_of": ["exactly the same thing", "identical construct", "interchangeable with no difference"]},
        ],
    },
    {
        "id": "zero_fitted_coefficient",
        "category": "critical_thinking",
        "prompt": "A coach says 'the descent coefficient in my durability model fit to zero, so descending "
                  "is free and causes no fatigue.' What's the more careful interpretation?",
        "key_points": [
            {"desc": "zero coefficient can reflect collinearity/confounding, not true absence of effect",
             "any_of": ["collinear", "confound", "correlated with", "not separately identifiable"]},
            {"desc": "absence of evidence is not evidence of absence",
             "any_of": ["absence of evidence", "not evidence of absence", "doesn't prove", "does not prove"]},
            {"desc": "correct statement is the effect isn't separately identifiable, not that it's zero",
             "any_of": ["not identifiable", "cannot be separated", "can't be separated"]},
        ],
        "red_flags": [
            {"desc": "claims a zero-fitted coefficient proves the effect doesn't exist",
             "any_of": ["proves the effect doesn't exist", "proves there is no effect", "definitively no effect"]},
        ],
    },
    {
        "id": "individual_heat_sensitivity",
        "category": "critical_thinking",
        "prompt": "An athlete's heat sensitivity is measured as 2-3x higher than population-average figures "
                  "from the literature. Should this be treated as a data error and corrected to the "
                  "population value?",
        "key_points": [
            {"desc": "individual variation can genuinely differ substantially from population averages",
             "any_of": ["individual variation", "genuine difference", "individual physiology"]},
            {"desc": "population figures may come from different populations/methods and not transfer",
             "any_of": ["different population", "may not transfer", "methodology differ"]},
            {"desc": "check internal evidence quality before overwriting with a population prior",
             "any_of": ["evidence quality", "sample size", "consistency", "check the data"]},
        ],
        "red_flags": [
            {"desc": "claims individual measurements should always be overridden by population averages",
             "any_of": ["should always be overridden", "must be corrected to the population", "always a measurement error"]},
        ],
    },
]
