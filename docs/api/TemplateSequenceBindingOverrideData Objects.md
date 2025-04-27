## TemplateSequenceBindingOverrideData Objects

```python
class TemplateSequenceBindingOverrideData(StructBase)
```

Template sequence binding override data

This is similar to FMovieSceneBindingOverrideData, but works only for a template sequence's root object,
so we don't need it to store the object binding ID.

**C++ Source:**

- **Plugin**: TemplateSequence
- **Module**: TemplateSequence
- **File**: TemplateSequenceActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``object`` (Object):  [Read-Write] Specifies the object binding to override.
- ``overrides_default`` (bool):  [Read-Write] Specifies whether the default assignment should remain bound (false) or if this should completely override the default binding (true).

<a id="unreal.TemplateSequenceBindingOverrideData.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.FOscillator"></a>