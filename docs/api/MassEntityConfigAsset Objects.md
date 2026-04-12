## MassEntityConfigAsset Objects

```python
class MassEntityConfigAsset(DataAsset)
```

Agent Config asset allows to create shared configs that can be used as base for derived configs.
The asset can be used as is i.e. on a spawner, or you can use FMassEntityConfig to allow last minute changes at use site.

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassSpawner
- **File**: MassEntityConfigAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``config`` (MassEntityConfig):  [Read-Write] The config described in this asset.

<a id="unreal.MassEntitySpawnDataGeneratorBase"></a>