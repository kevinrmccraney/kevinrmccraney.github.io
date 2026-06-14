---
title: 💼 Job Search Sankey Diagram
date: 2026-05-05
template: about
keywords: project, self-reflection
---
<details><summary>When I think about self-tracking, I think about my dad.</summary>

The quantified self movement started hitting when I was a teenager, and people began more rigorous documentation of the choices that they made, the things that they went through. But my dad has been tracking his heart rate fairly consistently since about 1972, so it was old hat to me. He only took a break when he experienced a traumatic brain injury, putting the project on pause after a few years. His heart rate tracking project wasn't stable afterward, and neither was his career.</details>

<details><summary>He was (and is) a great father, and he tried hard, but he always had trouble in a career sense. Psychologically, I suppose I've inherited parts of this trouble.</summary>

Despite two degree programs and a spate of trying new things across different industries, I've never truly found myself "at home" anywhere professionally. The closest degree of alignment has been something like 70% at best, which is certainly not bad, but could be much better.</details>

This professional feeling of disequilibrium has led to me passively applying for jobs as a coping mechanism. For *years*.

<details><summary>But since I've been doing it passively, it's been harder to notice patterns.</summary>

Even at points when I was professionally frustrated, I've mostly never been interested enough in interviewing to seriously seek out recommendations from friends about where I could work, which I know is the winning strategy for getting a job. As a data scientist and software developer, I've wanted to explore what I could understand about my application funnel, see if I could identify any trends in the job descriptions, see if there's any patterns year-over-year.</details>

This visualization tool takes a look at that data. Generated with the help of Claude Code, I was able to take a niche dataset (all the jobs I applied for on a month-by-month basis for the past several years), clean up the data, and visualize it.

<iframe src="iframes/sankey.html" style="width:100%; height:650px; border:none;"></iframe>

<details>
There's a couple of notes:

 - It only includes data for complete years. I have data going back to 2018, but it's intermittent; maybe I'll sort it out; otherwise I will update for the current year annually.

 - This captures emailed applications and direct applications on company platforms. It does not include LinkedIn applications (though I mostly don't apply there anyway)
 
 - I generalized multi-step hiring funnels into two different states: hiring manager/code challenge and panel/code challenge/follow-up conversation. This collapses a lot of complexity (and, frankly, anti-candidate practices) into more salient groupings for charting. For example, the hiring process I had to repeat with pre-DOGE USDS because they forgot where I was in the pipeline, or the education technology nonprofit that took more time and more interviews to decide on whether to hire me than it took to select the new Pope, a process that was happening at the same time.
 </details>