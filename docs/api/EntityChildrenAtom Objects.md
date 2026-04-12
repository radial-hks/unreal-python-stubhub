## EntityChildrenAtom Objects

```python
class EntityChildrenAtom(EntityAtomBase)
```

Entity Children Atom

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: EntityChildrenAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``children_eids`` (Array[int64]):  [Read-Write]

<a id="unreal.EntityChildrenAtom.children_eids"></a>

#### children\_eids

```python
@property
def children_eids() -> Array[int]
```

(Array[int64]):  [Read-Only]

<a id="unreal.EntityChildrenAtom.remove_items"></a>

#### remove\_items

```python
def remove_items(to_remove_eids: Array[int]) -> bool
```

x.remove_items(to_remove_eids) -> bool
Remove Items

Args:
    to_remove_eids (Array[int64]): 

Returns:
    bool:

<a id="unreal.EntityPickAtom"></a>