## PCGManagedResource Objects

```python
class PCGManagedResource(Object)
```

This class is used to hold resources and their mechanism to delete them on demand.
In order to allow for some reuse (e.g. components), the Release call supports a "soft"
release by marking them unused in order to be potentially re-used down the line.
At the end of the generate, a call to ReleaseIfUnused will serve to finally cleanup
what is not needed anymore.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGManagedResource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``crc`` (PCGCrc):  [Read-Only]
- ``is_marked_unused`` (bool):  [Read-Only]
- ``marked_transient_on_load`` (bool):  [Read-Only] Resources on a Load-as-preview component are marked as 'transient on load'; these resources must not be affected in any
   permanent way in order to make sure they are not serialized in a different state if their outer is saved.
  These resources will generally have a different Release path, and will be managed differently from the PCG component as well.
  Note that this flag will be reset if there is a transient state change originating from the component, which might trigger resource deletion, flags change, etc.

<a id="unreal.PCGManagedComponentBase"></a>