## AnimationCompressionLibraryDatabase Objects

```python
class AnimationCompressionLibraryDatabase(Object)
```

An ACL database object references several UAnimSequence instances that it contains.

**C++ Source:**

- **Plugin**: ACLPlugin
- **Module**: ACLPlugin
- **File**: AnimationCompressionLibraryDatabase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_sequences`` (Array[AnimSequence]):  [Read-Only] The anim sequences contained within the database. Built manually from the asset UI, content browser, or with a commandlet.
- ``anim_sequences_new_size_kb`` (int32):  [Read-Only] The total size of all Animation Sequences with the database in use.
- ``anim_sequences_old_size_kb`` (int32):  [Read-Only] The total size of all Animation Sequences if the database were not used.
- ``database_metadata_size_kb`` (int32):  [Read-Only] The size of the database metadata.
- ``database_size_kb`` (int32):  [Read-Only] The total size of the database.
- ``default_visual_fidelity`` (ACLVisualFidelity):  [Read-Write] The default level of quality to set when the database loads in-game. By default, nothing is streamed in.
- ``highest_importance_proportion`` (float):  [Read-Only] What percentage of the key frames should remain in the anim sequences.
- ``low_importance_size_size_kb`` (int32):  [Read-Only] The size of the database low importance streaming tier before any stripping.
- ``lowest_importance_proportion`` (float):  [Read-Write] What percentage of the key frames should be moved to the database. Least important key frames are moved first.
- ``max_stream_request_size_kb`` (uint32):  [Read-Write] The maximum size in KiloBytes of streaming requests. Setting this to 0 will force tiers to load in a single request regardless of their size.
- ``medium_importance_proportion`` (float):  [Read-Write] What percentage of the key frames should be moved to the database. Medium importance key frames are moved second.
- ``medium_importance_size_kb`` (int32):  [Read-Only] The size of the database medium importance streaming tier.
- ``num_anim_sequences`` (int32):  [Read-Only] The total num of Animation Sequences in this database.
- ``preview_visual_fidelity`` (ACLVisualFidelity):  [Read-Write] The level of quality to preview with the database when decompressing in the editor.
- ``strip_lowest_importance_tier`` (PerPlatformBool):  [Read-Write] Whether or not to strip the lowest importance tier entirely from disk. Stripping the lowest tier means that the visual fidelity of Highest and Medium are equivalent.

<a id="unreal.AnimationCompressionLibraryDatabase.set_visual_fidelity"></a>

#### set_visual_fidelity

```python
@classmethod
def set_visual_fidelity(
    cls,
    world_context_object: Object,
    latent_info: LatentActionInfo,
    database_asset: AnimationCompressionLibraryDatabase,
    visual_fidelity: ACLVisualFidelity = ACLVisualFidelity.HIGHEST
) -> ACLVisualFidelityChangeResult
```

X.set_visual_fidelity(world_context_object, latent_info, database_asset, visual_fidelity=ACLVisualFidelity.HIGHEST) -> ACLVisualFidelityChangeResult
Initiate a latent database change in quality by streaming in/out as necessary.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    database_asset (AnimationCompressionLibraryDatabase): 
    visual_fidelity (ACLVisualFidelity): 

Returns:
    ACLVisualFidelityChangeResult: 

    result (ACLVisualFidelityChangeResult):

<a id="unreal.AnimationCompressionLibraryDatabase.get_visual_fidelity"></a>

#### get_visual_fidelity

```python
@classmethod
def get_visual_fidelity(
        cls, database_asset: AnimationCompressionLibraryDatabase
) -> ACLVisualFidelity
```

X.get_visual_fidelity(database_asset) -> ACLVisualFidelity
Get Visual Fidelity

Args:
    database_asset (AnimationCompressionLibraryDatabase): 

Returns:
    ACLVisualFidelity:

<a id="unreal.ComputeGraphComponent"></a>