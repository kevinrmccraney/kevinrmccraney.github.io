---
title: 💼 Job Search Sankey Diagram
date: 2026-05-05
template: about
keywords: project, self-reflection
---
<details>For most of my life I've been curious about personal data. The quantified self movement started hitting when I was a teenager, and people began more rigorous documentation of the choices that they made, the things that they went through. <summary>Mostly, when I think about self-tracking, I think about my dad.</details></summary>

<details>The first reason is because he has been tracking his heart rate fairly consistently since 1972 or so. The second is that he suffered a traumatic brain injury when I was a kid, and had lots of challenges being stable professionally afterward.

<summary>He was (and is) a great father, and he tried hard, but he always had trouble in a career sense. Psychologically, I suppose I've inherited parts of this trouble.</summary></details>

<details>Despite two degree programs and a spate of trying new things across different industries, I've never truly found myself "at home" anywhere professionally. The closest degree of alignment has been something like 70% at best, which is certainly not bad. <summary>It contributes to a feeling of disequilibrium, and led to me passively applying for jobs. For *years*.</summary></details>

<details>Even at points when I was professionally frustrated, I've mostly never been interested enough in interviewing to seriously seek out recommendations from friends about where I could work, which I know is the winning strategy for getting a job. As a data scientist and software developer, I've wanted to explore what I could understand about my application funnel. <summary>But since I've been doing it passively, it's been harder to notice patterns.</summary></details>

This visualization tool takes a look at that data. Generated with the help of Claude Code, I was able to take a niche dataset (all the jobs I applied for on a month-by-month basis for the past several years), clean up the data, and visualize it.

There's a couple of notes:

 - It only includes data for complete years. I have data going back to 2018, but it's intermittent; maybe I'll sort it out; otherwise I will update for the current year annually.
 - This captures emailed applications and direct applications on company platforms. It does not include LinkedIn applications (though I mostly don't apply there anyway)
 - I generalized multi-step hiring funnels into two different states: hiring manager/code challenge and panel/code challenge/follow-up conversation. This collapses a lot of complexity (and, frankly, anti-candidate practices) into more salient groupings for charting. For example, the hiring process I had to repeat with pre-DOGE USDS because they forgot where I was in the pipeline, or the education technology nonprofit that took more time and more interviews to decide on whether to hire me than it took to select the new Pope, a process that was happening at the same time.

<iframe src="iframes/sankey.html" style="width:100%; height:500px; border:none;"></iframe>