+++
date = '2026-05-23T07:46:43-05:00'
draft = false
title = 'Why Does AI Scale With Engineering Skill?'
tags = ["engineering", "process"]
description = "How engineering skill affects the use of AI development tools, and why the person directing the work still matters."
+++

I'm frequently asked why some people see more success with AI than others.  The following are largely hypotheses and anecdotes (not data!), but I'll try to list several with some conjecture.  I'm personally looking forward to more hard scientific research in this area I can cite one day.

## Written Communication

Experience with coding means that you're writing frequently.  Writing is the main skill you use when communicating with AI.  Therefore, good written communication is transferable between the two.

This is true but incomplete, as it fails to adequately explain why LLMs are responsive to written communication - more on that to follow.

## Bias

LLMs are based on a machine learning techniques, and all machine learning techniques are inherently biased.  Specifically, a core of the tech is neural networks.  It's well documented that differences in input bias the output of the model.  One example - writing differently may "activate" a different set of neurons.  As NNs are a sort of lossy compression mechanism, phD level writing may "activate" sections of the NN that are more closely tied to other phD level writing, resulting in phD level performance.

This is a well known limitation of all machine learning models.

## Delegation

As software engineers scale in impact, they are forced to delegate.  LLMs are nondeterministic entities that nevertheless must produce deterministic outcomes.  Juniors are nondeterministic entities that nevertheless must produce deterministic outcomes.  Therefore, techniques to thin-slice, delegate, and coordinate allow scaled LLM usage, leading to better results.

I think there is something here, but the comparison is inherently flawed.  Techniques for delegation do transfer.  However, techniques for improvement (juniors inherently have  capacity for learning, LLMs must have that explicitly built) are drastically different.  Similarly, you can fire or reassign juniors.  You can change models, but that doesn't really change the outcomes of the model itself.

## Context

This is a tautology, but many great software engineers work in great codebases.  Those codebases are great because the great engineers work on them and invest in them.  To the point of bias, the context you're working in is an important factor in the LLM's bias.  Garbage in, garbage out.  That means that working on a higher quality code base generally means better output.

This one is extremely compelling.  We can just look at dead code - dead code eats up the context window and dilutes attention.  That means not only is it more expensive to work in that part of the codebase, it has knock on effects: it informs the agent to leave dead code in (exacerbating the problem).  It also biases the model.  It also means that analysis will take longer and have false negatives/positives, especially if attention locks into the dead area.  And this is just one straightforward category of technical debt - there can also be feature branches, problematic architectures, and more which have less straightforward downsides.

## When to hold 'em and when to fold 'em

Talented engineers have optionality.  They aren't forced to AI maximize - they can use the tools when appropriate, and code by hand when appropriate.  Other developers may be wholly reliant on AI for some changesets.

This is one I've observed firsthand several times.  LLMs are great for some tasks, and very bad at others.  If you try to use agents for everything, you'll generally have a bad time.  Skill preserves optionality.

## Know truth from fiction

Talented engineers are experienced.  They know when the AI is telling the truth and when it's mistaken.  And if they're not sure, they know how to find out.

This is certainly true, and frequently observed.  If you're new to coding, you're dependent on the agent for architecture & other decisions, because you don't know the options or tradeoffs.  With experience, you can know when the recommended solution is really the best one, or if what you're looking for isn't even on the table.

## Review Skill

Talented engineers have and will continue to review code.  As such, they are effective at it - not necessarily in terms of bug finding (bugs are better left to tests) or style (just lint), but in terms of an overall cohesive picture.  A simple example is in comments - which comments are useful, and which are likely to confuse a reader or an agent.

This is compelling, although I do know great engineers who are not great reviewers.  This is probably a second order effect, where review leads to domain knowledge which leads to better prompts.

## Thin-slicing

A core skill in engineering is working on small things.  That is to say, don't boil the ocean - turn the giant project into milestones, the milestones into deliverables, and the deliverables into small actionable items.  Deliver on each in turn.  The LLM's attention mechanism dilutes quickly.  Small one-shot work plays to the strengths of the tools and techniques.

This is compelling and true where possible.  Smaller units of work are more comprehensible, easier to test, quicker to QA, and therefore reach customers more quickly for feedback.  These effects on LLMs have been well documented as well.

## Domain Knowledge

This is touched on earlier for prompting, but knowing about the customer and about the codebase feed into communication.  To the point of bias, using the right terminology probably gets better output from LLMs as it points the attention in the right direction & is more token efficient (the LLM can act, instead of burning tokens trying to infer your intent).  Adherence to your domain results in clearer code, and LLMs scale on clarity.

This is also fairly compelling if indirect

---
This is a set of hypotheses, none of which are especially compelling on their own.  I suspect at this point that all are true.

So what do you do about it?  First, live in the code, and engage directly with the tools.  Prompt, but verify.  Ship, and review output.  Attach yourself to the customer, and advocate for them to the LLM.  Develop strong opinions, and express them to the agent.  Keep your skills sharp - reading, writing, and reasoning.