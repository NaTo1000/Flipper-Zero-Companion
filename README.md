# Flipper-Zero-Companion

Lightweight companion controller with basic safety checks for servo-style operations.

## Usage

```python
from companion import FlipperZeroCompanion

controller = FlipperZeroCompanion()
controller.connect()
controller.move_servo(0, 15.0)
controller.emergency_stop()
```

## Tests

```bash
python -m unittest
```
