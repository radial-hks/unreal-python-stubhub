## TouchInterface Objects

```python
class TouchInterface(Object)
```

Defines an interface by which touch input can be controlled using any number of buttons and virtual joysticks

**C++ Source:**

- **Module**: Engine
- **File**: TouchInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``activation_delay`` (float):  [Read-Write] How long after joystick enabled for touch (0.0 will disable this feature)
- ``active_opacity`` (float):  [Read-Write] Opacity (0.0 - 1.0) of all controls while any control is active
- ``controls`` (Array[TouchInputControl]):  [Read-Write]
- ``inactive_opacity`` (float):  [Read-Write] Opacity (0.0 - 1.0) of all controls while no controls are active
- ``prevent_recenter`` (bool):  [Read-Write] Prevent joystick re-centering and moving from Center through user taps
- ``startup_delay`` (float):  [Read-Write] Delay at startup before virtual joystick is drawn
- ``time_until_deactive`` (float):  [Read-Write] How long after user interaction will all controls fade out to Inactive Opacity
- ``time_until_reset`` (float):  [Read-Write] How long after going inactive will controls reset/recenter themselves (0.0 will disable this feature)

<a id="unreal.GameInstance"></a>