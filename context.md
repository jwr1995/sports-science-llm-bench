# Reference material: sports science & sports data science

Canonical frameworks and sources a strong MSc-level answer in this domain
would draw on. Use these by name where relevant; don't invent citations
that aren't grounded in real, established methodology.

## Exercise physiology

- **Critical power / critical speed model** (Monod & Scherrer, 1965; later
  physiological grounding by Poole, Jones, Vanhatalo and colleagues): a
  hyperbolic relationship between power or speed and time-to-exhaustion.
  Critical power/speed is the asymptote — a sustainable boundary
  approximating the edge between the "heavy" and "severe" exercise
  intensity domains. The second parameter (W' or D') is a finite work/
  distance capacity available above that asymptote.
- **Minetti's cost of locomotion curve** (Minetti et al., 2002, "Energy
  cost of walking and running at extreme uphill and downhill slopes"): a
  polynomial curve relating the metabolic cost of locomotion to gradient.
  Cost is minimised around -10% descent and rises sharply on both very
  steep descents and steep climbs. This is a metabolic-cost model, not a
  speed model — on technical terrain, mechanical/neuromuscular limits
  (footing, eccentric loading, nerve) can dominate over what the metabolic
  curve alone would predict.
- **Substrate crossover concept**: fat oxidation predominates at low
  exercise intensity; carbohydrate oxidation rises with intensity and
  becomes dominant above a "crossover" point. Since glycogen stores are
  limited, this interacts directly with pacing and fuelling strategy in
  endurance events. Training status shifts where the crossover point sits.
- **Heat acclimatization physiology** (summarised in Sawka and colleagues'
  work): repeated heat exposure over roughly 1-2 weeks drives plasma
  volume expansion, earlier onset and increased rate of sweating, reduced
  sweat sodium concentration, and a lower heart rate/core temperature at a
  given workload.
- **Sports nutrition / glycogen**: classic glycogen depletion work
  (Bergström & Hultman) established muscle glycogen as a limiting
  endurance fuel; Jeukendrup's later work on multiple-transportable-
  carbohydrate ingestion established that combining glucose and fructose
  sources raises achievable carbohydrate oxidation rates (commonly cited
  figures around 90 g/h) versus a single carbohydrate source.
- **Sleep and athletic performance** (Halson and colleagues): sleep
  restriction impairs recovery, glucose metabolism, and endurance/cognitive
  performance in athletes; sleep is now treated as a first-class recovery
  variable alongside training load.

## Training theory and periodization

- **Banister's impulse-response / TRIMP model** (Banister, 1975/1991):
  training load is transformed into fitness and fatigue signals via
  exponentially weighted moving averages with different time constants.
  Popularised in practice as CTL (chronic training load / "fitness",
  long time-constant), ATL (acute training load / "fatigue", short
  time-constant), and TSB = CTL − ATL ("form"/freshness), as used in
  tools like TrainingPeaks' Performance Manager. A key limitation: the
  model assumes a single training-load number (e.g. TSS) is a valid,
  fungible proxy for physiological stress across very different types of
  training, and doesn't capture non-linear or individual dose-response.
- **Acute:chronic workload ratio (ACWR)** (popularised by Gabbett as an
  injury-risk indicator): the ratio of short-term to long-term training
  load. Methodologically critiqued by Impellizzeri and colleagues for
  mathematical coupling (the acute load is a subset of the chronic load
  it's divided by, which can inflate the apparent relationship) and for
  obscuring the absolute loads involved; evidence for a precise causal
  "sweet spot" ratio is contested.
- **Polarized training intensity distribution** (associated with Seiler's
  research on elite endurance athletes): roughly 80% of training time at
  low intensity (below the first physiological threshold) and about 20%
  at high intensity, with comparatively little time spent in the
  moderate/threshold zone, as observed in many elite endurance athletes'
  actual training distributions.
- **Tapering**: reducing training volume while maintaining or slightly
  increasing intensity in the final one to three weeks before a race,
  allowing accumulated fatigue to dissipate while fitness adaptations
  (which decay more slowly) are largely preserved, and neuromuscular
  sharpness is maintained by keeping some intensity in the plan.

## Sports data science methodology

- **Fitting individual physiological models**: two-parameter models like
  critical speed require effort data spanning multiple durations —
  typically both short maximal efforts (a few minutes) and longer
  sub-maximal efforts — to identify both parameters reliably; with too few
  or too clustered durations the parameters become poorly identified
  (collinear), and extrapolating far outside the fitted duration range is
  unreliable.
- **Point-level noise vs aggregate signal**: a low R² on noisy, granular
  samples (e.g. individual short GPS-derived speed/gradient samples) does
  not by itself invalidate a real underlying relationship — point-level
  noise can coexist with a genuine, well-supported trend that shows up
  clearly in aggregate or out-of-sample evaluation (e.g. a back-test
  against whole-race outcomes). The right way to validate a predictive
  model is out-of-sample predictive performance, not raw point-level fit.
- **Correlation, confounding, and causal claims in training-load research**:
  observed correlations between training-load metrics and injury or
  performance outcomes are vulnerable to confounding (e.g. prior injury
  history, fitness level, training experience), reverse causation, and —
  for ratio-based metrics — mathematical coupling. Aggregate/ecological
  correlations don't necessarily hold at the individual level.
- **In-sample vs out-of-sample evaluation**: error measured on the same
  data a model was fitted to is systematically optimistic. With a small
  number of observations (e.g. an individual athlete's race history),
  leave-one-out cross-validation is a practical way to get an honest
  estimate of predictive performance, provided held-out cases aren't
  systematically different (e.g. confounded) in a way that biases the
  test.
- **Uncertainty quantification**: reporting a distribution or confidence
  band (e.g. via Monte Carlo simulation over plausible input variation)
  rather than a single point estimate communicates the model's actual
  uncertainty and avoids false precision; the spread should reflect
  genuine variability in the underlying inputs/assumptions, not be a
  cosmetic addition.
