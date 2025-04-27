## PCGManagedComponentList Objects

```python
class PCGManagedComponentList(PCGManagedComponentBase)
```

This managed resource class is used to tie multiple components in the same resource so that they are cleaned up all at the same time.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGManagedResource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``crc`` (PCGCrc):  [Read-Only]
- ``generated_components`` (Array[ActorComponent]):  [Read-Write]
- ``is_marked_unused`` (bool):  [Read-Only]
- ``marked_transient_on_load`` (bool):  [Read-Only] Resources on a Load-as-preview component are marked as 'transient on load'; these resources must not be affected in any
   permanent way in order to make sure they are not serialized in a different state if their outer is saved.
  These resources will generally have a different Release path, and will be managed differently from the PCG component as well.
  Note that this flag will be reset if there is a transient state change originating from the component, which might trigger resource deletion, flags change, etc.

<a id="unreal.PCGManagedComponentList.generated_components"></a>

#### generated_components

```python
@property
def generated_components() -> Array[ActorComponent]
```

(Array[ActorComponent]):  [Read-Write]

<a id="unreal.PCGManagedComponentList.generated_components"></a>

#### generated_components

```python
@generated_components.setter
def generated_components(value: Array[ActorComponent]) -> None
```

<a id="unreal.PCGManagedComponentDefaultList"></a>