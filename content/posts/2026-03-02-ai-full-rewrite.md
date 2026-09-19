+++
date = '2026-03-02T14:14:43-05:00'
draft = false
title = 'The Full Rewrite: AI edition'
tags = ["engineering", "ai", "process", "product"]
slug = "ai-full-rewrite"
description = "The engineering, product, and project risks of a full rewrite, and why AI does not remove the need to manage them."
+++

I've had full rewrites come up several times recently, and so I wanted to write about them.  The full rewrite is a kind of siren song - beckoning on the horizon is a future with higher velocity and lower technical debt.  But actually doing one is one of the riskiest types of projects and organization can take on.  The topic has been covered extensively, and yet it recurs, often, for good reasons.  One fundamental question is - has AI & AI assisted coding changed the space?  I'll look at different types of risk in 3 areas to try to unpack this.

## Engineering Risk

This is the easiest part!  There is essentially no engineering (feasibility) risk - you're reimplementing all your functionality.  All your functionality exists.  Therefore it is possible.  There does exist risk in changing languages and changing architectural patterns, but the basic functionality on a behavioural level is proven.  You can strategically opt into additional risk where it makes sense (for example, for performance).

## Product Management Risk

This is difficult to disentangle from Project Management Risk, but I'll try.

To do this project, some amount of capacity must be allocated to rebuilding what already exists - essentially treading water.  This is difficult to do!  Most product organizations thrive on pushing the product forward, and an internally focused initiative is out of the skillset for many product leaders.  This adds delivery risk, as there are frequently incentives to can the rewrite project (or effectively can it, via deprioritization) in favor of revenue generating product incentives.

Add to this timelines - if you're a 10 year old company, by default you should expect about 10 years worth of work for a rebuild!  In reality this is a hazy upper limit that does not account for staffing changes, but the point of the timeline stands.

## Project Management Risk

This is the big one.  Given the engineering incentives (boring, cost center, just rebuilding), and the Product incentives (cost center, not customer centric, inwardly focused), there is a high likelihood of team members or stakeholders trying to deprioritize the project, especially if it goes badly.  As such, the formative parts of the project are critical.  Several major patterns emerge:

### Strangler Fig Pattern

This is the classic solution to the full rewrite.  Replace the system in pieces, incrementally.  This relieves pressure as product initiatives can advance, while things under the hood can be swapped.  It also favors smaller changes, so the project can be put on the backburner and returned.  That said, it can be difficult to significantly change code quality or switch languages with this approach.

#### Migration Pattern

This is a pattern where a discrete feature is popped into the new technology, language, or framework, and new clients are onboarded onto the new platform while old clients stay on the old one.  This has the upfront cost of rebuilding the feature, but allows a cleaner break with the old system.  There is significant delivery risk here, since abandoning the project midway results in two codebases, or a need to migrate new or old customers.  There is also a strong downside that the old codebase will stay around for a long period of time.

I've seen several startups where the old codebase was never deprecated.  To do this successfully, a plan needs to be committed to, to finish the migration of old customers.  As such, there is significant sales-related risk, since new Sales motion will move towards a feature-sparse version of the product, and customers may churn when asked to migrate.

##### Complexity-First Rewrite

You can start your migration with the most complex part of your application.  As an example, this might be your telecom feature which integrates with Twilio.  This has a major advantage regarding delivery risk, since you can get a clear estimate on the upper bound of complexity, and therefore you can estimate the real duration of the project with high fidelity.  This allows you to pull the plug proactively if the expected duration of the project is untenable.

#### Revenue-First Rewrite

You can also start your migration with the most revenue-generating part of the application.  This is convenient in that it reduces the sales related risk associated with the rewrite, easing pressure on Product and Sales.

#### Just Rewrite Wholesale

I'm mentioning this as an option, but don't recommend it.  Without a strategic angle and without getting customers using the new version proactively, there is a strong chance that at 12-18 months this initiative will be cancelled, resulting in significant lost productivity.  In general, I view it as best to use one of the other patterns, or jump straight to the conclusion not to rewrite.

## AI in the mix

It's clear therefore that regardless of speed, delivery risk still exists.  AI is predominantly helpful in that it allows for significant speed increases with the process.  Categorically, a faster project here means lower delivery risk.  And relatedly, since feasibility is done, a project like this is naturally well-suited to AI.  You also may be starting in a new codebase, which in turn decreases token costs when writing some of the functionality.

## Conclusion

Caution is still required, as it's easy to become mired in a longer-term project like this, especially for teams optimized for shorter-term shipping.  But AI speed combined with product direction can make projects like this more actionable than ever.
