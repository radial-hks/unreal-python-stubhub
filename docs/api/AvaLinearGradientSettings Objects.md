## AvaLinearGradientSettings Objects

```python
class AvaLinearGradientSettings(StructBase)
```

Ava Linear Gradient Settings

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheText
- **File**: AvaTextDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_a`` (LinearColor):  [Read-Write]
- ``color_b`` (LinearColor):  [Read-Write]
- ``direction`` (AvaGradientDirection):  [Read-Write]
- ``offset`` (float):  [Read-Write]
- ``rotation`` (float):  [Read-Write]
- ``smoothness`` (float):  [Read-Write]

<a id="unreal.AvaLinearGradientSettings.__init__"></a>

#### __init__

```python
def __init__(direction: AvaGradientDirection = 0,
             color_a: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             color_b: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             smoothness: float = 0.000000,
             offset: float = 0.000000,
             rotation: float = 0.000000) -> None
```

<a id="unreal.AvaLinearGradientSettings.direction"></a>

#### direction

```python
@property
def direction() -> AvaGradientDirection
```

(AvaGradientDirection):  [Read-Write]

<a id="unreal.AvaLinearGradientSettings.direction"></a>

#### direction

```python
@direction.setter
def direction(value: AvaGradientDirection) -> None
```

<a id="unreal.AvaLinearGradientSettings.color_a"></a>

#### color_a

```python
@property
def color_a() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaLinearGradientSettings.color_a"></a>

#### color_a

```python
@color_a.setter
def color_a(value: LinearColor) -> None
```

<a id="unreal.AvaLinearGradientSettings.color_b"></a>

#### color_b

```python
@property
def color_b() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaLinearGradientSettings.color_b"></a>

#### color_b

```python
@color_b.setter
def color_b(value: LinearColor) -> None
```

<a id="unreal.AvaLinearGradientSettings.smoothness"></a>

#### smoothness

```python
@property
def smoothness() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaLinearGradientSettings.smoothness"></a>

#### smoothness

```python
@smoothness.setter
def smoothness(value: float) -> None
```

<a id="unreal.AvaLinearGradientSettings.offset"></a>

#### offset

```python
@property
def offset() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaLinearGradientSettings.offset"></a>

#### offset

```python
@offset.setter
def offset(value: float) -> None
```

<a id="unreal.AvaLinearGradientSettings.rotation"></a>

#### rotation

```python
@property
def rotation() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaLinearGradientSettings.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: float) -> None
```

<a id="unreal.AvaMaterialMaskSettings"></a>