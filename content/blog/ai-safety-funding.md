Title: Automating AI Safety Research Requires an Open Ecosystem, Not Bigger Grants
Date: 2026-04-03
Tags: ai-safety, funding, research
Summary: A response to Marius Hobbhahn's ["There should be $100M grants to automate AI safety"](https://www.lesswrong.com/posts/qdhyrN4uKwBAftmQx/there-should-be-usd100m-grants-to-automate-ai-safety)

# Automating AI Safety Research Requires an Open Ecosystem, Not Bigger Grants

*A response to Marius Hobbhahn's ["There should be $100M grants to automate AI safety"](https://www.lesswrong.com/posts/qdhyrN4uKwBAftmQx/there-should-be-usd100m-grants-to-automate-ai-safety)*

---

Marius Hobbhahn published a post today arguing that funders should create staged scaling grants for automated AI safety work. The core idea: fund organizations to build safety pipelines, show they scale, then double down with increasingly large grants. I agree with the urgency and most of the technical framing. Where I disagree is the implicit model for how this work should be organized.

## The Problem with Hub-and-Spoke Funding

The proposal, at its core, assumes a small number of well-funded organizations will each build their own scaling pipelines, demonstrate results, and receive progressively larger grants. This is a reasonable model for many kinds of research. It is the wrong model for this problem.

Automating AI safety research requires an ecosystem, not a single pipeline. You need benchmarks to measure whether agents can actually do research. You need datasets to train and evaluate those agents. You need scaffolding and infrastructure to run experiments at scale. You need evaluation methodology that doesn't immediately get goodharted. And you need all of these things to be interoperable so that results from one group are comparable to and buildable upon by another.

If five organizations each receive $20M and build five independent, incompatible pipelines, you haven't spent $100M on automating AI safety. You've spent $100M on five siloed prototypes that can't talk to each other.

## This Needs to Be Open, Collaborative, and Cross-Sector

Where my opinion differs from some in this space is that I think this work should be highly collaborative, moderately open source, and come from a mix of nonprofits, for-profits, and academia.

There have been signals that work like this is already happening within a few safety organizations, and that it's being kept closely guarded. I don't know this for a fact, but the inference seems reasonable given the lack of public output relative to the amount of talent and funding in those orgs. If that is the case, I don't think that approach will get us there, regardless of the amount of funding behind it.

The concern that this work is dual-use, that open infrastructure for automated safety research could be leveraged by labs for capabilities research, is presumably part of the reasoning for keeping it guarded. It should be taken seriously but ultimately shelved as a blocking consideration. That ship has sailed. The frontier labs are already automating their research processes. The capabilities side of automated AI research is happening with or without the safety community's participation. Automated research will exist regardless. The question is whether the safety community will have comparable tooling, shared benchmarks, and open infrastructure, or whether it will be perpetually playing catch-up with proprietary tools it can't inspect or build on.

This needs to be bottom-up and community-driven. A grad student at a university, a researcher at a safety nonprofit, and a team at a frontier lab should all be able to contribute to, evaluate against, and build on the same foundation. That is not what happens when you give $100M to three organizations and tell them to show you a scaling plot.

## What This Actually Looks Like

The proposed model: one organization builds a safety pipeline, shows it scales on a compute-versus-proxy plot, and receives progressively larger grants to scale it further. The alternative: the pipeline components (benchmarks, datasets, evaluation protocols) are public infrastructure, and many organizations independently build and test agents against that shared layer.

This pattern exists in other fields. Genomics organized itself around publicly funded shared databases (GenBank, BLAST) maintained as infrastructure, with fully independent and competitive research on top. Any lab in the world can query the same databases, submit new data, and publish results. Nobody owns the infrastructure, and the research agenda is set by the researchers, not the database maintainers. The result is a field that moves fast, builds on itself, and doesn't fragment into incompatible silos.

The equivalent for automated safety research has three layers:

**A maintained open benchmark and evaluation layer.** Think SWE-bench but for automated safety research, adversarially maintained, versioned, with clear methodology for reporting results. Multiple benchmarks covering different aspects of the problem: agent research capability, interpretability automation, red-teaming, eval generation. Crucially, the benchmark maintainers should be independent of the groups competing on the benchmarks. Benchmarks get retired and replaced as they saturate or get goodharted. This is a standing research program that requires continuous maintenance.

**Open datasets as a public good.** Parsed papers, code repositories, experimental results, methodological knowledge. The raw material that automated research agents need to work with. A living, continuously maintained resource. Most of this curation work is currently done by individual researchers as side projects. It should be funded as core infrastructure.

**Distributed agent development with shared evaluation.** Anyone can build agents, scaffolding, pipelines. No central authority decides the "right" approach. Groups publish their methods, share what works, iterate in the open. The benchmarks and datasets provide the common measuring stick. A grad student, an independent lab, a safety nonprofit, and a frontier lab team all evaluate against the same benchmarks and compare results on equal footing. Competition happens at the research layer, not the infrastructure layer.

**Shared compute infrastructure.** There is already precedent here. CAIS runs a [compute cluster](https://safe.ai/work/compute-cluster) that provides free GPU access to safety researchers, currently supporting around 20 research labs. This model works: shared compute lowers the barrier to entry for smaller teams and independents who would otherwise be priced out of meaningful experiments. Scaling this kind of shared resource, and pairing it with the open benchmarks and datasets described above, would go a long way toward enabling the distributed research ecosystem this problem requires.

Some of this is already happening, and it's worth calling out the work that's pointing in the right direction. UK AISI's [Inspect](https://inspect.ai-safety-institute.org.uk/) is an open-source framework for LLM evaluations that anyone can use and extend. [ControlArena](https://github.com/UKGovernmentBEIS/control-arena) provides a shared benchmark for control research. METR's [task standard](https://github.com/METR/task-standard) defines a common format for agent evaluation tasks that other groups can build on. These are the kinds of open, shared infrastructure components that make a distributed research ecosystem possible. The field needs more of this, and it needs sustained funding behind it.

## On the Dual-Use Question

Infrastructure for automated safety research could theoretically be repurposed for automated capabilities research. But this framing treats the safety community as if it operates in a vacuum. It does not. The frontier labs have massive internal teams working on automated research. They have more compute, more data, and more engineering resources than the safety community will ever have. The marginal contribution of open safety infrastructure to capabilities acceleration is negligible compared to what is already happening inside these organizations.

IMHO, on the other hand, the cost of keeping safety research infrastructure closed is enormous. It means duplicated effort. It means smaller organizations and independent researchers are locked out. It means the field cannot build on itself. It means we are choosing to handicap the safety side of the race in exchange for a security benefit that does not meaningfully exist.

The pragmatic position is: build it open, build it collaboratively, and accept that the capabilities externalities will be present but slim. 

## What I'd Like to See

I'd like to see funders take this seriously at the ecosystem level. That means:

1. Dedicated funding for open research infrastructure (benchmarks, datasets, shared tooling) with multi-year commitments, not one-off project grants.
2. Explicit preference for collaborative, cross-sector proposals over single-organization pipelines.
3. Willingness to fund maintenance as well as creation. Benchmarks decay. Datasets need updating. Infrastructure needs upkeep. This work is unglamorous, but without it, everything else falls apart.

I'll have more to say about specific technical directions and how existing open-source work fits into this picture in a follow-up post. For now, I'll just say: the post is right that this is urgent. I think the path forward is more open and more collaborative than what it proposes.