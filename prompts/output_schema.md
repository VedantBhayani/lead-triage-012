# Output schema

Return exactly:

```json
{
  "decision": "QUALIFY | NURTURE | REJECT | ESCALATE",
  "reason": "One concise sentence grounded in the supplied lead data.",
  "confidence": 0.0
}
```

`confidence` must be a number from 0 to 1. The reason must not claim facts that are absent from the record.
