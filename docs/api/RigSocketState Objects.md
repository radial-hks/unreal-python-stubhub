## RigSocketState Objects

```python
class RigSocketState(StructBase)
```

Rig Socket State

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``description`` (str):  [Read-Write]
- ``initial_local_transform`` (Transform):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``parent`` (RigElementKey):  [Read-Write]

<a id="unreal.RigSocketState.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             parent: RigElementKey = [RigElementType.NONE, "None"],
             initial_local_transform: Transform = [[
                 0.000000, 0.000000, 0.000000
             ], [-0.000000, 0.000000,
                 0.000000], [1.000000, 1.000000, 1.000000]],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             description: str = "") -> None
```

<a id="unreal.RigSocketState.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigSocketState.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigSocketState.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigSocketState.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigSocketState.initial_local_transform"></a>

#### initial_local_transform

```python
@property
def initial_local_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigSocketState.initial_local_transform"></a>

#### initial_local_transform

```python
@initial_local_transform.setter
def initial_local_transform(value: Transform) -> None
```

<a id="unreal.RigSocketState.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigSocketState.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigSocketState.description"></a>

#### description

```python
@property
def description() -> str
```

(str):  [Read-Write]

<a id="unreal.RigSocketState.description"></a>

#### description

```python
@description.setter
def description(value: str) -> None
```

<a id="unreal.RigSocketElement"></a>