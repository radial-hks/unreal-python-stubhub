## UVMapSettings Objects

```python
class UVMapSettings(StructBase)
```

UV map generation settings that are exposed to the user for scripting and through the editor

**C++ Source:**

- **Module**: StaticMeshDescription
- **File**: UVMapSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``position`` (Vector):  [Read-Write] Position of the UV mapping gizmo
- ``rotation`` (Rotator):  [Read-Write] Rotation of the UV mapping gizmo (angles in degrees)
- ``scale`` (Vector):  [Read-Write] Scale of the UV mapping gizmo
- ``size`` (Vector):  [Read-Write] Length, width, height of the UV mapping gizmo
- ``uv_tile`` (Vector2D):  [Read-Write] Tiling of the UV mapping

<a id="unreal.UVMapSettings.__init__"></a>

#### __init__

```python
def __init__(size: Vector = [0.000000, 0.000000, 0.000000],
             uv_tile: Vector2D = [0.000000, 0.000000],
             position: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.UVMapSettings.size"></a>

#### size

```python
@property
def size() -> Vector
```

(Vector):  [Read-Write] Length, width, height of the UV mapping gizmo

<a id="unreal.UVMapSettings.size"></a>

#### size

```python
@size.setter
def size(value: Vector) -> None
```

<a id="unreal.UVMapSettings.uv_tile"></a>

#### uv_tile

```python
@property
def uv_tile() -> Vector2D
```

(Vector2D):  [Read-Write] Tiling of the UV mapping

<a id="unreal.UVMapSettings.uv_tile"></a>

#### uv_tile

```python
@uv_tile.setter
def uv_tile(value: Vector2D) -> None
```

<a id="unreal.UVMapSettings.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write] Position of the UV mapping gizmo

<a id="unreal.UVMapSettings.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.UVMapSettings.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write] Rotation of the UV mapping gizmo (angles in degrees)

<a id="unreal.UVMapSettings.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.UVMapSettings.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write] Scale of the UV mapping gizmo

<a id="unreal.UVMapSettings.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.BoneID"></a>