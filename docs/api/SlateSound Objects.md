## SlateSound Objects

```python
class SlateSound(StructBase)
```

An intermediary to make UBaseSound available for Slate to play sounds

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateSound.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``resource_object`` (Object):  [Read-Write] Pointer to the USoundBase. Holding onto it as a UObject because USoundBase is not available in Slate core.
  Edited via FSlateSoundStructCustomization to ensure you can only set USoundBase assets on it.

<a id="unreal.SlateSound.__init__"></a>

#### __init__

```python
def __init__(resource_object: Object = None) -> None
```

<a id="unreal.SlateSound.resource_object"></a>

#### resource_object

```python
@property
def resource_object() -> Object
```

(Object):  [Read-Write] Pointer to the USoundBase. Holding onto it as a UObject because USoundBase is not available in Slate core.
Edited via FSlateSoundStructCustomization to ensure you can only set USoundBase assets on it.

<a id="unreal.SlateSound.resource_object"></a>

#### resource_object

```python
@resource_object.setter
def resource_object(value: Object) -> None
```

<a id="unreal.ComboButtonStyle"></a>