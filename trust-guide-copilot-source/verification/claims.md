# Factual claims in "AI Trust Boundary Framework: Microsoft 365 Copilot Edition"

Each claim is quoted or closely paraphrased from the guide. Page numbers refer to the guide.

## Page 2 (What changes with Copilot)
C01. Microsoft 365 Copilot works inside email, Teams chats, meetings, OneDrive and SharePoint, and can draw on anything the person using it is allowed to open.
C02. Microsoft's own SharePoint guidance warns that Copilot can bring up widely shared files a person didn't know they could open.

## Page 3 (Finance mirror)
C03. Admins can see, block and unblock agents from the Microsoft 365 admin center.
C04. Sensitivity labels mark files as Confidential or Highly Confidential, and Copilot respects them.

## Page 4 (Owner)
C05. In Microsoft 365, anyone with a Copilot license can build an agent with Agent Builder and share it with colleagues.
C06. Copilot activity is recorded in the Microsoft Purview audit log. How long it's kept depends on your license.
C07. Admins can block or unblock an agent for the whole organization from the Agents page in the Microsoft 365 admin center.
C08. A person's access to Copilot can be removed by unassigning their Copilot license.
C09. Several settings in the guide need the AI Administrator role.

## Page 5 (Data)
C10. Four classes map to labels: Public, General, Confidential, Highly Confidential (with encryption). Label names vary by organization. (Check that these are Microsoft's default/common label names.)
C11. If a label encrypts a file and the person doesn't have the EXTRACT usage right, Copilot can't show them its text; it can only point to (reference/link) the file.
C12. Copilot shows the labels of the files it used (in citations/references).
C13. New content Copilot creates from a labeled file can pick up (inherit) that label.
C14. Publishing labels and deciding which ones encrypt is done in Microsoft Purview.

## Page 6 (Environment)
C15. Consumer Copilot is used with a personal Microsoft account (and is not covered by enterprise protections).
C16. Copilot Chat: work account, no Microsoft 365 Copilot license; grounded in the web and in files the user uploads.
C17. Licensed Microsoft 365 Copilot also draws on the user's email, chats and files (Microsoft Graph).
C18. Agents are built in Agent Builder or Copilot Studio, with their own knowledge and tools.
C19. Signing in with a work account is what turns on enterprise data protection, which covers both Copilot Chat and Microsoft 365 Copilot.
C20. Under enterprise data protection, Microsoft says prompts, responses and the data Copilot accesses aren't used to train foundation models.
C21. Purview retention policies can cover Copilot prompts and responses.
C22. Those retention policies aren't retroactive (they don't apply to interactions before the policy was created).
C23. Files uploaded to Copilot Chat are saved in the person's OneDrive.
C24. Copilot's memory feature isn't covered by standard retention policies or holds.
C25. Copilot runs under Microsoft's Product Terms and Data Protection Addendum.
C26. Copilot can send search queries to Bing (web grounding). Admins can turn web search off with a policy.
C27. When an admin allows it, people can choose Claude (Anthropic's model) for an answer in Microsoft 365 Copilot (a model choice/picker).
C28. When Claude is used, Anthropic processes the request as a Microsoft subprocessor.
C29. As of November 2026, Claude in Copilot runs outside Microsoft's EU Data Boundary.
C30. Web search and model choice are tenant (admin) settings.

## Page 7 (Access)
C31. Copilot works as the person using it and sees what they can see (permission trimming).
C32. Data access governance reports show sites that are shared broadly or have sharing links.
C33. Restricted Content Discovery keeps a site out of Copilot and organization-wide search results without changing anyone's permissions.
C34. "Restricted access control" limits a SharePoint site to the members of a named group.
C35. Sensitivity labels on sites (containers) set privacy and sharing rules for a whole site or team.
C36. These SharePoint Advanced Management features become available once at least one Microsoft 365 Copilot license is assigned; a few features still need a separate add-on.
C37. An Agent Builder agent can answer questions from one chosen SharePoint folder (knowledge source scoped to a folder).

## Page 8 (Action)
C38. Copilot in Word, Outlook and Excel drafts; the person presses Send.
C39. Copilot Studio agents can have actions set to ask the user for confirmation before they run.
C40. Copilot Studio agents can run with triggers and connectors (autonomous agents).
C41. Copilot Cowork breaks a goal into tasks across Outlook, Teams and Office apps, and can be allowed to use a browser.
C42. Copilot Chat and Agent Builder are included with Microsoft 365 Copilot and don't need a separate Copilot Studio license or IT project. (Agent Builder agents are declarative agents.)
C43. Cowork must be turned on by an admin, uses usage-based billing, and browser use stays off unless an admin allows it.
C44. Copilot can suggest meeting times.

## Page 9 (Oversight)
C45. The Purview audit log records that Copilot interactions happened, with the user, time and app. How long logs are kept depends on your license.
C46. Retention policies can keep Copilot prompts and responses for as long as records rules require.
C47. eDiscovery lets legal and compliance find and export Copilot prompts and responses.

## Page 11 (Red flag)
C48. "Lethal trifecta" is Simon Willison's term for an AI with access to private data, exposure to untrusted content and a way to communicate externally.
C49. Microsoft has its own defenses against prompt injection in Copilot.

## Page 13 (Checklist)
C50. There is an admin setting named (approximately) "AI providers operating as Microsoft subprocessors" for Anthropic models.
C51. Users can have a Microsoft 365 Copilot license or only Copilot Chat.

## Page 14 (Sources): every URL must resolve and match its title
S01 https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection
S02 https://learn.microsoft.com/en-us/sharepoint/sharepoint-copilot-best-practices
S03 https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-features-copilot-license
S04 https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture-data-protection-auditing
S05 https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
S06 https://learn.microsoft.com/en-us/copilot/microsoft-365/manage-public-web-access
S07 https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps
S08 https://www.directionsonmicrosoft.com/reports/m365-copilot-adds-choice-and-risk-with-anthropics-claude
S09 https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
S10 https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions
S11 https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/cost-considerations
S12 https://genai.owasp.org/llm-top-10
S13 https://www.nist.gov/itl/ai-risk-management-framework
S14 https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
