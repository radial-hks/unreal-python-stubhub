## HairAdvancedRenderingSettings Objects

```python
class HairAdvancedRenderingSettings(StructBase)
```

Hair Advanced Rendering Settings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetRendering.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``scatter_scene_lighting`` (bool):  [Read-Write] Light hair with the scene color. This is used for vellus/short hair to bring light from the surrounding surface, like skin.
- ``use_stable_rasterization`` (bool):  [Read-Write] Insure the hair does not alias. When enable, group of hairs might appear thicker. Isolated hair should remain thin.

<a id="unreal.HairAdvancedRenderingSettings.__init__"></a>

#### __init__

```python
def __init__(use_stable_rasterization: bool = False,
             scatter_scene_lighting: bool = False) -> None
```

<a id="unreal.HairAdvancedRenderingSettings.use_stable_rasterization"></a>

#### use_stable_rasterization

```python
@property
def use_stable_rasterization() -> bool
```

(bool):  [Read-Only] Insure the hair does not alias. When enable, group of hairs might appear thicker. Isolated hair should remain thin.

<a id="unreal.HairAdvancedRenderingSettings.scatter_scene_lighting"></a>

#### scatter_scene_lighting

```python
@property
def scatter_scene_lighting() -> bool
```

(bool):  [Read-Only] Light hair with the scene color. This is used for vellus/short hair to bring light from the surrounding surface, like skin.

<a id="unreal.HairGroupsRendering"></a>