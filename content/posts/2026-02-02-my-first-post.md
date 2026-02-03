+++
date = '2026-02-02T12:58:43-05:00'
draft = false
title = 'The Value of PRDs (Product Requirements Doc) in the Age of AI'
+++

I had a few recurring conversations recently in one of my communities: Engineers were preparing high volumes of code in pull requests, that were then getting jammed up in review.  This is a common problem that has been exacerbated with AI.

Whatever is to be done?

Counterintuitively, alleviating bottlenecks in review is best done not in the review stage, but far earlier.  There are many ways to chip away at this problem, but I wanted to focus on one that might not occur to most: PRDs.  Specifically, preventing last-stage scope and spec changes.

PRDs are one of the least liked forms of documentation, but at the same time one of the most useful.  Many companies add a lot of pomp and circumstance to them, but there is a better way to do them.  At the core, these areas should be answered:
- Why are we doing this? (I prefer specificity, in dollars)
  - What is the impact to the company if we do this?
  -What is the impact to the company if we do NOT do this?
- What do we even want to do?
  - Is it possible to do this? (Feasibility)
  - Do we know how to do this?

The first question should be table stakes.  The next two are where the work comes in.  Bring in engineers (a Technical Lead if you have one, or the engineer in charge of the effort), and get them to ask questions about the specifics of what you're doing.

All those questions start as unknowns: Known unknowns and unknown unknowns.  As you categorize these (it doesn't have to be formal), you decrease the uncertainty of your project.

Answer questions in advance. Not only will AI give you better results, you can avoid meetings and an extended code review, resulting in repeated time savings.  At the low cost of a document, and a series of questions.

(I should add - failing to ask the right questions regularly costs companies millions.  I've seen too many products built the wrong way for the wrong users)