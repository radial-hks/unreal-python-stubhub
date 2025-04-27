## MovieSceneBindingOverrideData Objects

```python
class MovieSceneBindingOverrideData(StructBase)
```

Movie scene binding override data

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneBindingOverrides.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``object`` (Object):  [Read-Write] Specifies the object to override the binding with.
- ``object_binding_id`` (MovieSceneObjectBindingID):  [Read-Write] Specifies the object binding to override.
- ``overrides_default`` (bool):  [Read-Write] Specifies whether the default assignment should remain bound (false) or if this should completely override the default binding (true).

<a id="unreal.MovieSceneBindingOverrideData.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RuntimeCellTransformerInstance"></a>