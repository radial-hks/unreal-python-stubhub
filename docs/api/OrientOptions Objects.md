## OrientOptions Objects

```python
class OrientOptions(StructBase)
```

Orient Options

**C++ Source:**

- **Plugin**: MeshModelingToolsetExp
- **Module**: SkeletalMeshModifiers
- **File**: SkeletonModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``orient_children`` (bool):  [Read-Write]
- ``primary`` (OrientAxis):  [Read-Write]
- ``secondary`` (OrientAxis):  [Read-Write]
- ``secondary_target`` (Vector):  [Read-Write]
- ``use_plane_as_secondary`` (bool):  [Read-Write]

<a id="unreal.OrientOptions.__init__"></a>

#### __init__

```python
def __init__(primary: OrientAxis = OrientAxis.NONE,
             secondary: OrientAxis = OrientAxis.NONE,
             use_plane_as_secondary: bool = False,
             secondary_target: Vector = [0.000000, 0.000000, 0.000000],
             orient_children: bool = False) -> None
```

<a id="unreal.OrientOptions.primary"></a>

#### primary

```python
@property
def primary() -> OrientAxis
```

(OrientAxis):  [Read-Write]

<a id="unreal.OrientOptions.primary"></a>

#### primary

```python
@primary.setter
def primary(value: OrientAxis) -> None
```

<a id="unreal.OrientOptions.secondary"></a>

#### secondary

```python
@property
def secondary() -> OrientAxis
```

(OrientAxis):  [Read-Write]

<a id="unreal.OrientOptions.secondary"></a>

#### secondary

```python
@secondary.setter
def secondary(value: OrientAxis) -> None
```

<a id="unreal.OrientOptions.use_plane_as_secondary"></a>

#### use_plane_as_secondary

```python
@property
def use_plane_as_secondary() -> bool
```

(bool):  [Read-Write]

<a id="unreal.OrientOptions.use_plane_as_secondary"></a>

#### use_plane_as_secondary

```python
@use_plane_as_secondary.setter
def use_plane_as_secondary(value: bool) -> None
```

<a id="unreal.OrientOptions.secondary_target"></a>

#### secondary_target

```python
@property
def secondary_target() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.OrientOptions.secondary_target"></a>

#### secondary_target

```python
@secondary_target.setter
def secondary_target(value: Vector) -> None
```

<a id="unreal.OrientOptions.orient_children"></a>

#### orient_children

```python
@property
def orient_children() -> bool
```

(bool):  [Read-Write]

<a id="unreal.OrientOptions.orient_children"></a>

#### orient_children

```python
@orient_children.setter
def orient_children(value: bool) -> None
```

<a id="unreal.PropertyAnimatorCounterFormat"></a>