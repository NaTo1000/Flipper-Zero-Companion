import unittest

from companion import FlipperZeroCompanion, SafetyError


class FlipperZeroCompanionTests(unittest.TestCase):
    def test_connection_sequence(self):
        controller = FlipperZeroCompanion()

        self.assertTrue(controller.connect())
        self.assertFalse(controller.connect(), "Second connect should not reopen the link")
        self.assertTrue(controller.connected)

        self.assertTrue(controller.disconnect())
        self.assertFalse(controller.disconnect(), "Second disconnect should be a no-op")
        self.assertFalse(controller.connected)

    def test_move_servo_requires_connection(self):
        controller = FlipperZeroCompanion()
        with self.assertRaises(SafetyError):
            controller.move_servo(0, 10)

    def test_move_servo_validates_inputs(self):
        controller = FlipperZeroCompanion()
        controller.connect()

        with self.assertRaises(ValueError):
            controller.move_servo(-1, 0)
        with self.assertRaises(ValueError):
            controller.move_servo(10, 0)
        with self.assertRaises(ValueError):
            controller.move_servo(0, 120)
        with self.assertRaises(TypeError):
            controller.move_servo("0", 0)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            controller.move_servo(0, "0")  # type: ignore[arg-type]

    def test_move_servo_records_command(self):
        controller = FlipperZeroCompanion(angle_limit=45)
        controller.connect()
        command = controller.move_servo(1, 30)

        self.assertEqual(command.channel, 1)
        self.assertEqual(command.angle, 30.0)
        self.assertEqual(
            controller.command_log[-1],
            {"type": "servo", "channel": 1, "angle": 30.0},
        )

    def test_emergency_stop_disconnects_safely(self):
        controller = FlipperZeroCompanion()
        controller.connect()
        controller.move_servo(0, 0)

        status = controller.emergency_stop("test")
        self.assertFalse(controller.connected)
        self.assertEqual(status, "disconnected")
        self.assertEqual(
            controller.command_log[-1],
            {"type": "stop", "reason": "test", "status": "disconnected"},
        )


if __name__ == "__main__":
    unittest.main()
