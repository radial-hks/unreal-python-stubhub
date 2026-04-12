## NodesTrInfo Objects

```python
class NodesTrInfo(StructBase)
```

Nodes Tr Info

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpInstanceEntityAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]
- ``scale3d`` (Vector):  [Read-Write]

<a id="unreal.NodesTrInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_ids: Array[int] = [],
             location: Vector = [0.000000, 0.000000, 0.000000],
             rotator: Rotator = [0.000000, 0.000000, 0.000000],
             scale3d: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.NodesTrInfo.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.NodesTrInfo.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.NodesTrInfo.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.NodesTrInfo.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.NodesTrInfo.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.NodesTrInfo.rotator"></a>

#### rotator

```python
@rotator.setter
def rotator(value: Rotator) -> None
```

<a id="unreal.NodesTrInfo.scale3d"></a>

#### scale3d

```python
@property
def scale3d() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.NodesTrInfo.scale3d"></a>

#### scale3d

```python
@scale3d.setter
def scale3d(value: Vector) -> None
```

<a id="unreal.NodesTrParams"></a>