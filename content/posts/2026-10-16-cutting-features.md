+++
date = '2026-10-09T0:03:43-05:00'
draft = false
title = "What Features Get Cut?"
tags = ["leadership", "product"]
description = "So you've built a wide product.  What do you keep, and what do you cut?"
+++

OK, so AI is here.  I see tons of building right now - building is easier than ever.  Unfortunately, this results in a pretty predictable result: a product with tons of features, and churn that's higher than comfortable.  Or, you've built out heavily, and now it's getting harder to keep everything moving together.  Customers report this screen and that screen have some weird defects, and you're at a point where checking everything is hard.

Something's got to give.  And that means some features have to be cut.

How do you go about actually paring things back?

## What to keep

The first thing you need to know is - what do your customers care about?  I'm not talking about what they SAY they care about, but their demonstrated preference?  How do you know what customer*s* care about, *in aggregate*?

First off, I highly recommend checking out tools like Heap, Posthog, Fullstory, Mixpanel, or Amplitude.  Fullstory (at least how I've used it) is a little categorically different, but we'll get to that.  The point of these tools is tracking your users.  Where do they go, where do they get stuck, what do they do when they get stuck.

Let's use onboarding as an example.  You send an invite link, they accept, they fill out a form, they're in the product.  Simple, right?  You'd be surprised - while this pattern is common, there's a common friction point - the form.  The form is for YOU, not for your customers.  If it's lightweight, you might expect to see a small dropoff on users when they reach the form (in a multistep process, you'll always see dropoff - some % will always say "whoops, not right now").  What you want to look for, is a categorical step change in the %.  Let's say, at the form, you see 30% dropoff (real number), vs 2% through the rest of the process (most notably, 2% after).  That is a very interesting and useful datapoint!  You should inspect that form and ask yourself - do we really need what we're asking for here?  As a simple fix, you might have a free text field which can be swapped to a dropdown.  Maybe you have a 48 question form (real number again), which could be simplified.  If you're unsure, you can A/B test separating pieces of a larger process to get deeper visibility too.

But that's setting the table.  So now you can see what users are doing in your application.  You should use that to see *what users are doing in your application*.  Specifically, who is going where, and are there any ghost towns.  It should be sort of obvious at this point - if there are flows that the majority of your customer base uses (preferably 75%, even more preferably 95%+), *do not tear that thing out*.  This should come as no surprise - the point of this section is mostly to give you the knowledge that yes you can get real data for this, and yes you can effectively use that data.

A note about FullStory now.  Fullstory is an odd duck in that list for a couple reasons.  First, tools like heap predominantly track users in aggregate.  This has an important place, as I've articulated above.  Fullstory is the same but opposite - you can track what an individual is doing (and especially what a user is struggling with).  To extend the example above, you can see that dropoff is high in a particular flow.  You can capture one of the users that is struggling with the flow, go to Fullstory, and watch a replay of that session.  This allows you to get real feedback on where on a page the dropoff is happening, and what leads up to the droppoff or thrash in the session.  Let me tell you, this has been *invaluable* in reproducing weird bugs and strage user behaviour.  You can learn an insane amount about your customer and how they use your product this way (it's no substitute for talking to your customers though)

## What to cut

So hopefully now, you have an idea of where your core flows are.  We're getting to the meat of it now.

First, trivially, look for dead code.  It's not being used, so slash it.  If you need it, it's in git history.
Second, look for unreleased features older than 3 months.  No, these will not see the light of day.  If you need them, they're in git history.  Gone.
Third, look for experiments aged over 3 months.  Do you have the answers you need?  If not, that's an answer in and of itself.  If you need it, git history, you know the drill already.  Cut it.

In some products, this pass alone can cut 300-600 features worth of aging cruft.You'd be shocked at how much can accumulate, and how quickly.  But this is the "engineering" pass.  Next is the product pass.

Next, look at your usage metrics.
Ghost towns?  Close them down.
Next, look for areas of your product with less than 10% usage.  Be judicious here.  If you have a billing page that's only used by admins once a month, it's probably worth leaving it, even if usage is sparse.  On the other hand, if you have a "share link" function that no one shares, cut it.
I want to stress on this point, as it's one of the grittier details here.  You do not have to service every human or agent that comes your way.  You may need to take things away from non-ICPs so you can better serve ICPs.

I want you to drive this usage % up until just after it feels uncomfortable.  You do not have to do it all at once.  You should expect to see some churn as some non-ICPs leave.  This is a feature, not a bug.  We hope to see velocity increase,  cost decrease, churn *over time* decrease, and long term revenue increase (short term, expect some decrease).  The goal is to focus velocity - pull the direction more towards the ICP, which necessitates dropping direction towards non-ICPs.

## Conclusion

Look, I know part of this is easy and part of this is hard.  It's easy to get metrics.  It's hard to use those metrics to tell people "no I do not want your money" because you probably do want their money.  But the reality is that time is more limited than money, and being able to prove validation and prove traction and prove speed *quickly*.

It takes courage to do this.  But the reality is that there is cost associated both with doing this, and failing to do so.  I'd rather take the hit that buys me more time, than the hit that buys me more money.  I can always use time to get more money.  I cannot convert money into more time.