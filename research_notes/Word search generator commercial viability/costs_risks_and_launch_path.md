# Costs, risks and launch path for a paid AI themed word search generator (as of 13 Nov 2026)

Reading notes for the report writer:
- Official pages that were opened directly: Anthropic pricing, Google Gemini API pricing, OpenAI API pricing. Everything else comes from web-search result summaries (pages not opened in full); those are marked "(search summary)". Treat them as indicative and re-check before quoting as final.
- All prices USD. Not legal advice.
- Coverage was uneven: AI costs are solid; revenue benchmarks for comparable sites were mostly NOT found (see Gaps). Several sub-topics in the brief were not researched at all for lack of time; they are listed under Gaps rather than filled from memory.

## Running costs: AI calls, hosting/auth/database, payment fees and sales-tax handling

### Takeaway
The AI call is effectively free at small scale: roughly $0.0001 per puzzle ($0.09 to $0.15 per 1,000 puzzles) on the cheapest current models from all three providers, so hosting minimums ($0 to about $45/month) and payment fees (about 3% to 7% plus $0.30 to $0.50 per sale) dominate. A merchant of record (Paddle, Lemon Squeezy, Stripe Managed Payments) costs roughly 2 percentage points more than plain Stripe but takes over sales tax/VAT/GST collection and remittance.

### Cited Findings

AI model list prices (per million tokens, standard tier, read from official pages on 13 Nov 2026):
- Anthropic Claude Haiku 5.5: $0.10 input / $0.50 output (prompts up to 100k tokens); batch $0.05 / $0.25; cache hits $0.01. Claude Haiku 4.5: $1 / $5. Claude Sonnet 5.5: $2 / $10. — [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- Anthropic notes that Claude 4.7-and-later models use a newer tokenizer producing about 30% more tokens for the same text. — [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- Anthropic Batch API gives 50% off input and output (asynchronous; useful for pre-generating popular themes, not for live requests). — [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- OpenAI: gpt-5-nano $0.05 / $0.40; gpt-6-luna $0.10 / $0.50; gpt-4o-mini $0.15 / $0.60; gpt-5.4-nano $0.20 / $1.25; gpt-5.6-luna $0.20 / $1.20; gpt-5-mini $0.25 / $2.00. Flagship gpt-6-astra is $10 / $50. — [OpenAI API pricing](https://developers.openai.com/api/docs/pricing.md)
- Google: Gemini 2.5 Flash-Lite $0.10 / $0.40; Gemini 3.1 Flash-Lite $0.25 / $1.50; Gemini 3.5 Flash-Lite $0.30 / $2.50; Gemini 3.8 Flash $0.75 / $3.75, doubling to $1.50 / $7.50 on 1 Jan 2027. — [Gemini API pricing](https://aistudio.google.com/docs/pricing)
- Google offers a free tier on these models, but free-tier content may be used to improve Google products; paid-tier content is not. — [Gemini API pricing](https://aistudio.google.com/docs/pricing)
- Gemini 2.5 Flash (not Flash-Lite) is deprecated and reroutes to Gemini 3.5 Flash-Lite on 1 Dec 2026, an example of forced model migration with a price change. — [Gemini API pricing](https://aistudio.google.com/docs/pricing)

Hosting, auth, database (search summaries; official pages not opened):
- Supabase: Free plan pauses projects after 1 week of inactivity and allows 2 active projects; Pro from $25/month including 100,000 monthly active users, then $0.00325 per MAU; Team $599/month. Sources conflict on whether Pro is billed per project or per organization. — [Supabase pricing](https://supabase.com/pricing.md) (search summary)
- Vercel: Hobby listed with 100 GB bandwidth; Pro $20 per user per month. Cloudflare Workers: free allowance 100k requests/day; Workers Paid $5/month. Single comparison-table source. — [Developers Digest cloud cost compare](https://www.developersdigest.tech/tools/cloud-cost-compare) (search summary)

Payment processing (search summaries, mostly competitor-vendor blogs):
- Stripe base rate 2.9% + $0.30; the seller remains responsible for sales tax. Loaded cost with Billing, Tax and FX is put at 4.1% to 6.6% + $0.30. — [dev.to fee comparison 2026](https://dev.to/jettfu/stripe-vs-paddle-vs-lemon-squeezy-fee-comparison-2026-2c77) (search summary)
- Stripe Managed Payments (Stripe's own merchant-of-record product) charges 3.5% per successful transaction on top of standard Stripe processing fees. — [Merchant of Record in 2026](https://alexcloudstar.com/md/blog/merchant-of-record-indie-saas-2026/) (search summary)
- Paddle: 5% + $0.50, merchant of record, handles tax collection and remittance. — [Dodo Payments: Paddle vs Lemon Squeezy](https://dodopayments.com/blogs/paddle-vs-lemon-squeezy/) (search summary)
- Lemon Squeezy: headline 5% + $0.50, with surcharges for international, PayPal and subscription payments (one source: +1.5% international); a competitor puts the all-in rate at 7% + $0.50. Stripe acquired Lemon Squeezy in 2024. — [Rework: Paddle vs Lemon Squeezy](https://resources.rework.com/tools/billing-revenue/paddle-vs-lemon-squeezy); higher figure from [Creem fee breakdown](https://www.creem.io/blog/honest-payment-fee-breakdown-creem-vs-stripe-paddle-ls) (search summaries; vendor-biased)

### Inferences
- Cost per puzzle (my arithmetic, assuming about 200 input tokens and about 200 output tokens per call, which is generous for a short prompt plus 20 words as JSON):

| Model | Per puzzle | Per 1,000 puzzles |
|---|---|---|
| gpt-5-nano | $0.00009 | $0.09 |
| Gemini 2.5 Flash-Lite | $0.00010 | $0.10 |
| Claude Haiku 5.5 | $0.00012 | $0.12 |
| gpt-6-luna | $0.00012 | $0.12 |
| gpt-4o-mini | $0.00015 | $0.15 |
| Gemini 3.1 Flash-Lite | $0.00035 | $0.35 |
| Gemini 3.5 Flash-Lite | $0.00056 | $0.56 |
| Claude Haiku 4.5 | $0.0012 | $1.20 |
| Claude Sonnet 5.5 | $0.0024 | $2.40 |

- Caveat on the table: models that "think" before answering bill reasoning tokens as output, which can multiply the output count several-fold on a trivial task unless reasoning is set to minimal. Even at 10x, the cheapest tier stays near $1 per 1,000 puzzles.
- At 10,000 puzzles a month the AI bill is about $1 to $6 on the cheapest tier. AI cost is not the constraint; a $5/month subscription pays for tens of thousands of generations.
- A plausible fixed stack at launch is $0 to $45/month (free tiers, or Supabase Pro $25 + Vercel Pro $20), plus domain. On a $5 sale, plain Stripe keeps about $0.45 (9%); a 5% + $0.50 merchant of record keeps about $0.75 (15%). Low price points are hit hard by the fixed per-transaction fee, which favors annual plans or bundles over $1 to $3 one-off purchases.
- For a US founder selling to the UK and Australia, a merchant of record removes the need to track UK VAT and Australian GST registration for digital services personally; that is the main reason indie sellers accept the higher fee.

### Gaps
- Official pricing pages for Stripe, Paddle, Lemon Squeezy, Gumroad, Vercel, Netlify, Cloudflare and Firebase were not opened. Gumroad, Netlify and Firebase figures were not found at all.
- Whether Vercel's free Hobby plan prohibits commercial use was searched but not confirmed in results (this restriction is widely reported; verify on Vercel's fair-use page).
- UK VAT and Australian GST thresholds for overseas digital sellers, and South Carolina / US state sales-tax treatment of SaaS, were not researched.
- Email-sending, domain, error-monitoring and PDF-generation costs were not researched.

## Abuse and cost control; content safety for user-typed themes

### Takeaway
Little direct evidence was gathered on this question. What the sources do show is that the common failures in small AI-built apps are exactly the ones that create cost abuse: API keys exposed in the browser and no rate limiting.

### Cited Findings
- A scan of 62 Lovable-built apps in early 2026 reported recurring exposed API keys, disabled row-level security, missing authentication on routes, and no rate limiting on login endpoints. — [Indie Hackers: why vibe-coded apps are still leaking user data in 2026](https://www.indiehackers.com/post/why-vibe-coded-apps-are-still-leaking-user-data-in-2026-4a6ab2fbdd) (search summary)
- Apps generated by Bolt.new were reported with Stripe secret keys and OpenAI API keys hardcoded in client-side JavaScript. — [dev.to scan of 1,764 vibe-coded apps](https://dev.to/stefan_lederer_8b1bbcef01/we-scanned-1764-vibe-coded-apps-453-had-critical-vulnerabilities-heres-what-we-found-beyond-464e) (search summary; scanner-vendor source)
- Anthropic's prompt caching prices cache hits at $0.01 per million tokens on Haiku 5.5, and the Batch API halves prices, both relevant to pre-generating popular themes. — [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- Anthropic's Usage Policy requires developers to maintain their own safeguards; products serving minors carry additional requirements (age-appropriate safeguards, compliance with child-protection law). — [Anthropic Usage Policy](https://www.anthropic.com/aup); [Child safety guidance for developers](https://support.claude.com/en/articles/15591275-child-safety-guidance-for-developers) (search summary)

### Inferences
- Because one generation costs about $0.0001, the realistic abuse risk is not a bankrupting bill from ordinary users but (a) a leaked key being used for other, expensive work, and (b) scripted hammering. The controls that matter are: key held server-side only, a hard monthly spend cap set in the provider console, per-IP and per-account rate limits, and a cap on theme length.
- Caching is unusually effective here: themes repeat heavily (Christmas, Halloween, animals, Bible, states), so storing the word list per normalized theme makes most requests cost nothing and also allows human review of popular lists.
- Content safety has three separate surfaces: the typed theme, the generated word list, and accidental words formed by random filler letters. The third is not an AI problem; it needs a blocklist scan of the finished grid in all 8 directions with regeneration on a hit. No source was found documenting how existing generators handle it.

### Gaps
- No sourced data on what rate limits, CAPTCHA or login-wall settings comparable tools use, or on conversion impact of a login wall.
- No sourced guidance found on profanity filtering in filler letters or on moderation API pricing (OpenAI and others offer moderation endpoints; not verified here).

## Legal and compliance: children, schools, privacy, accessibility, IP, AI provider terms

### Takeaway
The heaviest exposure comes from knowingly serving children or schools: the amended COPPA rule has been fully in force since 22 April 2026 and the UK Children's Code has no small-business exemption. Purely AI-generated word lists are not protected by US copyright, so the output itself is not a moat, and branded themes carry takedown risk that grows once puzzles are sold.

### Cited Findings

COPPA (US):
- Amendments were published 22 April 2025, took effect 23 June 2025, and most operators had until 22 April 2026 to comply; the rule is now fully in force. — [Hunton: FTC publishes final COPPA rule amendments](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-publishes-final-coppa-rule-amendments); [Mondaq: COPPA's amended rule is now in full effect](https://webiis10.mondaq.com/unitedstates/privacy-protection/1790866/coppas-amended-rule-is-now-in-full-effect-what-operators-need-to-know) (search summaries)
- Key changes: separate parental consent before using children's data for targeted advertising or disclosing it to third parties; biometric identifiers added to "personal information"; indefinite retention of children's data prohibited; more safe-harbor transparency. — [Loeb: the amended COPPA rule](https://www.loeb.com/en/insights/publications/2025/05/childrens-online-privacy-in-2025-the-amended-coppa-rule); [Foley Hoag, July 2026](https://foleyhoag.com/news-and-insights/blogs/security-privacy-and-the-law/2026/july/the-amended-children-s-online-privacy-protection-act-(coppa)-regulations-what-your-business-needs/) (search summaries)
- One compliance blog cites a maximum civil penalty of $53,088 per violation per day for 2026; not verified against the FTC. — [ComplianceHub](https://compliancehub.wiki/coppa-april-22-deadline-ftc-updated-rule-compliance/) (search summary; low-authority)

UK Children's Code (Age Appropriate Design Code):
- Applies to online services "likely to be accessed by children" (under 18), meaning more probable than not, even if children are not the target audience. — [ICO: introduction to the Children's code](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/introduction-to-the-childrens-code) (search summary)
- Edtech offered directly to consumers is in scope; edtech supplied through schools is in scope where the provider influences the nature and purpose of processing children's data. Schools themselves are not in scope. In-scope providers must carry out a DPIA. — [ICO FAQs for edtech and schools](https://ico.org.uk/for-organisations/childrens-code-hub/faqs-for-education-technologies-edtech-and-schools/) (search summary)
- No small-business exemption was found in the results. — [ICO FAQs for edtech and schools](https://ico.org.uk/for-organisations/childrens-code-hub/faqs-for-education-technologies-edtech-and-schools/) (search summary; absence of evidence, not confirmed)

Accessibility:
- Seyfarth Shaw counted about 3,117 website accessibility cases within 8,667 ADA Title III federal suits in 2025, up 27% on 2024; another tracker counts 3,948 federal web cases (different method). — [Clym: accessibility lawsuits 2025](https://www.clym.io/blog/accessibility-lawsuits-2025-small-business-websites) (search summary; vendor blog)
- About two-thirds of website/app suits tracked to mid-June 2025 were against companies with under $50 million revenue; ecommerce is 69% to 77% of cases; filings concentrate in New York, Florida and Illinois. — [Stacker via KEYT](https://keyt.com/news/money-and-business/stacker-money/2026/01/14/accessibility-lawsuits-rose-by-37-in-2025-why-small-businesses-can-no-longer-ignore-their-websites/) (search summary)
- A Florida flower shop owner paid about $7,000 to settle a web accessibility suit, an indication of small-business settlement size. — [Moneywise](https://moneywise.com/news/florida-flower-shop-owner-pays-7k-to-settle-web-accessibility-lawsuit) (search summary; headline only)
- European Accessibility Act applies from 28 June 2025 to EU and non-EU businesses offering covered services in the EU; microenterprises providing services (fewer than 10 employees and turnover or balance sheet not above EUR 2 million) are exempt from the service requirements under Article 4(5). Sources disagree on whether the two tests are "and" or "or". — [Level Access: EAA](https://www.levelaccess.com/compliance-overview/european-accessibility-act-eaa/); [Deque: EAA](https://www.deque.com/?p=42677) (search summaries)

Copyright in AI output:
- US Copyright Office, Part 2 "Copyrightability" (29 Jan 2025): "prompts alone do not provide sufficient human control to make users of an AI system the authors of the output"; wholly AI-generated output is not protected; protection can attach to human selection, arrangement or significant modification, case by case. — [Copyright Alliance summary](https://copyrightalliance.org/ai-report-part-2-copyrightability/); [IPWatchdog](https://ipwatchdog.com/2025/01/29/part-two-copyright-office-ai-report-says-creative-prompting-doesnt-constitute-authorship/) (search summaries; report is nearly two years old, no later change found)

Branded themes:
- Etsy fan-sellers of Harry Potter-inspired goods reported takedown notices from Warner Bros., and Disney removals reached products that were not copies of official merchandise. — [Marmalead: Etsy copyright infringement](https://blog.marmalead.com/etsy-copyright-infringement/) (search summary; blog)
- Teachers Pay Teachers leaves policing to rights holders via a DMCA notice process. — [Education Week, Dec 2018](https://www.edweek.org/ew/articles/2018/12/19/on-teachers-pay-teachers-some-sellers-are.html) (search summary; 8 years old)
- Licensed classroom material exists: Twinkl's Harry Potter display pack was made in partnership with Bloomsbury. — [Twinkl](https://www.twinkl.com/resource/harry-potter-display-pack-t-e-1647510928) (search summary)

AI provider terms:
- Anthropic's Commercial Terms: the customer owns outputs to the extent permitted by law, keeps rights to inputs, and Anthropic may not train on customer content from the commercial services. — [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms) (search summary)
- Anthropic's Usage Policy defines a minor as anyone under 18 and lets API customers build products for minors subject to extra safeguards; Anthropic's own consumer apps remain 18+. — [Anthropic Usage Policy](https://www.anthropic.com/aup); [TechCrunch, May 2024](https://techcrunch.com/2024/05/10/anthropic-now-lets-kids-use-its-ai-tech-within-limits) (search summaries)

### Inferences
- Design choice with the largest legal payoff: sell to adults (teachers, parents, activity directors, puzzle hobbyists) who print or share puzzles, and do not create child accounts. A child solving a shared puzzle link with no login and no tracking collects far less personal data than a child account does. Third-party ad or analytics trackers on pages children use would reopen the COPPA question, which matters if the plan is ad-funded.
- Selling directly to schools is a different, heavier product: it brings data-processing agreements and the edtech limb of the UK Children's Code. Selling to individual teachers who pay with their own card avoids most of that.
- A US solo founder likely falls under the EAA microenterprise exemption for services, and the UK is outside the EAA, but ADA demand letters are the practical US risk. An interactive 13 by 13 letter grid is hard to make keyboard- and screen-reader-accessible, so this is real build work, not a checkbox.
- Since a raw AI word list has no copyright, competitors can copy generated lists freely; equally, the founder gets little protection for them. Protectable assets would be the brand, the code, human-curated collections and design.
- Branded themes: a user privately generating a "Harry Potter" puzzle is low-risk for the founder, but the founder publishing SEO landing pages, paid packs or marketplace listings built on brand names is where takedowns land. Blocking or not indexing brand-name themes on public pages is the conservative reading.

### Gaps
- FERPA, state student-privacy laws and student data privacy agreements: not researched.
- GDPR / UK GDPR basics (representative requirements, lawful basis, ICO fee) and Australian Privacy Act: not researched.
- WCAG 2.2 specifics, the DOJ Title II rule and its deadlines: not researched.
- No case or official guidance found on trademark liability for word lists containing brand or character names, or on nominative fair use for such tools.
- OpenAI and Google commercial-use and under-18 terms: not researched. Anthropic terms were not opened directly.
- UK and Australian positions on copyright in AI-generated works: not researched.

## Business models and benchmarks

### Takeaway
I found no reliable, documented revenue or traffic figures for an indie word search generator or worksheet-maker site; that absence is itself a finding. The usable benchmarks are generic: freemium conversion commonly 2% to 5%, and premium ad networks now reachable at far lower traffic than a year ago.

### Cited Findings
- ChartMogul's conversion report: for freemium self-serve products 3% to 5% free-to-paid is "good" and 8% to 12% "great"; a quarter of freemium products convert below 2.5% (measured as free signup to paying within six months). — [ChartMogul SaaS Conversion Report](https://chartmogul.com/reports/saas-conversion-report/) (search summary)
- First Page Sage (80+ SaaS clients, 2021 to 2025): 3.7% average for traditional freemium; EdTech lowest at 2.6%. — [Userpilot summary](https://userpilot.com/blog/freemium-to-premium) (search summary; attribution to this URL uncertain)
- Mediavine's entry program Journey requires over 1,000 monthly sessions (lowered from 10,000, reported effective 15 Jan 2026); the main Mediavine program is described as requiring $5,000+ annual ad revenue. — [Mediavine help center](https://help.mediavine.com/what-does-it-take-to-get-approved-by-mediavine); [Productive Blogging](https://www.productiveblogging.com/everything-you-need-to-know-about-journey-by-mediavine/) (search summaries)
- Raptive cut its minimum from 100,000 to 25,000 monthly pageviews in October 2025. — [Search Engine Journal](https://www.searchenginejournal.com/raptive-drops-traffic-requirement-by-75-to-25000-views/558780/) (search summary)
- Ad RPM estimates conflict and are low-authority: AdSense $1 to $5 in one source and $5 to $15 in another; Mediavine $15 to $35; Raptive $20 to $50; education content about $5 to $7 on AdSense. No puzzle/games-specific RPM found. — [Newor Media](https://newormedia.com/blog/best-adsense-alternatives/); [MonetizeMore](https://www.monetizemore.com/blog/how-much-should-my-website-be-earning/) (search summaries; ad-vendor blogs)
- Comparable-ish cases found, none with generator revenue: Jumblie (daily word search, built solo in about a week in plain HTML/CSS/JS, traffic from a game-show fan community, no revenue disclosed) — [Indie Hackers](https://www.indiehackers.com/post/i-made-jumblie-a-daily-word-search-game-44fc9ef768); OneWordSearch from the maker of Waffle, about 44k players, no revenue disclosed — [mobilegamer.biz](https://mobilegamer.biz/daily-word-game-studio-waffle-is-the-latest-small-dev-to-find-a-big-audience); IT Word Search Labs, launched Jan 2026, no numbers — [Indie Hackers](https://www.indiehackers.com/product/it-word-search-labs) (search summaries)
- Hey, Good Game is a studio that buys indie puzzle games (acquired Mathler, Sumplete and Crosswordle from Daniel Tait), showing an exit market exists for daily puzzle games with audiences; prices not disclosed. — [hey.gg](https://www.hey.gg/) (search summary; company marketing)
- ChartSheets, a bootstrapped spreadsheet-template seller, is reported at $40,000/month driven by Pinterest traffic; this is a template business, not a generator, and the figure is self-reported via a secondary post. — [Goodreads author blog repost](https://www.goodreads.com/author_blog_posts/25460887-40-000-per-month-selling-spreadsheet-templates-via-pinterest) (search summary; weak source)

### Inferences
- Illustrative arithmetic only (not a forecast): 10,000 monthly visitors, 10% signing up, 3% of signups paying $5/month gives 30 payers and about $150/month. The same traffic at a $10 to $20 RPM on roughly 20,000 pageviews gives $200 to $400/month from ads. At small scale, ads and subscriptions are the same order of magnitude, and both are small until traffic reaches the hundreds of thousands.
- Ads conflict with a child-facing or school-facing positioning (COPPA consent rules for targeted ads), so the founder likely has to choose between an ad-funded general-audience site and a paid, ad-free teacher/caregiver product.
- The successes that surfaced in this niche are daily games with a shared-habit loop (Jumblie, Waffle) or printable-content sellers on marketplaces, not on-demand generators.

### Gaps
- No Flippa or Acquire.com listings for puzzle/worksheet generator sites were retrieved; no documented revenue for incumbents (for example Discovery Education's Puzzlemaker, TheWordSearch.com, Education.com's generator, WordMint, My Word Search). A targeted pass on those names is needed.
- No sourced figure for how long SEO takes for a new site in this niche, nor for the effect of AI search overviews on tool-site traffic.
- No sourced typical price points for worksheet-maker subscriptions (WordMint, Twinkl, Education.com pricing not checked).

## Distribution channels and defensibility of an LLM wrapper

### Takeaway
Marketplaces reach buyers immediately but take a large cut (TPT Basic now pays out about 55% minus $0.30 per resource), and they sell finished printables rather than access to a tool. No source was found supporting the defensibility of a pure generator when ChatGPT, Claude and Gemini produce word searches on request; that question remains open and unfavorable on the evidence gathered.

### Cited Findings
- Teachers Pay Teachers retired its Premium Seller tier on 1 Oct 2026; options are now Basic and Exclusive. Basic: one-time $29 fee, 55% payout and $0.30 per resource (older guides say 60%). Exclusive: $59.95/year; payout rate not captured. — [Edubracket platform comparison, prices read 19 Oct 2026](https://edubracket.com/articles/best-platforms-to-sell-teaching-resources-2026) (search summary; verify on TPT help center)
- Etsy permits AI-generated items if disclosed under its "Designed by a seller" label (introduced July 2024); total platform take for most US sellers is described as roughly 10% to 12%; Offsite Ads fee 12% for shops above $10,000 annual sales. — [ecomcrew](https://www.ecomcrew.com/etsy-calls-itself-human-centered-its-sellers-have-a-more-complicated-story-to-tell/); [selfemployed.com](https://www.selfemployed.com/news/etsy-seller-ai-disclosure-fees-2026/) (search summaries)
- Community-led traffic worked for Jumblie: a good share of its early traffic came from the fan community of a Netflix game show. — [Indie Hackers](https://www.indiehackers.com/post/i-made-jumblie-a-daily-word-search-game-44fc9ef768) (search summary)
- Pinterest is reported as the main traffic source for a template seller at $40,000/month. — [Goodreads author blog repost](https://www.goodreads.com/author_blog_posts/25460887-40-000-per-month-selling-spreadsheet-templates-via-pinterest) (search summary; weak source)
- A solo builder of a free random-letter generator reported 8,250 search impressions in 10 weeks with no ad spend, a data point for how slowly a new tool site accrues search visibility (impressions, not clicks). — [Indie Hackers](https://www.indiehackers.com/post/i-built-a-free-random-letter-generator-8-250-impressions-in-10-weeks-with-zero-ad-spend-cfd8ec386f) (search summary; title only)

### Inferences
- The generation step is a commodity: it costs a hundredth of a cent and any general chatbot can do it. What a chatbot does less well is the finished artifact and the workflow: a guaranteed-valid grid, print-ready PDF with answer key, large-print and difficulty options, saved libraries, class or resident-group share links, and vetted kid-safe or senior-friendly word lists. Any defensibility would sit there, plus audience and brand, not in the AI call.
- Marketplace mismatch: TPT and Etsy buyers purchase packs of ready puzzles. The generator could be the founder's production tool for such packs (with human curation, which also helps the copyright position) while the site sells the tool; those are two different businesses with different margins.
- Niche positioning (senior-care activity directors, ESL teachers, church groups, party planners) looks more reachable for a solo founder than head-on SEO against long-established free generators, but this is reasoning, not sourced evidence.

### Gaps
- Not researched: ChatGPT GPT store economics, Claude artifact sharing as a channel, app-store distribution, newsletter benchmarks, senior-care or education partnership examples, per-theme SEO landing page results, Pinterest data specific to puzzles.
- Etsy's exact fee schedule ($0.20 listing, transaction and processing percentages) was not confirmed from an official page.
- No source found that directly argues for or against defensibility of AI puzzle generators versus general chatbots.

## Build path for a non-developer and minimum sellable version

### Takeaway
AI app builders make a working version reachable for a non-developer, but the documented failure pattern is security basics (exposed keys, open databases, no rate limiting), which are exactly what this product adds when it moves from a single page to accounts and payments. Ongoing maintenance is real: model deprecations and platform fee changes happened within the months reviewed.

### Cited Findings
- Escape.tech's scan of 5,600 public vibe-coded apps (Oct 2025) reported more than 2,000 high-impact vulnerabilities and more than 400 exposed secrets. — [The Next Web: Lovable and the vibe coding security crisis](https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed) (search summary; attribution of the statistic to this URL uncertain)
- Replit employees found a flaw in Lovable's row-level security implementation; Lovable said it shipped fixes and has added warnings when users paste API keys into chat plus detection of incorrect database access rules. — [Analytics India Magazine](https://analyticsindiamag.com/ai-features/when-replit-employees-found-a-critical-security-vulnerability-in-lovable) (search summary)
- A UK "platform rescue" agency published (2 Apr 2026) on what it finds when auditing AI-generated code, evidence of a paid-cleanup market for such apps. — [Rocking Tech](https://rockingtech.co.uk/blog/ai-generated-code-security-what-we-find) (search summary; vendor)
- Pre-launch checklists for Cursor/Lovable/Bolt/Replit apps center on keeping secrets out of client code, enabling row-level security, route authentication and rate limiting. — [dev.to: vibe coder's pre-launch security checklist](https://dev.to/hacksafe/the-vibe-coders-pre-launch-security-checklist-25-checks-for-cursor-lovable-bolt-replit-apps-12i) (search summary)
- Examples of forced upkeep seen during this research: Gemini 2.5 Flash reroutes to another model on 1 Dec 2026 and Gemini Flash prices double on 1 Jan 2027 — [Gemini API pricing](https://aistudio.google.com/docs/pricing); TPT restructured seller tiers on 1 Oct 2026 — [Edubracket](https://edubracket.com/articles/best-platforms-to-sell-teaching-resources-2026) (search summary)
- A solo developer built a daily word search game in about a week with plain HTML, CSS and JavaScript, showing the puzzle itself is a small build. — [Indie Hackers: Jumblie](https://www.indiehackers.com/post/i-made-jumblie-a-daily-word-search-game-44fc9ef768) (search summary)

### Inferences
- The existing single page already covers the hard-looking part (generation and the interactive grid). The commercial additions are the standard, well-trodden ones: a server-side function holding the AI key, sign-in, a database of saved puzzles, a hosted checkout, and PDF export with answer key. Using a merchant of record's hosted checkout and a managed auth/database service keeps the founder out of card data and password storage.
- A minimum sellable version, by inference from the gaps chatbots leave and from the compliance findings: free generation with a daily cap; paid tier with saved puzzles, print/PDF export with answer key, share links, size and difficulty options, no ads; privacy policy and terms; blocklist for themes and grids; spend cap and rate limits.
- Budget a one-off independent security review before taking payments; given the audit findings above, this is the highest-value outside spend for a non-developer.

### Gaps
- No sourced figures on hours per month of maintenance for a micro-SaaS, on the cost of AI builder subscriptions (Lovable, Bolt, Replit, Cursor, Claude Code), or on freelance security-review prices.
- No sourced feature comparison of existing paid word search makers to confirm what paying users expect in a minimum version.
