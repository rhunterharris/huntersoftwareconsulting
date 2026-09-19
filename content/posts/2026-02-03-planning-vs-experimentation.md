+++
date = '2026-02-03T12:58:43-05:00'
draft = false
title = 'AI Velocity: Planning Vs Experimentation'
tags = ["engineering", "process"]
description = "When to plan and when to experiment with AI development tools, and how to use each approach to learn what will work."
+++

In talking with founders about their AI strategy, I've noticed consolidation into two major camps of AI assisted acceleration: Planners and Experimenters.  Each of these has strengths and weaknesses in their delivery execution.

## Planning

A currently popular variant of this approach is "spec driven development", and this approach is somewhat of a return to waterfall.

A given person (frequently an product + engineer persona) will attempt to spell out all variants of behaviour in advance, and document them in writing.  Once this is done (with frequent revisions of course), the spec is fed to an agent to develop a plan that starts with writing tests.  After reviewing the tests, the tests are used to fill out the code.

Pros:
- Extremely fast when spec is done
- Cheaper tokenomics
- More engineering focused
- More likely to one-shot the activity

Cons:
- Planning and specifying can take considerable time
- Human review of specs is still very important
- Subject to the same difficulties of Waterfall

## Experimenting

This approach takes advantage of "vibe coding" (or vibe-product-design-engineering) to elaborate on multiple variant solutions of the same problem.  It is subject to similar limitations to raw vibe coding.

In this case, the product persona might prompt only with a high level description, often without designs or deep specification.  They will generally use the same prompt multiple times (or ones with minor differences), leaving the LLM to decide on significant parts of the specification.  The goal here is not production ready code though, but instead to explore the space of possible solutions.  After creating multiple feature artifacts, the persona and others can demo and check the look, feel, and experience of different alternatives, and then move towards productizing one.

Pros:
- Relatively quick to get started
- Extremely useful when a clear outcome isn't available
- Leverages advantages of multi-agents for faster outcomes
- Deployable artifacts with code are generally more useful than mockups or Figma

Cons
- Token costs can add up fast, especially for complex projects
- If back and forth is necessary across multiple agents, cognitive load adds up
- In most orgs, the artifacts will be deployed as-is without being revised, so tech debt is a concern


## When to use each
Based on these pros and cons, it should be clear when to use each approach:
- In a low-uncertainty environment, plan and execute.
- When uncertainty is high, use experimentation to explore and execute.