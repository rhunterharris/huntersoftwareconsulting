+++
date = '2026-05-10T07:46:43-05:00'
draft = false
title = 'Agentic Tasks: a Few Samples'
tags = ["engineering", "process"]
description = "Hunter's approach to agentic development workflows and the decisions involved in putting AI agents to work."
+++

What models are capable of and what they aren't capable of continues to astound me.  I've been pushing myself to use pi for a number of tasks these few weeks and wanted to share some learnings.

## Image manipulation: Replacing Profile Picture

This was shockingly good.  Pi one-shot cropping the new image and replacing it.  No notes.

## Image manipulation: Text Replacement

This was surprisingly a struggle (after how well the image manipulation worked).  The model consistently struggled to follow instructions, and frequently went "above and beyond" - frequently ruminating significantly to get a subpart result.  I haven't found a great solution for this yet.  It does seem like the thinking causes the model to ruminate, in a way where it talks itself out of doing what I want it to do.

## Quote extraction from text

Easy as expected.  I had it go and acquire quotes from a number of transcripts, and extracting insight from them was very straightforward.

## Insight extraction from text

Easy.  It's worth noting that this was closer to summarization - to keep it on track, I had it make sure it was referencing quotes with filenames.  

## Theme extraction

This was a little dicier.  Models routinely would confuse me and my guests or other parties I was interviewing.  Some themes were valid, but several were trite, obvious, uninteresting, or otherwise unusable.

## Bash script generation

I had a few automations I wanted to run, but which I wanted to do in bulk.  Accordingly, I had pi generate bash scripts to execute the work, instead of having Pi do it.  This went well as expected.

## Bash scripts for executing pi

The next step was writing bash scripts to invoke pi, followed by deterministic logic on the output (finally writing the results to file).  This worked quite well as well.  The non-determinism in acting on a weaker model in bulk hurt a little, but for the tasks I was using it for, it was fine.

## Pi self-modification: Extensions

Extensions are code that Pi can run, outside an LLM.  I for example made a plan extension, to automatically swap to a stronger model before generating a plan document.  This works extremely well.

## Pi self-modification: Skills

I've actually been trying to create skills, when pi struggles to complete an activity.  I had previously thought that the context of solving the problem would translate into writing the skill, but in general the models have struggled, predominantly by re-solving the problem.  This is frustrating and token-hungry - frequently I've run into the rumination problem as well.  In fact, in one case, it talked itself out of writing a skill, and instead wrote a (buggy) python script for example.

## Onwards

I'm currently planning to continue with self-modifying pi.  Personally, I'm a little frustrated with the sharp edges - In some of these tasks, I definitely get better performance from Claude.  But that's part of the journey.