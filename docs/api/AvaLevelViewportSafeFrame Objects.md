## AvaLevelViewportSafeFrame Objects

```python
class AvaLevelViewportSafeFrame(StructBase)
```

Ava Level Viewport Safe Frame

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheViewport
- **File**: AvaViewportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``screen_percentage`` (float):  [Read-Write] Distance from the center of the screen to the edge in percent.
- ``thickness`` (float):  [Read-Write]

<a id="unreal.AvaLevelViewportSafeFrame.__init__"></a>

#### __init__

```python
def __init__(screen_percentage: float = 0.000000,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000) -> None
```

<a id="unreal.AvaLevelViewportSafeFrame.screen_percentage"></a>

#### screen_percentage

```python
@property
def screen_percentage() -> float
```

(float):  [Read-Write] Distance from the center of the screen to the edge in percent.

<a id="unreal.AvaLevelViewportSafeFrame.screen_percentage"></a>

#### screen_percentage

```python
@screen_percentage.setter
def screen_percentage(value: float) -> None
```

<a id="unreal.AvaLevelViewportSafeFrame.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaLevelViewportSafeFrame.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.AvaLevelViewportSafeFrame.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaLevelViewportSafeFrame.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.BoolConverterCondition"></a>