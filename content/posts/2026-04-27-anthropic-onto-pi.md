+++
date = '2026-04-27T07:46:43-05:00'
draft = false
title = 'From Anthropic Toward Pi (for now)'
tags = ["engineering", "ai"]
description = "Hunter's account of moving his AI development workflow from Anthropic tools toward Pi, and the tradeoffs behind that choice."
+++

I really see this moment as an inflection point (as so many recent moments have been).  And actually that's overstating it - the moment was a few weeks ago with Opus 4.7.  I see us moving towards another period of tool flux.

## From Anthropic

Anthropic has been having a bad month.

- Mythos was announced! https://red.anthropic.com/2026/mythos-preview/
  - Due to safety concerns, access was restricted
  - The model was accessed without authorization: https://www.wired.com/story/security-news-this-week-discord-sleuths-gained-unauthorized-access-to-anthropics-mythos/
- Claude Code leak https://www.axios.com/2026/03/31/anthropic-leaked-source-code-ai
- 4.7 release
  - New tokenizer is uses significantly more tokens
- ClaudeCode is temporarily removed from Pro tier https://news.ycombinator.com/item?id=47855832
  - Apparently this was a "test"
- Bugs occur: https://www.anthropic.com/engineering/april-23-postmortem
- Uptime: https://status.claude.com/ (Which is well documented to be inaccurate)

This isn't a comprehensive list, just what I could list off the top of my head.  Avid users can probably point to at least another 3-5 issues. Many focused on how quickly changes burned through their weekly and daily quotas.

Over the past months, my network has moved overwhelmingly off CUrsor and Codex onto ClaudeCode (Plus, who uses Copilot or Google's solution?).  This trend hasn't reversed.  At the moment, CC is overwhelmingly in the lead, but everyone is eyeing the exit.

I'm not going to call the game here, and say the era of cheap tokens is over.  But the writing does seem to be on the wall - things seem to be getting more expensive, faster, from here.  Anthropic appears to be heavily compute constrained.  They have dry powder, including another 5B from Amazon (https://www.cnbc.com/2026/04/24/google-to-invest-up-to-40-billion-in-anthropic-as-search-giant-spreads-its-ai-bets.html), but the pain remains.

Where to next?

## To Pi(.dev)

In my network, I've been hearing good things about pi.dev (https://pi.dev/) for a while now.  You might be familiar with OpenClaw - this is the harness that underpins it.

So I decided to try it.

I have to say, I'm impressed.  It's a more minimal solution (you can see a short presentation about it here: https://www.youtube.com/watch?v=_zdroS0Hc74&t=3665s), which is something i appreciate.  That means no subagents, no planning mode, no bells and whistles.  Just you and the context window.

So, my first task was generating some skills to recreate plan mode, and to provide some ergonomics to swap models.  As an example, I want to use Opus for planning, Sonnet for execution, and Haiku for simple question and response (I wanted to stay on Anthropic models for the moment).  Pi knocked this out of the park, but API tokens are *expensive*.

Next, I made a dumb idle game to run in pi.  I like making toy games to try out new models.  Some people like TODO apps or blogs, I like idle games.

As of late last week, DeepSeek announced new models, and I'm swapping over to experiment with those.

It's interesting, I have a similar reaction to Pi that I previously had with ClaudeCode.  It felt like shackles I was unaware of fell away.  Things got easier again (for now!).

## And Onward

From here, I have a set of ergonomics I want to configure towards a software factory (essentially, a polyagent workflow with pi calling pi across multiple models, to build and deploy software fully autonomously).  With that forge, I have a few agent ideas I want to try out.

One interesting one - I want to see if I can replace my Google browsing with a personal agent in slack.  As a note, I know this is technically feasible, it's more a question of whether the form factor works as well as I hope.

I have a series of other ideas, but I'm keeping more of those closer to the chest for now.

Stay tuned for more!