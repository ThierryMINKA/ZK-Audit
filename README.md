# Proofs – Tamarin Verification Output

This folder is reserved for exporting the formal verification results of the Tamarin model used in ZK-Audit.

## Purpose

To archive and provide reproducible evidence for the verified symbolic security lemma:

> Any verified proof must originate from a log genuinely emitted by a Logger.

This supports the claim of **non-repudiation** as modeled in `zk_audit_nonrepudiation.spthy`.

---

## Expected Files (to be added manually)

- `output_nonrepudiation.pdf`:  
  A PDF export from Tamarin's GUI showing the successful validation of the `NonRepudiation` lemma.

- `zk_audit_nonrepudiation.proof`:  
  Optional export of the full proof session for reuse or audit.

- `log_verification.txt`:  
  Optional terminal log of verification run using CLI (`--prove` mode).

---

## Note

This folder is currently empty. Please run the model using Tamarin and export the corresponding outputs here for completeness.
