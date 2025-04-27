## BrushEffectDisplacement Objects

```python
class BrushEffectDisplacement(StructBase)
```

Brush Effect Displacement

**C++ Source:**

- **Plugin**: Landmass
- **Module**: Landmass
- **File**: BrushEffectsList.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (LinearColor):  [Read-Write]
- ``displacement_height`` (float):  [Read-Write]
- ``displacement_tiling`` (float):  [Read-Write]
- ``midpoint`` (float):  [Read-Write]
- ``texture`` (Texture2D):  [Read-Write]
- ``weightmap_influence`` (float):  [Read-Write]

<a id="unreal.BrushEffectDisplacement.__init__"></a>

#### __init__

```python
def __init__(displacement_height: float = 0.000000,
             displacement_tiling: float = 0.000000,
             texture: Texture2D = None,
             midpoint: float = 0.000000,
             channel: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             weightmap_influence: float = 0.000000) -> None
```

<a id="unreal.BrushEffectDisplacement.displacement_height"></a>

#### displacement_height

```python
@property
def displacement_height() -> float
```

(float):  [Read-Write]

<a id="unreal.BrushEffectDisplacement.displacement_height"></a>

#### displacement_height

```python
@displacement_height.setter
def displacement_height(value: float) -> None
```

<a id="unreal.BrushEffectDisplacement.displacement_tiling"></a>

#### displacement_tiling

```python
@property
def displacement_tiling() -> float
```

(float):  [Read-Write]

<a id="unreal.BrushEffectDisplacement.displacement_tiling"></a>

#### displacement_tiling

```python
@displacement_tiling.setter
def displacement_tiling(value: float) -> None
```

<a id="unreal.BrushEffectDisplacement.texture"></a>

#### texture

```python
@property
def texture() -> Texture2D
```

(Texture2D):  [Read-Write]

<a id="unreal.BrushEffectDisplacement.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture2D) -> None
```

<a id="unreal.BrushEffectDisplacement.midpoint"></a>

#### midpoint

```python
@property
def midpoint() -> float
```

(float):  [Read-Write]

<a id="unreal.BrushEffectDisplacement.midpoint"></a>

#### midpoint

```python
@midpoint.setter
def midpoint(value: float) -> None
```

<a id="unreal.BrushEffectDisplacement.channel"></a>

#### channel

```python
@property
def channel() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.BrushEffectDisplacement.channel"></a>

#### channel

```python
@channel.setter
def channel(value: LinearColor) -> None
```

<a id="unreal.BrushEffectDisplacement.weightmap_influence"></a>

#### weightmap_influence

```python
@property
def weightmap_influence() -> float
```

(float):  [Read-Write]

<a id="unreal.BrushEffectDisplacement.weightmap_influence"></a>

#### weightmap_influence

```python
@weightmap_influence.setter
def weightmap_influence(value: float) -> None
```

<a id="unreal.BrushEffectSmoothBlending"></a>