## ModifyHeatMapParam Objects

```python
class ModifyHeatMapParam(ParamsBase)
```

Modify Heat Map Param

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``features`` (Array[ModifyHeatMapfeatures]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``index`` (Array[int32]):  [Read-Write]
- ``method`` (str):  [Read-Write]

<a id="unreal.ModifyHeatMapParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             method: str = "",
             index: Array[int] = [],
             features: Array[ModifyHeatMapfeatures] = []) -> None
```

<a id="unreal.ModifyHeatMapParam.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.ModifyHeatMapParam.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.ModifyHeatMapParam.method"></a>

#### method

```python
@property
def method() -> str
```

(str):  [Read-Write]

<a id="unreal.ModifyHeatMapParam.method"></a>

#### method

```python
@method.setter
def method(value: str) -> None
```

<a id="unreal.ModifyHeatMapParam.index"></a>

#### index

```python
@property
def index() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.ModifyHeatMapParam.index"></a>

#### index

```python
@index.setter
def index(value: Array[int]) -> None
```

<a id="unreal.ModifyHeatMapParam.features"></a>

#### features

```python
@property
def features() -> Array[ModifyHeatMapfeatures]
```

(Array[ModifyHeatMapfeatures]):  [Read-Write]

<a id="unreal.ModifyHeatMapParam.features"></a>

#### features

```python
@features.setter
def features(value: Array[ModifyHeatMapfeatures]) -> None
```

<a id="unreal.HeatMapInfoParam"></a>