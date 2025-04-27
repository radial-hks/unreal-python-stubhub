## CompositeReroute Objects

```python
class CompositeReroute(StructBase)
```

Collection of pins used for tunneling between graphs.
Utilizes reroute expressions to ensure zero overhead in the compiled material.

     _________________          _________________
    |   INPUT BASE    |        |   OUTPUT BASE   |
    +--------+--------+        +--------+--------+
    |        |   (>)  |   ->   |  (>)   |        |
    |        |   (>)  |        |  (>)   |        |
    |        |   (>)  |        |  (>)   |        |
    |        |   (>)  |        |  (>)   |        |
    |        |        |        |        |        |
    +--------+--------+        +--------+--------+
    | NODE IN:  NONE  |        | NODE IN:  PINS  |
    | NODE OUT: PINS  |        | NODE OUT: NONE  |
    |_________________|        |_________________|

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionPinBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]

<a id="unreal.CompositeReroute.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SwitchCustomInput"></a>