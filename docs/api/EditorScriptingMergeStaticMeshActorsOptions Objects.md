## EditorScriptingMergeStaticMeshActorsOptions Objects

```python
class EditorScriptingMergeStaticMeshActorsOptions(MergeStaticMeshActorsOptions
                                                  )
```

deprecated: 'EditorScriptingMergeStaticMeshActorsOptions' was renamed to 'MergeStaticMeshActorsOptions'.

<a id="unreal.EditorScriptingMergeStaticMeshActorsOptions.__init__"></a>

#### __init__

```python
def __init__(
    destroy_source_actors: bool = False,
    new_actor_label: str = "",
    rename_components_from_source: bool = False,
    spawn_merged_actor: bool = False,
    base_package_name: str = "",
    mesh_merging_settings: MeshMergingSettings = [
        256,
        [
            TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE,
            5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000,
            0.000000, 0.500000, 1.000000, 1.000000, 1.000000,
            BlendMode.BLEND_OPAQUE, True, True, False, False, False, False,
            False, False, False, False, False, [1024, 1024], [1024, 1024],
            [1024, 1024], [1024, 1024], [1024, 1024], [1024,
                                                       1024], [1024, 1024],
            [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024]
        ], MeshLODSelectionType.CALCULATE_LOD, 0, True, False, False, False,
        False, False, False, True, False, False, True, True,
        [
            False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000,
            NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0
        ]
    ]
) -> None
```

<a id="unreal.CreateProxyMeshActorOptions"></a>