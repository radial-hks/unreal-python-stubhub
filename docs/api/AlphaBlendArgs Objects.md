## AlphaBlendArgs Objects

```python
class AlphaBlendArgs(StructBase)
```

Alpha Blend construction arguments. Used for creation of an AlphaBlend.

**C++ Source:**

- **Module**: Engine
- **File**: AlphaBlend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_option`` (AlphaBlendOption):  [Read-Write] Type of blending used (Linear, Cubic, etc.)
- ``blend_time`` (float):  [Read-Write] Blend Time
- ``custom_curve`` (CurveFloat):  [Read-Write] If you're using Custom BlendOption, you can specify curve

<a id="unreal.AlphaBlendArgs.__init__"></a>

#### __init__

```python
def __init__(custom_curve: CurveFloat = None,
             blend_time: float = 0.000000,
             blend_option: AlphaBlendOption = AlphaBlendOption.LINEAR) -> None
```

<a id="unreal.AlphaBlendArgs.custom_curve"></a>

#### custom_curve

```python
@property
def custom_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] If you're using Custom BlendOption, you can specify curve

<a id="unreal.AlphaBlendArgs.custom_curve"></a>

#### custom_curve

```python
@custom_curve.setter
def custom_curve(value: CurveFloat) -> None
```

<a id="unreal.AlphaBlendArgs.blend_time"></a>

#### blend_time

```python
@property
def blend_time() -> float
```

(float):  [Read-Write] Blend Time

<a id="unreal.AlphaBlendArgs.blend_time"></a>

#### blend_time

```python
@blend_time.setter
def blend_time(value: float) -> None
```

<a id="unreal.AlphaBlendArgs.blend_option"></a>

#### blend_option

```python
@property
def blend_option() -> AlphaBlendOption
```

(AlphaBlendOption):  [Read-Write] Type of blending used (Linear, Cubic, etc.)

<a id="unreal.AlphaBlendArgs.blend_option"></a>

#### blend_option

```python
@blend_option.setter
def blend_option(value: AlphaBlendOption) -> None
```

<a id="unreal.BlendSampleData"></a>