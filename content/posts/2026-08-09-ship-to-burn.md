+++
date = '2026-08-09T07:46:43-05:00'
draft = false
title = 'Ship to Burn'
tags = ["process", "leadership", "product"]
description = "Separate work that answers a customer question, work that earns revenue, and work that consumes effort without creating value."
offerContext = "When the roadmap is consuming effort without helping revenue or retention, the first decision is what the team should work on."
+++

Recently I had the pleasure of taking a workshop by [Jeff Patton](https://jpattonassociates.com/).  We covered a ton of concepts and practices that I had experienced firsthand.  Two pithy terms he uses are "build to learn" and "build to earn".  You might notice this is the foundation of [Dual Track Development](https://jpattonassociates.com/dual-track-development/)You can read some writing about it [here](https://www.svpg.com/build-to-learn-vs-build-to-earn/) for example.  I'll cover the two for you briefly before covering a third category that I consider the bane of my existence - one that keeps recurring too.

## Ship to Learn

"Who is going to buy this?"
"What will they pay for this?"
"Can we even build this?"
"Are we trying to prove P = NP ???"

Software development involves a lot of questions (this list is not comprehensive).  Sometimes you know the question up front.  Other questions arrive through reasoning, and some only arrive through building or experimentation.  The later you arrive at a question, the more expensive the answer tends to be.  That's the purpose of this cycle - answer questions, and see what questions arise from those answers.

This is inherently not a revenue generating step - but it lays the foundation for revenue.  This is where your bets lie - where you reinvent the company, swing from loss into profit, and generally save the day.  Don't scrimp on it.

## Ship to Earn

This is the classic, easiest phase of software development (well, if you've done things right).  Customer A has committed to pay you $X for feature Y with delivery day Z.  You know what to build, you build it by the deadline, you get paid.

Not exactly, although that is an ideal scenario.  It's usually something closer to "we lost X deals this quarter due to missing feature Y, let's build it and try to rescue".

The point is, this is less experimental (you just finished that phase) and more mechanical.  You've identified an opportunity - now execute on it and collect.

As this *is* revenue generating, this should be the bulk of your executive capacity.  Over-committing here (to the detriment of the Learn track) can be long term problematic - that's classically how you eventually lose product market fit.  But hey, shipping to earn gets you bucks, and that capital can be spent to work your way out of problems.

## Ship to Burn

And now we get to another category.  This is not like the other two.  This is not sunshine and rainbows, learnings and dollars (although learnings and dollars are involved!).  This is the other side of the wall, the mire, the trash heap.

This is the cycle where you throw away productivity for no real reason.  Some examples:
- Let's spend weeks or months changing colors on our emails!
- Let's reskin our mobile app
- Let's swap to a proprietary DB because the CTO likes it ("it's fast" - for our 12 DAU)
- Let's integrate with company X because a board member is an investor in X
- Let's adopt Google's development workflow because they have a lot of money
And so on

The point here is - each of these actions here is an action that *could be fine* given *a different context*.

Changing colors / rebranding / reskinning: Legitimately, this is a growth thing that mature companies do to wring a few basis points of growth once they've done everything else.  It can move the needle, but a tiny amount.  For a huge company, that tiny amount can be big enough to be profitable.  If you're here, reading this, that *probably* isn't you.  If you're a startup, you probably have massive features to write and sell for eye-popping multipliers, and I would rather you ship those than be a CSS jockey.

"It's fast" -  extremely relevant for Google scale!  Extremely irrelevant for you!  You've probably got maybe 1000 DAU, which means you can run your business comfortably off a raspberry pi.  Scalability should be a distant concern unless people actually complain.  Just use boring tools like Ruby or Postgres.  Shiny Tool Syndrome will cost you more in upkeep and hiring than the speedup will buy you (approx buying you flat 0!)

"Integrate with company X" - You should integrate with a company because your customers see value from it, not because someone told you to do it.  It's a recipe for building a chickenwire and duct tape connection with a product no one uses and your customers don't care about.  Of course, this doesn't apply if the customers asked for the integration first!

"Let's do it like BigCorp" - You fundamentally misunderstand the causality between FAANG development and their money faucet.  You believe they had great people and great processes, and they iterated quickly and dug out an Unlimited Money Faucet.  The reality is, the Unlimited Money Faucet was hiding just under the surface, they discovered it, and they have enough Unlimited Money to do whatever weird stuff they want to.  It doesn't matter what they do, it doesn't matter how many products they kill, it doesn't matter how unethically they act, nothing matters so long as the Unlimited Money Faucet pours Unlimited Money.  Do you have one?  No?  Then you have to obey the law of gravity like the rest of us mere mortals and go work hard and build things right.

The frightening part is how prevalent Ship to Burn is.  I'm regularly seeing companies with 8-10% Ship to Earn, 0% Ship to Learn, and ~90% Ship to Burn.  And of course AI scales this - your average AI adopting company just uses AI to scale a combination of toil and rework, so Ship to Burn grows faster than the other two too.

-----

So what is to be done?

First off, start with results, not output.  What results do you want?  More money? Better logos?  Spend actual time thinking about this, even if it takes away from output.  You have to have a goal to have a direction.

Next, focus on outcomes - specific ones.  What outcomes do your customers get from a rebrand?  What outcomes do your customers get from other features?  What outcomes are you willing to provide, where parting from their hard-won cash is a no-brainer?

Finally, then focus on the output - aim it at the outcomes ties to the results.

You'll probably find yourself moving slower at first, but making progress faster.  It doesn't matter how much you scale up development capacity if it all ends up in Ship to Burn.