# Unit Tests – ZK-Audit

This folder contains unit tests for key components of the ZK-Audit prototype. These tests ensure correctness of hashing, Merkle tree construction, proof simulation, and BLS signature aggregation.

---

## Structure

- `test_hash_utils.py`: Tests for SHA-3 hashing and nonce-based commitments.
- `test_merkle_tree.py`: Validates Merkle root calculation and input integrity.
- `test_zk_stark_sim.py`: Verifies simulated proof generation and validation logic.
- `test_bls_agg.py`: Checks simulated BLS signature aggregation and verification.

---

## Running Tests

Install required packages:

```bash
pip install pytest
```

Run all tests from the root directory:

```bash
pytest tests/
```

---

## Recommendation

These tests are simplified due to the prototype nature of ZK-Audit and may be expanded with:
- Property-based testing (e.g. with Hypothesis)
- Formal integration with test suites for ZK backends

