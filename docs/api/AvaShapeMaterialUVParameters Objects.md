## AvaShapeMaterialUVParameters Objects

```python
class AvaShapeMaterialUVParameters(StructBase)
```

Ava Shape Material UVParameters

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapeUVParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anchor`` (Vector2D):  [Read-Write]
- ``anchor_preset`` (AvaAnchors):  [Read-Write]
- ``flip_horizontal`` (bool):  [Read-Write]
- ``flip_vertical`` (bool):  [Read-Write]
- ``mode`` (AvaShapeUVMode):  [Read-Write]
- ``offset`` (Vector2D):  [Read-Write]
- ``rotation`` (float):  [Read-Write]
- ``scale`` (Vector2D):  [Read-Write]

<a id="unreal.AvaShapeMaterialUVParameters.__init__"></a>

#### __init__

```python
def __init__(mode: AvaShapeUVMode = AvaShapeUVMode.STRETCH,
             anchor_preset: AvaAnchors = 0,
             anchor: Vector2D = [0.000000, 0.000000],
             scale: Vector2D = [0.000000, 0.000000],
             offset: Vector2D = [0.000000, 0.000000],
             rotation: float = 0.000000,
             flip_horizontal: bool = False,
             flip_vertical: bool = False) -> None
```

<a id="unreal.AvaShapeMaterialUVParameters.mode"></a>

#### mode

```python
@property
def mode() -> AvaShapeUVMode
```

(AvaShapeUVMode):  [Read-Write]

<a id="unreal.AvaShapeMaterialUVParameters.mode"></a>

#### mode

```python
@mode.setter
def mode(value: AvaShapeUVMode) -> None
```

<a id="unreal.AvaShapeMaterialUVParameters.anchor_preset"></a>

#### anchor_preset

```python
@property
def anchor_preset() -> AvaAnchors
```

(AvaAnchors):  [Read-Write]

<a id="unreal.AvaShapeMaterialUVParameters.anchor_preset"></a>

#### anchor_preset

```python
@anchor_preset.setter
def anchor_preset(value: AvaAnchors) -> None
```

<a id="unreal.AvaShapeMaterialUVParameters.anchor"></a>

#### anchor

```python
@property
def anchor() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.AvaShapeMaterialUVParameters.anchor"></a>

#### anchor

```python
@anchor.setter
def anchor(value: Vector2D) -> None
```

<a id="unreal.AvaShapeMaterialUVParameters.scale"></a>

#### scale

```python
@property
def scale() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.AvaShapeMaterialUVParameters.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector2D) -> None
```

<a id="unreal.AvaShapeMaterialUVParameters.offset"></a>

#### offset

```python
@property
def offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.AvaShapeMaterialUVParameters.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector2D) -> None
```

<a id="unreal.AvaShapeMaterialUVParameters.rotation"></a>

#### rotation

```python
@property
def rotation() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaShapeMaterialUVParameters.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: float) -> None
```

<a id="unreal.AvaShapeMaterialUVParameters.flip_horizontal"></a>

#### flip_horizontal

```python
@property
def flip_horizontal() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaShapeMaterialUVParameters.flip_horizontal"></a>

#### flip_horizontal

```python
@flip_horizontal.setter
def flip_horizontal(value: bool) -> None
```

<a id="unreal.AvaShapeMaterialUVParameters.flip_vertical"></a>

#### flip_vertical

```python
@property
def flip_vertical() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaShapeMaterialUVParameters.flip_vertical"></a>

#### flip_vertical

```python
@flip_vertical.setter
def flip_vertical(value: bool) -> None
```

<a id="unreal.AvaToolboxMaterialUVParameters"></a>