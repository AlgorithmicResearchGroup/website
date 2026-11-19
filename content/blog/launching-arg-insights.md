Title: The Work Before the Build
Date: 2026-05-28
Slug: launching-arg-insights
Summary: A project gets easier to build when its owner, interfaces, test cases, and operating assumptions are already on the table.
Tags: announcements, consulting, operations
Home_order: 11
Home_label: Studio note
Author: ARG Studio
Template: article
Category: blog
Url: blog/launching-arg-insights.html
Save_as: blog/launching-arg-insights.html

Before I think about an agent's tools or a model's prompt, I want to see a piece of work moving through the existing process. Where did it come from? What changed along the way? Who decided it was finished?

Those details make a project concrete. They expose the decisions that engineering will otherwise have to guess at. They also reveal when a promising idea needs more groundwork before anyone should commit to building it.

At ARG Studio, deciding which projects to take on includes this work. A project can be technically interesting and still lack the conditions needed to make it useful.

## Bring an ordinary case and a difficult one

A walkthrough of the current workflow is more informative than a list of desired features. Show the source material, the intermediate steps, the destination, and the corrections someone made along the way.

An ordinary case establishes the sequence. A difficult case shows its limits. If people disagree about the right outcome, capture the disagreement and decide who can resolve it. Process documentation can be a worthwhile first deliverable.

For an automation project, an established workflow provides a useful starting point. A new process needs design work of its own. Combining the two is possible, but the scope should acknowledge both.

## Make the economics legible

Count the recurring work before estimating what it would cost to automate. Five cases per week and fifty per day create very different opportunities to recover time and gather feedback.

Twenty hours of potential weekly savings can be a useful initial screening figure for a substantial implementation. Treat it as a starting heuristic. Lower-volume work may matter because mistakes are costly or delays block something valuable. Higher volume can still fail to justify an expensive integration.

Include ongoing operation in the estimate. Someone will need to watch failures, maintain connections, and test changes. A project should have room in its economics for that work.

## Prove the connections

An input needs a location and a format. An output needs a destination and a definition. “A new form submission produces a draft record for review” describes a connection that can be investigated.

Before promising the finished workflow, check whether the source can be read and the destination can be written. Verify the permissions, available APIs, representative sample data, and a place to test without changing production records.

Security reviews, vendor approvals, and access requests can determine the schedule. Start them early. If direct access is unavailable, anonymized extracts or a mock system may support development, but record what remains untested. Manual exports and screen-driven integrations introduce dependencies that deserve explicit treatment.

The proof can be small: read one real example, transform it, and place the result in a test destination. That establishes more than an architecture diagram alone.

## Name the people who can decide

The workflow owner should know the work well enough to answer questions about edge cases and have the authority to settle them. The person operating the finished system needs time and access to do that job. These may be different people.

A sponsor must also be able to resolve the larger constraints: budget, cooperation across teams, changes to responsibilities, and ongoing support. Technical delivery does not settle those questions automatically.

Discuss how work will change with the people doing it. Their existing checks may encode important knowledge. Their willingness to use the new system will depend partly on whether that knowledge survives the redesign.

## Agree on what a pilot is allowed to do

A pilot needs a scope, a review process, and criteria for expanding or stopping it. It also needs a practical response to mistakes. Decide which actions can be reversed, which require approval, and where incomplete work goes.

Iteration works when feedback can change the next version. Set aside time to review real outputs together. Use representative cases to establish an initial quality bar, then keep the failures as tests. An expectation of perfect performance from the first release makes that learning difficult; an undefined quality bar makes it impossible to know when to ship.

The brief I want to begin with is compact: a workflow, a named owner, a working connection, a set of examples, a measure of success, and a plan for operating the result. Once those pieces are visible, the technical choices have something to answer to.
