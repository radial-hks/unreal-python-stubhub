## AttributeMetaData Objects

```python
class AttributeMetaData(TableRowBase)
```

DataTable that allows us to define meta data about attributes. Still a work in progress.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AttributeSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_value`` (float):  [Read-Write]
- ``can_stack`` (bool):  [Read-Write]
- ``max_value`` (float):  [Read-Write]
- ``min_value`` (float):  [Read-Write]

<a id="unreal.AttributeMetaData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(base_value: float = 0.000000,
             min_value: float = 0.000000,
             max_value: float = 0.000000,
             can_stack: bool = False) -> None
```

<a id="unreal.AttributeMetaData.base_value"></a>

#### base\_value

```python
@property
def base_value() -> float
```

(float):  [Read-Only]

<a id="unreal.AttributeMetaData.min_value"></a>

#### min\_value

```python
@property
def min_value() -> float
```

(float):  [Read-Only]

<a id="unreal.AttributeMetaData.max_value"></a>

#### max\_value

```python
@property
def max_value() -> float
```

(float):  [Read-Only]

<a id="unreal.AttributeMetaData.can_stack"></a>

#### can\_stack

```python
@property
def can_stack() -> bool
```

(bool):  [Read-Only]

<a id="unreal.GameplayAbilityTargetingLocationInfo"></a>