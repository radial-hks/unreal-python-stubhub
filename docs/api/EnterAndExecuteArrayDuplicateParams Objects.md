## EnterAndExecuteArrayDuplicateParams Objects

```python
class EnterAndExecuteArrayDuplicateParams(ParamsBase)
```

Enter and Execute Array Duplicate Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpArrayDuplicateAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_type`` (str):  [Read-Write]
- ``eids`` (Set[int64]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``instance`` (bool):  [Read-Write]
- ``instance_name`` (str):  [Read-Write]
- ``num`` (int32):  [Read-Write]
- ``rotator`` (Vector):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``translation`` (Vector):  [Read-Write]

<a id="unreal.EnterAndExecuteArrayDuplicateParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Set[int] = [],
             num: int = 0,
             translation: Vector = [0.000000, 0.000000, 0.000000],
             rotator: Vector = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000],
             coord_type: str = "",
             instance: bool = False,
             instance_name: str = "") -> None
```

<a id="unreal.EnterAndExecuteArrayDuplicateParams.eids"></a>

#### eids

```python
@property
def eids() -> Set[int]
```

(Set[int64]):  [Read-Write]

<a id="unreal.EnterAndExecuteArrayDuplicateParams.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Set[int]) -> None
```

<a id="unreal.EnterAndExecuteArrayDuplicateParams.num"></a>

#### num

```python
@property
def num() -> int
```

(int32):  [Read-Write]

<a id="unreal.EnterAndExecuteArrayDuplicateParams.num"></a>

#### num

```python
@num.setter
def num(value: int) -> None
```

<a id="unreal.EnterAndExecuteArrayDuplicateParams.translation"></a>

#### translation

```python
@property
def translation() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.EnterAndExecuteArrayDuplicateParams.translation"></a>

#### translation

```python
@translation.setter
def translation(value: Vector) -> None
```

<a id="unreal.EnterAndExecuteArrayDuplicateParams.rotator"></a>

#### rotator

```python
@property
def rotator() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.EnterAndExecuteArrayDuplicateParams.rotator"></a>

#### rotator

```python
@rotator.setter
def rotator(value: Vector) -> None
```

<a id="unreal.EnterAndExecuteArrayDuplicateParams.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.EnterAndExecuteArrayDuplicateParams.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.EnterAndExecuteArrayDuplicateParams.coord_type"></a>

#### coord\_type

```python
@property
def coord_type() -> str
```

(str):  [Read-Write]

<a id="unreal.EnterAndExecuteArrayDuplicateParams.coord_type"></a>

#### coord\_type

```python
@coord_type.setter
def coord_type(value: str) -> None
```

<a id="unreal.EnterAndExecuteArrayDuplicateParams.instance"></a>

#### instance

```python
@property
def instance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EnterAndExecuteArrayDuplicateParams.instance"></a>

#### instance

```python
@instance.setter
def instance(value: bool) -> None
```

<a id="unreal.EnterAndExecuteArrayDuplicateParams.instance_name"></a>

#### instance\_name

```python
@property
def instance_name() -> str
```

(str):  [Read-Write]

<a id="unreal.EnterAndExecuteArrayDuplicateParams.instance_name"></a>

#### instance\_name

```python
@instance_name.setter
def instance_name(value: str) -> None
```

<a id="unreal.UpdateArrayDuplicateParams"></a>