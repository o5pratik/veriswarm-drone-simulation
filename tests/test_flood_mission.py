import unittest

from examples.flood_mission import (
    Lease, decide, demo, formation, minimum_separation, safe_z, world_to_ned,
)


class InvariantTests(unittest.TestCase):
    def test_world_coordinates_are_relative_and_z_is_down(self):
        self.assertEqual(world_to_ned((13070, 2950, 130), (13000, 2900, 100)),
                         (0.7, 0.5, -0.3))

    def test_rising_water_raises_drone(self):
        self.assertEqual(safe_z(-3, -4, 2), -6)

    def test_already_higher_cruise_is_preserved(self):
        self.assertEqual(safe_z(-10, -4, 2), -10)

    def test_bad_clearance_and_nonfinite_values_rejected(self):
        for args in ((-3, 0, 0), (-3, 0, -1), (-3, float("nan"), 2)):
            with self.assertRaises(ValueError):
                safe_z(*args)

    def test_formation_has_five_separated_drones(self):
        positions = formation((0, 0, -3))
        self.assertEqual(len(positions), 5)
        self.assertGreater(minimum_separation(positions), 2.7)

    def test_separation_is_translation_invariant(self):
        self.assertAlmostEqual(minimum_separation(formation((0, 0, -3))),
                               minimum_separation(formation((90, 40, -9))))

    def test_exact_timeout_and_future_lease_fail_closed(self):
        self.assertFalse(Lease("ALLOW", 0).permits(2000))
        self.assertFalse(Lease("ALLOW", 2001).permits(2000))
        self.assertTrue(Lease("ALLOW", 0).permits(1999))

    def test_missing_or_nonallow_lease_holds(self):
        self.assertEqual(decide(None, 0), "HOLD")
        self.assertEqual(decide(Lease("QUARANTINE", 0), 0), "HOLD")

    def test_collision_and_obstacle(self):
        lease = Lease("ALLOW", 0)
        self.assertEqual(decide(lease, 0, collision=True), "STOP")
        self.assertEqual(decide(lease, 0, obstacle=True), "HOLD")

    def test_demo_keeps_clearance(self):
        self.assertTrue(all(s["clearance_m"] >= 2 for s in demo()["samples"]))


if __name__ == "__main__":
    unittest.main()
