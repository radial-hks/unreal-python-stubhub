## GizmoBPLibrary Objects

```python
class GizmoBPLibrary(BlueprintFunctionLibrary)
```

Gizmo BPLibrary

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpGizmoTool
- **File**: GizmoBPLibrary.h

<a id="unreal.GizmoBPLibrary.is_bit_set"></a>

#### is\_bit\_set

```python
@classmethod
def is_bit_set(cls, b: int, bit: int) -> bool
```

X.is_bit_set(b, bit) -> bool
Is Bit Set

Args:
    b (uint8): 
    bit (int32): 

Returns:
    bool:

<a id="unreal.GizmoBPLibrary.case_switch_object"></a>

#### case\_switch\_object

```python
@classmethod
def case_switch_object(cls, only_check_first_x: int, value: Object,
                       case_1: Object, case_2: Object, case_3: Object,
                       case_4: Object, case_5: Object, case_6: Object,
                       case_7: Object, case_8: Object, case_9: Object,
                       case_10: Object) -> GizmoBPLibrary1to10other
```

X.case_switch_object(only_check_first_x, value, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) -> GizmoBPLibrary1to10other
Executes a the pin of the matching value.

Args:
    only_check_first_x (int32): 
    value (Object): 
    1 (Object): 
    2 (Object): 
    3 (Object): 
    4 (Object): 
    5 (Object): 
    6 (Object): 
    7 (Object): 
    8 (Object): 
    9 (Object): 
    10 (Object): 

Returns:
    GizmoBPLibrary1to10other: 

    branch (GizmoBPLibrary1to10other):

<a id="unreal.WdpCoordAxisGizmo"></a>