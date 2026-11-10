# Fact-check results A: claims C01-C26, sources S01-S07

Checked November 10, 2026. Checker A.

## How the pages were read

- The WebFetch tool could not reach learn.microsoft.com from this session (host failed to resolve). I downloaded every page directly with curl through the session's network proxy, converted the HTML to text, and read it. All quotes below come from those downloads, not from search-result summaries. Local copies are in `/tmp/claude-0/-home-user-GPT5/1c53a6ff-b81e-5da4-bc19-2151e3272608/scratchpad/verify/pages/`.
- web.archive.org reset the connection, so I could not read the old (pre-redirect) version of S02.
- **Cross-cutting finding:** Microsoft has renamed the product. The Copilot Chat privacy page says: "Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. Some experiences, licenses, and capabilities might continue to reference Microsoft 365 Copilot ... during the transition period." (https://learn.microsoft.com/en-us/copilot/plan/privacy-and-protections). License names still use "Microsoft 365 Copilot (Basic)" and "Microsoft 365 Copilot (Premium)". There is also a new **Microsoft 365 Copilot (Basic)** tier: users *without* the add-on license still get "standard access to Copilot capabilities inside apps (for example, Word or Excel)" (https://learn.microsoft.com/en-us/copilot/plan/copilot-overview). This affects C08, C16 and the guide's naming throughout.
- Five of the seven S-URLs now redirect to new paths under `/copilot/plan/` or `/copilot/implement/`. They still resolve, but the guide should list the current URLs.

Verdict key: VERIFIED, PARTLY, NOT SUPPORTED, WRONG.

---

## Claims

### C01. Copilot works inside email, Teams chats, meetings, OneDrive and SharePoint, and can draw on anything the person is allowed to open.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C01 | PARTLY | "It can generate responses anchored in your organizational data, such as user documents, emails, calendar, chats, meetings, and contacts." / "Microsoft Copilot only surfaces organizational data to which individual users have at least view permissions." / Exceptions on S04: "Encrypted content requires EXTRACT and VIEW." and "Copilot and agents can't access content protected by DKE." | https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy ; https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing | "Licensed Copilot can draw on the email, chats, meetings and files the person has permission to view." (Drop "anything": encryption without EXTRACT, Double Key Encryption and Restricted Content Discovery all narrow it. Full Graph grounding is also for the Premium license only.) |

### C02. Microsoft's own SharePoint guidance warns that Copilot can bring up widely shared files a person didn't know they could open.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C02 | PARTLY | The cited SharePoint best-practices page (S02) now redirects to a deployment blueprint that says only that it helps by "remediating oversharing." The warning now lives on the Copilot data protection page: "Copilot respects existing SharePoint and OneDrive permissions. If content is already overshared, Copilot can surface it to anyone who has access." The RCD page adds: "This restriction helps reduce the likelihood of accidental discovery of content." No current page says "didn't know they could open." | https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing ; https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery | "Microsoft warns that if content is already overshared, Copilot can surface it to anyone who has access." Cite the data protection page, not S02. |

### C03. Admins can see, block and unblock agents from the Microsoft 365 admin center.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C03 | VERIFIED | "The Microsoft 365 admin center provides governance and lifecycle management capabilities for agents through the Agent Registry." / "Block or unblock agents for the entire organization by using the same controls that work for any other app in the Microsoft 365 admin center." | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-actions (the guide's S10 URL redirects here) | None needed. |

### C04. Sensitivity labels mark files as Confidential or Highly Confidential, and Copilot respects them.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C04 | PARTLY | "Copilot honors Microsoft Purview sensitivity labels and encryption when it grounds responses and generates content." But the blocking comes from encryption or DLP, not the label name: "the user must have both the VIEW and EXTRACT usage rights for Copilot to summarize" and "A DLP policy for Copilot can keep Copilot from summarizing labeled files and emails." Also: "Copilot and agents don't currently recognize sensitivity labels that protect Teams meetings and chats." | https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing | "Copilot honors sensitivity labels. A label only stops Copilot from using a file if the label encrypts it or a DLP policy blocks it. Labels on Teams meetings and chats aren't recognized yet." |

### C05. Anyone with a Copilot license can build an agent with Agent Builder and share it with colleagues.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C05 | PARTLY | "Administrators can control whether Agent Builder is available to users in their organization." Sharing defaults to open but can be restricted: "All users (default): Everyone can share agents with the organization." / "Specific users or groups: Limit sharing permissions to selected users or groups." Not limited to licensed users: "Declarative agents that are grounded in instructions and public websites are included with Copilot Chat." | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder ; https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents ; https://learn.microsoft.com/en-us/copilot/plan/copilot-overview | "By default, people can build agents in Agent Builder and share them across the organization. Admins can turn Agent Builder off or limit who can share. Copilot Chat users without a license can also build simple web-grounded agents." |

### C06. Copilot activity is recorded in the Microsoft Purview audit log. How long it's kept depends on your license.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C06 | VERIFIED | "Microsoft Purview Audit automatically logs Copilot interactions." / "The default retention period for audit records varies by license type and when the records were generated." (180 days for Audit Standard; one year needs E5 or an add-on; up to 10 years needs a further add-on.) | https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing ; https://learn.microsoft.com/en-us/purview/audit-log-retention-policies | None needed. Consider adding: "Audit records don't contain the text of prompts or responses" (same S04 page), which matters for C45. |

### C07. Admins can block or unblock an agent for the whole organization from the Agents page in the Microsoft 365 admin center.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C07 | VERIFIED | "Block or unblock agents for the entire organization ..." / "Select Agents > All agents." / "In the agent details pane that opens, immediately under the agent's name, select Block or Unblock." | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-actions | None needed. Optional note from the same page: blocking a SharePoint or Foundry agent "only impacts its availability in Microsoft Copilot Chat." |

### C08. A person's access to Copilot can be removed by unassigning their Copilot license.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C08 | PARTLY | The license page links to "Assign or unassign licenses for users in the Microsoft 365 admin center." But unlicensed users keep some Copilot: "Microsoft 365 Copilot (Basic) refers to users without the Copilot add-on license, but who still have standard access to Copilot capabilities inside apps (for example, Word or Excel)." Copilot Chat removal is a separate control: "Remove user access to Copilot Chat entirely, including for Copilot Chat (Basic) users." | https://learn.microsoft.com/en-us/copilot/plan/copilot-license-options ; https://learn.microsoft.com/en-us/copilot/plan/copilot-overview | "Unassigning the Copilot license removes the paid features. The person keeps Copilot Chat and basic in-app Copilot unless an admin also removes that access in Copilot controls." |

### C09. Several settings in the guide need the AI Administrator role.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C09 | PARTLY | "You must be a member of the AI Administrator or Global Administrator role to perform this task." (Anthropic setting). Entra role list: AI Administrator can "Manage all aspects of Microsoft Copilot" and "Approve and publish line-of-business copilot agents." So these settings need AI Administrator *or* Global Administrator. The Purview, SharePoint and Cloud Policy settings in the guide use other roles. | https://learn.microsoft.com/en-us/copilot/implement/copilot-anthropic-apps ; https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference ; https://learn.microsoft.com/en-us/copilot/plan/copilot-overview | "Copilot and agent settings in the Microsoft 365 admin center can be managed by an AI Administrator, so you don't need a Global Administrator. Purview and SharePoint settings need their own admin roles." |

### C10. Four classes map to labels: Public, General, Confidential, Highly Confidential (with encryption). Label names vary by organization.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C10 | PARTLY | Microsoft's default labels are Personal, Public, General, Confidential and Highly Confidential: "When you don't have sensitivity labels that are published, we'll create the following labels for you." In the defaults, encryption sits on sublabels under **both** Confidential and Highly Confidential (for example "Confidential \ All Employees ... Encryption: All users and groups in the org: Co-Author"). The parent "Highly Confidential" label itself only adds a watermark. | https://learn.microsoft.com/en-us/purview/default-sensitivity-labels-policies | "These four names match Microsoft's default labels, which also include Personal. In the defaults, encryption is set on sublabels under Confidential and Highly Confidential. Your organization's names and settings may differ." |

### C11. If a label encrypts a file and the person doesn't have the EXTRACT usage right, Copilot can't show its text and can only link to the file.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C11 | VERIFIED | "If the user has VIEW but not EXTRACT, Copilot doesn't summarize the content, but it can return a link so the user can open it outside Copilot. When this content is open in an app, the user can't use Copilot with it." | https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing ; also https://learn.microsoft.com/en-us/purview/ai-m365-copilot-considerations | None needed. |

### C12. Copilot shows the labels of the files it used (in citations/references).

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C12 | PARTLY | "Labels are shown in Copilot Chat. When Copilot Chat returns data from labeled items, it can display the sensitivity label. If the response draws on items with different labels, the label with the highest priority is shown." Exceptions: container (site/team) labels "won't display their container label in Copilot", and meeting/chat labels aren't shown. No Learn page I read says each citation shows its own label for Microsoft 365 Copilot. | https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing ; https://learn.microsoft.com/en-us/purview/ai-m365-copilot-considerations | "Copilot Chat can show the sensitivity label of the content it used. If several labels apply, it shows the highest-priority one." |

### C13. New content Copilot creates from a labeled file can pick up (inherit) that label.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C13 | VERIFIED | "New content can inherit labels. When Copilot creates new content from labeled items, the label with the highest priority is applied to the new content, where label inheritance is supported." | https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing | None needed. Optional: inheritance isn't supported for user-defined permissions or Teams meeting/chat labels (considerations page). |

### C14. Publishing labels and deciding which ones encrypt is done in Microsoft Purview.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C14 | VERIFIED | "To create and publish these labels, use the Microsoft Purview portal." / "Until you publish your labels, they won't be available to select in apps or for services. To publish the labels, they must be added to a label policy." | https://learn.microsoft.com/en-us/purview/create-sensitivity-labels | None needed. |

### C15. Consumer Copilot is used with a personal Microsoft account and is not covered by enterprise protections.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C15 | PARTLY | "Users signing in with a Microsoft Entra work or school account to Microsoft Copilot Chat are covered by the enterprise data protection commitment." / "the Microsoft Copilot app, which is a consumer experience, doesn't support Microsoft Entra authentication." Support page: Copilot Chat "automatically provides enterprise data protection when you're signed in with that account." No page I read says in so many words that consumer Copilot lacks EDP; it follows from these statements. | https://learn.microsoft.com/en-us/windows/client-management/manage-windows-copilot ; https://support.microsoft.com/en-us/privacy/data-protection-when-using-microsoft-365-copilot-chat-for-work-or-school | "Enterprise data protection applies only when people sign in with a work account. Consumer Copilot uses a personal Microsoft account, so it doesn't get those protections." |

### C16. Copilot Chat: work account, no Microsoft 365 Copilot license; grounded in the web and in files the user uploads.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C16 | PARTLY | "Copilot Chat is not grounded in organizational content like files, emails, or chats as part of the chat experience—it is grounded in data from the web only." It has more routes in than uploads: "By using Copilot Chat in Outlook. In this scenario, Copilot Chat can access user data including their emails, calendar, meetings, chats, and limited file content (OneDrive and SharePoint)." Also open files in Word, Excel and PowerPoint, files picked with "/", and pay-as-you-go agents. | https://learn.microsoft.com/en-us/copilot/plan/privacy-and-protections ; https://learn.microsoft.com/en-us/copilot/plan/copilot-overview | "Copilot Chat: work account, no Copilot license. It's grounded in the web, plus content the person adds: uploaded or selected files, the file or email they have open, and in Outlook their mail, calendar and recent files." (For a bank, the Outlook route matters.) |

### C17. Licensed Microsoft 365 Copilot also draws on the user's email, chats and files (Microsoft Graph).

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C17 | VERIFIED | "Microsoft 365 Copilot (Premium) uses both web and organizational data via Microsoft Graph and Work IQ, and pulls information automatically." / "Microsoft Graph brings a personalized organizational data context into the prompt, like information from a user's emails, files, meetings, calendars, teams, or organizational relationships." | https://learn.microsoft.com/en-us/copilot/plan/copilot-overview | None needed. Optional: "Work IQ" can be turned off, which removes this grounding. |

### C18. Agents are built in Agent Builder or Copilot Studio, with their own knowledge and tools.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C18 | PARTLY | "You can specify dedicated knowledge sources, including content on SharePoint and information provided by Copilot connectors." But: "Agent Builder doesn't support authoring actions that integrate external services. To add low-code actions, connectors, or workflows, copy the agent to Microsoft Copilot Studio." The admin center also lists agents built in SharePoint and Microsoft Foundry. | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder ; https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-actions | "Agents are built in Agent Builder (instructions, knowledge sources and built-in skills) or in Copilot Studio, which adds actions, connectors and workflows." |

### C19. Signing in with a work account is what turns on enterprise data protection, which covers both Copilot Chat and Microsoft 365 Copilot.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C19 | VERIFIED | "Copilot Chat (Basic), Microsoft 365 Copilot (Basic), and Microsoft 365 Copilot (Premium) are protected by Enterprise Data Protection (EDP) when you sign in with Microsoft Entra accounts." | https://learn.microsoft.com/en-us/copilot/plan/copilot-overview | None needed. |

### C20. Under enterprise data protection, prompts, responses and the data Copilot accesses aren't used to train foundation models.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C20 | VERIFIED | "Your data isn't used to train foundation models ... the prompts, responses, and data accessed through Microsoft Graph aren't used to train foundation models." | https://learn.microsoft.com/en-us/copilot/plan/enterprise-data-protection | None needed. |

### C21. Purview retention policies can cover Copilot prompts and responses.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C21 | VERIFIED | "Use retention policies to automatically retain or delete user prompts and responses for AI apps." / "Retention policies for AI apps include user prompts and responses for Microsoft 365 Copilot and Copilot Studio." | https://learn.microsoft.com/en-us/purview/ai-microsoft-purview ; https://learn.microsoft.com/en-us/purview/retention-policies-copilot | None needed. Worth adding: "Microsoft Copilot experiences is a new, dedicated policy location. It isn't included in existing policies and must be selected" (https://learn.microsoft.com/en-us/training/modules/purview-ai-secure-copilot/retention-copilot). Older "Teams chats and Copilot interactions" policies can't be edited once the tenant has the separate locations (https://learn.microsoft.com/en-us/purview/retention). |

### C22. Those retention policies aren't retroactive (they don't apply to interactions before the policy was created).

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C22 | PARTLY | Not stated on any Purview product page I read. A Microsoft-authored Zero Trust workshop page says: "Retention policies are not retroactive for interactions that occurred before the policy was applied. If an organization enables Copilot without a retention policy ... those early interactions may already be gone." This is Microsoft guidance hosted on microsoft.github.io, not Learn product docs. The general retention page measures retention "from when the content was created", which suggests items still in the mailbox can be picked up. | https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_097 ; https://learn.microsoft.com/en-us/purview/retention | "Set up retention before rollout. A policy can't bring back interactions that were deleted before it existed, and existing policies don't cover the new Copilot location automatically." |

### C23. Files uploaded to Copilot Chat are saved in the person's OneDrive.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C23 | VERIFIED | "Files uploaded to Copilot Chat (OneDrive): This folder in the user's OneDrive stores files that users upload to Copilot Chat." / "Uploaded files are stored in a user's OneDrive for Business as part of enterprise data protection." | https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing ; https://learn.microsoft.com/en-us/copilot/plan/privacy-and-protections | None needed. |

### C24. Copilot's memory feature isn't covered by standard retention policies or holds.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C24 | PARTLY | Retention part confirmed: "Retention policies and retention labels configured in Purview by organization admins don't apply to Copilot memory." / "There are no admin controls to enforce retention rules specifically for Copilot memory." The page says nothing about holds. It also says: "Admins can search their users' memory in Microsoft Copilot via Microsoft Purview eDiscovery or Content Search" and "Memory and personalization actions don't generate audit log entries in Purview." (Page updated 2026-11-03.) | https://learn.microsoft.com/en-us/copilot/manage/copilot-personalization-memory | "Copilot memory isn't covered by Purview retention policies or labels, and memory changes aren't audited. Admins can still search and delete memories with eDiscovery." Drop "holds" unless the other checker finds a primary source. |

### C25. Copilot runs under Microsoft's Product Terms and Data Protection Addendum.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C25 | VERIFIED | "The use of Microsoft Copilot and Microsoft Copilot Chat, as used by organizations, is covered by the terms of the Microsoft Products and Services Data Protection Addendum (DPA) and Microsoft Product Terms, with Microsoft acting as a data processor." | https://learn.microsoft.com/en-us/copilot/plan/enterprise-data-protection | None needed. Bing web queries are the exception: see C26. |

### C26. Copilot can send search queries to Bing (web grounding). Admins can turn web search off with a policy.

| ID | Verdict | Quote | URL | Suggested wording |
|---|---|---|---|---|
| C26 | VERIFIED | "Copilot generates a search query that it sends to the Bing search service asking for more information." / "The primary way that IT admins can control access to web search is by using the Allow web search in Copilot policy, which is available only in Cloud Policy service for Microsoft 365." | https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access | None needed. Strongly consider adding for a bank: "The Microsoft Products and Services Data Protection Addendum (DPA) doesn't apply to the use of generated web search queries" and "Microsoft acts as a data controller" for them. HIPAA and the EU Data Boundary also don't apply to these queries (same page). |

---

## Sources S01-S07

Titles given are from the guide's Sources page (page 14).

| ID | URL in guide | Resolves? | Lands on (after redirect) | Real page title (H1) | Updated | Title given in guide | Match? |
|---|---|---|---|---|---|---|---|
| S01 | learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection | Yes (200, 2 redirects) | /en-us/copilot/plan/enterprise-data-protection | Enterprise data protection in Microsoft Copilot and Microsoft Copilot Chat | 2026-11-04 | Enterprise data protection in Microsoft 365 Copilot and Copilot Chat | Close. Same page; product renamed. Update the title and URL. |
| S02 | learn.microsoft.com/en-us/sharepoint/sharepoint-copilot-best-practices | Redirects to a different page (200, 3 redirects) | /en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance | Secure and govern Microsoft Copilot: Foundational deployment guidance | 2026-11-03 | Microsoft 365 Copilot best practices with SharePoint | **No.** The SharePoint best-practices article is gone. The new page is a short landing page for a downloadable blueprint (PDF and PowerPoint) and doesn't hold the guide's points. Replace it with the S04 page (oversharing, RCD, RAC) and/or https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery. |
| S03 | learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license | Yes (200, no redirect) | same | SharePoint Advanced Management features in Microsoft Copilot licenses | 2026-08-18 | SharePoint Advanced Management features with a Copilot license | Yes (minor wording). |
| S04 | learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture-data-protection-auditing | Yes (200, 3 redirects) | /en-us/copilot/plan/architecture-data-protection-auditing | Data protection and auditing for Microsoft Copilot | 2026-11-10 (updated today) | Copilot architecture, data protection and auditing | Close. Update the title and URL. |
| S05 | learn.microsoft.com/en-us/purview/ai-microsoft-purview | Yes (200, no redirect) | same | Microsoft Purview data security and compliance protections for generative AI apps (browser title adds "Microsoft 365 Copilot and other") | 2026-05-27 | Microsoft Purview protections for Copilot | Yes, loosely (short form). |
| S06 | learn.microsoft.com/en-us/copilot/microsoft-365/manage-public-web-access | Yes (200, 2 redirects) | /en-us/copilot/plan/manage-public-web-access | Data, privacy, and security for web search in Microsoft Copilot and Microsoft Copilot Chat | 2026-11-03 | Manage public web access in Copilot | **No.** Same topic, but the title has changed. Update the title and URL. |
| S07 | learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps | Yes (200, 1 redirect) | /en-us/copilot/implement/copilot-anthropic-apps | Enable Claude models only for Copilot experiences in Microsoft 365 apps | 2026-11-10 (updated today) | Copilot in Microsoft 365 apps with Anthropic models | **Partly.** The title has changed, and the page now begins: "The information in this article applies only to customer in the European Union (EU), European Free Trade Association (EFTA), and United Kingdom (UK)." For a non-EU bank, the general page "Claude models from Anthropic in Microsoft Online Services" may be the better source (this is relevant to C27-C30 and C50, which the other checker owns). The page does confirm the setting name "AI providers operating as Microsoft subprocessors" and the "AI Administrator or Global Administrator" requirement. |

Current URLs to use in the guide:
- S01: https://learn.microsoft.com/en-us/copilot/plan/enterprise-data-protection
- S02: replace (see above)
- S03: unchanged
- S04: https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing
- S05: unchanged
- S06: https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access
- S07: https://learn.microsoft.com/en-us/copilot/implement/copilot-anthropic-apps

## Notes for the other checker (C27-C51)

- C45: S04 says "Audit records don't contain the text of prompts or responses. To view that text, use eDiscovery or Data Security Posture Management (DSPM) for AI." S05 says "prompts and responses are captured in the unified audit log." The considerations page agrees with S04: "Auditing captures the Microsoft 365 Copilot activity of search, but not the actual user prompt or response." Microsoft's own pages conflict here. The newer S04 (updated 2026-11-10) agrees with the considerations page.
- C29: S01 footnote 3: "Claude models from Anthropic are currently excluded from the EU Data Boundary and when applicable, in-country processing commitments."
- C28: S07: "When Anthropic operates as a Microsoft subprocessor it's governed by the Microsoft Product Terms and the Microsoft Data Protection Addendum (DPA)."
- C33/C36: S03 says RCD prevents sites "from surfacing in Microsoft Copilot Business Chat, unless a user had a recent interaction". The RCD page now says it limits discovery "including recently interacted files". S03 also says "Restricted site creation by apps isn't included with your Microsoft Copilot license. This feature requires the SharePoint Advanced Management Plan 1 add-on."
- C51: The overview now lists three tiers: Copilot Chat (Basic), Microsoft 365 Copilot (Basic) and Microsoft 365 Copilot (Premium).
