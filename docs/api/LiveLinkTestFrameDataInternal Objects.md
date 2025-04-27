## LiveLinkTestFrameDataInternal Objects

```python
class LiveLinkTestFrameDataInternal(LiveLinkBaseFrameData)
```

Live Link Test Frame Data Internal

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLinkEditor
- **File**: LiveLinkTest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``float_array`` (Array[float]):  [Read-Write]
- ``int_array`` (Array[int32]):  [Read-Write]
- ``meta_data`` (LiveLinkMetaData):  [Read-Write] Frame's metadata.
- ``property_values`` (Array[float]):  [Read-Write] Values of the properties defined in the static structure. Use FLiveLinkBaseStaticData.FindPropertyValue to evaluate.
- ``single_float`` (float):  [Read-Write]
- ``single_int`` (int32):  [Read-Write]
- ``single_struct`` (LiveLinkInnerTestInternal):  [Read-Write]
- ``single_vector`` (Vector):  [Read-Write]
- ``struct_array`` (Array[LiveLinkInnerTestInternal]):  [Read-Write]
- ``vector_array`` (Array[Vector]):  [Read-Write]
- ``world_time`` (LiveLinkWorldTime):  [Read-Only] Time in seconds the frame was created.

<a id="unreal.LiveLinkTestFrameDataInternal.__init__"></a>

#### __init__

```python
def __init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]],
             property_values: Array[float] = [],
             single_vector: Vector = [0.000000, 0.000000, 0.000000],
             single_struct: LiveLinkInnerTestInternal = [],
             single_float: float = 0.000000,
             single_int: int = 0,
             vector_array: Array[Vector] = [],
             struct_array: Array[LiveLinkInnerTestInternal] = [],
             float_array: Array[float] = [],
             int_array: Array[int] = []) -> None
```

<a id="unreal.LiveLinkTestFrameDataInternal.single_vector"></a>

#### single_vector

```python
@property
def single_vector() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.LiveLinkTestFrameDataInternal.single_struct"></a>

#### single_struct

```python
@property
def single_struct() -> LiveLinkInnerTestInternal
```

(LiveLinkInnerTestInternal):  [Read-Only]

<a id="unreal.LiveLinkTestFrameDataInternal.single_float"></a>

#### single_float

```python
@property
def single_float() -> float
```

(float):  [Read-Only]

<a id="unreal.LiveLinkTestFrameDataInternal.single_int"></a>

#### single_int

```python
@property
def single_int() -> int
```

(int32):  [Read-Only]

<a id="unreal.LiveLinkTestFrameDataInternal.vector_array"></a>

#### vector_array

```python
@property
def vector_array() -> Array[Vector]
```

(Array[Vector]):  [Read-Only]

<a id="unreal.LiveLinkTestFrameDataInternal.struct_array"></a>

#### struct_array

```python
@property
def struct_array() -> Array[LiveLinkInnerTestInternal]
```

(Array[LiveLinkInnerTestInternal]):  [Read-Only]

<a id="unreal.LiveLinkTestFrameDataInternal.float_array"></a>

#### float_array

```python
@property
def float_array() -> Array[float]
```

(Array[float]):  [Read-Only]

<a id="unreal.LiveLinkTestFrameDataInternal.int_array"></a>

#### int_array

```python
@property
def int_array() -> Array[int]
```

(Array[int32]):  [Read-Only]

<a id="unreal.LiveLinkSubjectProperty"></a>