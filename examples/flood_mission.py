"""Synthetic portfolio example; never connects to or commands a drone."""

import json
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Lease:
    decision: str
    issued_ms: int

    def permits(self, now_ms: int, timeout_ms: int = 2000) -> bool:
        age = now_ms - self.issued_ms
        return self.decision == "ALLOW" and 0 <= age < timeout_ms


def world_to_ned(point_cm, origin_cm):
    """Axis-aligned frame only; Z sign flips and centimetres become metres."""
    dx, dy, dz = (p - o for p, o in zip(point_cm, origin_cm))
    return dx / 100, dy / 100, -dz / 100


def safe_z(cruise_z: float, water_z: float, clearance: float) -> float:
    if not all(math.isfinite(v) for v in (cruise_z, water_z, clearance)):
        raise ValueError("finite altitude inputs required")
    if clearance <= 0:
        raise ValueError("clearance must be positive")
    return min(cruise_z, water_z - clearance)


OFFSETS = ((0, 0), (-2, -2), (-2, 2), (2, -2), (2, 2))


def formation(centre):
    x, y, z = centre
    return [(x + dx, y + dy, z) for dx, dy in OFFSETS]


def minimum_separation(positions):
    if len(positions) < 2:
        raise ValueError("at least two positions required")
    return min(math.dist(a, b) for i, a in enumerate(positions)
               for b in positions[i + 1:])


def decide(lease, now_ms, collision=False, obstacle=False):
    """Illustrative gate; not a cryptographic authorization implementation."""
    if collision:
        return "STOP"
    if lease is None or not lease.permits(now_ms) or obstacle:
        return "HOLD"
    return "MOVE"


def demo():
    rows = []
    for step in range(6):
        water_z = -step * 0.5
        z = safe_z(-3, water_z, 2)
        positions = formation((step * 10, 0, z))
        rows.append({"step": step, "water_ned_z_m": water_z,
                     "drone_ned_z_m": z, "clearance_m": water_z - z,
                     "minimum_separation_m": round(minimum_separation(positions), 4),
                     "decision": decide(Lease("ALLOW", step * 1000), step * 1000)})
    return {"kind": "synthetic_educational_demo", "samples": rows,
            "expired_lease_decision": decide(Lease("ALLOW", 0), 2000)}


if __name__ == "__main__":
    print(json.dumps(demo(), indent=2))
