# Upwork MCP Configuration — Prompt Record

Date: 2026-09-24
Task type: Configuration + verification (no Upwork write actions)

The following is the exact prompt used for this task, preserved verbatim:

---

Configure the official Upwork MCP server for this Devin environment.

Upwork's official MCP server is:
https://mcp.upwork.com/mcp

Requirements:

1. Determine the correct way to add a remote MCP server with OAuth 2.1 in this Devin environment.
2. Add the Upwork MCP server using the official URL above.
3. Do NOT look for or request an Upwork API key, API secret, password, cookies, or access token. The official MCP uses OAuth 2.1 with dynamic client registration.
4. Do not create a custom Upwork API application.
5. Do not use browser automation as a substitute for the MCP connection.
6. Do not make any Upwork actions, submit proposals, send messages, or change account data. This task is ONLY to configure and authenticate the MCP connection.
7. If the configuration requires an OAuth login/authorization in a browser, stop at that point and tell me that the Upwork login window is ready. I can log in and authorize the connection immediately.
8. After I complete authentication, verify that the MCP connection is active and enumerate the Upwork tools that are actually available to this Devin session.
9. Report:
   - whether the server was successfully added
   - whether OAuth authentication succeeded
   - whether the Upwork account is accessible
   - which Upwork capabilities/tools are available
   - any limitations or errors encountered

Do not proceed to job searching or any other Upwork activity after authentication. Stop after the connection has been successfully verified.
