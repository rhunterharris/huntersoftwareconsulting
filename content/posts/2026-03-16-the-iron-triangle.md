+++
date = '2026-03-16T14:14:43-05:00'
draft = false
title = 'On the Iron Triangle'
tags = ["engineering", "process", "product"]
slug = "the-iron-triangle"
description = "How scope, time, and resources constrain software delivery, and what leaders need to decide when those constraints collide."
offerContext = "When missed delivery is putting revenue at risk, scope and priorities need an owner who can connect product decisions to the work."
+++

The Iron Triangle is a classic model of constraints.  According to the model, there are Quality, Time, and Cost.  Pick one, at most two.  But what if this model is inherently misleading?

## Round 1

### Choose Cost

When selecting for cost, we sacrifice quality and time.  Release is delayed in terms of absolute time, and is further delayed by bugs.  In terms of ROI, loss occurs due to missed contracts and churn.

### Choose Time

When selecting for time, we sacrifice quality and cost.  Bugs occur, but release happens quicker, allowing for time to fix them.  In terms of ROI, loss occurs due to churn before bugs are fixed, and development is more expensive.

### Choose Quality.

When selecting for quality, time and cost are sacrificed.  Release is delayed.  ROI is lost to missed contracts and more expensive development.

### OK, so?

So up until this point, there is nothing groundbreaking.  Selecting for time may be a dominant strategy, since early feedback can result in fewer bugs, quicker revenue, and funding.

## Round 1, but choose two

### Sacrifice Cost

Sacrificing cost, we have rapid development at high quality.  Development is significantly more expensive, but customer feedback begins early, and customers are not deterred by bugs.

### Sacrifice Time

Sacrificing time, we have extremely slow development, but cheaply and without bugs.  Development cost is minimal, but contracts are lost due to speed, and customer feedback is delayed significantly, which adds existential risk.

### Sacrifice Quality

Sacrificing quality, we have rapid development on the cheap (this is a dominant strategy using AI).  Development cost is low, and feedback is reached early.

### OK, so?  You haven't made a point yet.

I'm getting to it.  As you can see, sacrificing quality looks optimal - you reach more revenue substantially faster.


## Round Two+ - Lying in the bed you made

Development is an ongoing process though.  Once built, it must be maintained.

### If you sacrificed Cost

Now, you have a high quality codebase put together quickly.  Your situation is quite good - you've pushed to revenue early, and have breathing room to continue iterating quickly.

### If you sacrificed Time

In this situation, you're about baseline.  Revenue is delayed, so you're constrained in choosing Time again, as further delays may cost you the company.

### If you sacrificed Quality

You are in a bad situation.  Quality compromises will prevent you from moving quickly.  They will also prevent you from developing cheaply.  You're forced into a situation where you must pivot towards writing better code more expensively, for no marginal benefit.  This is in essence what tech debt is - an inevitable repayment of previous compromises, until you can move swiftly and cheaply again.

### The Point

The iron triangle is a false dilemma.  In essence, there is only one choice - quality, unless the code is thrown away.  Early investments in quality pay off in preventing cost and speed degradation.  Time compromises are neutral benefit - you have advantages and disadvantages.  Selecting for low cost is systemically risky on multiple fronts.  

Therefore, as much as possible, prioritize quality as quickly as possible, and avoid overly selecting for cost.  Systemic over-focus on cost adds risk over time.

