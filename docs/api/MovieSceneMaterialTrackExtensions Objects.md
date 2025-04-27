## MovieSceneMaterialTrackExtensions Objects

```python
class MovieSceneMaterialTrackExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto UMovieSceneMaterialTrack for scripting

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneMaterialTrackExtensions.h

<a id="unreal.MovieSceneMaterialTrackExtensions.set_material_info"></a>

#### set_material_info

```python
@classmethod
def set_material_info(cls, track: MovieSceneComponentMaterialTrack,
                      material_info: ComponentMaterialInfo) -> None
```

X.set_material_info(track, material_info) -> None
Set material info of the component that is animated by the material track.

Args:
    track (MovieSceneComponentMaterialTrack): The track to use
    material_info (ComponentMaterialInfo): The desired material info to animate.

<a id="unreal.MovieSceneMaterialTrackExtensions.set_material_index"></a>

#### set_material_index

```python
@classmethod
def set_material_index(cls, track: MovieSceneComponentMaterialTrack,
                       material_index: int) -> None
```

X.set_material_index(track, material_index) -> None
Set Material Index
deprecated: Use SetMaterialInfo instead

Args:
    track (MovieSceneComponentMaterialTrack): 
    material_index (int32):

<a id="unreal.MovieSceneMaterialTrackExtensions.get_material_info"></a>

#### get_material_info

```python
@classmethod
def get_material_info(
        cls, track: MovieSceneComponentMaterialTrack) -> ComponentMaterialInfo
```

X.get_material_info(track) -> ComponentMaterialInfo
Get material info of the component that is animated by the material track.
deprecated: Use SetMaterialInfo instead

Args:
    track (MovieSceneComponentMaterialTrack): The track to use

Returns:
    ComponentMaterialInfo: The material info.

<a id="unreal.MovieSceneMaterialTrackExtensions.get_material_index"></a>

#### get_material_index

```python
@classmethod
def get_material_index(cls, track: MovieSceneComponentMaterialTrack) -> int
```

X.get_material_index(track) -> int32
Get Material Index
deprecated: Use SetMaterialInfo instead

Args:
    track (MovieSceneComponentMaterialTrack): 

Returns:
    int32:

<a id="unreal.MovieScenePrimitiveMaterialTrackExtensions"></a>