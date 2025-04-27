## RigUnit_HierarchyGetChainItemArray Objects

```python
class RigUnit_HierarchyGetChainItemArray(RigUnit_HierarchyBase)
```

Returns a chain between two items

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chain`` (Array[RigElementKey]):  [Read-Write]
- ``end`` (RigElementKey):  [Read-Write]
- ``include_end`` (bool):  [Read-Write]
- ``include_start`` (bool):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]
- ``start`` (RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChainItemArray.__init__"></a>

#### __init__

```python
def __init__(start: RigElementKey = [RigElementType.NONE, "None"],
             end: RigElementKey = [RigElementType.NONE, "None"],
             include_start: bool = False,
             include_end: bool = False,
             reverse: bool = False,
             chain: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_HierarchyGetChainItemArray.start"></a>

#### start

```python
@property
def start() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChainItemArray.start"></a>

#### start

```python
@start.setter
def start(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetChainItemArray.end"></a>

#### end

```python
@property
def end() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChainItemArray.end"></a>

#### end

```python
@end.setter
def end(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetChainItemArray.include_start"></a>

#### include_start

```python
@property
def include_start() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChainItemArray.include_start"></a>

#### include_start

```python
@include_start.setter
def include_start(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetChainItemArray.include_end"></a>

#### include_end

```python
@property
def include_end() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChainItemArray.include_end"></a>

#### include_end

```python
@include_end.setter
def include_end(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetChainItemArray.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetChainItemArray.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetChainItemArray.chain"></a>

#### chain

```python
@property
def chain() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_HierarchyGetPose"></a>