# DTQEM-Negative-Time-Model-of-Quantum-Non-locality
DTQEM (Dual‑Time Quantum Entanglement Model) attributes non‑locality to a negative imaginary time carried by entangled particles. Calibrated to Gisin’s lower bound (v>1e7c at 0K) and returning to classical speed at 300K, it explains thermal decoherence, Heisenberg uncertainty, and double‑slit fringe contrast. Includes interactive Python simulation.
# DTQEM: Dual-Time Quantum Entanglement Model

**Version:** 2.0 (Final Calibrated)  
**License:** MIT  
**Author:** [Your Full Name]  
**DOI:** (to be added after Zenodo archiving)

---

## Overview

**DTQEM** is a physics‑based model that explains quantum non‑locality (the “spooky action at a distance”) using a **negative imaginary time** dimension. Each entangled particle is assumed to carry two times:

- a real time \( t_r \) (the usual time),
- an imaginary time \( t_v = -\alpha(\theta)\,t_r \) that can be **negative**.

The effective speed of the quantum influence is then:

\[
v_{\text{eff}}(\theta,T) = \frac{v_c}{1 - \alpha(\theta)\,\exp\!\bigl(-(\Gamma_0 + aT)\,t_{\text{obs}}\bigr)}
\]

where \( \alpha(\theta)=\sin(\theta/2) \), \( t_{\text{obs}} \) is the observation time, and the decoherence coefficient \( \Gamma(T)=\Gamma_0 + aT \) is **calibrated to experiments** (Gisin et al., 1998).

---

## Key Features

- **Calibrated model** – matches the lower bound \(10^7c\) at 0 K and returns to classical speed \(1200c\) at 300 K.
- **Heisenberg‑compatible** – the uncertainty relation \( \Delta E \cdot t_{\text{eff}} \ge \hbar/2 \) is explicitly satisfied.
- **Physical double‑slit simulator** – realistic interference patterns with diffraction, wavelength, slit width and separation.
- **Interactive GUI** – sliders for \( \theta \), temperature, \( t_{\text{obs}} \), wavelength, and slit distance.
- **Automatic output** – all figures and numerical results saved to `dtqem_outputs/`.
- **Unit tested** – validates critical predictions and input error handling.

---

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/DTQEM.git
cd DTQEM
pip install -r requirements.txt
