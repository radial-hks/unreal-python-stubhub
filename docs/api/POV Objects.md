## POV Objects

```python
class POV(StructBase)
```

Point Of View structure used in Camera calculations

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fov`` (float):  [Read-Write] FOV angle
- ``location`` (Vector):  [Read-Write] Location
- ``rotation`` (Rotator):  [Read-Write] Rotation

<a id="unreal.POV.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             fov: float = 0.000000) -> None
```

<a id="unreal.POV.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] Location

<a id="unreal.POV.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.POV.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write] Rotation

<a id="unreal.POV.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.POV.fov"></a>

#### fov

```python
@property
def fov() -> float
```

(float):  [Read-Write] FOV angle

<a id="unreal.POV.fov"></a>

#### fov

```python
@fov.setter
def fov(value: float) -> None
```

<a id="unreal.MeshBuildSettings"></a>