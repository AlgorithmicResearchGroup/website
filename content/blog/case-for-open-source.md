Title: The Capabilities Concern Is Wrong: Why AI Safety Work Should Be Open
Date: 2026-04-13
Tags: ai-safety, research
Summary: Why openness specifically, and why the most common objection to it is wrong.

# The Capabilities Concern Is Wrong: Why AI Safety Work Should Be Open

*A follow-up to ["Automating AI Safety Research Requires an Open Ecosystem, Not Bigger Grants"](https://algorithmicresearchgroup.com/blog/automating-ai-safety-research-requires-an-open-ecosystem-not-bigger-grants.html)*

---

In a previous post, I argued that automating AI safety research requires open, shared infrastructure rather than large grants funneled to a small number of organizations. This post is about the deeper question underneath that argument: why openness specifically, and why the most common objection to it is wrong.

## The Position of the Safety Community

AI safety is important. It is also hard, expensive, and poorly defined. Alignment as a research agenda does not have consensus definitions, consensus metrics, or consensus threat models. Reasonable researchers disagree about what the core problems even are, let alone how to solve them. This is not a criticism. It is the nature of working on a problem that is both technically deep and entangled with questions about values, institutions, and the trajectory of a technology that is changing faster than anyone predicted.

The other defining feature of the safety community's position is the asymmetry between it and the frontier AI labs. The labs have hundreds of billions of dollars in capital. They have the largest and most capable models. They have tens of thousands of GPUs. They have the best internal tooling, the most engineering talent, and the ability to fine-tune their own models on their own scaffolds using their own data. They have political relationships with governments. They set the pace of development and the terms of public discourse about it.

There is no axis on which an independent safety organization, a university lab, or a nonprofit has a structural advantage over a frontier lab. If an outside group develops a useful technique, the labs can replicate it in days. If an outside group builds a dataset, the labs can build a better one faster and cheaper. This is not a competitive landscape. It is a categorical asymmetry.

These two facts together, the ill-defined nature of the problem and the overwhelming resource advantage of the labs, should determine the strategy of the safety community. I think they point clearly toward openness and distributed collaboration, and away from the closed, guarded posture that much of the field has adopted.

## The Capabilities Concern

The most common argument against open safety work goes something like this: if safety researchers publish their tools, datasets, benchmarks, and agent infrastructure openly, that work could be absorbed by the labs and repurposed for capabilities research. Therefore safety work should be kept closed to avoid contributing to capabilities acceleration.

This argument is wrong. It is wrong because it rests on an inaccurate model of where the safety community sits relative to the labs.

Consider what the argument assumes. It assumes that a safety organization's artifacts, its agent scaffolds, its evaluation datasets, its research tooling, represent some kind of capabilities edge that the labs do not already possess. It assumes that releasing these artifacts would provide the labs with something meaningfully new. It assumes, in other words, that the safety community is near enough to the frontier that its work constitutes a meaningful capabilities input.

None of this is true. The frontier labs already have internal agents, internal evaluation infrastructure, internal datasets, and internal tooling that are comparable to or better than anything the safety community has built. They have the additional advantage of being able to train their models directly on their own infrastructure, creating a feedback loop that no outside organization can replicate. A safety organization's closed-source agent is not protecting anyone from capabilities acceleration, because the labs already have agents that are at least as capable. A privately held dataset is not preventing capabilities uplift, because the labs could replicate it in a fraction of the time and cost it took to build.

The scale of the gap matters here. People in the safety community routinely underestimate what hundreds of billions of dollars and hundreds of thousands of GPUs actually mean in practice. A dataset that represents months of work for a small safety team could be reproduced by a lab team in days, possibly less, at a cost that rounds to zero relative to their annual compute spend. An agent scaffold that represents a safety organization's primary technical contribution is, from a lab's perspective, a small project. The safety community is not sitting on capabilities secrets. It is operating at a scale that is, from the labs' vantage point, negligible.

This is not a comfortable thing to say, but it is the reality, and strategy should be built on reality. The safety community does not have a capabilities edge to protect. It never has. It almost certainly never will. The entire framing of "we must keep our work closed to prevent capabilities leakage" is built on a premise that does not hold.

## The Real Cost of Closing Safety Work

If the capabilities concern were costless, it would be harmless even if wrong. But it is not costless. The decision to keep safety work closed has concrete, measurable consequences for the field.

When a safety organization keeps its agent infrastructure closed, independent researchers cannot build on it. When evaluation datasets are held privately, smaller labs and university groups cannot benchmark against them. When tooling is not shared, effort gets duplicated across organizations that are all solving the same infrastructure problems independently. When benchmarks are proprietary, results from different groups cannot be meaningfully compared.

The net effect is straightforward. Capabilities research at the labs continues at the same pace, because it was never dependent on what the safety community published. Safety research gets slower, because researchers outside of a few well-funded organizations are locked out of the tools and data they need to contribute. The capabilities concern, put into practice, produces the opposite of its intended effect: capabilities stay the same, safety falls further behind.

This is the core dysfunction. The safety community is handicapping itself in exchange for a security benefit that does not meaningfully exist. Every closed dataset, every proprietary benchmark, every guarded scaffold is a decision to slow down the very work the community exists to do, based on a threat model that does not survive contact with the actual numbers.

## The Case for Openness

If the capabilities concern is off the table, as I believe it should be, the case for openness becomes straightforward. It is the correct strategy for a community that is tackling an ill-defined problem from a position of massive resource disadvantage.

When a problem is ill-defined, you need breadth of approach. No single organization, no matter how well-funded, can credibly claim to have the right framing for alignment. The space of possible approaches is large, and the history of the field is littered with confident claims about what the "real" problem is that turned out to be incomplete or wrong. Openness maximizes the number of independent perspectives working on the problem. It lets a grad student in a university lab try an approach that a well-funded nonprofit would never prioritize. It lets a small team iterate on a technique that a large organization dismissed. The diversity of approach that openness enables is not a nice-to-have. When the problem itself is not well enough understood to know which approaches will work, it is the primary strategic asset available to the field.

When you face a categorical resource asymmetry, coordination breadth is the one advantage you can build. The safety community will never match the labs on compute, on talent density, on iteration speed, or on access to frontier models. What it can do, if it organizes correctly, is distribute work across many independent groups that share infrastructure, build on each other's results, and collectively cover more of the problem space than any single organization could. This only works if the foundational layers, the benchmarks, datasets, evaluation protocols, and tooling, are open and shared. Without that shared layer, you don't have a distributed research effort. You have a collection of isolated groups duplicating each other's infrastructure work.

## The Uncomfortable Question

There is a related point that is worth raising, even though it is less comfortable.

The capabilities concern provides a convenient justification for opacity. If releasing work is characterized as dangerous, then not releasing work looks like responsibility. An organization can absorb significant funding, produce minimal public output, and frame the absence of visible results as a deliberate safety decision rather than a productivity problem. I am not claiming that every closed safety organization is using the capabilities argument as cover for low output. But the incentive structure makes it possible, and the community does not currently have good mechanisms for distinguishing between "we are keeping important work private for safety reasons" and "we do not have much to show."

Open work is accountable work. When research is published, when code is open-source, when benchmarks are public, the community can evaluate whether the work is good, whether the claims hold up, whether the direction is promising. Closed work, by definition, cannot be evaluated by anyone outside the organization. In a field that is absorbing hundreds of millions of dollars in philanthropic funding, that lack of accountability should be concerning regardless of one's position on the capabilities question.

## A Genuine Concern Worth Distinguishing

There is a version of the openness concern that I do take seriously, and it is important to distinguish it from the capabilities argument addressed above. Benchmarks and evaluations, specifically, face a contamination problem. If a safety benchmark's test data is publicly available, it can leak into training corpora. Models get trained on it, performance on the benchmark inflates, and the benchmark stops measuring what it was designed to measure. This is a real and well-documented problem across ML, and it applies to safety evaluations as much as any other kind.

This concern is legitimate, but it is categorically different from the capabilities concern. It is not about preventing the labs from gaining some advantage. It is about preserving the measurement validity of evaluations that the entire field depends on. The response to it is also different. Benchmark test sets may need to be held back or rotated. Evaluations may need adversarial maintenance, with retired versions replaced by new ones on a regular cadence. These are methodological problems with methodological solutions. They do not require keeping agents, datasets, tooling, or research infrastructure closed.

The distinction matters because the two concerns are frequently conflated. An organization might keep an entire evaluation pipeline closed, citing the risk of benchmark contamination, when the actual test data could be held back while the rest of the infrastructure is published openly. Contamination risk is a reason to be thoughtful about how benchmarks are released. It is not a reason to keep the broader ecosystem of safety research closed.

## Where This Leaves the Field

The safety community faces a choice about how it organizes itself. One path continues the current pattern: funded organizations working in relative isolation, keeping infrastructure closed, citing capabilities risk as justification, and producing work that the broader community cannot inspect, build on, or evaluate. The other path treats safety research infrastructure as a shared resource, accepts that the capabilities externalities of openness are negligible, and builds the kind of distributed, collaborative research ecosystem that the problem actually demands.

The labs will continue to build capabilities regardless of what the safety community publishes. That much is certain. The question is whether the safety community will organize itself to move as fast as it can, or whether it will continue to handicap itself in defense of a threat that does not survive contact with the actual numbers.