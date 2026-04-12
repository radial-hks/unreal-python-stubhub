## GameplayAttributeData Objects

```python
class GameplayAttributeData(StructBase)
```

Place in an AttributeSet to create an attribute that can be accesed using FGameplayAttribute. It is strongly encouraged to use this instead of raw float attributes

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AttributeSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_value`` (float):  [Read-Write]
- ``current_value`` (float):  [Read-Write]

<a id="unreal.GameplayAttributeData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(base_value: float = 0.000000,
             current_value: float = 0.000000) -> None
```

<a id="unreal.GameplayAttributeData.base_value"></a>

#### base\_value

```python
@property
def base_value() -> float
```

(float):  [Read-Only]

<a id="unreal.GameplayAttributeData.current_value"></a>

#### current\_value

```python
@property
def current_value() -> float
```

(float):  [Read-Only]

<a id="unreal.AttributeMetaData"></a>