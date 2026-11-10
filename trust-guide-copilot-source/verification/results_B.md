# Fact-check results, checker B (claims C27 to C51, sources S08 to S14)

Checked on November 10, 2026.

**How pages were read.** WebFetch could not reach any host in this session; it returned a DNS block for learn.microsoft.com, directionsonmicrosoft.com and simonwillison.net. Each page was downloaded instead with curl through the session's HTTPS proxy, and the HTML was turned into text with BeautifulSoup. Every quote below is copied from that downloaded page text, not from a search-result summary. WebSearch was used only to find URLs. The "Updated" date is the page's own `ms.date` / "Last updated on" value.

**Verdict counts (25 claims):** VERIFIED 21 · PARTLY 4 (C27, C28, C38, C42) · NOT SUPPORTED 0 · WRONG 0.

Two of the 21 VERIFIED claims, C39 and C43, are marked "VERIFIED (add condition)". They're accurate as written, but each leaves out a default or condition that matters to a regulated reader.

---

## Claims

### C27. When an admin allows it, people can choose Claude (Anthropic's model) for an answer in Microsoft 365 Copilot.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **PARTLY** | "Microsoft enables Claude models on by default for most customers in commercial cloud (excluding EU/EFTA and UK)." / "In Copilot Studio, creators must select the model during agent creation. In capabilities such as Edit with Copilot in Microsoft 365 apps or Researcher, users can select Claude." / "Customers within the EU Data Boundary and customers in the UK have Claude models disabled by default." (Updated 2026-11-04, last updated 2026-11-10) | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor | "People can choose Claude (Anthropic's model) in some Copilot features, such as Researcher and editing in Word, Excel and PowerPoint. It is on by default for most commercial tenants and off by default in the EU, EFTA and UK. Admins can turn it on or off and limit it to chosen users or groups." |

Why PARTLY: "when an admin allows it" suggests Claude is off until an admin acts. Outside the EU, EFTA and UK it is on by default, so a bank there may already have it switched on. Choice is also per feature, not a general picker for every answer. In Cowork and AI in SharePoint, Claude can be used without the user picking it (Cowork model page: "The default selection is Auto"). Directions on Microsoft (S08, secondary) agrees: "Anthropic's Claude models are enabled by default in commercial tenancies and disabled in the EU and UK."

### C28. When Claude is used, Anthropic processes the request as a Microsoft subprocessor.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **PARTLY** | Supports: "To enable this change, Anthropic has onboarded as a Microsoft subprocessor." / "Unless models are labeled 'Anthropic models with Data Retention,' the Microsoft Product Terms and Microsoft Data Protection Addendum (DPA) apply." Exception: "In this scenario, Anthropic acts as an independent processor and use of Anthropic models with Data Retention is subject to acceptance of Anthropic's Commercial Terms of Service and Anthropic's Data Protection Addendum." / "Anthropic (not Microsoft) stores most inputs and outputs for up to 30 days." | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor | "For standard Claude models, Anthropic acts as a Microsoft subprocessor under Microsoft's Product Terms and DPA. Some advanced Claude models, labeled 'Anthropic models with Data Retention,' run under Anthropic's own terms, keep data for up to 30 days, and need a separate admin opt-in. Leave those off unless you have reviewed them." |

Why PARTLY: the claim is true for standard models but not for every Claude model. The exception matters a great deal for a bank.

### C29. As of November 2026, Claude in Copilot runs outside Microsoft's EU Data Boundary.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Claude models deployed in Microsoft offerings such as Microsoft Copilot, Researcher, Copilot Studio, Power Platform, and Copilot in Microsoft 365 apps are currently excluded from the EU Data Boundary, and when applicable, in-country processing commitments." (Updated 2026-11-04) / "When Claude models from Anthropic are used in Copilot experiences in Excel, PowerPoint, or Word, data processing for these models occurs outside of the EU Data Boundary." (Updated 2026-11-09) | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor ; https://learn.microsoft.com/en-us/copilot/implement/copilot-anthropic-apps | Optional addition: "It is also excluded from in-country processing commitments." Supporting: Cowork model page: "If your organization is within the EU Data Boundary, only GPT models are supported." |

### C30. Web search and model choice are tenant (admin) settings.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | Web: "The primary way that IT admins can control access to web search is by using the Allow web search in Copilot policy, which is available only in Cloud Policy service for Microsoft 365. This policy allows IT admins to either turn on or turn off web search for users or user groups across the tenant." Model: "You can restrict user access to AI provider subprocessors by assigning permissions to specific users or Microsoft Entra ID security groups in the Microsoft 365 admin center." | https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access ; https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor | Optional tweak: "Web search and Claude access are admin settings that can be scoped to users or groups." Note that users also have a "Web content" toggle when the admin allows web search. |

### C31. Copilot works as the person using it and sees what they can see (permission trimming).
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Permissions come first. Copilot only summarizes or references content that the user is already authorized to access." / "Copilot respects existing SharePoint and OneDrive permissions. If content is already overshared, Copilot can surface it to anyone who has access." (Updated 2026-11-09) | https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing | None |

### C32. Data access governance reports show sites that are shared broadly or have sharing links.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "The reports let you discover sites that contain potentially overshared or sensitive content." Reports listed: "Sharing links", "Shared with 'Everyone except external users'", "Site permissions across your organization". (Updated 2026-07-09) | https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports | None |

### C33. Restricted Content Discovery keeps a site out of Copilot and organization-wide search results without changing anyone's permissions.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Restricted Content Discovery helps you limit discovery of content from specific SharePoint sites, including recently interacted files, in organization-wide search results and Microsoft Copilot responses." / "Restricted Content Discovery doesn't change existing permissions. Users who already have access to content can continue to access that content directly." (Updated 2026-10-11) | https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery | Optional caveat: "It doesn't hide content from searches run inside the site, and it can take time to take effect." Page: "doesn't affect searches that originate from site context." Note: the S03 table still says RCD applies "unless a user had a recent interaction," which conflicts with the newer RCD page. |

### C34. "Restricted access control" limits a SharePoint site to the members of a named group.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Users not in the specified group can't access the site or its content, even if they had prior permissions or a shared link. You can apply this policy on ... sites, and OneDrive by using Microsoft 365 groups or Microsoft Entra security groups." / "Copilot and organization wide search results also honor the policy." (Updated 2026-07-30) | https://learn.microsoft.com/en-us/sharepoint/restricted-access-control | None |

### C35. Sensitivity labels on sites (containers) set privacy and sharing rules for a whole site or team.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "you can also use sensitivity labels to protect content in the following containers: Microsoft Teams sites, Microsoft 365 groups, SharePoint sites ... use the following label settings: Privacy (public or private), External user access, External sharing from SharePoint sites ..." (Updated 2026-05-07) | https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites | Optional caveat: files inside don't take the site label. Page: "Items in these containers however, do not inherit the labels." |

### C36. These SharePoint Advanced Management features become available once at least one Microsoft 365 Copilot license is assigned; a few features still need a separate add-on.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "If your organization assigns at least one Microsoft Copilot license to a user, SharePoint administrators get access to the SharePoint Advanced Management (SAM) features that support your Copilot deployment." / "Restricted site creation by apps isn't included with your Microsoft Copilot license. This feature requires the SharePoint Advanced Management Plan 1 add-on." / "Sensitivity labels (Requires E5 or G5)". (Updated 2026-06-30) | https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license | None |

### C37. An Agent Builder agent can answer questions from one chosen SharePoint folder.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Enter a URL for a SharePoint site, folder, or file ... The agent searches the URL and subpaths." / "Browse - Use the Attach cloud files picker to browse for and select SharePoint or OneDrive files, folders, or lists." / "The agent respects existing permissions and sensitivity labels." (Updated 2026-09-30) | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge | Optional: the limit is 100 SharePoint files per agent. For users without a Copilot license, SharePoint grounding is billed in Copilot Credits (S11). |

### C38. Copilot in Word, Outlook and Excel drafts; the person presses Send.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **PARTLY** | Outlook: "Edit the draft as needed, and then select Send." (Updated 06/29/2026). Word: "Copilot opens in the chat pane with Edit mode turned on." / "describe the change in your own words in chat pane ... and Copilot makes it for you." / "When Copilot plans to make changes to those [shared] documents, it shows you a preview of suggested changes in chat first." (07/06/2026) | https://support.microsoft.com/en-us/outlook/copilot-pages/draft-an-email-message-with-copilot-in-outlook ; https://support.microsoft.com/en-us/word/welcome-to-copilot-in-word | "In Outlook, Copilot drafts and the person presses Send. In Word and Excel, Copilot can now edit the open file directly, so people should review the changes before they share the file." |

Why PARTLY: true for Outlook, but Word now opens in Edit mode and changes the file itself. Only shared documents get a preview before changes. Also, Copilot Chat (Frontier users) and Cowork can send email from inside Copilot after the user approves.

### C39. Copilot Studio agents can have actions set to ask the user for confirmation before they run.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED (add condition)** | "Ask the end user before running: In the end user chat experience, ask the agent for confirmation before running the tool. This option is set to No by default." (Updated 2026-10-01) | https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent | "Copilot Studio makers can set each tool to ask the user for confirmation before it runs. This is off by default, so it has to be turned on for each tool." |

### C40. Copilot Studio agents can run with triggers and connectors (autonomous agents).
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Unlike topic triggers, which require input from a user, event triggers allow an agent to act autonomously in response to the specified event." / "Event triggers require a chosen event that generates a trigger payload and sends it to the agent through a connector." (Updated 2026-11-03) | https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about | Optional: trigger runs use Copilot Credits ("Event trigger activity counts toward Copilot Credit consumption"). |

### C41. Copilot Cowork breaks a goal into tasks across Outlook, Teams and Office apps, and can be allowed to use a browser.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "It carries out tasks on your behalf. For example, it can send emails, schedule meetings, create documents, post in Teams, and handle multistep tasks across your Microsoft 365 environment." (FAQ, 2026-11-06) / "Copilot Cowork uses Anthropic models to help securely carry out tasks across Microsoft 365 apps including Outlook, Teams, Word, Excel, SharePoint, and OneDrive." / "Cowork can complete web tasks for users in Microsoft Edge on their device." | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq ; https://learn.microsoft.com/en-us/copilot/plan/copilot-subprocessor-overview ; https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance | Optional, closer to the source: "Copilot Cowork carries out multistep tasks across Outlook, Teams and Office apps, and can be allowed to use the Edge browser." Note: Cowork uses Anthropic models, which ties it to C27 to C29. |

### C42. Copilot Chat and Agent Builder are included with Microsoft 365 Copilot and don't need a separate Copilot Studio license or IT project. (Agent Builder agents are declarative agents.)
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **PARTLY** | "Agent Builder provides an easy way to build declarative agents for Microsoft 365." / "Administrators can control whether Agent Builder is available to users." (2026-10-26) / "If you have a Microsoft 365 Copilot license, you don't need additional licenses to build declarative agents ... You don't need a Copilot Studio license to build agents." (FAQ, dated 2025-11-18) / Licensed users: "No extra charges for accessing or using extensibility features (Copilot connectors, agents, plugins)." (2026-10-26) | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder ; https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/faq ; https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/cost-considerations | "With a Microsoft 365 Copilot license, people can use Copilot Chat and build declarative agents in Agent Builder at no extra cost and without a Copilot Studio license, unless an admin has turned Agent Builder off." |

Why PARTLY: the licensing part is supported. "Or IT project" isn't on any page, and admins can switch Agent Builder off. Users with only Copilot Chat can also use Agent Builder, but SharePoint-grounded agents are then billed in Copilot Credits.

### C43. Cowork must be turned on by an admin, uses usage-based billing, and browser use stays off unless an admin allows it.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED (add condition)** | "To allow users to access Cowork, admins must enable usage-based billing." / "Access is granted only through a spending policy that selects Cowork." / "Cowork uses a usage-based billing model." (2026-10-09, last updated 2026-11-06). Browser: "Tenant admins must enable Cowork browsing by performing the following steps. This feature is disabled by default." (2026-10-22) | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance ; https://learn.microsoft.com/en-us/copilot/cowork/cowork-local-browser | "Admins turn on Cowork by adding users to a usage-based billing (spending) policy that includes Cowork. Any user in such a policy can use it, however low the credit limit. Browser use is off by default until an admin allows it." |

Condition to add: access is controlled by spending-policy scope, not by the credit limit. The access page says: "A policy with a limit of one credit still grants access." The old Agents > All Agents control no longer works: "any configuration on it has no effect on who can use Cowork." The Get started page also lists "An active Microsoft 365 Copilot license" as a prerequisite.

### C44. Copilot can suggest meeting times.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Start typing a prompt in the chat and Copilot will suggest available times and help organize your meetings and appointments." / "Copilot in Outlook will check the calendars of all the attendees and recommend a mutually convenient time to meet." (06/16/2026) | https://support.microsoft.com/en-us/outlook/schedule-a-meeting-using-copilot | None |

### C45. The Purview audit log records that Copilot interactions happened, with the user, time and app. How long logs are kept depends on your license.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "These audit records contain details about which user interacted with Copilot, when the interaction took place, and where it occurred." (2026-08-26) / "In Audit (Standard), the system retains records for 180 days." / "retain audit records for longer periods, up to one year (and up to 10 years for users with the required add-on license)." (2026-05-18) | https://learn.microsoft.com/en-us/purview/audit-copilot ; https://learn.microsoft.com/en-us/purview/audit-solutions-overview | Optional specifics: "180 days by default, up to one year with Audit (Premium), and up to 10 years with an add-on." |

### C46. Retention policies can keep Copilot prompts and responses for as long as records rules require.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Retention policies for AI apps include user prompts and responses for Microsoft 365 Copilot and Copilot Studio ... These messages can then be retained and deleted for compliance reasons." / "If the retention policy is configured to retain forever, the item remains there." (last updated 2026-06-25) | https://learn.microsoft.com/en-us/purview/retention-policies-copilot | None |

### C47. eDiscovery lets legal and compliance find and export Copilot prompts and responses.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Because user prompts and responses for AI apps are stored in a user's mailbox, you can create a case and use search ... After the search is refined, you can export the results or add to a review set." (2026-05-27) | https://learn.microsoft.com/en-us/purview/ai-microsoft-purview | Optional caveat from the eDiscovery page: "Deleting a conversation or message from Microsoft Purview or eDiscovery doesn't delete the associated Copilot memory." |

### C48. "Lethal trifecta" is Simon Willison's term for an AI with access to private data, exposure to untrusted content and a way to communicate externally.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "The lethal trifecta of capabilities is: Access to your private data ... Exposure to untrusted content ... The ability to externally communicate in a way that could be used to steal your data." (16th June 2025) | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | None. The post introduces and defines the term. It doesn't literally say "I coined," but calling it his term is fair. |

### C49. Microsoft has its own defenses against prompt injection in Copilot.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Microsoft Copilot helps mitigate these attacks by using proprietary techniques, such as jailbreak and cross-prompt injection attack (XPIA) classifiers. These classifiers analyze inputs to the Copilot service and help block high-risk prompts prior to model execution. These classifiers may not be available in all Microsoft Copilot scenarios." (2026-07-09) | https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy ; also https://learn.microsoft.com/en-us/copilot/plan/copilot-prompt-defense-in-depth | Optional caveat: "Microsoft says these defenses may not cover every Copilot scenario." |

### C50. There is an admin setting named (approximately) "AI providers operating as Microsoft subprocessors" for Anthropic models.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED (exact name)** | "Go to the Microsoft 365 admin center and select Copilot > Settings > View all. Select AI providers operating as Microsoft subprocessors. On the AI providers operating as Microsoft subprocessors page, under Available subprocessors for your organization, select Anthropic." Role: "You must be a member of the AI Administrator or Global Administrator role." | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor | Use the exact name: "Microsoft 365 admin center > Copilot > Settings > View all > AI providers operating as Microsoft subprocessors > Anthropic." The user scoping option is under "Choose who can access Anthropic models for Copilot and generative AI experiences." "Anthropic models with Data Retention" has its own separate control. |

### C51. Users can have a Microsoft 365 Copilot license or only Copilot Chat.
| Verdict | Quote | URL | Suggested wording |
|---|---|---|---|
| **VERIFIED** | "Microsoft 365 Copilot is available with two different license options: Microsoft 365 Copilot Chat is included in your Microsoft 365 subscription at no additional charge ... Microsoft 365 Copilot add-on license is available with an eligible Microsoft 365 subscription." (2026-10-26) | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/cost-considerations | None. Optional: Copilot Chat users can also be given pay-as-you-go access to work data. |

---

## Sources (S08 to S14)

| ID | Guide URL | Resolves? | Real page title (and final URL if redirected) | Matches guide title? |
|---|---|---|---|---|
| S08 | directionsonmicrosoft.com/reports/m365-copilot-adds-choice-and-risk-with-anthropics-claude | Yes, 200 (adds a trailing slash) | "M365 Copilot Adds Choice (and Risk) with Anthropic's Claude", by David Berry. Page shows "Updated: June 12, 2026 (January 20, 2026)" | **Yes.** Guide has "M365 Copilot adds choice and risk with Anthropic's Claude ... updated June 12, 2026". Only case and parentheses differ. Not paywalled: the full 1,307-word text loaded. It's a third-party analyst source, so it should support Microsoft pages, not replace them. Some of its details are now dated: it says scoping by group is "rolling out," which Microsoft now documents as available. |
| S09 | learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | Yes, redirects to learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance | "Manage Copilot Cowork for your organization" (ms.date 2026-10-09, last updated 2026-11-06) | **Close but not exact.** Guide says "Copilot Cowork admin and governance". Suggest the real title and the new URL. |
| S10 | learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions | Yes, redirects to learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-actions | "Governance and lifecycle actions for agents available in Microsoft 365 admin center" (ms.date 2026-09-23, last updated 2026-10-23) | **Yes** (wording nearly the same). Suggest the new URL. Page confirms "Block and unblock: Restrict access to an agent across the organization." |
| S11 | learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/cost-considerations | Yes, 200, no redirect | "Plan licensing and cost" (browser title: "Plan Licensing and Cost for Microsoft 365 Copilot Extensibility", ms.date 2026-10-26, last updated 2026-11-05) | **No.** Guide says "Cost considerations for Copilot agents". The page has been retitled; use "Plan licensing and cost for Microsoft 365 Copilot extensibility". |
| S12 | genai.owasp.org/llm-top-10 | Yes, redirects to /llm-top-10/ | Browser title "LLMRisks Archive - OWASP Gen AI Security Project". Main heading "2025 Top 10 Risk & Mitigations for LLMs and Gen AI Apps", listing LLM01:2025 Prompt Injection to LLM10:2025 | **Substantially yes.** The content is the 2025 Top 10 the guide names, though the page title is generic. Acceptable. |
| S13 | nist.gov/itl/ai-risk-management-framework | Yes, 200 | "AI Risk Management Framework" (NIST AI RMF landing page, dated 2026-08-13) | **No.** Guide says "NIST AI 600-1, Generative AI Profile," but the URL is the general AI RMF page. The page does mention AI 600-1 ("On July 26, 2024, NIST released NIST-AI-600-1 ... Generative Artificial Intelligence Profile"). Either retitle the entry "NIST AI Risk Management Framework (includes AI 600-1, Generative AI Profile)" or link the AI 600-1 publication directly. |
| S14 | simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | Yes, 200 | "The lethal trifecta for AI agents: private data, untrusted content, and external communication", dated 16th June 2025 | **Yes.** Guide: "The lethal trifecta for AI agents," Simon Willison, June 16, 2025. |

### Note on S07 (belongs to checker A, but C27 to C29 and C50 depend on it)
S07 (`learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps`) now redirects to `learn.microsoft.com/en-us/copilot/implement/copilot-anthropic-apps`. Its title is "Enable Claude models only for Copilot experiences in Microsoft 365 apps", not the guide's "Copilot in Microsoft 365 apps with Anthropic models". The page also starts: "The information in this article applies only to customer in the European Union (EU), European Free Trade Association (EFTA), and United Kingdom (UK)." For a general Anthropic source, the better page is "Claude models from Anthropic in Microsoft Online Services" at https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor (updated 2026-11-04). It covers the default-on/off rules, the EU Data Boundary exclusion, the setting name, and the "with Data Retention" exception. I suggest adding it or using it in place of S07.

### Other Microsoft pages used as evidence
- Claude models from Anthropic in Microsoft Online Services: https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor
- Overview of AI Subprocessors: https://learn.microsoft.com/en-us/copilot/plan/copilot-subprocessor-overview
- Determine access controls for Copilot Cowork: https://learn.microsoft.com/en-us/copilot/cowork/cowork-access
- Use the local browser with Copilot Cowork: https://learn.microsoft.com/en-us/copilot/cowork/cowork-local-browser
- Choose a model for Copilot Cowork: https://learn.microsoft.com/en-us/copilot/cowork/cowork-models
- Copilot Cowork common questions: https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq
- Add tools to custom agents (Copilot Studio): https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent
- Event triggers overview (Copilot Studio): https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about
- Agent Builder overview: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder
- Add knowledge sources in Agent Builder: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
- Extensibility FAQ: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/faq
- Audit logs for Copilot and AI applications: https://learn.microsoft.com/en-us/purview/audit-copilot
- Auditing solutions overview: https://learn.microsoft.com/en-us/purview/audit-solutions-overview
- Retention for Copilot and AI apps: https://learn.microsoft.com/en-us/purview/retention-policies-copilot
- eDiscovery for AI data: https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data
- Restricted Content Discovery: https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
- Restricted access control: https://learn.microsoft.com/en-us/sharepoint/restricted-access-control
- Data access governance reports: https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports
- Container sensitivity labels: https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites
- Data, Privacy, and Security for Microsoft Copilot: https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy
- Schedule a meeting using Copilot (Support): https://support.microsoft.com/en-us/outlook/schedule-a-meeting-using-copilot
- Draft an email with Copilot in Outlook (Support): https://support.microsoft.com/en-us/outlook/copilot-pages/draft-an-email-message-with-copilot-in-outlook
- Welcome to Copilot in Word (Support): https://support.microsoft.com/en-us/word/welcome-to-copilot-in-word
