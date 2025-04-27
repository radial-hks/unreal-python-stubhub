## MovieSceneEvent Objects

```python
class MovieSceneEvent(StructBase)
```

Movie Scene Event

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneEvent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bound_object_pin_name`` (Name):  [Read-Write]
- ``payload_variables`` (Map[Name, MovieSceneEventPayloadVariable]):  [Read-Write] Array of payload variables to be added to the generated function
- ``weak_endpoint`` (Object):  [Read-Write] Serialized weak pointer to the function entry (UK2Node_FunctionEntry) or custom event node (UK2Node_CustomEvent) within the blueprint graph for this event. Stored as an editor-only UObject so UHT can parse it when building for non-editor.

<a id="unreal.MovieSceneEvent.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MovieSceneEvent.get_bound_object_property_class"></a>

#### get_bound_object_property_class

```python
def get_bound_object_property_class() -> Class
```

x.get_bound_object_property_class() -> type(Class)
* Return the class of the bound object property
*
*

Returns:
    type(Class): The class of the bound object property

<a id="unreal.MovieSceneObjectBindingID"></a>