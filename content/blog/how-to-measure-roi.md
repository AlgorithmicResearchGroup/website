Title: Count the Whole Workflow
Date: 2026-05-28
Slug: how-to-measure-roi
Summary: A useful automation calculation includes exceptions, operating costs, and what happens to the time you recover.
Tags: announcements, consulting, operations
Author: ARG Studio
Template: article
Category: blog
Url: blog/how-to-measure-roi.html
Save_as: blog/how-to-measure-roi.html

The easiest automation metric to collect is often the least useful on its own. Documents processed, model accuracy, seconds per response: each describes part of the system. None tells you whether the finished workflow is worth maintaining.

I want the measurement to follow a case from arrival to completion, including its corrections and delays. The economics become much clearer once the whole path is visible.

## Establish a baseline with a distribution

Before changing the workflow, measure volume, handling time, elapsed time, errors, and cost. Handling time is active work. Elapsed time includes waiting. A form may take ten minutes to process and two days to reach the person who can process it.

Record the spread as well as the average. If most cases take two minutes and a smaller group takes an hour, that distinction will shape the automation. Sample completed work for errors when no reliable error log exists. Describe the sample and its limitations so the next measurement can be compared fairly.

Set release criteria in the same units. Illustrative targets might include reducing handling time from 12 minutes to under three, maintaining a measured 94% accuracy baseline, or bringing elapsed time from 48 hours to under four. If the target is 80% autonomous processing within 90 days, define which incoming cases count toward that percentage.

## Keep exceptions in the arithmetic

Suppose the current process takes ten minutes per case. In a hypothetical automated version, 80% of cases take two minutes of human handling and the other 20% take fifteen minutes. The weighted average is:

    (0.80 × 2 minutes) + (0.20 × 15 minutes) = 4.6 minutes

That is a 54% reduction in handling time. It is a useful improvement, and it is smaller than the reduction suggested by looking only at the easy cases.

Track automated and escalated cases separately, then combine them. Include checking, corrections, retries, and the work of finding out why a case got stuck. If the system saves eight minutes on a task but creates several minutes of supervision elsewhere, both belong in the calculation.

## Say what the recovered time becomes

Time multiplied by a loaded hourly rate estimates the value of capacity. Actual cash savings depend on what changes in spending. A reduction in overtime is observable. A hiring decision deferred because the same team can handle more volume is a different kind of benefit. Shorter gaps between tasks may be useful without changing either.

Keep those outcomes distinct in the report. Describe the work that can now fit into the week and measure whether it happens. Also check the next queue: finishing intake faster has limited effect on customer waiting time if approval remains backed up.

Error reduction deserves its own calculation. Group mistakes by consequence, estimate their frequency and correction cost, and repeat the measurement after launch. A hypothetical workflow with $50,000 in annual rework warrants close attention, just as one consuming 500 hours of labor does. Severity and avoidable downstream costs determine the comparison.

## Put costs on the same timeline

Count engineering, integration, infrastructure setup, and the time domain experts spend defining and testing the workflow. Then include recurring costs: compute, storage, model calls, maintenance, monitoring, and review.

For illustration, a $100,000 build with $30,000 in annual operating costs totals $190,000 over three years. Compare it with three years of estimated benefits, and state the assumptions about volume and useful life. A one-year comparison answers a different question.

Use a consistent accounting boundary. If review time is already included in the post-launch handling cost, do not subtract it again as a separate operating expense. A conventional net-return calculation is:

    ROI = (benefits over the period − costs over the period) / costs over the period

Keep capacity estimates, realized savings, and uncertain benefits visible alongside that number.

## Make the report useful during development

A small dashboard can show baseline and current handling time, elapsed time, automation rate, errors by severity, review backlog, usage, and operating spend. Watch override rates and recurring failure types. Confidence scores become useful indicators when they have been checked against observed outcomes.

Review those measures weekly during an active pilot. Compare actual results with the original forecast after 90 days, then revisit the economics as volume and costs change.

“50,000 documents processed,” “97% test accuracy,” and “85% faster” can all describe useful progress. Each needs an accompanying account of quality, exceptions, and the work that followed. That account is what lets you decide whether to expand the system, revise it, or spend the next month elsewhere.
