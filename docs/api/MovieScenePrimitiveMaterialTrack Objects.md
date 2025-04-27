## MovieScenePrimitiveMaterialTrack Objects

```python
class MovieScenePrimitiveMaterialTrack(MovieScenePropertyTrack)
```

Movie Scene Primitive Material Track

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieScenePrimitiveMaterialTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_name`` (Text):  [Read-Write] The track's human readable display name.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``track_row_display_names`` (Array[Text]):  [Read-Write] The track display name per row.
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieScenePrimitiveMaterialTrack.set_material_info"></a>

#### set_material_info

```python
def set_material_info(material_info: ComponentMaterialInfo) -> None
```

x.set_material_info(material_info) -> None
Set material info of the component that is animated by the material track.

Args:
    material_info (ComponentMaterialInfo): The desired material info to animate.

<a id="unreal.MovieScenePrimitiveMaterialTrack.set_material_index"></a>

#### set_material_index

```python
def set_material_index(material_index: int) -> None
```

x.set_material_index(material_index) -> None
Set Material Index
deprecated: Use SetMaterialInfo instead

Args:
    material_index (int32):

<a id="unreal.MovieScenePrimitiveMaterialTrack.get_material_info"></a>

#### get_material_info

```python
def get_material_info() -> ComponentMaterialInfo
```

x.get_material_info() -> ComponentMaterialInfo
Get material info of the component that is animated by the material track.
deprecated: Use SetMaterialInfo instead

Returns:
    ComponentMaterialInfo: The material info.

<a id="unreal.MovieScenePrimitiveMaterialTrack.get_material_index"></a>

#### get_material_index

```python
def get_material_index() -> int
```

x.get_material_index() -> int32
Get Material Index
deprecated: Use SetMaterialInfo instead

Returns:
    int32:

<a id="unreal.MovieSceneSkeletalAnimationTrack"></a>