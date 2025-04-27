## StaticMeshSocket Objects

```python
class StaticMeshSocket(Object)
```

Static Mesh Socket

**C++ Source:**

- **Module**: Engine
- **File**: StaticMeshSocket.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``preview_static_mesh`` (StaticMesh):  [Read-Write]
- ``relative_location`` (Vector):  [Read-Write]
- ``relative_rotation`` (Rotator):  [Read-Write]
- ``relative_scale`` (Vector):  [Read-Write]
- ``socket_name`` (Name):  [Read-Write] Defines a named attachment location on the UStaticMesh.
  These are set up in editor and used as a shortcut instead of specifying
  everything explicitly to AttachComponent in the StaticMeshComponent.
  The Outer of a StaticMeshSocket should always be the UStaticMesh.
- ``tag`` (str):  [Read-Write]

<a id="unreal.StaticMeshSocket.socket_name"></a>

#### socket_name

```python
@property
def socket_name() -> Name
```

(Name):  [Read-Only] Defines a named attachment location on the UStaticMesh.
These are set up in editor and used as a shortcut instead of specifying
everything explicitly to AttachComponent in the StaticMeshComponent.
The Outer of a StaticMeshSocket should always be the UStaticMesh.

<a id="unreal.StaticMeshSocket.relative_location"></a>

#### relative_location

```python
@property
def relative_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.StaticMeshSocket.relative_location"></a>

#### relative_location

```python
@relative_location.setter
def relative_location(value: Vector) -> None
```

<a id="unreal.StaticMeshSocket.relative_rotation"></a>

#### relative_rotation

```python
@property
def relative_rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.StaticMeshSocket.relative_rotation"></a>

#### relative_rotation

```python
@relative_rotation.setter
def relative_rotation(value: Rotator) -> None
```

<a id="unreal.StaticMeshSocket.relative_scale"></a>

#### relative_scale

```python
@property
def relative_scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.StaticMeshSocket.relative_scale"></a>

#### relative_scale

```python
@relative_scale.setter
def relative_scale(value: Vector) -> None
```

<a id="unreal.StaticMeshSocket.tag"></a>

#### tag

```python
@property
def tag() -> str
```

(str):  [Read-Write]

<a id="unreal.StaticMeshSocket.tag"></a>

#### tag

```python
@tag.setter
def tag(value: str) -> None
```

<a id="unreal.StereoLayerShape"></a>