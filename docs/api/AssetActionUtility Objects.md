## AssetActionUtility Objects

```python
class AssetActionUtility(EditorUtilityObject)
```

Base class for all asset action-related utilities
Any functions/events that are exposed on derived classes that have the correct signature will be
included as menu options when right-clicking on a group of assets in the content browser.

**C++ Source:**

- **Module**: Blutility
- **File**: AssetActionUtility.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_action_for_blueprints`` (bool):  [Read-Write] Is this action designed to work specifically on Blueprints (true) or on all assets (false).
  If true, SupportedClasses is treated as a filter against the Parent Class of selected Blueprint assets.
- ``supported_classes`` (Array[Class]):  [Read-Write] The supported classes controls the list of classes that may be operated on by all of the asset functions in this
  utility class.
  note: When bIsActionForBlueprints is true, this will compare against the generated class of any Blueprint assets.
- ``supported_conditions`` (Array[AssetActionSupportCondition]):  [Read-Write] The supported conditions for any asset to use these utility functions.  Note: all of these conditions must pass
  in sequence.  So if you have earlier failure conditions you want to be run first, put them first in the list,
  if those fail, their failure reason will be handled first.

<a id="unreal.AssetActionUtility.is_action_for_blueprints"></a>

#### is_action_for_blueprints

```python
def is_action_for_blueprints() -> bool
```

x.is_action_for_blueprints() -> bool
Returns whether or not this action is designed to work specifically on Blueprints (true) or on all assets (false).
If true, GetSupportedClass() is treated as a filter against the Parent Class of selected Blueprint assets.
note: Returns the value of bIsActionForBlueprints by default.

Returns:
    bool:

<a id="unreal.AssetActionUtility.get_supported_classes"></a>

#### get_supported_classes

```python
def get_supported_classes() -> Array[Class]
```

x.get_supported_classes() -> Array[Class]
Gets the statically determined supported classes, these classes are used as a first pass filter when determining
if we can utilize this asset utility action on the asset.

Returns:
    Array[Class]:

<a id="unreal.AssetActionUtility.get_supported_class"></a>

#### get_supported_class

```python
def get_supported_class() -> Class
```

x.get_supported_class() -> type(Class)
Get Supported Class
deprecated: If you were just returning a single class add it to the SupportedClasses array (you can find it listed in the Class Defaults).  If you were doing complex logic to simulate having multiple classes act as filters, add them to the SupportedClasses array.  If you were doing 'other' logic, you'll need to do that upon action execution.

Returns:
    type(Class):

<a id="unreal.AsyncCaptureScene"></a>