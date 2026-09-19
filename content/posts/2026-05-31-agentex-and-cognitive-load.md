+++
date = '2026-05-31T07:46:43-05:00'
draft = false
title = 'AgentEx and Cognitive Load'
tags = ["engineering", "process"]
description = "An exploration of agent experience and cognitive load in AI-assisted software development."
+++

I've said it a few times, and I'll say it again - AgentEx is DevEx.  What scales engineering success scales agentic performance.  I usually talk about  feedback loops, but that's one part of it.  Today I want to talk a little about cognitive load.

## Human Cognitive Load

Feedback looks are the most important aspect for continuing work, but cognitive load is the most important for beginning work.  That is to say, how much work do you have to do to fit a problem in your head? (You should immediately see where I'm going after that sentence).

### Comments

Good comments clarify and simplify.  Bad comments mislead.  In essence, a good comment allows you to fit a summary into your mind, while bad comments add additional work for clarification.  You could think of a good comment as a compaction mechanism, that allows you to skip over adding load from certain sections of the code.

### Tests

Tests add safety.  A well tested area means that you don't need to understand that area in as much depth.  You can make a change and see if it breaks.  On the other hand, bad tests do the opposite.  If you cannot trust the area, you have to read the entirety of the tests, to see whether the behaviour you're changing is tested or not (You can't just search, because remember, you cannot trust it).  Good tests add speed, bad tests add work.

### Abstraction

Abstraction is another technique for pushing complexity "under the fold".  As a simple example, a well named module might take a single responsibility in a workflow (say, enriching an email address).  When you're modifying the workflow outside this boundary, you don't need to worry about what this module does.  You put in an email, it gives you additional data.  Who cares how?

When abstraction breaks down, this trust is lost.  Imagine for example, that this email enrichment deletes database records if an email isn't found.  Suddenly, to do the rest of the workflow, you need to know details of how this module does its' job.  You can't focus on the workflow - you have to dive into and understand this module.  And that trust erosion means you have to check each piece as well (and again, you cannot trivially search, because you can't trust the code).

So again, good abstraction means speed, bad abstraction means more work.

## Agentic Cognitive Load

The core thing to understand here is attention.  Tokens are expensive, but attention is much more so.  If you dilute attention, you agent will reason itself into doing things you don't want to do, burning tokens and time.

### Comments

Useful comments save tokens.  Bad comments instruct the model to search unnecessarily.

It's also worth nothing that many coding agents (looking at you claude!) tend to add comments as a way of writing notes to itself.  That means that it will leave comments regarding the current work.  As an example, it will leave comments about what it is removing.

This is BAD!  The next time you return to this module, the agent will read comments and be informed about code that isn't present, not code that is present.  This leads the agent to get confused about the module, leading it to think it has the previous, removed behaviour (that the comment references).

Presto, dead ends and wasted attention, tokens, and context window.

### Tests

As with humans, tests add safety.  If tests pass, it should be correct.

The problem is, agents like to add tests that assert true === true.  This is of course true, but not especially useful. It's important to check on these tests and make sure not only that you're covering the code, but that you're asserting the right things.

### Abstraction

Leaky abstractions are dangerous.  If you've developed weird enough classes, you can confuse the agent enough that it stops working.  Single responsibility principle (plus shorter classes) makes a huge difference.  Assume that the agent will assume about your code - so guide it along the right path.

## A Defensive Technique

There's a simple agentic pattern you can follow to fight the issues mentioned here.  Instruct your agent to do cleanup periodically.  To reference comments as an example, you can ask your agent to go through the codebase and search for stale comments, removing them when found.  This is a simple oneshot prompt, and can catch many issues, as you probably have lots of files.

The core innovation here though is that you can afford to be laxer with comments directly, so long as you frequently and effectively clean up.  That is to say, if you're entering into a new code base, you may need to do a large cleanup.  Then for a period of time, you need to do this cleanup weekly, then daily.  But once the codebase is clean, it's easy to patch this in as a skill and do it as part of your workflow.  Then, cleanliness is guaranteed (with the corresponding tokenomic benefits!)

Give it a try!