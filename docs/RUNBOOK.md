# Reproduction paths

## Portable portfolio example

Run from the repository root:

```sh
python examples/flood_mission.py
python -m unittest discover -s tests -v
```

It runs locally without Unreal, networks, API credentials or third-party packages. JSON output goes to stdout; it is synthetic, not flight telemetry.

## Original live simulator

Use the [team source](https://github.com/berlinflix/VeriSwarm_SIH/tree/5411a4e), the compatible CoSys client/runtime and the externally held Unreal project. The reviewed map is `/Game/VeriSwarm/FactoryCity_Disaster`.

1. Preserve the original project and known-good nominal runner.
2. Verify Point_A, Point_B, the simulator origin and the physical roof/ground collision meshes.
3. Start the disaster level in Play mode; confirm the five vehicles.
4. Use the team's `Run_Five_Drone_A_to_B.cmd` nominal launcher and its current documentation.
5. For movement-v2, start the authorization sender/receiver first, confirm all five fresh leases, then use `ops/start_pratik_movement_v2.ps1`.
6. Retain run-specific evidence outside Git. Do not label a run PASS unless its acceptance measurements pass.

Machine-specific paths, lease snapshots, Ethernet configuration and simulator assets are deliberately not copied into this repository. These instructions describe the upstream workflow, not a one-command full simulator installation.
