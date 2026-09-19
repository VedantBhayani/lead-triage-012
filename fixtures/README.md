# Fixture labeling

## Official challenge fixture

`inbound_leads.csv` is the official fixture from the challenge repository. Its checksum is recorded in `output/run.log` and `submission.md`.

## Supplementary adversarial validation

`adversarial_leads.csv` and `adversarial_expected.json` are additional tests created for this project. They are **not** part of the official challenge fixture and their output must not replace `output/decisions.json` for submission.

Run them with:

```powershell
python triage.py --input fixtures\adversarial_leads.csv --output output\adversarial_decisions.json --log output\adversarial_run.log
python check_adversarial.py
```
