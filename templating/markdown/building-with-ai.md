---
title: 🤖 Building with AI Agents
date: 2026-06-14
template: about
keywords: project, self-reflection
---

<details><summary>This is almost facile to say at this point, but tools like Claude Code and Codex have taken the internet by storm. Over the next several years we will begin to see a renaissance in software that is designed with only a handful of individuals in mind for its use—as Robin Sloan writes about, the app as home cooked meal is going to be the new paradigm.</summary><br>

The software as a service platform will still probably be around, but the facility with which a generative AI coding companion can build a ninety percent solution for what you're looking for will only increase over time. That is if software as we know it sticks around. A lot of major developments seem to be agents that crawl the web and perform actions for you, which means that the only permanent interface that you need is either a terminal prompt or even speech-to-text. </details>

<details>I've seen it firsthand, in fact. <summary>During some time off from my professional duties, where I ramped down a little bit to provide care for my parents, I put in some work to explore an entirely new (to me) programming ecosystem--Swift, iOS, and macOS.</summary> Owing to time and some life complexities, I elected not to spend money on any of these tools, and instead use the free version. I would ping pong between a couple of different generative AI platforms, asking specific questions about what changes needed to be made to my codebase to get the feature set I was looking for.</details>

<details><summary>Of course, prior to that I did one very important thing: I prototyped a solution using no code tools that were easily accessible to me. </summary>I had a very precise sense of the usability and functionality that I wanted, and I also was quite specific about the set of features that needed to be delivered before the app was "ready".</details>

<details><summary>Eventually I bought the bullet and acquired a subscription to Cursor. It was able to knock out the most important features to me with minimal context and essentially accelerate my development by a factor of ten.</summary> Where some of my commits would be over the span of multiple days (due to token response caps) Cursor could instead take care of those within an hour.</details>

There are a handful of things to note for somebody who has never traveled down this path before.

<details><summary>**Context is key.** If the thing that you are trying to build is well represented within the training data, then you're going to have a great time being imprecise with your language as you work with the generative AI tool to get the output.</summary> If you have a very niche problem that needs to be solved, it's likely the case that that information is not represented within the training data of a generative AI tool.</details>

<details><summary>**Writing code isn't the problem; building the system is.** A lot of the coding that I did resulted in specific chunks of code that would function entirely fine on my system, but would fail if I attempted to deploy it or use it in production.</summary> That's why the moat for a lot of tools like Base44 or Lovable is putting everything together end-to-end for you. If you do want to deploy something by yourself, you probably need to get some documentation on AWS or one of the established platforms, and that's totally fine. But it's likely that anything that you get out of one of these generative AI agents will not work from the very beginning, and if you don't have the baseline computer literacy, then you're going to have a bad time attempting to deploy it.</details>

<details><summary>**These tools are designed to create disposable software.** That is, software which is a means to an end, which might not even be used more than once.</summary> A one-off script that runs in the background to clean up a directory or some kind of API call to retrieve the data that you need. This is the kind of thing that AI excels at--the simple, straightforward idea that exists in the training data (read; is all over the web as a tutorial or proof-of-concept).</details>

<details><summary>In that sense, I am quite excited about the idea of the bespoke user interface that any user can get at by prompting an existing large language model in the right way.</summary> Certainly in the future people will be making more software for themselves and thinking hard about the ways in which they would prefer to interact with the tool. However, because of that emergent property of software--the "wanting" to be more stable as we interact with it more--I don't think that the need for literacy with computer science concepts or system building is going away any time soon. But what especially is not going away is capacity for empathy, to think about a problem, really live it, and then respond with an intervention. AI can't do that.</details>
