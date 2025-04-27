## DatasmithImportBaseOptions Objects

```python
class DatasmithImportBaseOptions(StructBase)
```

Datasmith Import Base Options

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_options`` (DatasmithAssetImportOptions):  [Read-Write]
- ``include_animation`` (bool):  [Read-Write] Specifies whether or not to import animations
- ``include_camera`` (bool):  [Read-Write] Specifies whether or not to import cameras
- ``include_geometry`` (bool):  [Read-Write] Specifies whether or not to import geometry
- ``include_light`` (bool):  [Read-Write] Specifies whether or not to import lights
- ``include_material`` (bool):  [Read-Write] Specifies whether or not to import materials and textures
- ``scene_handling`` (DatasmithImportScene):  [Read-Write] Specifies where to put the content
- ``static_mesh_options`` (DatasmithStaticMeshImportOptions):  [Read-Write]

<a id="unreal.DatasmithImportBaseOptions.__init__"></a>

#### __init__

```python
def __init__(
    scene_handling: DatasmithImportScene = DatasmithImportScene.NEW_LEVEL,
    include_geometry: bool = False,
    include_material: bool = False,
    include_light: bool = False,
    include_camera: bool = False,
    include_animation: bool = False,
    asset_options: DatasmithAssetImportOptions = [],
    static_mesh_options: DatasmithStaticMeshImportOptions = [
        DatasmithImportLightmapMin.LIGHTMAP_64,
        DatasmithImportLightmapMax.LIGHTMAP_512, True, True
    ]
) -> None
```

<a id="unreal.DatasmithImportBaseOptions.scene_handling"></a>

#### scene_handling

```python
@property
def scene_handling() -> DatasmithImportScene
```

(DatasmithImportScene):  [Read-Write] Specifies where to put the content

<a id="unreal.DatasmithImportBaseOptions.scene_handling"></a>

#### scene_handling

```python
@scene_handling.setter
def scene_handling(value: DatasmithImportScene) -> None
```

<a id="unreal.DatasmithImportBaseOptions.include_geometry"></a>

#### include_geometry

```python
@property
def include_geometry() -> bool
```

(bool):  [Read-Write] Specifies whether or not to import geometry

<a id="unreal.DatasmithImportBaseOptions.include_geometry"></a>

#### include_geometry

```python
@include_geometry.setter
def include_geometry(value: bool) -> None
```

<a id="unreal.DatasmithImportBaseOptions.include_material"></a>

#### include_material

```python
@property
def include_material() -> bool
```

(bool):  [Read-Write] Specifies whether or not to import materials and textures

<a id="unreal.DatasmithImportBaseOptions.include_material"></a>

#### include_material

```python
@include_material.setter
def include_material(value: bool) -> None
```

<a id="unreal.DatasmithImportBaseOptions.include_light"></a>

#### include_light

```python
@property
def include_light() -> bool
```

(bool):  [Read-Write] Specifies whether or not to import lights

<a id="unreal.DatasmithImportBaseOptions.include_light"></a>

#### include_light

```python
@include_light.setter
def include_light(value: bool) -> None
```

<a id="unreal.DatasmithImportBaseOptions.include_camera"></a>

#### include_camera

```python
@property
def include_camera() -> bool
```

(bool):  [Read-Write] Specifies whether or not to import cameras

<a id="unreal.DatasmithImportBaseOptions.include_camera"></a>

#### include_camera

```python
@include_camera.setter
def include_camera(value: bool) -> None
```

<a id="unreal.DatasmithImportBaseOptions.include_animation"></a>

#### include_animation

```python
@property
def include_animation() -> bool
```

(bool):  [Read-Write] Specifies whether or not to import animations

<a id="unreal.DatasmithImportBaseOptions.include_animation"></a>

#### include_animation

```python
@include_animation.setter
def include_animation(value: bool) -> None
```

<a id="unreal.DatasmithImportBaseOptions.asset_options"></a>

#### asset_options

```python
@property
def asset_options() -> DatasmithAssetImportOptions
```

(DatasmithAssetImportOptions):  [Read-Write]

<a id="unreal.DatasmithImportBaseOptions.asset_options"></a>

#### asset_options

```python
@asset_options.setter
def asset_options(value: DatasmithAssetImportOptions) -> None
```

<a id="unreal.DatasmithImportBaseOptions.static_mesh_options"></a>

#### static_mesh_options

```python
@property
def static_mesh_options() -> DatasmithStaticMeshImportOptions
```

(DatasmithStaticMeshImportOptions):  [Read-Write]

<a id="unreal.DatasmithImportBaseOptions.static_mesh_options"></a>

#### static_mesh_options

```python
@static_mesh_options.setter
def static_mesh_options(value: DatasmithStaticMeshImportOptions) -> None
```

<a id="unreal.DatasmithTessellationOptions"></a>