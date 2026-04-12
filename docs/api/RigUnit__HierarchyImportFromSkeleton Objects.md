## RigUnit\_HierarchyImportFromSkeleton Objects

```python
class RigUnit_HierarchyImportFromSkeleton(RigUnit_DynamicHierarchyBaseMutable)
```

Imports all bones (and curves) from the currently assigned skeleton.
Note: This node only runs as part of the construction event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``include_curves`` (bool):  [Read-Write]
- ``items`` (Array[RigElementKey]):  [Read-Write]
- ``name_space`` (Name):  [Read-Write]

<a id="unreal.RigUnit_HierarchyImportFromSkeleton.__init__"></a>

#### \_\_init\_\_

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             name_space: Name = "None",
             include_curves: bool = False,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_HierarchyImportFromSkeleton.name_space"></a>

#### name\_space

```python
@property
def name_space() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_HierarchyImportFromSkeleton.name_space"></a>

#### name\_space

```python
@name_space.setter
def name_space(value: Name) -> None
```

<a id="unreal.RigUnit_HierarchyImportFromSkeleton.include_curves"></a>

#### include\_curves

```python
@property
def include_curves() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyImportFromSkeleton.include_curves"></a>

#### include\_curves

```python
@include_curves.setter
def include_curves(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyImportFromSkeleton.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_HierarchyRemoveElement"></a>