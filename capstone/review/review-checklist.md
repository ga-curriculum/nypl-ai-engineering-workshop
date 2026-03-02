# Capstone Review Checklist

Use this checklist to evaluate your capstone implementation. Apply both personas in order.

---

## Primary Persona: Security Auditor

The Security Auditor focuses on data protection, input validation, and secure coding practices — especially important for encryption code.

### Encryption Implementation
- [ ] Does `encrypt()` validate inputs before passing them to the KMS API?
- [ ] Are plaintext values logged anywhere? (They should NOT be — check logger calls)
- [ ] Does the error handling avoid leaking sensitive data in error messages?
- [ ] Is the base64 encoding applied correctly (encode before return, decode on decrypt)?
- [ ] Are all exceptions from the KMS API caught and wrapped in `KmsClientError`?

### Secret Rotation (Stretch Tier)
- [ ] If encryption fails, is the old secret preserved? (The function should NOT update the secret)
- [ ] Are both clients closed even if an error occurs? (Consider using try/finally)
- [ ] Is the encrypted value stored, not the plaintext? (Verify the order of operations)
- [ ] Could a partial failure leave the system in an inconsistent state?

### General Security
- [ ] Are there any hardcoded keys, secrets, or credentials?
- [ ] Does the code follow the principle of least privilege?
- [ ] Are error messages informative without being exploitable?

---

## Secondary Persona: Edge Case Hunter

The Edge Case Hunter looks for unusual inputs, boundary conditions, and failure modes.

### Input Edge Cases
- [ ] What happens if `plaintext` is an empty string?
- [ ] What happens if `key_id` is `None`?
- [ ] What happens if `plaintext` contains Unicode characters (e.g., emoji, CJK)?
- [ ] What happens if `plaintext` is very large (e.g., 10MB)?
- [ ] What happens if `key_id` is a valid format but doesn't exist in KMS?

### Error Path Edge Cases
- [ ] What happens if the KMS service is unavailable?
- [ ] What happens if the caller doesn't have `kms:Encrypt` permissions?
- [ ] What happens if `encrypt()` is called after `close()`?
- [ ] Does the error message help the developer debug the issue?

### Integration Edge Cases (Stretch Tier)
- [ ] What happens if encryption succeeds but secret storage fails?
- [ ] What happens if the secret name doesn't exist in Secrets Manager?
- [ ] Is the `rotate_secret` function idempotent? (Can you safely retry it?)

---

## Self-Evaluation

After applying both personas, rate your implementation:

| Criterion | Score (1-5) | Notes |
|---|---|---|
| **Correctness** — Does it work as specified? | | |
| **Security** — Would the Security Auditor approve? | | |
| **Robustness** — Does it handle edge cases? | | |
| **Test Coverage** — Are the important paths tested? | | |
| **Code Quality** — Does it follow existing patterns? | | |

### Reflection Questions
1. Which persona found more issues — Security Auditor or Edge Case Hunter?
2. Did the AI tools help or hinder your security review?
3. What would you do differently in your next AI-assisted implementation?
