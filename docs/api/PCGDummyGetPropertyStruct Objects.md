## PCGDummyGetPropertyStruct Objects

```python
class PCGDummyGetPropertyStruct(StructBase)
```

PCGDummy Get Property Struct

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGGetActorPropertyTest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``float_property`` (float):  [Read-Write]
- ``int_array_property`` (Array[int32]):  [Read-Write]
- ``level2_struct`` (PCGDummyGetPropertyLevel2Struct):  [Read-Write]

<a id="unreal.PCGDummyGetPropertyStruct.__init__"></a>

#### __init__

```python
def __init__(int_array_property: Array[int] = [],
             float_property: float = 0.000000,
             level2_struct: PCGDummyGetPropertyLevel2Struct = [[]]) -> None
```

<a id="unreal.PCGDummyGetPropertyStruct.int_array_property"></a>

#### int_array_property

```python
@property
def int_array_property() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.PCGDummyGetPropertyStruct.float_property"></a>

#### float_property

```python
@property
def float_property() -> float
```

(float):  [Read-Only]

<a id="unreal.PCGDummyGetPropertyStruct.level2_struct"></a>

#### level2_struct

```python
@property
def level2_struct() -> PCGDummyGetPropertyLevel2Struct
```

(PCGDummyGetPropertyLevel2Struct):  [Read-Only]

<a id="unreal.PCGTestMyColorStruct"></a>