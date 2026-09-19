+++
date = '2026-05-05T07:46:43-05:00'
draft = false
title = 'About Weirdness Budgets'
tags = ["engineering", "process", "leadership"]
description = "How to decide where a company needs innovation and where boring, familiar choices leave more room for the work that matters."
+++

What is a weirdness budget?  You might have heard about this concept as an "innovation budget" or a "risk budget".  I personally don't like the term "risk budget", as I think that underestimates risk itself.

Typically, when we talk about a weirdness budget, we refer to a particular project.  Within this project, we usually have a block of work that is well understood - reusing API integrations, or existing data structures for example.  Then, there is work that is clearly net new, like integrating with a brand new API.  The interesting part is the third - work where optionality exists.  Do we reuse an existing queueing mechanism, or is this work appropriate for something new?  Do we need to explore different architectures to make this work?  And so on.  This is where weirdness budgets come in - for decisioning on this space where optionality exists.  Let's start with some basics.

## Boring is short-term profitable

In general, we can expect boring approaches to be profitable.  If we reduce to extremes - the market has proven boring to work (that's why it's boring - it was not always that way).  That sentence also illustrates the risk of boring - it may be tried and true, but failing to innovate eventually brings risk.

## Innovation (weirdness) is long-term profitable

Innovation and risk come hand in hand.  Innovation means trying things and experimenting - inherently, some things will work and others will not.  The goal is not to take the fastest route to completion, but to learn along the way.  Therefore, we can see similar extremes - too much innovation may bring learning but little progress.

## Meet in in the middle

The obvious conclusion here is that there is a goldilocks zone with a mix of boring + innovation.  This also shows why I dislike the term "risk budget" - minimizing your risk budget may decrease your risk for that project, while increasing your organizational, strategic, or long-term risk.

I recently read through Elizabeth Hendrick's upcoming ["Signals & Levers"](https://www.simonandschuster.com/books/Signals-Levers/Elisabeth-Hendrickson/9781966280293 ), and realized this is a classic U-curve with regards to risk.

## It depends

As with all U-curves, that means the best allocation depends on the project.  Tight timelines?  You probably need to index on the side of "boring".  Adopting a new tool like AI (or evaluating new tools)?  You probably need to index much more heavily towards innovation.

### Indexing toward boring

This is probably straightforward.  Use what works.  Have experts do the work.  Use your existing tools.  Essentially, business as usual.

### Indexing towards innovation

This is less straightforward, but some organizations do use this as a default.  Have non-specialists own specialist work (preferably with the help of a specialist!).  Use new tools.  Use new patterns.  Add in new libraries.  Essentially, trade time for knowledge.

## Extrapolating out

You might notice that I've shifted from code, towards process.  This concept was introduced to me in terms of actual code, but the U-curves do apply elsewhere.  This extrapolates out of engineering itself into projects, and even into org design.  A classic example is skunkworks - you may have 5 teams focused on the core of the business ("boring"), and 1 team focused on big bets which may not pay off ("innovation").

All you need to start with is an idea of where your risk lies - in tactical delivery, or in strategic innovation.

Note: I do use the word "boring", which I realize is perjorative.  I personally like working on boring things - as I mentioned, boring tends to be profitable.