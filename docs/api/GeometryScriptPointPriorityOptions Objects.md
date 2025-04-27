## GeometryScriptPointPriorityOptions Objects

```python
class GeometryScriptPointPriorityOptions(StructBase)
```

Geometry Script Point Priority Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PointSetFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``optional_priority_weights`` (Array[float]):  [Read-Write] If not empty, will be used to order the points so that higher-priority points are kept.
- ``uniform_spacing`` (bool):  [Read-Write] Whether to ensure the kept points are approximately uniformly spaced

<a id="unreal.GeometryScriptPointPriorityOptions.__init__"></a>

#### __init__

```python
def __init__(optional_priority_weights: Array[float] = [],
             uniform_spacing: bool = False) -> None
```

<a id="unreal.GeometryScriptPointPriorityOptions.optional_priority_weights"></a>

#### optional_priority_weights

```python
@property
def optional_priority_weights() -> Array[float]
```

(Array[float]):  [Read-Write] If not empty, will be used to order the points so that higher-priority points are kept.

<a id="unreal.GeometryScriptPointPriorityOptions.optional_priority_weights"></a>

#### optional_priority_weights

```python
@optional_priority_weights.setter
def optional_priority_weights(value: Array[float]) -> None
```

<a id="unreal.GeometryScriptPointPriorityOptions.uniform_spacing"></a>

#### uniform_spacing

```python
@property
def uniform_spacing() -> bool
```

(bool):  [Read-Write] Whether to ensure the kept points are approximately uniformly spaced

<a id="unreal.GeometryScriptPointPriorityOptions.uniform_spacing"></a>

#### uniform_spacing

```python
@uniform_spacing.setter
def uniform_spacing(value: bool) -> None
```

<a id="unreal.GeometryScriptPointFlatteningOptions"></a>