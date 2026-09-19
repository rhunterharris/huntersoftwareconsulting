+++
date = '2026-06-07T07:46:43-05:00'
draft = false
title = 'A Very Brief History of AI'
tags = ["engineering", "process"]
description = "Hunter's short account of the shift from language models and prompting to agents, context, and development harnesses."
+++

One thing that strikes me recently is how disparate AI adoption has become.  To that effect, I'd like to recap some of the recent eras of AI we've seen.  As a note, I'm not trying to capture the entire history of machine learning or artificial intelligence.  I'm more focused on "AI" as we currently refer to it - LLMs.  I hope to taxonomize and identify a few key concepts that have appeared as a result. Do note that these periods are rough - some people were ahead of the game and many were behind.

## Era of the LLM - Nov 2022 (ChatGPT release)

LLMs entered the mainstream with ChatGPT's release.  I won't cover this much, as this era is still unfolding

### Period of the Model - Nov 2022 (ChatGPT release)

This period began with the release of ChatGPT, and ended August 7 2025.  I choose this date as it is the release date of ChatGPT 5.  It wasn't clear at the time, but that was the watershed moment - from that point, Anthropic, OpenAI, and other models reached roughly similar performance.  Up until that point, additional gains were found through direct iteration on the model and related training mechanisms.  Within this period, the model you used mattered significantly.  Upgrading models would result in large performance increases.

#### Epoch of the Prompt - Early 2023 (prompt engineering is coined as a term)

This leads us to the first set of "AI-native" companies & features.  These were prompt-forward, and as such generally leaned on the models themselves significantly.  Many chat-type applications fall into this epoch.  Most products were a direct extension of ChatGPT, frequently just proxying customer requests with a small shell prompt.

(Note, Feb 2025 is when Claude Code releases, April when Codex releases - both slot better into later eras)

#### Epoch of the Context - June 2025 (Context engineering is coined)

It became apparent that prompts leaned too heavily on models, and needed additional information added.  This led to the concept of the context, based on the prompt's context window.  Relatedly, this is when MCPs were introduced (Nov 2024), to add to the context.  Products in this era add context to the prompt - consider simple applications like a customer service chatbot.  The FAQ section can be fed in as context, allowing the agent to make intelligent observations about the contents, especially as it related ot the prompt.

### Period of the Agent - Summer, 2025 (Chat GPT 5 release)

As of this period, model performance has stagnated, and AI companies are increasingly turning to improvements after the model.  Anthropic and OpenAI turn to product improvements to get better performance, suggesting we've left the importance of models behind.  From this point forward, new models are better, but not significantly so.  Users often choose to stay on older models or downgrade.

#### Epoch of Claw - Nov 2025 (Clawd release)

Clawd (Now OpenClaw) is important to note, as it shows the first real autonomous AI agent.  This implementation is overly aggressive and insecure, but inspires many to start working on similar projects.  The underlying wrapper is Pi, which allows for easy self-improvement.  It becomes clear at this point that standalone agents are possible, but risky to use.  Clawd based products are generally one-off at this point, driven as consulting exercises.

#### Epoch of the Harness - Feb 2026 (Harness Engineering is coined)

Limitations of OpenClaw are clear, but as it is open source, people are free to improvise on its skeleton.  ClaudeCode adopts features from Clawd, including dispatch and recurring jobs.  Harness Engineering becomes important, as an agent requires tool access (skills) & memory to do discrete functions (on top ofn na context & a given prompt for an action).  There may be an age of memory under here - memory is one of the most interesting problems here.

We're still seeing one-off deployments at the moment, but there's a clear move towards consulting & eventual productization by Anthropic

## Onwards into the future

We're clearly still in the era of the harness for now.  Significant new work is being done to not only enable easy agent deployment, but also to hook in memory systems and surrounding tools so those agents are immediately useful.  That said, I don't expect this time to last long.  I'm already seeing a move to climb to higher levels of abstraction.  MCPs for example seem to be in the process of being supplanted by regular APIs plus skills (agents no longer need the offered crutch).  Single-use agents are being replaced (or added into) multi-agent workflows.

These workflows are what I'm currently expecting for the next level of agents.  Perhaps we'll see something like "Agentic Workflow Engineering" by Dec this year.