# Lead Triage Agent

Minimal Mistral-backed implementation for the AI Automation Intern 012 challenge. It is deliberately one Python file plus inspectable Markdown policies.

## Setup

```powershell
$env:MISTRAL_API_KEY = "your-key"
```

## Run the real Mistral workflow

```powershell
python triage.py
```

This writes `output/decisions.json` and `output/run.log`. The script processes every input row, validates risky data before the API call, uses Mistral JSON mode for commercial judgment, validates the response, and escalates API/model failures. It uses Python's standard library to call the Mistral HTTPS API directly.

It also writes `output/prompt_trace.jsonl`, which records the policy prompt, each model input row, raw model response, final validated decision, and any execution error. The API key is never written to any artifact.

## Local smoke test

```powershell
python triage.py --dry-run
python -m unittest discover -v
```

The dry run is only for checking the pipeline. Submit the live Mistral output and its real run log.

## Adversarial stress test

This separate fixture is intentionally designed to expose silent errors in model judgment. It is not the official submission fixture.

```powershell
python triage.py --input fixtures\adversarial_leads.csv --output output\adversarial_decisions.json --log output\adversarial_run.log --trace output\adversarial_trace.jsonl
python check_adversarial.py
```

It covers valid low-budget enterprise leads, prompt injection, malformed budgets, duplicate identity, privacy, executable links, competitor research, early-stage nurturing, foreign-language leads, contradictory budget claims, empty messages, fake data, and anonymous enterprise claims.

## Verify the submission packet

```powershell
python -m unittest discover -v
python -c "import json; d=json.load(open('output/decisions.json',encoding='utf-8')); assert len(d)==20 and len({x['lead_id'] for x in d})==20; print('20 unique decisions verified')"
Get-FileHash .\fixtures\inbound_leads.csv -Algorithm SHA256
```

Submit `submission.md`, `triage.py`, `prompts/`, `fixtures/inbound_leads.csv`, `output/decisions.json`, `output/run.log`, and `output/prompt_trace.jsonl`. Do not submit `.env`.

## Policy design

Markdown files in `prompts/` are loaded as the system policy. Python owns data integrity and safety gates. Mistral owns commercial interpretation, including the difference between a valid but low budget (often NURTURE) and malformed data (ESCALATE).
