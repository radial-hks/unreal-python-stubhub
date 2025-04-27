## PropertyPathTestObject Objects

```python
class PropertyPathTestObject(Object)
```

Property Path Test Object

**C++ Source:**

- **Module**: PropertyPath
- **File**: PropertyPathHelpersTest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bool`` (bool):  [Read-Write]
- ``enum_four`` (PropertyPathTestEnum):  [Read-Write]
- ``enum_one`` (PropertyPathTestEnum):  [Read-Write]
- ``enum_three`` (PropertyPathTestEnum):  [Read-Write]
- ``enum_two`` (PropertyPathTestEnum):  [Read-Write]
- ``float`` (float):  [Read-Write]
- ``inner_object`` (PropertyPathTestObject):  [Read-Write]
- ``integer`` (int32):  [Read-Write]
- ``string`` (str):  [Read-Write]
- ``struct`` (PropertyPathTestStruct):  [Read-Write]
- ``struct_const_ref`` (PropertyPathTestStruct):  [Read-Write]
- ``struct_ref`` (PropertyPathTestStruct):  [Read-Write]

<a id="unreal.PropertyPathTestObject.bool"></a>

#### bool

```python
@property
def bool() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PropertyPathTestObject.bool"></a>

#### bool

```python
@bool.setter
def bool(value: bool) -> None
```

<a id="unreal.PropertyPathTestObject.integer"></a>

#### integer

```python
@property
def integer() -> int
```

(int32):  [Read-Write]

<a id="unreal.PropertyPathTestObject.integer"></a>

#### integer

```python
@integer.setter
def integer(value: int) -> None
```

<a id="unreal.PropertyPathTestObject.string"></a>

#### string

```python
@property
def string() -> str
```

(str):  [Read-Write]

<a id="unreal.PropertyPathTestObject.string"></a>

#### string

```python
@string.setter
def string(value: str) -> None
```

<a id="unreal.PropertyPathTestObject.float"></a>

#### float

```python
@property
def float() -> float
```

(float):  [Read-Write]

<a id="unreal.PropertyPathTestObject.float"></a>

#### float

```python
@float.setter
def float(value: float) -> None
```

<a id="unreal.PropertyPathTestObject.struct"></a>

#### struct

```python
@property
def struct() -> PropertyPathTestStruct
```

(PropertyPathTestStruct):  [Read-Write]

<a id="unreal.PropertyPathTestObject.struct"></a>

#### struct

```python
@struct.setter
def struct(value: PropertyPathTestStruct) -> None
```

<a id="unreal.PropertyPathTestObject.struct_ref"></a>

#### struct_ref

```python
@property
def struct_ref() -> PropertyPathTestStruct
```

(PropertyPathTestStruct):  [Read-Write]

<a id="unreal.PropertyPathTestObject.struct_ref"></a>

#### struct_ref

```python
@struct_ref.setter
def struct_ref(value: PropertyPathTestStruct) -> None
```

<a id="unreal.PropertyPathTestObject.struct_const_ref"></a>

#### struct_const_ref

```python
@property
def struct_const_ref() -> PropertyPathTestStruct
```

(PropertyPathTestStruct):  [Read-Write]

<a id="unreal.PropertyPathTestObject.struct_const_ref"></a>

#### struct_const_ref

```python
@struct_const_ref.setter
def struct_const_ref(value: PropertyPathTestStruct) -> None
```

<a id="unreal.PropertyPathTestObject.inner_object"></a>

#### inner_object

```python
@property
def inner_object() -> PropertyPathTestObject
```

(PropertyPathTestObject):  [Read-Only]

<a id="unreal.LiveLinkFramePreProcessor"></a>