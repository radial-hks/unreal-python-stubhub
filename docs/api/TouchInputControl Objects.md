## TouchInputControl Objects

```python
class TouchInputControl(StructBase)
```

Touch Input Control

**C++ Source:**

- **Module**: Engine
- **File**: TouchInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alt_input_key`` (Key):  [Read-Write] The alternate input to send from this control (for sticks, this is the vertical axis)
- ``center`` (Vector2D):  [Read-Write] The initial center point of the control. If Time Until Reset is < 0, control resets back to here.
  Use negative numbers to invert positioning from top to bottom, left to right. (if <= 1.0, it's relative to screen, > 1.0 is absolute)
- ``image1`` (Texture2D):  [Read-Write] For sticks, this is the Thumb
- ``image2`` (Texture2D):  [Read-Write] For sticks, this is the Background
- ``input_scale`` (Vector2D):  [Read-Write] The scale for control input
- ``interaction_size`` (Vector2D):  [Read-Write] The interactive size of the control. Measured outward from Center. (if <= 1.0, it's relative to screen, > 1.0 is absolute)
- ``main_input_key`` (Key):  [Read-Write] The main input to send from this control (for sticks, this is the horizontal axis)
- ``thumb_size`` (Vector2D):  [Read-Write] For sticks, the size of the thumb (if <= 1.0, it's relative to screen, > 1.0 is absolute)
- ``treat_as_button`` (bool):  [Read-Write] Set this to true to treat the joystick as a simple button
- ``visual_size`` (Vector2D):  [Read-Write] The size of the control (if <= 1.0, it's relative to screen, > 1.0 is absolute)

<a id="unreal.TouchInputControl.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.WorldPartitionActorFilter"></a>