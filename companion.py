from dataclasses import dataclass
from typing import Any, Dict, List


class SafetyError(RuntimeError):
    """Raised when attempting an unsafe operation (e.g., without connection)."""


@dataclass(frozen=True)
class ServoCommand:
    channel: int
    angle: float


class FlipperZeroCompanion:
    """Lightweight controller facade with basic safety checks."""

    def __init__(self, servo_channels: int = 4, angle_limit: float = 90.0) -> None:
        if servo_channels <= 0:
            raise ValueError("Servo channel count must be positive")
        if angle_limit <= 0:
            raise ValueError("Angle limit must be positive")

        self.servo_channels = int(servo_channels)
        self.angle_limit = float(angle_limit)
        self.connected = False
        self.command_log: List[Dict[str, Any]] = []

    def connect(self) -> bool:
        if self.connected:
            return False
        self.connected = True
        self.command_log.append({"type": "connect"})
        return True

    def disconnect(self) -> bool:
        if not self.connected:
            return False
        self.connected = False
        self.command_log.append({"type": "disconnect"})
        return True

    def _require_connection(self) -> None:
        if not self.connected:
            raise SafetyError("Controller is not connected")

    def move_servo(self, channel: int, angle: float) -> ServoCommand:
        self._require_connection()

        if not isinstance(channel, int):
            raise TypeError("Channel must be an integer")
        if channel < 0 or channel >= self.servo_channels:
            raise ValueError("Channel is out of range")

        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be numeric")
        if abs(angle) > self.angle_limit:
            raise ValueError("Angle exceeds configured limit")

        command = ServoCommand(channel=channel, angle=float(angle))
        self.command_log.append({"type": "servo", "channel": command.channel, "angle": command.angle})
        return command

    def emergency_stop(self, reason: str = "manual") -> str:
        status = "disconnected" if self.connected else "idle"
        self.connected = False
        self.command_log.append({"type": "stop", "reason": reason, "status": status})
        return status
