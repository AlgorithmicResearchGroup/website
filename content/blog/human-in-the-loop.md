Title: Design the Handoff
Date: 2026-05-28
Slug: human-in-the-loop
Summary: Human review is part of the product. Design the evidence, decisions, and recovery path with the same care as the automation.
Tags: announcements, consulting, operations
Home_order: 03
Home_label: Studio note
Author: ARG Studio
Template: article
Category: blog
Url: blog/human-in-the-loop.html
Save_as: blog/human-in-the-loop.html

“Send it to a human” leaves a surprising amount of software unspecified. Which human? What will they see? What can they change? Where does the case go afterward? What happens while they are away?

Those questions belong in the first version of an automated workflow. The review interface, queue, and recovery path determine whether the system saves work or quietly creates another job. A capable model can still leave its operator with a miserable experience.

I want the handoff to be as carefully designed as the part that runs by itself.

## Give the reviewer a decision

Consider a hypothetical document intake system. It has extracted a company name, a date, and a reference number. Two pages disagree about the date. The system could send the entire packet to a reviewer with a red warning icon. That makes the reviewer repeat the extraction before they can resolve the disagreement.

A more useful interface shows both dates, the relevant passages, and the field that will be written to the destination record. The reviewer can choose a date, enter a correction, or ask for clarification. The system records the choice and resumes from that point.

That small interaction needs several things to work together:

- The source material stays attached to the proposed answer.
- The reason for escalation is specific.
- The available actions correspond to real next steps.
- The reviewer can correct the result without rebuilding the case.
- Resuming the workflow cannot accidentally repeat an action already completed.

Open-ended judgment still has a place. A customer dispute may require context that no form captures. Give that case an owner and a way to explain the decision. Forcing every exception into an approve/reject pair only hides the uncertainty.

## Decide what can proceed

Predictable inputs, explicit rules, and inexpensive recovery make autonomous processing easier to justify. Scheduled reports, routine data transformations, backups, and established system integrations are useful starting points. Ambiguous documents and consequential communications need more careful boundaries.

Confidence scores can help route work, provided their relationship to actual errors has been measured. A score of 95% and a score of 62% are useful only when testing shows what those numbers mean for this task. Choosing a 90% cutoff by intuition gives the interface a precise-looking number without establishing reliability.

Use representative historical cases to compare scores with observed mistakes. Separate error types. A wrong category that can be changed later deserves a different treatment from an action that is difficult to reverse. High-confidence cases might proceed, an intermediate band might receive a quick check, and uncertain cases might require a fuller investigation.

The thresholds belong to a particular workflow and its consequences. Revisit them when the inputs, model, or operating rules change.

## Budget the review work

Suppose a workflow receives 500 documents a day and each takes ten minutes to process. That is about 83 hours of handling time. If 80% can pass through automatically and the remaining 100 still take ten minutes each, human handling falls to about 17 hours: a fivefold reduction.

Those are illustrative assumptions. The remaining cases may be harder than the average case, and monitoring takes time too. Measure both before claiming the saving. Even a 60–90% reduction would leave a real review operation to staff and maintain.

Track the age of the oldest unresolved case alongside the number of cases automated. A growing exception queue can conceal a system that is shifting its hardest work downstream. Make ownership, escalation, and overdue cases visible.

## Make corrections useful

An override should leave a record of what changed and why. That record can reveal a missing rule, a confusing interface, an inadequate example, or a model error. Each diagnosis suggests different work. Changing the prompt will not repair an interface that presents the wrong source page. The same decision history makes the workflow easier to audit.

Corrections also create material for regression tests. Keep representative failures and check them when the system changes. Reviewers should be able to see that their feedback affects the next version; otherwise the same corrections become a recurring tax.

Human involvement can decrease as evidence accumulates. Six months with few overrides is useful information, especially when spot checks support it. Remove a review step deliberately, retain monitoring, and keep a route back to manual handling.

Before shipping, walk one uncertain case through the entire system. Follow it from arrival to a named reviewer, through a correction, and back into the workflow. That exercise exposes more than another flawless demo of the happy path.
