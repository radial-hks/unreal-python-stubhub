## InstanceComponentInfo Objects

```python
class InstanceComponentInfo(StructBase)
```

Instance Component Info

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: StaticMeshAssetLoader
- **File**: IsmEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_id`` (str):  [Read-Write]
- ``component_location`` (Vector):  [Read-Write]
- ``component_name`` (str):  [Read-Write]
- ``component_rotator`` (Rotator):  [Read-Write]
- ``component_scale`` (Vector):  [Read-Write]
- ``hidden_ids`` (Set[int32]):  [Read-Write]
- ``id_to_rotator`` (Map[int32, Rotator]):  [Read-Write]
- ``id_to_scale`` (Map[int32, Vector]):  [Read-Write]
- ``mesh_name`` (str):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]
- ``parent_name`` (str):  [Read-Write]
- ``positions`` (Array[Vector]):  [Read-Write]

<a id="unreal.InstanceComponentInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(component_name: str = "",
             parent_name: str = "",
             asset_id: str = "",
             mesh_name: str = "",
             component_location: Vector = [0.000000, 0.000000, 0.000000],
             component_rotator: Rotator = [0.000000, 0.000000, 0.000000],
             component_scale: Vector = [0.000000, 0.000000, 0.000000],
             node_ids: Array[int] = [],
             positions: Array[Vector] = [],
             id_to_rotator: Map[int, Rotator] = {},
             id_to_scale: Map[int, Vector] = {},
             hidden_ids: Set[int] = []) -> None
```

<a id="unreal.InstanceComponentInfo.component_name"></a>

#### component\_name

```python
@property
def component_name() -> str
```

(str):  [Read-Only]

<a id="unreal.InstanceComponentInfo.parent_name"></a>

#### parent\_name

```python
@property
def parent_name() -> str
```

(str):  [Read-Only]

<a id="unreal.InstanceComponentInfo.asset_id"></a>

#### asset\_id

```python
@property
def asset_id() -> str
```

(str):  [Read-Only]

<a id="unreal.InstanceComponentInfo.mesh_name"></a>

#### mesh\_name

```python
@property
def mesh_name() -> str
```

(str):  [Read-Only]

<a id="unreal.InstanceComponentInfo.component_location"></a>

#### component\_location

```python
@property
def component_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.InstanceComponentInfo.component_rotator"></a>

#### component\_rotator

```python
@property
def component_rotator() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.InstanceComponentInfo.component_scale"></a>

#### component\_scale

```python
@property
def component_scale() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.InstanceComponentInfo.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.InstanceComponentInfo.positions"></a>

#### positions

```python
@property
def positions() -> Array[Vector]
```

(Array[Vector]):  [Read-Only]

<a id="unreal.InstanceComponentInfo.id_to_rotator"></a>

#### id\_to\_rotator

```python
@property
def id_to_rotator() -> Map[int, Rotator]
```

(Map[int32, Rotator]):  [Read-Only]

<a id="unreal.InstanceComponentInfo.id_to_scale"></a>

#### id\_to\_scale

```python
@property
def id_to_scale() -> Map[int, Vector]
```

(Map[int32, Vector]):  [Read-Only]

<a id="unreal.InstanceComponentInfo.hidden_ids"></a>

#### hidden\_ids

```python
@property
def hidden_ids() -> Set[int]
```

(Set[int32]):  [Read-Only]

<a id="unreal.WdpCoordinateTransformParams"></a>