## Object Objects

```python
class Object(_ObjectBase)
```

Direct base class for all UE objects
note: The full C++ class is located here: Engine\Source\Runtime\CoreUObject\Public\UObject\Object.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

<a id="unreal.Object.acquire_editor_element_handle"></a>

#### acquire_editor_element_handle

```python
def acquire_editor_element_handle(
        allow_create: bool = True) -> ScriptTypedElementHandle
```

x.acquire_editor_element_handle(allow_create=True) -> ScriptTypedElementHandle
K2 Acquire Editor Object Element Handle

Args:
    allow_create (bool): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.Object.reset_editor_property"></a>

#### reset_editor_property

```python
def reset_editor_property(
    property_name: Name,
    change_notify_mode:
    PropertyAccessChangeNotifyMode = PropertyAccessChangeNotifyMode.DEFAULT
) -> bool
```

x.reset_editor_property(property_name, change_notify_mode=PropertyAccessChangeNotifyMode.DEFAULT) -> bool
Attempts to reset the value of a named property on the given object so that it matches the value of the archetype.

Args:
    property_name (Name): The name of the object property to reset the value of.
    change_notify_mode (PropertyAccessChangeNotifyMode): When to emit property change notifications.

Returns:
    bool: Whether the property value was found and correctly reset.

<a id="unreal.Object.is_editor_property_overridden"></a>

#### is_editor_property_overridden

```python
def is_editor_property_overridden(
        property_name: Name) -> EditorPropertyValueState
```

x.is_editor_property_overridden(property_name) -> EditorPropertyValueState
Attempts to query whether the value of a named property on the given object overrides the value of its archetype (ie, would ResetEditorProperty do anything?).

Args:
    property_name (Name): The name of the object property to query the value of.

Returns:
    EditorPropertyValueState: What state the requested property is in.

<a id="unreal.Object.get_interpolated_pcg_landscape_layer_weights"></a>

#### get_interpolated_pcg_landscape_layer_weights

```python
def get_interpolated_pcg_landscape_layer_weights(
        location: Vector) -> Array[PCGLandscapeLayerWeight]
```

x.get_interpolated_pcg_landscape_layer_weights(location) -> Array[PCGLandscapeLayerWeight]
Get Interpolated PCGLandscape Layer Weights

Args:
    location (Vector): 

Returns:
    Array[PCGLandscapeLayerWeight]:

<a id="unreal.Interface"></a>