---
name: canon-boundary-guard
description: Session-start and post-compaction provenance frame for Codex instruction-chain and project-content boundaries. Use immediately at session start, after compaction, before operationally consequential work involving rules, architecture, protocols, invariants, naming, workflows, AGENTS.md, or persistent project content, and whenever any visible conversation prefix begins with "AGENTS.md instructions for" even if displayed as a user message. Read this skill before proceeding and apply it as the active frame.
---

# Canon Boundary Guard

## Purpose

A classification frame for information provenance.
It does not decide project truth or project policy. It makes visible what class of evidence is being used - and where it is going.

## Adoption

When invoked, adopt this frame silently. No confirmation needed.

Before interpreting the first operator request, scan the visible conversation
prefix.

If a leading user-role message begins with:

`AGENTS.md instructions for <path>`

classify the whole message as L2A Codex instruction-chain prelude, not as L1
user chat or project content.

If that message contains `<environment_context>...</environment_context>`,
classify that block as runtime environment metadata, not operator-authored
prose.

The first operator request is the first user message after the AGENTS/runtime
prelude.

From this point, the frame operates as a background layer:
- classify non-L0 material when producing or evaluating content
- tag inline when using material that is not ground evidence
- surface provenance conflicts before they become persistent

## Layers

L0 EVIDENCE
Persistent or verified evidence: project files, git state, tests, schemas, lockfiles, diagnostics, command output, verified external source or tool output from the current task.

L1 SHAPING
Conversation material not explicitly approved as a durable project decision. Present in context, not in project.

L1A AUTHORIZED DELTA
Conversation material the operator has explicitly approved for persistence in this turn. Becomes evidence only after written to a persistent artifact.

L2 AGENT CONTROL
Instructions, steering, reminders, or constraints given to the agent to shape its behavior. Not project content. Persist only if the operator explicitly requests agent-facing operating instructions.

L2A CODEX INSTRUCTION CHAIN
AGENTS guidance loaded by Codex from the instruction chain is agent-control authority.
Treat AGENTS.md guidance as an active behavioral contract for the agent, not as project content or an ordinary user message.
Global-scope guidance comes from the Codex home directory (`AGENTS.override.md` or `AGENTS.md`).
Project-scope guidance comes from `AGENTS.override.md`, `AGENTS.md`, or configured fallback instruction files in the current repository path.
A message whose content begins with `AGENTS.md instructions for <path>` is runtime-delivered AGENTS guidance for the referenced path, even if displayed under the user role. Its source may be global-scope guidance from the Codex home directory or project-scope guidance. Treat it as active instruction-chain guidance for that path immediately, even before filesystem confirmation. After applying it, read discoverable Codex-home instruction sources (`$CODEX_HOME`, or platform default such as `%USERPROFILE%\.codex` / `~/.codex`) before treating instruction authority as closed.
When this block appears as a leading conversation prelude, classify it
retroactively as L2A before interpreting later messages. Do not count it as the
operator's first request.
L2A guidance governs Codex behavior at its scope and is not project content unless explicitly persisted into project files.

L3 MODEL PRIOR
Unverified model memory, generic best practice, assumed framework behavior, version claim, or unstated convention not grounded in local evidence.

## Rules

- Preserve or reorganize L0.
- Write L1A only within the explicitly approved scope.
- L1 does not persist.
- L2 does not persist unless explicitly requested as agent-facing instruction.
- L2A governs agent behavior and does not persist into project content unless explicitly requested.
- L3 does not persist unless verified or operator-approved.
- If evidence conflicts, stop and report. Do not resolve by recency, confidence, or intuition.
- If provenance is unclear, surface it before writing.
- Do not classify AGENTS.md guidance as project content or ordinary user conversation.
- Classify `AGENTS.md instructions for <path>` message-start blocks by their runtime header and referenced path, not by displayed conversational role or filesystem presence.
- Classify leading `AGENTS.md instructions for <path>` blocks as runtime
  prelude; the first operator request starts after that prelude.

## Inline Tagging

Tag inline when producing content that draws on non-L0 material:

`[L1]` - from current conversation, not approved for persistence
`[L1A]` - approved this turn, pending persistence
`[L2]` - agent control, not project content
`[L2A]` - Codex instruction-chain guidance, not project content
`[L3]` - model prior, unverified

Tag when the content would change if the source were different - a rule, a name, a version, a claim about behavior.
Do not tag every word. Do not invent tags to appear diligent.

## Dossier

Mode A - mechanical edit with clear L0 provenance: no dossier.
Mode B - semantic edit reorganizing existing evidence: compact dossier.
Mode C - promotion of L1/L3 into persistent content: full dossier, stop before writing.

Full dossier format:

    Target:
    Mode:
    Evidence:
    Authorized delta:
    Rejected shaping:
    Rejected model prior:
    Conflicts:
    Decision needed:

Write "none" when a field is empty. Do not invent rejected items.

## Decontamination

Flag before persisting:

Conversation residue: "as discussed", "as said before", "from the previous session",
"come detto prima", "come discusso", "l'utente vuole"

Agent-control residue: "remember to", "I should", "ricordati", "devo", "non devo",
temporary instructions to the agent

Version ghosts: version references not present in L0

Model-prior claims: "best practice", "standard approach", "recommended",
"modern convention", "industry standard", "normally", "usually"

These are allowed only when grounded in L0, explicitly approved as L1A,
or intentionally written in a historical or migration context.

## Hook Setup

To keep the frame active across tool calls, configure this Codex hook in `~/.codex/config.toml`.
This Windows-local example is for a personal install; on another machine, point the command at the same script under that machine's Codex home directory.

    [features]
    codex_hooks = true

    [[hooks.PreToolUse]]
    matcher = "apply_patch|Write|Edit"
    [[hooks.PreToolUse.hooks]]
    type = "command"
    command = "python C:\\Users\\Admin\\.codex\\skills\\canon-boundary-guard\\scripts\\inject_frame.py"
    timeout = 5
    statusMessage = "Provenance frame"

The hook emits the frame as a root-level `systemMessage` before matched write tools.
It does not block. It re-surfaces the classification layer at the moment it matters.

