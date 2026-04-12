## UpdateArrayDuplicateParams Objects

```python
class UpdateArrayDuplicateParams(ParamsBase)
```

Update Array Duplicate Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpArrayDuplicateAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_type`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``num`` (int32):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``translation`` (Vector):  [Read-Write]

<a id="unreal.UpdateArrayDuplicateParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(num: int = 0,
             translation: Vector = [0.000000, 0.000000, 0.000000],
             rotator: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000],
             coord_type: str = "") -> None
```

<a id="unreal.UpdateArrayDuplicateParams.num"></a>

#### num

```python
@property
def num() -> int
```

(int32):  [Read-Write]

<a id="unreal.UpdateArrayDuplicateParams.num"></a>

#### num

```python
@num.setter
def num(value: int) -> None
```

<a id="unreal.UpdateArrayDuplicateParams.translation"></a>

#### translation

```python
@property
def translation() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.UpdateArrayDuplicateParams.translation"></a>

#### translation

```python
@translation.setter
def translation(value: Vector) -> None
```

<a id="unreal.UpdateArrayDuplicateParams.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.UpdateArrayDuplicateParams.rotator"></a>

#### rotator

```python
@rotator.setter
def rotator(value: Rotator) -> None
```

<a id="unreal.UpdateArrayDuplicateParams.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.UpdateArrayDuplicateParams.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.UpdateArrayDuplicateParams.coord_type"></a>

#### coord\_type

```python
@property
def coord_type() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateArrayDuplicateParams.coord_type"></a>

#### coord\_type

```python
@coord_type.setter
def coord_type(value: str) -> None
```

<a id="unreal.WDPSetCameraModeParams"></a>