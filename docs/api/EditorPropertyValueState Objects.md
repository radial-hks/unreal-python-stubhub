## EditorPropertyValueState Objects

```python
class EditorPropertyValueState(EnumBase)
```

States a property value queried by IsEditorPropertyOverridden can be in

**C++ Source:**

- **Module**: Engine
- **File**: KismetSystemLibrary.h

<a id="unreal.EditorPropertyValueState.DEFAULT"></a>

#### DEFAULT

0: This property is in a default state

<a id="unreal.EditorPropertyValueState.OVERRIDDEN"></a>

#### OVERRIDDEN

1: This property is in an overridden state

<a id="unreal.EditorPropertyValueState.NOT_FOUND"></a>

#### NOT_FOUND

2: The property was not found on the object or its archetype; its state is unknown

<a id="unreal.EditorPropertyValueState.ACCESS_DENIED"></a>

#### ACCESS_DENIED

3: The property could not be accessed to query its state; its state is unknown

<a id="unreal.LevelInstanceRuntimeBehavior"></a>