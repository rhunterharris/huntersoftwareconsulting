+++
date = '2026-02-15T16:38:43-05:00'
draft = false
title = 'DevEx is now supreme in AI Enablement'
tags = ["velocity", "engineering", "ai"]
description = "How engineering skill and developer experience shape the results teams get from AI development tools."
+++

I have frequent conversations (and frequently see conversations on LinkedIn) focused on whether Codex, Cursor, or Gemini is the best too.  This is the wrong question.  At the present moment, model choice matters significantly less than Developer Experience, or DevEx.

{{< figure src="image-1.png" alt="Illustrative heatmap of how engineering skill and developer experience affect AI-assisted development" title="AI Velocity Scaling" width="600">}}

This is a rough heatmap of what I've seen across organizations.  As a note, I'm lumping in issues like technical debt, flaky specs, language choice, and so on into broader DevEx.  They are not DevEx, but they tend to negatively impact it. I might do a future post trying to visualizing more variables.

## Engineering Skill Scales

As you can see above, your results from AI scale with the skill of your engineering organization.  On average, lower-skill engineers see negative output, medium-skill engineers see no major changes, and high-skill see positive outcomes.  I have several hypotheses for why this is, but one primary one:  LLMs are responsive to your input.  As statistical relationships between words, high-quality, terse, specific input gets high quality results.  

## Developer Experience Scales Harder

Compared to low-quality engineering, bad developer experience sees worth velocity degradation.  Compared to medium-quality engineering, medium DevEx sees a small velocity increase.  Between high-quality engineering and high-quality DevEx, there is no major difference.

Why is this?  High-quality DevEx means fast feedback loops for AI, which means the horizon for performance degradation is pushed out.  More tasks can run more successfully for longer.  Guardrails like linters prevent the worst behaviour from LLMs, which in turn means the output can be trusted and more rapidly reviewed.

##  Conclusions

There are several interesting conclusions we can take from this:
- It's always best to acquire the best that you can.  Investment in talent pays off regardless.
- Investment in DevEx matters most as a hedge.  With strong DevEx, you can get positive results from AI even if you can't hire top quality talent.
- Strong engineering and strong DevEx work affect bottlenecks differently.
  - Strong engineering can more effectively act at bottlenecks across the stack, but especially ones before Engineering like Product.
  - Strong DevEx eases the burden of review significantly, resulting in easing of post-Engineering bottlenecks