## glTFRuntimeSkeletalMeshConfig Objects

```python
class glTFRuntimeSkeletalMeshConfig(StructBase)
```

Gl TFRuntime Skeletal Mesh Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_virtual_bones`` (bool):  [Read-Write]
- ``auto_generate_physics_asset_bodies`` (bool):  [Read-Write]
- ``auto_generate_physics_asset_constraints`` (bool):  [Read-Write]
- ``bone_bounds_filter`` (glTFRuntimeBoneBoundsFilterHook):  [Read-Write]
- ``bounds_scale`` (Vector):  [Read-Write]
- ``cache_mode`` (EglTFRuntimeCacheMode):  [Read-Write]
- ``custom_skeleton`` (Array[glTFRuntimeBone]):  [Read-Write]
- ``disable_morph_targets`` (bool):  [Read-Write]
- ``ignore_empty_morph_targets`` (bool):  [Read-Write]
- ``ignore_missing_bones`` (bool):  [Read-Write]
- ``ignore_skin`` (bool):  [Read-Write]
- ``lod_screen_size`` (Map[int32, float]):  [Read-Write]
- ``materials_config`` (glTFRuntimeMaterialsConfig):  [Read-Write]
- ``merge_all_bones_to_bone_tree`` (bool):  [Read-Write]
- ``morph_targets_duplicate_strategy`` (EglTFRuntimeMorphTargetsDuplicateStrategy):  [Read-Write]
- ``normals_generation_strategy`` (EglTFRuntimeNormalsGenerationStrategy):  [Read-Write]
- ``outer`` (Object):  [Read-Write]
- ``override_skin_index`` (int32):  [Read-Write]
- ``overwrite_ref_skeleton`` (bool):  [Read-Write]
- ``per_poly_collision`` (bool):  [Read-Write]
- ``physics_asset_auto_body_config`` (glTFRuntimePhysicsAssetAutoBodyConfig):  [Read-Write]
- ``physics_asset_template`` (PhysicsAsset):  [Read-Write]
- ``physics_bodies`` (Map[str, glTFRuntimePhysicsBody]):  [Read-Write]
- ``physics_constraints`` (Array[glTFRuntimePhysicsConstraint]):  [Read-Write]
- ``reverse_tangents`` (bool):  [Read-Write]
- ``save_to_package`` (str):  [Read-Write]
- ``shift_bounds`` (Vector):  [Read-Write]
- ``shift_bounds_by_root_bone`` (bool):  [Read-Write]
- ``skeleton`` (Skeleton):  [Read-Write]
- ``skeleton_config`` (glTFRuntimeSkeletonConfig):  [Read-Write]
- ``tangents_generation_strategy`` (EglTFRuntimeTangentsGenerationStrategy):  [Read-Write]
- ``use_high_precision_u_vs`` (bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE,
    skeleton: Skeleton = None,
    overwrite_ref_skeleton: bool = False,
    merge_all_bones_to_bone_tree: bool = False,
    custom_skeleton: Array[glTFRuntimeBone] = [],
    ignore_skin: bool = False,
    override_skin_index: int = 0,
    skeleton_config: glTFRuntimeSkeletonConfig = [
        EglTFRuntimeCacheMode.READ_WRITE, False, "", {}, False, {}, False, -1,
        {}, False, None, False, "", {}, [glTFRuntimeBoneRemapper(), None],
        False, False, False, -1, False, {}, False
    ],
    materials_config: glTFRuntimeMaterialsConfig = [
        EglTFRuntimeCacheMode.READ_WRITE, {}, {}, {}, {}, {}, False, False,
        False, 0.000000, False, {},
        [
            TextureCompressionSettings.TC_DEFAULT,
            TextureGroup.TEXTUREGROUP_WORLD, False, 0, 0, False, False, False,
            False, 0
        ], "", False, None, {}, False, None, True,
        EglTFRuntimePointsTriangulationMode.
        OPENED_TETRAHEDRON_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, True,
        EglTFRuntimeLinesTriangulationMode.
        OPENED_TRIANGULAR_PRISM_WITH_XY_IN_UV1ZW_IN_UV2, None, 1.000000, {},
        {}, {}
    ],
    lod_screen_size: Map[int, float] = {},
    bounds_scale: Vector = [0.000000, 0.000000, 0.000000],
    shift_bounds_by_root_bone: bool = False,
    ignore_missing_bones: bool = False,
    physics_bodies: Map[str, glTFRuntimePhysicsBody] = {},
    outer: Object = None,
    save_to_package: str = "",
    per_poly_collision: bool = False,
    disable_morph_targets: bool = False,
    ignore_empty_morph_targets: bool = False,
    morph_targets_duplicate_strategy:
    EglTFRuntimeMorphTargetsDuplicateStrategy = EglTFRuntimeMorphTargetsDuplicateStrategy
    .IGNORE,
    shift_bounds: Vector = [0.000000, 0.000000, 0.000000],
    use_high_precision_u_vs: bool = False,
    physics_asset_template: PhysicsAsset = None,
    add_virtual_bones: bool = False,
    normals_generation_strategy:
    EglTFRuntimeNormalsGenerationStrategy = EglTFRuntimeNormalsGenerationStrategy
    .IF_MISSING,
    tangents_generation_strategy:
    EglTFRuntimeTangentsGenerationStrategy = EglTFRuntimeTangentsGenerationStrategy
    .IF_MISSING,
    reverse_tangents: bool = False,
    auto_generate_physics_asset_bodies: bool = False,
    physics_asset_auto_body_config: glTFRuntimePhysicsAssetAutoBodyConfig = [
        EglTFRuntimePhysicsAssetAutoBodyCollisionType.CAPSULE, 20.000000, True,
        False, CollisionTraceFlag.CTF_USE_DEFAULT,
        PhysicsType.PHYS_TYPE_DEFAULT, True, 1.010000
    ],
    auto_generate_physics_asset_constraints: bool = False,
    physics_constraints: Array[glTFRuntimePhysicsConstraint] = [],
    bone_bounds_filter: glTFRuntimeBoneBoundsFilterHook = [
        glTFRuntimeBoneBoundsFilter(), None
    ]
) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.cache_mode"></a>

#### cache\_mode

```python
@property
def cache_mode() -> EglTFRuntimeCacheMode
```

(EglTFRuntimeCacheMode):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.cache_mode"></a>

#### cache\_mode

```python
@cache_mode.setter
def cache_mode(value: EglTFRuntimeCacheMode) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.skeleton"></a>

#### skeleton

```python
@property
def skeleton() -> Skeleton
```

(Skeleton):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.skeleton"></a>

#### skeleton

```python
@skeleton.setter
def skeleton(value: Skeleton) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.overwrite_ref_skeleton"></a>

#### overwrite\_ref\_skeleton

```python
@property
def overwrite_ref_skeleton() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.overwrite_ref_skeleton"></a>

#### overwrite\_ref\_skeleton

```python
@overwrite_ref_skeleton.setter
def overwrite_ref_skeleton(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.merge_all_bones_to_bone_tree"></a>

#### merge\_all\_bones\_to\_bone\_tree

```python
@property
def merge_all_bones_to_bone_tree() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.merge_all_bones_to_bone_tree"></a>

#### merge\_all\_bones\_to\_bone\_tree

```python
@merge_all_bones_to_bone_tree.setter
def merge_all_bones_to_bone_tree(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.custom_skeleton"></a>

#### custom\_skeleton

```python
@property
def custom_skeleton() -> Array[glTFRuntimeBone]
```

(Array[glTFRuntimeBone]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.custom_skeleton"></a>

#### custom\_skeleton

```python
@custom_skeleton.setter
def custom_skeleton(value: Array[glTFRuntimeBone]) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.ignore_skin"></a>

#### ignore\_skin

```python
@property
def ignore_skin() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.ignore_skin"></a>

#### ignore\_skin

```python
@ignore_skin.setter
def ignore_skin(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.override_skin_index"></a>

#### override\_skin\_index

```python
@property
def override_skin_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.override_skin_index"></a>

#### override\_skin\_index

```python
@override_skin_index.setter
def override_skin_index(value: int) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.skeleton_config"></a>

#### skeleton\_config

```python
@property
def skeleton_config() -> glTFRuntimeSkeletonConfig
```

(glTFRuntimeSkeletonConfig):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.skeleton_config"></a>

#### skeleton\_config

```python
@skeleton_config.setter
def skeleton_config(value: glTFRuntimeSkeletonConfig) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.materials_config"></a>

#### materials\_config

```python
@property
def materials_config() -> glTFRuntimeMaterialsConfig
```

(glTFRuntimeMaterialsConfig):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.materials_config"></a>

#### materials\_config

```python
@materials_config.setter
def materials_config(value: glTFRuntimeMaterialsConfig) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.lod_screen_size"></a>

#### lod\_screen\_size

```python
@property
def lod_screen_size() -> Map[int, float]
```

(Map[int32, float]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.lod_screen_size"></a>

#### lod\_screen\_size

```python
@lod_screen_size.setter
def lod_screen_size(value: Map[int, float]) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.bounds_scale"></a>

#### bounds\_scale

```python
@property
def bounds_scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.bounds_scale"></a>

#### bounds\_scale

```python
@bounds_scale.setter
def bounds_scale(value: Vector) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.shift_bounds_by_root_bone"></a>

#### shift\_bounds\_by\_root\_bone

```python
@property
def shift_bounds_by_root_bone() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.shift_bounds_by_root_bone"></a>

#### shift\_bounds\_by\_root\_bone

```python
@shift_bounds_by_root_bone.setter
def shift_bounds_by_root_bone(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.ignore_missing_bones"></a>

#### ignore\_missing\_bones

```python
@property
def ignore_missing_bones() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.ignore_missing_bones"></a>

#### ignore\_missing\_bones

```python
@ignore_missing_bones.setter
def ignore_missing_bones(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.physics_bodies"></a>

#### physics\_bodies

```python
@property
def physics_bodies() -> Map[str, glTFRuntimePhysicsBody]
```

(Map[str, glTFRuntimePhysicsBody]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.physics_bodies"></a>

#### physics\_bodies

```python
@physics_bodies.setter
def physics_bodies(value: Map[str, glTFRuntimePhysicsBody]) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.outer"></a>

#### outer

```python
@property
def outer() -> Object
```

(Object):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.outer"></a>

#### outer

```python
@outer.setter
def outer(value: Object) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.save_to_package"></a>

#### save\_to\_package

```python
@property
def save_to_package() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.save_to_package"></a>

#### save\_to\_package

```python
@save_to_package.setter
def save_to_package(value: str) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.per_poly_collision"></a>

#### per\_poly\_collision

```python
@property
def per_poly_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.per_poly_collision"></a>

#### per\_poly\_collision

```python
@per_poly_collision.setter
def per_poly_collision(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.disable_morph_targets"></a>

#### disable\_morph\_targets

```python
@property
def disable_morph_targets() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.disable_morph_targets"></a>

#### disable\_morph\_targets

```python
@disable_morph_targets.setter
def disable_morph_targets(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.ignore_empty_morph_targets"></a>

#### ignore\_empty\_morph\_targets

```python
@property
def ignore_empty_morph_targets() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.ignore_empty_morph_targets"></a>

#### ignore\_empty\_morph\_targets

```python
@ignore_empty_morph_targets.setter
def ignore_empty_morph_targets(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.morph_targets_duplicate_strategy"></a>

#### morph\_targets\_duplicate\_strategy

```python
@property
def morph_targets_duplicate_strategy(
) -> EglTFRuntimeMorphTargetsDuplicateStrategy
```

(EglTFRuntimeMorphTargetsDuplicateStrategy):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.morph_targets_duplicate_strategy"></a>

#### morph\_targets\_duplicate\_strategy

```python
@morph_targets_duplicate_strategy.setter
def morph_targets_duplicate_strategy(
        value: EglTFRuntimeMorphTargetsDuplicateStrategy) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.shift_bounds"></a>

#### shift\_bounds

```python
@property
def shift_bounds() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.shift_bounds"></a>

#### shift\_bounds

```python
@shift_bounds.setter
def shift_bounds(value: Vector) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.use_high_precision_u_vs"></a>

#### use\_high\_precision\_u\_vs

```python
@property
def use_high_precision_u_vs() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.use_high_precision_u_vs"></a>

#### use\_high\_precision\_u\_vs

```python
@use_high_precision_u_vs.setter
def use_high_precision_u_vs(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.physics_asset_template"></a>

#### physics\_asset\_template

```python
@property
def physics_asset_template() -> PhysicsAsset
```

(PhysicsAsset):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.physics_asset_template"></a>

#### physics\_asset\_template

```python
@physics_asset_template.setter
def physics_asset_template(value: PhysicsAsset) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.add_virtual_bones"></a>

#### add\_virtual\_bones

```python
@property
def add_virtual_bones() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.add_virtual_bones"></a>

#### add\_virtual\_bones

```python
@add_virtual_bones.setter
def add_virtual_bones(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.normals_generation_strategy"></a>

#### normals\_generation\_strategy

```python
@property
def normals_generation_strategy() -> EglTFRuntimeNormalsGenerationStrategy
```

(EglTFRuntimeNormalsGenerationStrategy):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.normals_generation_strategy"></a>

#### normals\_generation\_strategy

```python
@normals_generation_strategy.setter
def normals_generation_strategy(
        value: EglTFRuntimeNormalsGenerationStrategy) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.tangents_generation_strategy"></a>

#### tangents\_generation\_strategy

```python
@property
def tangents_generation_strategy() -> EglTFRuntimeTangentsGenerationStrategy
```

(EglTFRuntimeTangentsGenerationStrategy):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.tangents_generation_strategy"></a>

#### tangents\_generation\_strategy

```python
@tangents_generation_strategy.setter
def tangents_generation_strategy(
        value: EglTFRuntimeTangentsGenerationStrategy) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.reverse_tangents"></a>

#### reverse\_tangents

```python
@property
def reverse_tangents() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.reverse_tangents"></a>

#### reverse\_tangents

```python
@reverse_tangents.setter
def reverse_tangents(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.auto_generate_physics_asset_bodies"></a>

#### auto\_generate\_physics\_asset\_bodies

```python
@property
def auto_generate_physics_asset_bodies() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.auto_generate_physics_asset_bodies"></a>

#### auto\_generate\_physics\_asset\_bodies

```python
@auto_generate_physics_asset_bodies.setter
def auto_generate_physics_asset_bodies(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.physics_asset_auto_body_config"></a>

#### physics\_asset\_auto\_body\_config

```python
@property
def physics_asset_auto_body_config() -> glTFRuntimePhysicsAssetAutoBodyConfig
```

(glTFRuntimePhysicsAssetAutoBodyConfig):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.physics_asset_auto_body_config"></a>

#### physics\_asset\_auto\_body\_config

```python
@physics_asset_auto_body_config.setter
def physics_asset_auto_body_config(
        value: glTFRuntimePhysicsAssetAutoBodyConfig) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.auto_generate_physics_asset_constraints"></a>

#### auto\_generate\_physics\_asset\_constraints

```python
@property
def auto_generate_physics_asset_constraints() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.auto_generate_physics_asset_constraints"></a>

#### auto\_generate\_physics\_asset\_constraints

```python
@auto_generate_physics_asset_constraints.setter
def auto_generate_physics_asset_constraints(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.physics_constraints"></a>

#### physics\_constraints

```python
@property
def physics_constraints() -> Array[glTFRuntimePhysicsConstraint]
```

(Array[glTFRuntimePhysicsConstraint]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.physics_constraints"></a>

#### physics\_constraints

```python
@physics_constraints.setter
def physics_constraints(value: Array[glTFRuntimePhysicsConstraint]) -> None
```

<a id="unreal.glTFRuntimeSkeletalMeshConfig.bone_bounds_filter"></a>

#### bone\_bounds\_filter

```python
@property
def bone_bounds_filter() -> glTFRuntimeBoneBoundsFilterHook
```

(glTFRuntimeBoneBoundsFilterHook):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalMeshConfig.bone_bounds_filter"></a>

#### bone\_bounds\_filter

```python
@bone_bounds_filter.setter
def bone_bounds_filter(value: glTFRuntimeBoneBoundsFilterHook) -> None
```

<a id="unreal.glTFRuntimePathItem"></a>