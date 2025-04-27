## AvaPatternModifierCircleLayoutOptions Objects

```python
class AvaPatternModifierCircleLayoutOptions(StructBase)
```

Ava Pattern Modifier Circle Layout Options

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaPatternModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accumulate_transform`` (bool):  [Read-Write]
- ``centered`` (bool):  [Read-Write] Center the layout based on the plane
- ``full_angle`` (float):  [Read-Write]
- ``plane`` (AvaPatternModifierPlane):  [Read-Write]
- ``radius`` (float):  [Read-Write]
- ``repeat_count`` (int32):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``start_angle`` (float):  [Read-Write]

<a id="unreal.AvaPatternModifierCircleLayoutOptions.__init__"></a>

#### __init__

```python
def __init__(plane: AvaPatternModifierPlane = AvaPatternModifierPlane.XY,
             radius: float = 0.000000,
             start_angle: float = 0.000000,
             full_angle: float = 0.000000,
             repeat_count: int = 0,
             centered: bool = False,
             accumulate_transform: bool = False,
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.AvaPatternModifierCircleLayoutOptions.plane"></a>

#### plane

```python
@property
def plane() -> AvaPatternModifierPlane
```

(AvaPatternModifierPlane):  [Read-Write]

<a id="unreal.AvaPatternModifierCircleLayoutOptions.plane"></a>

#### plane

```python
@plane.setter
def plane(value: AvaPatternModifierPlane) -> None
```

<a id="unreal.AvaPatternModifierCircleLayoutOptions.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaPatternModifierCircleLayoutOptions.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.AvaPatternModifierCircleLayoutOptions.start_angle"></a>

#### start_angle

```python
@property
def start_angle() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaPatternModifierCircleLayoutOptions.start_angle"></a>

#### start_angle

```python
@start_angle.setter
def start_angle(value: float) -> None
```

<a id="unreal.AvaPatternModifierCircleLayoutOptions.full_angle"></a>

#### full_angle

```python
@property
def full_angle() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaPatternModifierCircleLayoutOptions.full_angle"></a>

#### full_angle

```python
@full_angle.setter
def full_angle(value: float) -> None
```

<a id="unreal.AvaPatternModifierCircleLayoutOptions.repeat_count"></a>

#### repeat_count

```python
@property
def repeat_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.AvaPatternModifierCircleLayoutOptions.repeat_count"></a>

#### repeat_count

```python
@repeat_count.setter
def repeat_count(value: int) -> None
```

<a id="unreal.AvaPatternModifierCircleLayoutOptions.centered"></a>

#### centered

```python
@property
def centered() -> bool
```

(bool):  [Read-Write] Center the layout based on the plane

<a id="unreal.AvaPatternModifierCircleLayoutOptions.centered"></a>

#### centered

```python
@centered.setter
def centered(value: bool) -> None
```

<a id="unreal.AvaPatternModifierCircleLayoutOptions.accumulate_transform"></a>

#### accumulate_transform

```python
@property
def accumulate_transform() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaPatternModifierCircleLayoutOptions.accumulate_transform"></a>

#### accumulate_transform

```python
@accumulate_transform.setter
def accumulate_transform(value: bool) -> None
```

<a id="unreal.AvaPatternModifierCircleLayoutOptions.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.AvaPatternModifierCircleLayoutOptions.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.AvaPatternModifierCircleLayoutOptions.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.AvaPatternModifierCircleLayoutOptions.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.AvaCloneModifierCircleLayoutOptions"></a>