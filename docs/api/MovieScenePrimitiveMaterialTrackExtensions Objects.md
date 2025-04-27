## MovieScenePrimitiveMaterialTrackExtensions Objects

```python
class MovieScenePrimitiveMaterialTrackExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto UMovieScenePrimitiveMaterialTrack for scripting

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieScenePrimitiveMaterialTrackExtensions.h

<a id="unreal.MovieScenePrimitiveMaterialTrackExtensions.set_material_info"></a>

#### set_material_info

```python
@classmethod
def set_material_info(cls, track: MovieScenePrimitiveMaterialTrack,
                      material_info: ComponentMaterialInfo) -> None
```

X.set_material_info(track, material_info) -> None
Set material info of the component that is animated by the material track.

Args:
    track (MovieScenePrimitiveMaterialTrack): The track to use
    material_info (ComponentMaterialInfo): The desired material info to animate.

<a id="unreal.MovieScenePrimitiveMaterialTrackExtensions.set_material_index"></a>

#### set_material_index

```python
@classmethod
def set_material_index(cls, track: MovieScenePrimitiveMaterialTrack,
                       material_index: int) -> None
```

X.set_material_index(track, material_index) -> None
Set Material Index
deprecated: Use SetMaterialInfo instead

Args:
    track (MovieScenePrimitiveMaterialTrack): 
    material_index (int32):

<a id="unreal.MovieScenePrimitiveMaterialTrackExtensions.get_material_info"></a>

#### get_material_info

```python
@classmethod
def get_material_info(
        cls, track: MovieScenePrimitiveMaterialTrack) -> ComponentMaterialInfo
```

X.get_material_info(track) -> ComponentMaterialInfo
Get material info of the component that is animated by the material track.
deprecated: Use SetMaterialInfo instead

Args:
    track (MovieScenePrimitiveMaterialTrack): The track to use

Returns:
    ComponentMaterialInfo: The material info.

<a id="unreal.MovieScenePrimitiveMaterialTrackExtensions.get_material_index"></a>

#### get_material_index

```python
@classmethod
def get_material_index(cls, track: MovieScenePrimitiveMaterialTrack) -> int
```

X.get_material_index(track) -> int32
Get Material Index
deprecated: Use SetMaterialInfo instead

Args:
    track (MovieScenePrimitiveMaterialTrack): 

Returns:
    int32:

<a id="unreal.MovieScenePropertyTrackExtensions"></a>