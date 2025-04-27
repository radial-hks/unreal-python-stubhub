## MovieSceneDynamicBinding Objects

```python
class MovieSceneDynamicBinding(StructBase)
```

Data for a dynamic binding endpoint call.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneDynamicBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``payload_variables`` (Map[Name, MovieSceneDynamicBindingPayloadVariable]):  [Read-Write] Array of payload variables to be added to the generated function
- ``resolve_params_pin_name`` (Name):  [Read-Write] Pin name for passing the resolve params
- ``weak_endpoint`` (Object):  [Read-Write] Endpoint node in the sequence director

<a id="unreal.MovieSceneDynamicBinding.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MovieSceneCameraShakeSectionData"></a>