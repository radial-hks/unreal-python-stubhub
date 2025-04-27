## InputAlphaBoolBlend Objects

```python
class InputAlphaBoolBlend(StructBase)
```

Input Alpha Bool Blend

**C++ Source:**

- **Module**: Engine
- **File**: InputScaleBias.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_in_time`` (float):  [Read-Write]
- ``blend_option`` (AlphaBlendOption):  [Read-Write]
- ``blend_out_time`` (float):  [Read-Write]
- ``custom_curve`` (CurveFloat):  [Read-Write]

<a id="unreal.InputAlphaBoolBlend.__init__"></a>

#### __init__

```python
def __init__(blend_in_time: float = 0.000000,
             blend_out_time: float = 0.000000,
             blend_option: AlphaBlendOption = AlphaBlendOption.LINEAR,
             custom_curve: CurveFloat = None) -> None
```

<a id="unreal.InputAlphaBoolBlend.blend_in_time"></a>

#### blend_in_time

```python
@property
def blend_in_time() -> float
```

(float):  [Read-Write]

<a id="unreal.InputAlphaBoolBlend.blend_in_time"></a>

#### blend_in_time

```python
@blend_in_time.setter
def blend_in_time(value: float) -> None
```

<a id="unreal.InputAlphaBoolBlend.blend_out_time"></a>

#### blend_out_time

```python
@property
def blend_out_time() -> float
```

(float):  [Read-Write]

<a id="unreal.InputAlphaBoolBlend.blend_out_time"></a>

#### blend_out_time

```python
@blend_out_time.setter
def blend_out_time(value: float) -> None
```

<a id="unreal.InputAlphaBoolBlend.blend_option"></a>

#### blend_option

```python
@property
def blend_option() -> AlphaBlendOption
```

(AlphaBlendOption):  [Read-Write]

<a id="unreal.InputAlphaBoolBlend.blend_option"></a>

#### blend_option

```python
@blend_option.setter
def blend_option(value: AlphaBlendOption) -> None
```

<a id="unreal.InputAlphaBoolBlend.custom_curve"></a>

#### custom_curve

```python
@property
def custom_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.InputAlphaBoolBlend.custom_curve"></a>

#### custom_curve

```python
@custom_curve.setter
def custom_curve(value: CurveFloat) -> None
```

<a id="unreal.AlphaBlend"></a>