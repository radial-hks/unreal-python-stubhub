## ActorActionUtility Objects

```python
class ActorActionUtility(EditorUtilityObject)
```

Base class for all actor action-related utilities
Any functions/events that are exposed on derived classes that have the correct signature will be
included as menu options when right-clicking on a group of actors in the level editor.

**C++ Source:**

- **Module**: Blutility
- **File**: ActorActionUtility.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``supported_classes`` (Array[Class]):  [Read-Write] For simple Asset Action's you should fill out the supported class here.

<a id="unreal.ActorActionUtility.get_supported_classes"></a>

#### get_supported_classes

```python
def get_supported_classes() -> Array[Class]
```

x.get_supported_classes() -> Array[Class]
Gets the statically determined supported classes, these classes are used as a first pass filter when determining
if we can utilize this asset utility action on the asset.

Returns:
    Array[Class]:

<a id="unreal.ActorActionUtility.get_supported_class"></a>

#### get_supported_class

```python
def get_supported_class() -> Class
```

x.get_supported_class() -> type(Class)
Get Supported Class
deprecated: If you were just returning a single class add it to the SupportedClasses array (you can find it listed in the Class Defaults).  If you were doing complex logic to simulate having multiple classes act as filters, add them to the SupportedClasses array.  If you were doing 'other' logic, you'll need to do that upon action execution.

Returns:
    type(Class):

<a id="unreal.AssetActionUtility"></a>