# ZK-Audit

**Zero-Knowledge Non-Repudiation for Privacy-Preserving and Tamper-Proof Audit Logs**

---

## Overview

**ZK-Audit** is a cryptographic framework designed to ensure the **integrity**, **confidentiality**, and **non-repudiation** of audit logs in sensitive and regulated environments. It integrates:

- **zk-STARKs** for zero-knowledge proof generation without trusted setup,
- **Threshold BLS Signatures** for distributed verification,
- **Merkle Trees** for proof of inclusion,
- **GDPR-aligned mechanisms** for log forgettability.

The architecture is modular and compatible with existing **SIEM platforms** such as **Wazuh** and **Elasticsearch**.

---

## Key Features

- **Post-Quantum Security**: zk-STARKs ensure long-term cryptographic resilience.
- **No Trusted Third Party**: Full decentralization of proof generation and verification.
- **Selective Disclosure**: Metadata-only exposure through non-interactive proofs.
- **SIEM Integration**: Ready-to-use plugin design for Wazuh and other event management platforms.
- **GDPR Support**: Forgettable commitments and re-randomizable proofs.

---

## Architecture

ZK-Audit follows a four-entity design:
- **Logger**: Generates raw audit entries.
- **Prover**: Aggregates entries and generates zk-STARK proofs.
- **Verifier**: Validates proofs and threshold signatures.
- **Distributed Storage**: Anchors Merkle roots and metadata (e.g., via IPFS).

Full architecture and workflows are available in [`docs/architecture/`](./docs/architecture/).

---

## Getting Started

### Requirements
- Python 3.10+
- `hashlib`, `pytest`, `matplotlib`, `numpy`

### Installation

```bash
git clone https://github.com/<your-username>/zk-audit.git
cd zk-audit
pip install -r requirements.txt
```

### Run Example

```bash
python src/demo_zk_audit.py
```

---

## Reproducible Benchmarking

A Jupyter Notebook for simulated performance benchmarks is available in [`notebooks/`](./notebooks/).  
Data is based on public zk-STARK benchmarks and synthetic log entries.

---

## Formal Verification

Tamarin specifications for symbolic security properties (e.g., non-repudiation) are provided in [`tamarin/`](./tamarin/).  
You may verify the model with:

```bash
tamarin-prover zk_audit_nonrepudiation.spthy
```

---

## Documentation

- **Paper**: [`docs/paper/ZK-Audit_Final_Submission.pdf`](./docs/paper/)
- **Appendices**: Full pseudocode, assumptions, and model available in the annexes.
- **Glossary**: [`Appendix G`](./docs/paper/) for technical acronyms and concepts.

---

## License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](./LICENSE) file for details.

---

## Citation

If you use ZK-Audit in your work, please cite:

> Minka Mi Nguidjoi. (2025). *ZK-Audit: Zero-Knowledge Non-Repudiation for Privacy-Preserving and Tamper-Proof Audit Logs*. ICTO 2025 (forthcoming).

---

## Maintainer

**Thierry MINKA**  
Expert judiciaire en cybercriminalité | Enseignant à l’ENSPY | Auditeur des finances publiques  
For inquiries: minkathierry@gmail.com
