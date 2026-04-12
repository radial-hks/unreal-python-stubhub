## SmartObjectSlotHandle Objects

```python
class SmartObjectSlotHandle(StructBase)
```

Struct used to identify a runtime slot instance

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectTypes.h

<a id="unreal.SmartObjectSlotHandle.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.SmartObjectSlotHandle.not_equal"></a>

#### not\_equal

```python
def not_equal(b: SmartObjectSlotHandle) -> bool
```

x.not_equal(b) -> bool
Returns true if SmartObjectSlotHandle A is NOT equal to SmartObjectSlotHandle B (A != B)

Args:
    b (SmartObjectSlotHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectSlotHandle.equals"></a>

#### equals

```python
def equals(b: SmartObjectSlotHandle) -> bool
```

x.equals(b) -> bool
Returns true if SmartObjectSlotHandle A is equal to SmartObjectSlotHandle B (A == B)

Args:
    b (SmartObjectSlotHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectSlotHandle.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``SmartObjectSlotHandle`` Returns true if SmartObjectSlotHandle A is equal to SmartObjectSlotHandle B (A == B)

<a id="unreal.SmartObjectSlotHandle.__ne__"></a>

#### \_\_ne\_\_

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``SmartObjectSlotHandle`` Returns true if SmartObjectSlotHandle A is NOT equal to SmartObjectSlotHandle B (A != B)

<a id="unreal.SmartObjectHandle"></a>