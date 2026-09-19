+++
date = '2026-03-30T12:14:43-05:00'
draft = false
title = 'Onboarding: Time to First Release'
tags = ["engineering", "onboarding"]
description = "How a refined backlog, pairing, and usable setup instructions help new engineers reach their first release."
+++

I've joined many engineering organizations, and there's one metric I return to that differentiated successful organizations from unsuccessful ones - time to onboard, as measured by time to first release.  I should add that "success" here is subjective - the "successful" ones were able to extract much more objective value (in terms of ROI in increased ARR) from my fellow engineers and I, while the "unsuccessful" ones struggled or failed to extract similar value.

As a note, given that this is time to value, it compounds.  Early release means starting your *next* release sooner, and so on.  The difference can be magnified significantly over time.  I also differentiate this from time-to-first-commit - which measures when work *starts*, vs when the first work item *ends*.

## Low hanging fruit - a suitably-refined backlog

Where every organization should start is by having a somewhat refined backlog, with some pool of easy work to complete.  It may be easy to do some of this with AI, but resist!  Leaving some easy work for someone new allows them an easy entrypoint into the system - instead of discovering how your microservice architecture is laid out on day one, they can focus on learning narrow frequently-used tooling, and expand from there.  This slots into an onboarding as well, providing ample time for meeting the team while also doing some coding.

"Suitably-refined" is an important detail here as well.  You want real 1-point level complexity if you can - trivial stuff like text changes.  I'll never forget one onboarding, where I was assigned a 1-point card that ended up taking 3 engineers 4 months to complete (with AI!).  It doesn't need to be perfectly refined, but some thought needs to go into the ticket, so your new hire can focus on execution.  Bonus points if the ticket is well scoped enough that the hire can 1-shot it with Claude Code - more time to focus on learning.

One might argue "Hey, isn't this gaming the metric?" - but I disagree.  Small is good.  Small is achievable.  Small shows that you care for your new hire enough to pave the way for them to start racking up successes on day one.  And don't forget to celebrate that win!  There's organizations who don't let new hires complete work for months.

## Onboarding Guide

This is a simple checklist, including the work item above.

Include an onboarding buddy (below), as well as a few people to meet in and out of the team.  Make sure there's a list of services you need accounts for, secret storage, cloud accounts, process accounts (github, JIRA, etc), and so on - basically a who's who of your relevant engineering SaaS subscriptions.  Don't forget to lay out goals - I prefer daily goals for the first week, then 30/60/90 day milestones.  If you're someone's manager, make sure you have your 1 on 1 in the doc as well, and use that for continuing followup on these milestones!

Best practice for this is that you update your guide as you go through it, and provide an updated one to the next hire.  It's never perfect, but it provides living documentation that changes with the organization.  If you hire sporadically, consider having a lead run through the guide to make sure it's up to date.  

## Pairing / Onboarding Buddy

One of the easiest ways to welcome someone to your organization - get someone to work with them.  This is ideally a lead focused on mentoring, so they've self-selected for patience.  With the rigging described in the other points, this person can focus on answering questions and configuring access.  Given other surrounding onboarding activities, the buddy can still focus on core job activities - but there should be some time set aside for pairing on the ticket above.  Relatedly, don't slam them with work, so they have enough time to consider onboarding as their first priority.

This personal touch opens creates an opportunity for mentorship, relationships, and trust from day 1, at the cost of a few hours.  The ROI is huge.

## Setup instructions

This one should be easy.  Gold star test - you can prompt an agent with the README and have it install everything, start a server, and run some test.  Anything else is documentation debt, process debt, or straight technical debt.  The good news is this is easy to run - wipe out your installation and try to prompt AI to recreate it.  You'll discover the friction points rapidly, and they'll force you towards a better AgentEx (DevEx), or at least force you to acknowledge them in documentation.

Seriously though, take some time to fix these things.

-----

So that's 4 simple steps you can start today, to ease onboarding.  Give it a try - I recommend trying to make your new team members productive on day 1 where possible.