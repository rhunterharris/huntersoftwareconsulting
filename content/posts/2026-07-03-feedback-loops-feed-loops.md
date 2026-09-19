+++
date = '2026-07-03T07:46:43-05:00'
draft = false
title = 'Feedback Loops upon Loops upon Loops'
tags = ["engineering", "product", "leadership"]
description = "How feedback loops shape product development and the way teams learn from the results of their work."
+++

I keep returning to loops lately, with my work with engineering organizations (and with how popular AI loops have been across LinkedIn).  When we look at much of nature, cycles are a fundamental constant.  Earth moves around the sun (giving us seasons).  Earth spins on its axis (giving us days).  The moon moves through the lunar cycle (giving us the tides and such).  Life has cycles as well, from infant to adult back to infant.

But these are cycles.  Humans are capable of more, through feedback loops.  The earth spins upon its axis unchanging, but I have the capacity to spin (my brain), and end up in a radically different state.

Companies are no different - they are loops upon loops.  Economic cycles embed business cycles embed software development life cycles embed QA cycles and on down. We might start with the Sales cycle -  (simplified) qualification, to close, to referral, to qualification. Or we might start at the Engineering cycle - prototype, to development, to release, to feedback, back to prototype. Each department has their cycles - HR has employee feedback, Review, and hiring.  Marketing has its lifecycle.  Security has an audit cycle.

But what goes unacknowledged is the inter-departmental cycles.  Each of these cycles feeds into other cycles at points:
- Sales provides feedback for Product direction.
- Engineering creates demos for Marketing and Sales to use
- Engineering fixes bugs reported from Success

But these are cycles, not feedback loops.  

## Virtuous Cycles

So how does an organization strive towards bettering themselves with feedback loops?

For one, keep them short.  If Sales has to submit a ticket to Engineering for a feature request (which may sit for weeks), that particular opportunity may be stale before it can be acted upon.

Second, drive for positive outcomes.  Sales provides customer feedback to Engineering, which in turn builds the features to get Sales into more board rooms.  This means more customer feedback, more features, more sales, more feedback, and the flywheel turns.  Engineering can take triage from Support, allowing for faster issue close, allowing more time for Support to identify trends, which means better info on priority bugs for Engineering, which means faster close, leading to fewer incidents, and the flywheel turns (making both organization efficient in the process).

It's important to note that none of this is free, and none of this is locally optimal.  If sales just focuses on closing deals ASAP, they might make more sales today, but they miss the opportunity of sales on the features that can't get built.  If engineering is overly focused on closing support tickets without real triage ("not a bug"), their KPIs might look better (especially if it's KLoC), but they lose the velocity they would have with less time spent on bugfixes.

## Vicious Cycles

Feedback loops can also bite.  I see one particular example frequently with AI.

Product usually gathers requirements, passes them to Engineering for execution, and then checks if the requirements are met.  A simple cycle right?

Enter AI.  Execution goes drastically up.  Engineers close work faster than Product can prepare it.  Work accumulates waiting for review, and Engineers go beg product for the next thing to build.  Product, which would normally focus on strategic decisions like the future product and roadmaps, is now dragged into day to day planning of work.  Worse, in many organizations, they're expected to contribute to execution - putting more pressure on themselves paradoxically.  The queue begins stalling as work accumulates, and inevitably slips.  The quality bar is lowered, and things flow to production.

There's always someone who does QA, and in this case it is the customer.  Churn goes up, KPIs go red, and pressure is put on engineering and product to fix the problem.  The flywheel turns,  execution is added, and strategy falls to the wayside.

## Local optima vs global optima

Many startups fall flat on their face here.  They optimize for local speed - making each individual loop optimized, at the expense of cross communication.  locally maximized execution without any feedback - heads down, or siloed.  You can even see this within departments - when a single marketer is off on a project by themselves, or a single engineer.  They become experts, but wander the wilderness lost (and no one knows what they're doing, which limits their success).

One solution?  Bust down silos, and usher in the feedback.  Look, you don't need your whole engineering and your whole sales team to meet every day.  But maybe every week, you could have a single engineer shadow a couple sales calls?  Maybe it's a good idea to get together Engineering, Marketing, and Product when you're planning for a new product (it would be really unfortunate if, after 6 months of planning, you found out that it wasn't feasible!)?

Everyone's been talking about loops with AI, and this applies there as well.  Give you agent context, as much as possible.  Give it fast feedback.  Let it iterate and learn, fast.  Share skills that work, and let others know about approaches that don't.

Loops and cycles are fundamental to how we as humans operate.  Embrace them and embrace the feedback.

Note: I published an initial version of this, posted it to a professional community I'm in, and got valuable feedback that I used to rewrite it.  Feedback loops in action!