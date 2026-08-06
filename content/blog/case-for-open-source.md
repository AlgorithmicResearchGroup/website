Title: The Capabilities Concern Is Wrong: Why AI Safety Work Should Be Open
Date: 2026-04-13
Tags: ai-safety, research
Summary: Why openness specifically, and why the most common objection to it is wrong.

# The Position of the Safety Community

I think AI safety is important. It is also hard, expensive, and poorly defined. Alignment as a research agenda does not have consensus definitions, consensus metrics, or consensus threat models. Reasonable researchers disagree about what the core problems even are, let alone how to solve them. Imho this puts us at a disadvantage in relation to capabilities research, whose broad objectives are: 1) Make loss go down 2) Make capabilities less spikey

Another defining feature of the AI safety community’s position is the resource asymmetry between independent safety orgs and the frontier AI labs. I’ll qualify the rest of this post by saying the labs also do awesome, serious safety work. Some of the best safety researchers in the world work at Anthropic, OpenAI, DeepMind, and other frontier organizations. This is not an adversarial framing.

We can all agree that the labs have hundreds of billions of dollars in capital, the largest and most capable models, tens of thousands of GPUs, the best internal tooling, and the ability to fine-tune their own models on their own scaffolds using their own data.

Independent safety organizations, university labs, and nonprofits just operate at a totally categorically different scale.

I think this asymmetry matters a lot when thinking about how we distribute our work, and what small advantages we have over the labs. Independent safety organizations cannot compete with frontier labs on compute, capital, model access, or internal infrastructure. Their comparative advantages are independence, diversity of approach, and the ability to coordinate work across many groups.

## The Capabilities Concern

One of the most common arguments I hear against open safety work goes something like this:
"If safety researchers publish their tools, datasets, benchmarks, and agent infrastructure openly, that work could be absorbed by the labs and repurposed for capabilities research. Therefore safety work should be kept closed to avoid contributing to capabilities acceleration."

I think this argument is generally wrong, with a few caveats. Consider what the argument assumes:

* An independent researcher or safety org’s output represents some kind of capabilities edge that the labs do not already possess.
* Releasing these artifacts would provide the labs with something meaningfully new.

Independent safety organizations may occasionally produce work that provides a narrow capabilities advantage. But in most cases, they do not have an edge large enough to justify the systemic costs of keeping their work closed.

The different artifacts also have different risk profiles. A benchmark or evaluation protocol is not the same as an effective autonomous research scaffold or a technique for eliciting dangerous capabilities. Openness should be the default, but there should be exceptions where a concrete threat model shows that releasing something would materially accelerate dangerous capabilities.

## The Real Cost of Closing Safety Work

The decision to keep safety work closed has concrete consequences for the field.

First and foremost, safety research gets slower because researchers outside of a few well-funded organizations are locked out of the tools and data they need to contribute.

By not distributing their work, the safety community is often handicapping itself in exchange for a security benefit that is vague or negligible. Every closed dataset, proprietary benchmark, and scaffold should require a specific justification rather than a general appeal to capabilities risk.

This asymmetry should determine how the independent safety community organizes itself. It points toward openness and distributed collaboration, not a closed posture justified by capabilities concerns that mostly do not apply.

When you are tackling an ill-defined problem from a massive resource disadvantage, breadth is the main advantage you can build. Open benchmarks, datasets, evaluation protocols, and tooling let more groups test different approaches and build on each other’s work. The choice is between isolated organizations duplicating effort or a shared research ecosystem capable of covering more of the problem space.
