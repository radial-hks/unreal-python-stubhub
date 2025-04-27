## AvaPatternModifierLineLayoutOptions Objects

```python
class AvaPatternModifierLineLayoutOptions(StructBase)
```

Ava Pattern Modifier Line Layout Options

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaPatternModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accumulate_transform`` (bool):  [Read-Write]
- ``axis`` (AvaPatternModifierAxis):  [Read-Write]
- ``axis_inverted`` (bool):  [Read-Write]
- ``centered`` (bool):  [Read-Write] Center the layout based on the axis
- ``repeat_count`` (int32):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``spacing`` (float):  [Read-Write]

<a id="unreal.AvaPatternModifierLineLayoutOptions.__init__"></a>

#### __init__

```python
def __init__(axis: AvaPatternModifierAxis = AvaPatternModifierAxis.X,
             axis_inverted: bool = False,
             repeat_count: int = 0,
             spacing: float = 0.000000,
             centered: bool = False,
             accumulate_transform: bool = False,
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.AvaPatternModifierLineLayoutOptions.axis"></a>

#### axis

```python
@property
def axis() -> AvaPatternModifierAxis
```

(AvaPatternModifierAxis):  [Read-Write]

<a id="unreal.AvaPatternModifierLineLayoutOptions.axis"></a>

#### axis

```python
@axis.setter
def axis(value: AvaPatternModifierAxis) -> None
```

<a id="unreal.AvaPatternModifierLineLayoutOptions.axis_inverted"></a>

#### axis_inverted

```python
@property
def axis_inverted() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaPatternModifierLineLayoutOptions.axis_inverted"></a>

#### axis_inverted

```python
@axis_inverted.setter
def axis_inverted(value: bool) -> None
```

<a id="unreal.AvaPatternModifierLineLayoutOptions.repeat_count"></a>

#### repeat_count

```python
@property
def repeat_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.AvaPatternModifierLineLayoutOptions.repeat_count"></a>

#### repeat_count

```python
@repeat_count.setter
def repeat_count(value: int) -> None
```

<a id="unreal.AvaPatternModifierLineLayoutOptions.spacing"></a>

#### spacing

```python
@property
def spacing() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaPatternModifierLineLayoutOptions.spacing"></a>

#### spacing

```python
@spacing.setter
def spacing(value: float) -> None
```

<a id="unreal.AvaPatternModifierLineLayoutOptions.centered"></a>

#### centered

```python
@property
def centered() -> bool
```

(bool):  [Read-Write] Center the layout based on the axis

<a id="unreal.AvaPatternModifierLineLayoutOptions.centered"></a>

#### centered

```python
@centered.setter
def centered(value: bool) -> None
```

<a id="unreal.AvaPatternModifierLineLayoutOptions.accumulate_transform"></a>

#### accumulate_transform

```python
@property
def accumulate_transform() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaPatternModifierLineLayoutOptions.accumulate_transform"></a>

#### accumulate_transform

```python
@accumulate_transform.setter
def accumulate_transform(value: bool) -> None
```

<a id="unreal.AvaPatternModifierLineLayoutOptions.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.AvaPatternModifierLineLayoutOptions.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.AvaPatternModifierLineLayoutOptions.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.AvaPatternModifierLineLayoutOptions.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.AvaCloneModifierLineLayoutOptions"></a>