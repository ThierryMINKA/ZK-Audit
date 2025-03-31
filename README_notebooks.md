# Benchmark Simulations – ZK-Audit

This folder contains simulation notebooks used to project the expected performance of ZK-Audit in large-scale log verification scenarios.

---

## Purpose

To simulate key performance indicators (KPIs) such as:
- Proof generation time
- Proof verification latency
- Memory usage
- Merkle tree depth
- Proof size

All projections are based on public zk-STARK benchmarks (e.g., Cairo, zkSync) and adapted to log-scale scenarios (1k – 1M entries).

---

## Files

- `benchmarks_simulation.ipynb`  
  A Jupyter notebook with plots and metrics for:
  - Estimated performance
  - Cost trade-offs
  - Scalability patterns

---

## Requirements

- Python 3.10+
- `matplotlib`, `pandas`, `numpy`, `seaborn`, `jupyter`

Install dependencies:

```bash
pip install matplotlib pandas numpy seaborn jupyter
```

---

## Reference

These projections are discussed in **Appendix E** of the paper and support Section 4.4 on expected outcomes.

