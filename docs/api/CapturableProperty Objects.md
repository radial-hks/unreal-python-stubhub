## CapturableProperty Objects

```python
class CapturableProperty(StructBase)
```

Describes a property path that can be captured. It just exposes a display name but
uses internal data in order to be able to capture exception properties, like materials

**C++ Source:**

- **Plugin**: VariantManager
- **Module**: VariantManager
- **File**: CapturableProperty.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (str):  [Read-Only]

<a id="unreal.CapturableProperty.__init__"></a>

#### __init__

```python
def __init__(display_name: str = "") -> None
```

<a id="unreal.CapturableProperty.display_name"></a>

#### display_name

```python
@property
def display_name() -> str
```

(str):  [Read-Only]

<a id="unreal.InterchangeLodSceneNodeContainer"></a>