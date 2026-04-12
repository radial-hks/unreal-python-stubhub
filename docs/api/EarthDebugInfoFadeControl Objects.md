## EarthDebugInfoFadeControl Objects

```python
class EarthDebugInfoFadeControl(StructBase)
```

Earth Debug Info Fade Control

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthStats
- **File**: EarthDebuggerSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center_fade_radius`` (float):  [Read-Write] Radius from screen center where 0 is center to 1.0 is edge to avoid display too many Info attributes.
- ``clip_range`` (Vector2D):  [Read-Write] Clipping planes used to display Info attributes.
- ``fade_opacity_control`` (Vector2f):  [Read-Write] Fade opacity range used to display Info attributes.
- ``fade_range_control`` (Vector2f):  [Read-Write] Fade factor range used to display Info attributes.
- ``fade_scale_control`` (Vector2f):  [Read-Write] Fade scale range used to display Info attributes.
- ``use_center_fade_radius`` (bool):  [Read-Write] When enabled we use a radius from the display center to avoid showing too many Info attributes.
- ``use_clip`` (bool):  [Read-Write] When enabled we use the clip planes to narrow down which Info to display
- ``use_fade_control`` (bool):  [Read-Write] When enabled we use a fade factor as display alpha.

<a id="unreal.EarthDebugInfoFadeControl.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.EarthDebugPayloadControl"></a>