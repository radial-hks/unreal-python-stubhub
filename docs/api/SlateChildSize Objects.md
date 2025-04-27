## SlateChildSize Objects

```python
class SlateChildSize(StructBase)
```

A struct exposing size param related properties to UMG.

**C++ Source:**

- **Module**: UMG
- **File**: SlateWrapperTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``size_rule`` (SlateSizeRule):  [Read-Write] The sizing rule of the content.
- ``value`` (float):  [Read-Write] The parameter of the size rule.

<a id="unreal.SlateChildSize.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             size_rule: SlateSizeRule = SlateSizeRule.AUTOMATIC) -> None
```

<a id="unreal.SlateChildSize.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] The parameter of the size rule.

<a id="unreal.SlateChildSize.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.SlateChildSize.size_rule"></a>

#### size_rule

```python
@property
def size_rule() -> SlateSizeRule
```

(SlateSizeRule):  [Read-Write] The sizing rule of the content.

<a id="unreal.SlateChildSize.size_rule"></a>

#### size_rule

```python
@size_rule.setter
def size_rule(value: SlateSizeRule) -> None
```

<a id="unreal.WidgetEventField"></a>