## ModifyPathParams Objects

```python
class ModifyPathParams(ParamsBase)
```

Modify Path Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: PathAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coordinates`` (Array[Vector]):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``index`` (Array[int32]):  [Read-Write]
- ``method`` (str):  [Read-Write]

<a id="unreal.ModifyPathParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             method: str = "",
             index: Array[int] = [],
             coordinates: Array[Vector] = []) -> None
```

<a id="unreal.ModifyPathParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.ModifyPathParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.ModifyPathParams.method"></a>

#### method

```python
@property
def method() -> str
```

(str):  [Read-Write]

<a id="unreal.ModifyPathParams.method"></a>

#### method

```python
@method.setter
def method(value: str) -> None
```

<a id="unreal.ModifyPathParams.index"></a>

#### index

```python
@property
def index() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.ModifyPathParams.index"></a>

#### index

```python
@index.setter
def index(value: Array[int]) -> None
```

<a id="unreal.ModifyPathParams.coordinates"></a>

#### coordinates

```python
@property
def coordinates() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.ModifyPathParams.coordinates"></a>

#### coordinates

```python
@coordinates.setter
def coordinates(value: Array[Vector]) -> None
```

<a id="unreal.poiStyle_marker_image"></a>