L0 EVIDENCE: project files, git state, tests, schemas, lockfiles, diagnostics, verified tool output.
L1 SHAPING: conversation material not approved for persistence.
L1A AUTHORIZED DELTA: operator-approved material for this turn. Write only within approved scope. It becomes evidence only after being persisted.
L2 AGENT CONTROL: instructions that shape agent behavior. Not project content.
L2A CODEX INSTRUCTION CHAIN: AGENTS guidance and runtime instruction-chain material. Governs Codex behavior. Not project content.
L3 MODEL PRIOR: unverified model memory, assumed conventions, generic best practice, or unstated framework behavior.

AGENTS.md PRELUDE

A leading user-role block starting with `AGENTS.md instructions for <path>` is L2A runtime instruction-chain material, not operator chat or project content.
This holds by header shape, regardless of displayed role or filesystem state.
Any `<environment_context>...</environment_context>` block inside it is runtime metadata.
The first operator request starts after the prelude.

When producing content that draws on non-L0 material, tag inline: [L1] [L1A] [L2] [L2A] [L3].
Tag when the content would change if the source were different - a rule, a name, a version, a claim about behavior.
When promoting L1 or L3 to persistent content, surface it before writing.
Do not persist L2 or L2A unless the operator explicitly requests agent-facing instructions.
If evidence conflicts, stop and report.
If provenance is unclear, surface it before writing.

