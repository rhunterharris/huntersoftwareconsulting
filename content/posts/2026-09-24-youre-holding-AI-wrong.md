+++
date = '2026-09-24T07:46:43-05:00'
draft = false
title = 'You're holding AI wrong'
tags = ["product", "leadership"]
description = "AI can be used to productive ends.  But at the same time, I see most organizations using AI for output instead of results."
+++

I'd like to lead with - I use AI very actively.  As we speak (well, as I write), I have 7 discrete projects running X (X being a large number) of agents doing forward development.  Am I moving faster than I was pre-AI?  Sure.  Somewhat.  Probably not double - I feel like the 2-30% increase seems about right.  20-35% in what matters most, but it does allow me to do more "stuff" in parallel.  But today, I'm not talking about that.  I'm here to talk about how I actually used AI to get stuff done, very rapidly.

## The problem

Let me know if this situation rhymes with your experience.  You've got a mobile app.  It does some stuff well, but the design is... "unsatisfactory" to say the least.  So you and a bunch of stakeholders get together in a room, and you quickly establish (you, not others unfortunately) that not everyone is on the same page.  No one likes the state of things, but there are more opinions on direction than there are people in the room.  In short, discord.

In this case, the mobile app needed a design update.  Was it the worst in the world?  No.  But it was bad enough that Sales didn't want to sell it, and Product voices didn't want to talk to customers about it.On a deeper level, the information hierarchy was frankly confusing, and this led to both of these departments having to explain parts of the app that should have been self-explanatory.

More importantly, these conversations were cycling, and progress wasn't being made.  Someone needed to cut through the noise

## The solution

How I cut through this was pretty simple.  First, I asked CLaude to make a artifact - basically a website, with a mockup of the mobile app.  I had it take one slice of the experience, and create a 2 minute loop in HTML of that experience.  Easy enough.

Next, I shook through each stakeholder's wants (and dislikes) and hooked each into a toggle beside this experience.  In parallel, I took each of these asks, and had an agent write a short feasibility report on what it would take to enable that toggle - what needs to be added, or removed, and the risk.  Some items were trivial, some items would require some refactoring.  In general, there were a few refactors we'd need to consider to support "everything", such as adopting new rendering libraries.  I marked each item subtly along these refactor lines, for my own reference.

The next step should be obvious.  I sent the page to each stakeholder and told them "Toggle these to your heart's content, and send me your best one".  Of course, at this point some incredulation and adulation occured, but we got our toggles from each stakeholder (I had a one click export that would send me the state).

Plug the results into the LLM and suddenly we realize everyone is a lot more aligned than they seem.  In addition, almost everyone is aligned around the cheapest options.  I did have to go have a few chats and ask for a few compromises, but once these conversations were this close to done, agreement was quickly reached.

I had agreement in hours, a new version available a few hours later, and the new version went out that night.  A weekslong process boiled down to hours.  Disagree, commit, ship.

## What can we learn here?

Most people are using AI to "get more done".  More code, more output, more "stuff".  You're probably doing this, I am too.  It's easy, and honestly it's kinda fun.

But AI's value isn't really in the additional output - it's in driving outcomes and results faster.  It's the meetings you don't have to have, the agreements you can reach faster, the problems that don't occur.  If you know what to do, ship it.  It was fast before, it's fast now.  If you don't, use AI to figure it out.  This is the part that AI really accelerates.

If your organization is mostly using AI to scale output, try something different.  Try using AI to plan better, and plan faster.  Instead of adding more spinning plates, see if that doesn't make some plates go away.  I mean in my case I was getting ready to be very wrong - instead, AI turned the work into a triviality.

Org messes can still soak all the additional productivity gains if you're not careful.  Instead of adding to the noise, resolve it instead.  I think you'll like the results.