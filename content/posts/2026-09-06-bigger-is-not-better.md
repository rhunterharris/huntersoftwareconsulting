+++
date = '2026-09-06T07:46:43-05:00'
draft = false
title = 'Bigger is not Better'
tags = ["product", "engineering", "leadership"]
description = "A look at the tradeoffs of growing a company, and why bigger does not automatically mean better."
+++

Bigger is better, right?  Bigger company, more engineers, more product managers, more output.  That's unequivocally good, right?  Well, I think we all know that this isn't the case at large, but we still desire more and more and more.

## If You Give a Mouse a Cookie

It's funny, but I frequently come back to [If You Give a Mouse a Cookie](https://en.wikipedia.org/wiki/If_You_Give_a_Mouse_a_Cookie) when thinking about  product technology leadership.  I remember being an IC, and it always felt like we never had enough headcount to execute on the ambition we had in the team.  Just one more resource, and we could get that feature done even earlier.  Just one more resource, and we could knock out that side priority.  One more resource, and we could run those initiatives in parallel instead of serial, saving months!  But always just one more resource.

Let's look through the lens of giving a mouse a cookie, shall we?  We give the team one additional engineer.
First, that additional person needs work from the PM. (Product Management)
Second, that person starts generating more work for review and QA. (Engineering)
Third, that person needs to be managed. (Eng. Management)
Fourth, that person will have questions about design (Design)
Fifth, that person will need to manage priorities (Project Management)

So while we add engineering capacity, capacity is pulled from all the surrounding departments *including engineering itself*.  Of course, this is one source of capacity consumption among many.

## Scalability

This is an interesting observation, and just one aspect of scalability.  It should be obvious that departmentally, different responsibilities scale differently.  Looking at management for example - having 1 direct report is clearly an inefficient use of resources.  But similarly, having 100 direct reports means the manager is diluted enough that those people might as well be unmanaged (I should add, the cutoff here is dramatically lower than 100.  Generally lower than 10.).

Obviously, different people in different roles scale differently - and the scaling is dramatically influenced by their side priorities.  A gifted manager might be able to manage 8-10 direct reports if they're concentrating on that.  Meanwhile, if they're the owner for a series of internal dashboards, they might only have the bandwidth for 1-2 direct reports.

A larger, scarier scalability problem is communication overhead.

| Team Size | Communication Links |
|----------:|--------------------:|
| 1         | 0                   |
| 2         | 1                   |
| 3         | 3                   |
| 4         | 6                   |
| 5         | 10                  |
| 6         | 15                  |
| 7         | 21                  |
| 8         | 28                  |
| 9         | 36                  |
| 10        | 45                  |

As we can see, team size increases linearly, while links increase quadratically.  I should add, cancel all the meetings you want, but this overhead persists.  The only way to eliminate it is by siloing people (which has its own cost), or literally removing people from the loop via firing.  You can mitigate it by making teams of teams, but ultimately delays scaling (and does require dedicated resources for that).  Typically it does show up in sync meetings, but it shows up in grooming, planning, transferring and managing priorities, handoffs, stand-ups, code reviews, and really any process which requires you to coordinate more than yourself - the bad news being, that is most activity that businesses engage in.

This is a pretty compelling argument for the "two pizza team"!  Keeping this overhead low means individuals focus on their core responsibilities rather than communication management (they can leave much of that to the managers).

## Smaller is not Better, Either

Back to the previous paragraph - so we should conclude that we should all be platonic ideal Founder-Builders: everyone building solo with minimum coordination, right?  Well, that's an obvious strawman, no surprises here.

One reason we scale teams is risk and redundancy.

| Team Size | Productivity Lost if 1 Person Is Sick |
|----------:|---------------------------------------:|
| 1         | 100%                                   |
| 2         | 50%                                    |
| 3         | 33%                                    |
| 4         | 25%                                    |
| 5         | 20%                                    |

One important caveat to this chart - sometimes two people get sick at once.  Sometimes there are global pandemics and lots of people get sick at once.  Sometimes people also quit.

The point being that, a scaled team might be less efficient day to day, but dramatically more efficient "if something happens" (something always happens, ESPECIALLY at startups).  There's overhead associated with this as well - spinning priorities down, replanning, spinning up priorities are all work that takes time.  With a team that's too small, replanning overhead can swamp the gains from smaller communication overhead - handily, at that.

-----

So where do we go from here?

Personally, I've worked on teams from 1 - about 20.  Historically, I've found teams of about 7 to work quite well (frequently this grows to closer to 10 when you include specialists attached to the team).

Right now though? With AI?  I really recommend teams stick closer to 3.  3-5 is a sweet spot where you have basic redundancy, but various overheads are minimal.  This does represent a bet though - you're betting that multiple people won't be out at the same time (or that you can predict when they'll be out, which isn't impossible).  AI can mitigate some of the replanning overhead in this case.

The critical benefit here though, in my opinion, is avoiding swamping your organization.  Right now, we've drastically scaled building output, but haven't really holistically fixed Product and Review bottlenecks (I mean, I've solved them - but not the industry at large.  Just apply the theory of constraints).  AI can drastically scale useless work, so keeping your organization tight makes steering towards profit easier.