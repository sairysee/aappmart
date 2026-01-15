# Attack Path Prediction Engine (AAPP)

The AAPP subsystem predicts the most likely attack paths in a target environment.  
It combines graph analysis, heuristics, and optional machine learning.

---

## 1. Overview

AAPP performs:

- Environment analysis  
- Attack graph construction  
- Path prediction  
- Risk scoring  

Its output feeds directly into the MART subsystem.

---

## 2. Components

### 2.1 Analyzer (`analyzer.py`)
Parses input data:

- Hosts  
- Services  
- Vulnerabilities  
- Network structure  

Outputs normalized data.

---

### 2.2 Graph Builder (`graph_builder.py`)
Builds an attack graph using NetworkX:

- Nodes = assets  
- Edges = possible attack transitions  
- Attributes = vulnerabilities, privileges, access  

---

### 2.3 Predictor (`predictor.py`)
Predicts likely attack paths using:

- Heuristics  
- ML models  
- Scoring algorithms  

Outputs ranked attack paths.

---

### 2.4 Scoring (`scoring.py`)
Assigns risk scores based on:

- Exploitability  
- Impact  
- Privilege level  
- Path length  

---

## 3. Data Flow

```
Input → Analyzer → Graph Builder → Predictor → Scoring → Output
```

---

## 4. Output Format

AAPP produces:

- Attack graph  
- Ranked attack paths  
- Risk scores  
- Recommended entry points  

---

## 5. Extensibility

You can extend AAPP by:

- Adding new ML models  
- Adding new scoring algorithms  
- Adding new graph heuristics  

---

## 6. Summary

AAPP provides the predictive intelligence that guides the MART agents.  
It is modular, extensible, and designed for advanced attack modeling.
