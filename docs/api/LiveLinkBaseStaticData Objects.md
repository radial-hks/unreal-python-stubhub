## LiveLinkBaseStaticData Objects

```python
class LiveLinkBaseStaticData(StructBase)
```

Base static data structure for a subject
Use to store information that is common to every frame
note: subclass can't contains reference to UObject

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``property_names`` (Array[Name]):  [Read-Write] Names for each curve values that will be sent for each frame

<a id="unreal.LiveLinkBaseStaticData.__init__"></a>

#### __init__

```python
def __init__(property_names: Array[Name] = []) -> None
```

<a id="unreal.LiveLinkBaseStaticData.property_names"></a>

#### property_names

```python
@property
def property_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Names for each curve values that will be sent for each frame

<a id="unreal.LiveLinkBaseStaticData.property_names"></a>

#### property_names

```python
@property_names.setter
def property_names(value: Array[Name]) -> None
```

<a id="unreal.LiveLinkSkeletonStaticData"></a>