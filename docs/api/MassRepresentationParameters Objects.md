## MassRepresentationParameters Objects

```python
class MassRepresentationParameters(MassConstSharedFragment)
```

Mass Representation Parameters

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassRepresentation
- **File**: MassRepresentationFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_modify_representation_actor_management_class`` (bool):  [Read-Write] the property is marked like this to ensure it won't show up in UI
- ``force_actor_representation_for_external_actors`` (bool):  [Read-Write] If true, forces UMassRepresentationProcessor to override the WantedRepresentationType to actor representation whenever an external (non Mass owned)
  actor is set on an entitie's FMassActorFragment fragment. If / when the actor fragment is reset, WantedRepresentationType resumes selecting the
  appropriate representation for the current representation LOD.

  Useful for server-authoritative actor spawning to force actor representation on clients for replicated actors.
- ``keep_actor_extra_frame`` (bool):  [Read-Write] When switching to ISM keep the actor an extra frame, helps cover rendering glitches (i.e. occlusion query being one frame late)
- ``keep_low_res_actors`` (bool):  [Read-Write] If true, LowRes actors will be kept around, disabled, whilst StaticMeshInstance representation is active
- ``lod_representation`` (MassRepresentationType):  [Read-Write] What should be the representation of this entity for each specific LOD
- ``not_visible_update_rate`` (float):  [Read-Write] At what rate should the not visible entity be updated in seconds
- ``representation_actor_management_class`` (type(Class)):  [Read-Write] Allow subclasses to override the representation actor management behavior
- ``spread_first_visualization_update`` (bool):  [Read-Write] If true, will spread the first visualization update over the period specified in NotVisibleUpdateRate member
- ``world_partition_grid_name_containing_collision`` (Name):  [Read-Write] World Partition grid name to test collision against, default None will be the main grid

<a id="unreal.MassRepresentationParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.MassDistanceLODParameters"></a>