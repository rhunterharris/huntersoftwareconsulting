+++
date = '2026-09-20T07:46:43-05:00'
draft = false
title = 'The Release Tax'
tags = ["product", "leadership", "engineering"]
description = ""
+++

I've had a rough week.  One organization I'm associated with really struggled with their release.  In my humble opinion, you're moving slow if you don't ship every day - calibrated across orgs, that means I want to scale deployment roughly linearly with headcount.  Some people will be on large initiatives that take a while to ship, others will ship 15x in a day, so I've observed it to be a valid baseline.  This client takes about 9 days average to ship, for a team of 9. This is also obviously complicated by AI velocity - each release is large and bulky (we are fixing this), and as a result high risk, with many changes.  But the release itself was a 4 day marathon, shared among a set of engineers responsible for the release.

## What does it cost?

Let's examine a release process like this.  Let's assume you have a number of individuals - I've found $75-125 an hour to be pretty typical range, so let's go with a nice even 100.  Engineering workdays are technically 8 hours, but lots of us stick around for the love of the game, so let's assume a 10 hour day (again, nice and round).  This means that a typical cost for an engineer is 1000 per day.  Now, of course, this is COST, and totally ignores OPPORTUNITY cost (like delayed revenue).  But we'll discard that for now.

So in this example, your baseline cost for this release process if 4k/week, or 208k per year.  Staggering.  Enough for additional headcount even.  Caveat - this is one week on, one week off.  So actually 104k.  Whoops - "almost" forgot to mention that this is a 4 person effort, so we're back around 416k.  Again, staggering.

## Knock on effects

One core issue here is that for a week, a set of individuals are uniquely accountable for something the org at large should be caring about - releasing code.  Releasing code is a shared responsibility, not an individual one (although individuals should be accountable *for their release*).  This means that if you're writing code, you can freely release features without QA, with the expectation that other people will clean up after you.  You can ship faster and win big, and other people deal with the consequences!

I refer to this as responsibility laundering.  You see it all over the place in orgs with problematic culture and process.  When an exec vibe codes and someone else owns the release, that's responsibility laundering.  When you capture the benefit of using AI but AI owns your mistakes, the same.  The issue is not just the monetary cost, but the velocity dampening.

## Slowing down

The problem being that this is a loose feedback loop.  I make decisions, and don't document them.  I change application state.  I finish, and do not test, and move on.  Now, the next person using a branch may inherit my changes, and may immediately be less productive.  Tests might not be as fast, or something might be directly broken.  Now that engineer has to unpack the decisions - is this intentional?  or not?  Will it be fixed soon? or not? These question immediately introduce tension.  Worse, when these issues reach the customer, the path back to fixing the issue becomes tangled through Support, SUccess, and Product.  So the choice to prioritize individual speed immediately begins both slowing down employees and customers, while also delaying the fix - compounding problems.

## Speeding back up

The solution is clear - close down the feedback loop.  Ship more rapidly and more regularly.  Test - locally, in test, and in production.  It's easy to "complete" work, but harder to bring value to customers.  Define "shipped" as I have - in the hands of customers and being actively used.  Hold yourself and others accountable for bringing value to customers, rapidly.  Don't let process stand in your way - you are part of the same system as the process.  Advocate for change, and demonstrate it.  

Strive for better outcomes, faster.  Don't settle for "adequate".  By hook or by crook, ship.