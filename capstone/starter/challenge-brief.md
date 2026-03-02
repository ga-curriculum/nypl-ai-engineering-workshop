# Capstone Challenge: KMS Encryption & Secret Rotation

## Context

You've spent the day working with `S3Client`. Now you'll apply the same skills to a **different** client in the python-utils codebase: `KmsClient`.

The `KmsClient` class (in `src/nypl_py_utils/classes/kms_client.py`) currently supports one operation:

- `decrypt(encrypted_text)` — takes a base64-encoded KMS-encrypted string and decrypts it

Your challenge is to extend the KMS client with encryption capabilities and build a secret rotation function that integrates multiple clients.

## Target Files

- **Primary:** `python-utils/src/nypl_py_utils/classes/kms_client.py`
- **Stretch:** `python-utils/src/nypl_py_utils/classes/secrets_manager_client.py` (read-only reference for integration)

## Time Budget (45 minutes)

| Phase | Time | Activity |
|---|---|---|
| Decompose | 5 min | Use Gemini Code Assist to break down the feature |
| Implement | 20 min | Use Copilot to write the code |
| Test | 10 min | Generate and review tests |
| Review | 10 min | Apply QA personas |

---

## Base Tier

### Add `encrypt(plaintext, key_id)`

Add a method to `KmsClient` that encrypts a plaintext string using a KMS key.

**Behavior:**
- Accept `plaintext` (a string) and `key_id` (the KMS key identifier)
- Use `self.kms_client.encrypt(KeyId=key_id, Plaintext=plaintext.encode('utf-8'))` to encrypt
- The response dict has a `'CiphertextBlob'` key containing the encrypted bytes
- Base64-encode the ciphertext blob and return it as a string
- Raise `KmsClientError` on `ClientError`, `TypeError`, or `ValueError`
- Follow the existing logging pattern

**Example usage:**
```python
client = KmsClient()
encrypted = client.encrypt('my-secret-value', 'alias/my-key')
# Returns a base64-encoded string like "SGVsbG8gV29ybGQ="
```

**Hints:**
- You'll need `from base64 import b64encode` (note: `b64decode` is already imported)
- The encrypt/decrypt methods should be symmetric: `decrypt(encrypt(text, key))` should return the original text (assuming the same KMS key)

---

## Intermediate Tier

All of the Base tier, plus:

### Add input validation

Add validation to the `encrypt` method:
- Raise `KmsClientError` with message `'Plaintext must be a non-empty string'` if `plaintext` is not a string or is empty
- Raise `KmsClientError` with message `'Key ID must be a non-empty string'` if `key_id` is not a string or is empty

### Write tests

Write at least 5 tests for your `encrypt` method:
1. Happy path — encrypts and returns base64 string
2. Validates that the KMS client is called with correct parameters
3. Raises `KmsClientError` on empty plaintext
4. Raises `KmsClientError` on empty key_id
5. Raises `KmsClientError` when the KMS API returns a `ClientError`

### Apply QA personas

Apply at least 2 QA personas from the framework to your implementation:
- **Security Auditor** (recommended primary) — Is the encryption implementation secure? Are there data exposure risks?
- **Edge Case Hunter** (recommended secondary) — What happens with unusual inputs?

---

## Stretch Tier

All of the above, plus:

### Create `rotate_secret(secret_name, new_value, key_id)`

Create a standalone function (not a method on `KmsClient`) that rotates an encrypted secret by combining `KmsClient` and `SecretsManagerClient`.

**Behavior:**
1. Create a `KmsClient` instance
2. Encrypt `new_value` using `key_id` via `KmsClient.encrypt()`
3. Create a `SecretsManagerClient` instance
4. Store the encrypted value using `SecretsManagerClient` (you'll need to add a `set_secret` method — see below)
5. Close both clients
6. Return the encrypted value

**New method needed on `SecretsManagerClient`:**
Add `set_secret(secret_name, secret_value)` that calls:
```python
self.secrets_manager_client.put_secret_value(
    SecretId=secret_name, SecretString=secret_value)
```

**Where to put `rotate_secret`:**
Create a new file: `src/nypl_py_utils/functions/secret_rotation_helper.py`

**Tests for the stretch tier:**
- Test that `rotate_secret` encrypts before storing
- Test that both clients are closed after the operation
- Test error handling if encryption fails (secret should NOT be updated)

---

## Workflow Reminder

Use the full dual-tool workflow:
1. **Gemini Code Assist:** Decompose the challenge, ask about the KMS API, review your approach
2. **Copilot:** Implement the code, generate test stubs, write assertions
3. **Generate > Review > Refine:** Don't accept the first output — iterate

## When You're Done

Use the review checklist in [`../review/review-checklist.md`](../review/review-checklist.md) to self-evaluate your work.
