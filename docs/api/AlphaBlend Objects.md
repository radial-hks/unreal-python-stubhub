## AlphaBlend Objects

```python
class AlphaBlend(StructBase)
```

Alpha Blend class that supports different blend options as well as custom curves

**C++ Source:**

- **Module**: Engine
- **File**: AlphaBlend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_option`` (AlphaBlendOption):  [Read-Write] Type of blending used (Linear, Cubic, etc.)
- ``blend_time`` (float):  [Read-Write] Blend Time
- ``custom_curve`` (CurveFloat):  [Read-Write] If you're using Custom BlendOption, you can specify curve

<a id="unreal.AlphaBlend.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.InputScaleBias"></a>