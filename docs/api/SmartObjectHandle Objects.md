## SmartObjectHandle Objects

```python
class SmartObjectHandle(StructBase)
```

Handle to a registered smartobject.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``id`` (uint64):  [Read-Only]

<a id="unreal.SmartObjectHandle.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.SmartObjectHandle.not_equal"></a>

#### not\_equal

```python
def not_equal(b: SmartObjectHandle) -> bool
```

x.not_equal(b) -> bool
Returns true if SmartObjectHandle A is NOT equal to SmartObjectHandle B (A != B)

Args:
    b (SmartObjectHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectHandle.equals"></a>

#### equals

```python
def equals(b: SmartObjectHandle) -> bool
```

x.equals(b) -> bool
Returns true if SmartObjectHandle A is equal to SmartObjectHandle B (A == B)

Args:
    b (SmartObjectHandle): 

Returns:
    bool:

<a id="unreal.SmartObjectHandle.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``SmartObjectHandle`` Returns true if SmartObjectHandle A is equal to SmartObjectHandle B (A == B)

<a id="unreal.SmartObjectHandle.__ne__"></a>

#### \_\_ne\_\_

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``SmartObjectHandle`` Returns true if SmartObjectHandle A is NOT equal to SmartObjectHandle B (A != B)

<a id="unreal.SmartObjectID"></a>