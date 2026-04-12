## FbxExportOption Objects

```python
class FbxExportOption(Object)
```

Fbx Export Option

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxExportOption.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ascii`` (bool):  [Read-Write] If enabled, save as ascii instead of binary
- ``bake_actor_animation`` (MovieSceneBakeType):  [Read-Write] Bake settings for exported non-camera, non-light object animation
- ``bake_camera_and_light_animation`` (MovieSceneBakeType):  [Read-Write] Bake settings for camera and light animation curves. Camera Scale not exported.
- ``bake_material_inputs`` (FbxMaterialBakeMode):  [Read-Write] Bake mode determining if and how a material input is baked out to a texture. Baking is only used for non-trivial material inputs (i.e. not simple texture or constant expressions).
- ``collision`` (bool):  [Read-Write] If enabled, export collision
- ``default_material_bake_size`` (FbxMaterialBakeSize):  [Read-Write] Default size of the baked out texture (containing the material input).
- ``export_local_time`` (bool):  [Read-Write] If enabled, export sequencer animation in its local time, relative to its sequence.
- ``export_morph_targets`` (bool):  [Read-Write] If enabled, export the morph targets
- ``export_preview_mesh`` (bool):  [Read-Write] If enable, the preview mesh link to the exported animations will be also exported.
- ``export_source_mesh`` (bool):  [Read-Write] * If enabled, export the highest LOD source data instead of the render data.
  * Note:
  *     - No LOD will be exported for static meshes. (Level Of Detail option will be ignored)
  *     - No Collision will be exported for static meshes. (Collision option will be ignore)
- ``fbx_export_compatibility`` (FbxExportCompatibility):  [Read-Write] This will set the fbx sdk compatibility when exporting to fbx file. The default value is 2013
- ``force_front_x_axis`` (bool):  [Read-Write] If enabled, export with X axis as the front axis instead of default -Y
- ``level_of_detail`` (bool):  [Read-Write] If enabled, export the level of detail
- ``map_skeletal_motion_to_root`` (bool):  [Read-Write] If enable, Map skeletal actor motion to the root bone of the skeleton.
- ``vertex_color`` (bool):  [Read-Write] If enabled, export vertex color

<a id="unreal.FbxExportOption.fbx_export_compatibility"></a>

#### fbx\_export\_compatibility

```python
@property
def fbx_export_compatibility() -> FbxExportCompatibility
```

(FbxExportCompatibility):  [Read-Write] This will set the fbx sdk compatibility when exporting to fbx file. The default value is 2013

<a id="unreal.FbxExportOption.fbx_export_compatibility"></a>

#### fbx\_export\_compatibility

```python
@fbx_export_compatibility.setter
def fbx_export_compatibility(value: FbxExportCompatibility) -> None
```

<a id="unreal.FbxExportOption.ascii"></a>

#### ascii

```python
@property
def ascii() -> bool
```

(bool):  [Read-Write] If enabled, save as ascii instead of binary

<a id="unreal.FbxExportOption.ascii"></a>

#### ascii

```python
@ascii.setter
def ascii(value: bool) -> None
```

<a id="unreal.FbxExportOption.force_front_x_axis"></a>

#### force\_front\_x\_axis

```python
@property
def force_front_x_axis() -> bool
```

(bool):  [Read-Write] If enabled, export with X axis as the front axis instead of default -Y

<a id="unreal.FbxExportOption.force_front_x_axis"></a>

#### force\_front\_x\_axis

```python
@force_front_x_axis.setter
def force_front_x_axis(value: bool) -> None
```

<a id="unreal.FbxExportOption.vertex_color"></a>

#### vertex\_color

```python
@property
def vertex_color() -> bool
```

(bool):  [Read-Write] If enabled, export vertex color

<a id="unreal.FbxExportOption.vertex_color"></a>

#### vertex\_color

```python
@vertex_color.setter
def vertex_color(value: bool) -> None
```

<a id="unreal.FbxExportOption.level_of_detail"></a>

#### level\_of\_detail

```python
@property
def level_of_detail() -> bool
```

(bool):  [Read-Write] If enabled, export the level of detail

<a id="unreal.FbxExportOption.level_of_detail"></a>

#### level\_of\_detail

```python
@level_of_detail.setter
def level_of_detail(value: bool) -> None
```

<a id="unreal.FbxExportOption.collision"></a>

#### collision

```python
@property
def collision() -> bool
```

(bool):  [Read-Write] If enabled, export collision

<a id="unreal.FbxExportOption.collision"></a>

#### collision

```python
@collision.setter
def collision(value: bool) -> None
```

<a id="unreal.FbxExportOption.export_source_mesh"></a>

#### export\_source\_mesh

```python
@property
def export_source_mesh() -> bool
```

(bool):  [Read-Write] * If enabled, export the highest LOD source data instead of the render data.
* Note:
*     - No LOD will be exported for static meshes. (Level Of Detail option will be ignored)
*     - No Collision will be exported for static meshes. (Collision option will be ignore)

<a id="unreal.FbxExportOption.export_source_mesh"></a>

#### export\_source\_mesh

```python
@export_source_mesh.setter
def export_source_mesh(value: bool) -> None
```

<a id="unreal.FbxExportOption.export_morph_targets"></a>

#### export\_morph\_targets

```python
@property
def export_morph_targets() -> bool
```

(bool):  [Read-Write] If enabled, export the morph targets

<a id="unreal.FbxExportOption.export_morph_targets"></a>

#### export\_morph\_targets

```python
@export_morph_targets.setter
def export_morph_targets(value: bool) -> None
```

<a id="unreal.FbxExportOption.export_preview_mesh"></a>

#### export\_preview\_mesh

```python
@property
def export_preview_mesh() -> bool
```

(bool):  [Read-Write] If enable, the preview mesh link to the exported animations will be also exported.

<a id="unreal.FbxExportOption.export_preview_mesh"></a>

#### export\_preview\_mesh

```python
@export_preview_mesh.setter
def export_preview_mesh(value: bool) -> None
```

<a id="unreal.FbxExportOption.map_skeletal_motion_to_root"></a>

#### map\_skeletal\_motion\_to\_root

```python
@property
def map_skeletal_motion_to_root() -> bool
```

(bool):  [Read-Write] If enable, Map skeletal actor motion to the root bone of the skeleton.

<a id="unreal.FbxExportOption.map_skeletal_motion_to_root"></a>

#### map\_skeletal\_motion\_to\_root

```python
@map_skeletal_motion_to_root.setter
def map_skeletal_motion_to_root(value: bool) -> None
```

<a id="unreal.FbxExportOption.export_local_time"></a>

#### export\_local\_time

```python
@property
def export_local_time() -> bool
```

(bool):  [Read-Write] If enabled, export sequencer animation in its local time, relative to its sequence.

<a id="unreal.FbxExportOption.export_local_time"></a>

#### export\_local\_time

```python
@export_local_time.setter
def export_local_time(value: bool) -> None
```

<a id="unreal.FbxExportOption.bake_camera_and_light_animation"></a>

#### bake\_camera\_and\_light\_animation

```python
@property
def bake_camera_and_light_animation() -> MovieSceneBakeType
```

(MovieSceneBakeType):  [Read-Write] Bake settings for camera and light animation curves. Camera Scale not exported.

<a id="unreal.FbxExportOption.bake_camera_and_light_animation"></a>

#### bake\_camera\_and\_light\_animation

```python
@bake_camera_and_light_animation.setter
def bake_camera_and_light_animation(value: MovieSceneBakeType) -> None
```

<a id="unreal.FbxExportOption.bake_actor_animation"></a>

#### bake\_actor\_animation

```python
@property
def bake_actor_animation() -> MovieSceneBakeType
```

(MovieSceneBakeType):  [Read-Write] Bake settings for exported non-camera, non-light object animation

<a id="unreal.FbxExportOption.bake_actor_animation"></a>

#### bake\_actor\_animation

```python
@bake_actor_animation.setter
def bake_actor_animation(value: MovieSceneBakeType) -> None
```

<a id="unreal.FbxExportOption.bake_material_inputs"></a>

#### bake\_material\_inputs

```python
@property
def bake_material_inputs() -> FbxMaterialBakeMode
```

(FbxMaterialBakeMode):  [Read-Write] Bake mode determining if and how a material input is baked out to a texture. Baking is only used for non-trivial material inputs (i.e. not simple texture or constant expressions).

<a id="unreal.FbxExportOption.bake_material_inputs"></a>

#### bake\_material\_inputs

```python
@bake_material_inputs.setter
def bake_material_inputs(value: FbxMaterialBakeMode) -> None
```

<a id="unreal.FbxExportOption.default_material_bake_size"></a>

#### default\_material\_bake\_size

```python
@property
def default_material_bake_size() -> FbxMaterialBakeSize
```

(FbxMaterialBakeSize):  [Read-Write] Default size of the baked out texture (containing the material input).

<a id="unreal.FbxExportOption.default_material_bake_size"></a>

#### default\_material\_bake\_size

```python
@default_material_bake_size.setter
def default_material_bake_size(value: FbxMaterialBakeSize) -> None
```

<a id="unreal.FbxFactory"></a>