## MovieGraphSetCVarValueNode Objects

```python
class MovieGraphSetCVarValueNode(MovieGraphSettingNode)
```

A node which can set a specific console variable's value.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphSetCVarValueNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``name`` (str):  [Read-Write] The name of the CVar having its value set.
- ``override_name`` (bool):  [Read-Write]
- ``override_value`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``value`` (float):  [Read-Write] The new value of the CVar.

<a id="unreal.MovieGraphSetCVarValueNode.override_name"></a>

#### override_name

```python
@property
def override_name() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphSetCVarValueNode.override_name"></a>

#### override_name

```python
@override_name.setter
def override_name(value: bool) -> None
```

<a id="unreal.MovieGraphSetCVarValueNode.override_value"></a>

#### override_value

```python
@property
def override_value() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphSetCVarValueNode.override_value"></a>

#### override_value

```python
@override_value.setter
def override_value(value: bool) -> None
```

<a id="unreal.MovieGraphSetCVarValueNode.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] The name of the CVar having its value set.

<a id="unreal.MovieGraphSetCVarValueNode.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.MovieGraphSetCVarValueNode.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] The new value of the CVar.

<a id="unreal.MovieGraphSetCVarValueNode.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.MovieGraphMetadataAttributeCollection"></a>