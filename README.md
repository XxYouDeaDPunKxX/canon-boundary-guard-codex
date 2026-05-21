# 🛡️ Canon Boundary Guard

> This branch preserves the standalone skill layout of Canon Boundary Guard.
>
> The active package now lives on `main` as a Codex plugin. Use this branch only
> if you want the older manual setup: copy the `canon-boundary-guard/` folder
> into your Codex skills directory and configure the hook yourself.

Canon Boundary Guard is a Codex skill that gives Codex a cognitive frame for
keeping project evidence, chat context, operator instructions, working
hypotheses, and model assumptions in separate layers during a session.

It is meant for work where a mistaken boundary can matter: project rules,
architecture notes, protocols, naming decisions, workflows, `AGENTS.md`, or
anything that may be written back into a repository.

## 🔎 What It Does

Codex often works with several kinds of information at the same time:

- files already in the project
- messages from the current conversation
- instructions that tell Codex how to behave
- runtime context shown at the start of a session
- assumptions that come from the model itself

This skill gives Codex a small classification frame for those sources.

The goal is not only to protect file edits. The frame is meant to stay useful
while Codex reads, reasons, decides, restructures, and eventually writes
persistent project content.

## ⚠️ Why It Exists

When Codex works on a repository, it reads more than files.

It may also use conversation history, runtime context, tool output,
instructions, compressed summaries, and model assumptions.

Those sources do not have the same authority.

A project file is not the same thing as a temporary chat message. An instruction
for Codex is not the same thing as content that belongs in the repository. A
model assumption is not the same thing as verified evidence.

Canon Boundary Guard exists to keep those boundaries visible while Codex
reasons, decides, and eventually writes persistent project content.

## 🧩 AGENTS.md Authority

In some Codex environments, such as editor-integrated sessions, `AGENTS.md`
instructions may appear at the start of the conversation as a visible user-role
message before the operator's real first request.

That display role is not enough to decide authority.

The block may refer to the current working directory, even when the actual
instruction source is global, such as an `AGENTS.md` stored in Codex home.

Canon Boundary Guard includes a countermeasure for this case: a leading block
starting with `AGENTS.md instructions for <path>` is treated as Codex runtime
instruction-chain material, not ordinary chat and not repository content.

When this distinction matters, verify the authority layer before using the
block as project evidence or writing it into persistent files.

## 📦 Install

Copy the `canon-boundary-guard/` folder into your Codex skills directory.

Typical locations:

- Windows: `%USERPROFILE%\.codex\skills\canon-boundary-guard`
- macOS/Linux: `~/.codex/skills/canon-boundary-guard`

Restart Codex after installing the skill.

The hook is highly recommended and requires a `PreToolUse` entry in your Codex
`config.toml`.
See the technical details below.

## ▶️ Use

Use the skill when a session depends on keeping old context, current
instructions, external information, working hypotheses, model assumptions, and
project evidence separate.

```txt
Use $canon-boundary-guard before editing this protocol.
```

The skill can also be wired into a Codex hook so its compact frame is surfaced
before matched write tools. The hook setup is documented in
`canon-boundary-guard/SKILL.md`.

## 🤖 AI-Assisted Development

This project was developed with AI assistance.

The project, documentation, and repository materials were shaped through
human-directed work supported by AI tools during drafting, structuring, review,
and refinement.

AI assistance does not make the project automatically correct, complete, or
suitable for every use case. Read it, test it, and adapt it to your own context.

## 📜 License

This project is licensed under CC BY-SA 4.0: Creative Commons
Attribution-ShareAlike 4.0 International.

See [LICENSE](LICENSE).

<details>
<summary>⚙️ Technical details</summary>

This section is for readers who want to inspect the actual operating model
behind the skill. It uses the skill's internal terms directly.

## 🧱 Skill Structure

```txt
canon-boundary-guard/
|-- SKILL.md
|-- agents/openai.yaml
|-- references/frame.md
`-- scripts/inject_frame.py
```

- `canon-boundary-guard/SKILL.md` defines the full operating frame.
- `canon-boundary-guard/references/frame.md` contains the compact frame emitted
  by the hook script.
- `canon-boundary-guard/scripts/inject_frame.py` reads
  `canon-boundary-guard/references/frame.md` and emits a hook payload.
- `canon-boundary-guard/agents/openai.yaml` contains Codex-facing skill
  metadata.

## 🧠 Operating Posture

The skill is designed to keep source classes separate throughout the session,
not only at write time.

The frame should affect reading, analysis, planning, conflict detection, and
persistence decisions. The hook only re-surfaces the compact frame near matched
write tools.

## 🧬 Provenance Layers

Canon Boundary Guard uses six source classes. They do not decide whether
something is true by themselves. They describe where the material came from and
whether it can safely become persistent project content.

- `L0 EVIDENCE`: project files, git state, tests, schemas, lockfiles,
  diagnostics, command output, or verified tool output.
- `L1 SHAPING`: conversation material not approved for persistence.
- `L1A AUTHORIZED DELTA`: operator-approved material for the current turn,
  before it is written.
- `L2 AGENT CONTROL`: instructions that shape agent behavior, not project
  content.
- `L2A CODEX INSTRUCTION CHAIN`: AGENTS guidance and runtime instruction-chain
  material.
- `L3 MODEL PRIOR`: unverified model memory, assumed conventions, generic
  best practice, or unstated framework behavior.

Non-L0 material is tagged only when the output would change if the source
changed.

The important boundary is persistence. L1, L2, L2A, and L3 can shape how Codex
works, but they should not silently become repository content. L1A can be
written only inside the scope approved by the operator. L2 and L2A require an
explicit request for agent-facing instructions before they can be persisted.

## 🧩 AGENTS.md Prelude

A leading user-role block starting with:

```txt
AGENTS.md instructions for <path>
```

is classified as `L2A` runtime instruction-chain material.

It is not operator chat, not project content, and not dependent on filesystem
confirmation. If it contains an `<environment_context>...</environment_context>`
block, that block is runtime metadata.

The first operator request starts after this prelude.

## 🔁 Hook Injection

`canon-boundary-guard/scripts/inject_frame.py` is intentionally small. It reads
`canon-boundary-guard/references/frame.md`, strips surrounding whitespace, and
emits JSON for a Codex `PreToolUse` hook:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse"
  },
  "systemMessage": "<contents of canon-boundary-guard/references/frame.md>"
}
```

The hook is highly recommended for sessions where repository content, project
rules, protocols, naming, workflows, or `AGENTS.md` authority may matter. It is
intended for matched write tools, for example `apply_patch`, `Write`, or
`Edit`.

The hook is not the core mechanism of the skill. It is a reinforcement point
that re-surfaces the compact frame before matched write tools.

The frame is surfaced as a `systemMessage`. It does not block the tool call,
rewrite the requested operation, or decide project policy. Its job is to put the
classification frame back into the instruction stream at the moment a write may
happen.

## 🛠️ Hook Setup

Add the hook to your Codex `config.toml`.

Typical config locations:

- Windows: `%USERPROFILE%\.codex\config.toml`
- macOS/Linux: `~/.codex/config.toml`

Use an absolute path in `command`.

```toml
[features]
codex_hooks = true

[[hooks.PreToolUse]]
matcher = "apply_patch|Write|Edit"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python C:\\ABSOLUTE\\PATH\\TO\\.codex\\skills\\canon-boundary-guard\\scripts\\inject_frame.py"
timeout = 5
statusMessage = "Provenance frame"
```

Update the `command` path to match where you copied the
`canon-boundary-guard/` skill folder.

## 🧯 Fallback Behavior

If `canon-boundary-guard/references/frame.md` is missing, the hook script still emits a
`systemMessage`:

```txt
Canon Boundary Guard frame missing: provenance protection degraded.
```

This keeps the failure visible without blocking execution.

That fallback is deliberate: the skill should not make normal work impossible
because a local file is missing, but it should also not fail silently.

</details>
