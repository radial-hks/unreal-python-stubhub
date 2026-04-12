## UpdateAttrParams Objects

```python
class UpdateAttrParams(StructBase)
```

Update Attr Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ClusterAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aggicon`` (WdpJsonObjectWrapper):  [Read-Write]
- ``covering`` (WdpJsonObjectWrapper):  [Read-Write]
- ``query_id`` (str):  [Read-Write]

<a id="unreal.UpdateAttrParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(query_id: str = "",
             aggicon: WdpJsonObjectWrapper = [],
             covering: WdpJsonObjectWrapper = []) -> None
```

<a id="unreal.UpdateAttrParams.query_id"></a>

#### query\_id

```python
@property
def query_id() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateAttrParams.query_id"></a>

#### query\_id

```python
@query_id.setter
def query_id(value: str) -> None
```

<a id="unreal.UpdateAttrParams.aggicon"></a>

#### aggicon

```python
@property
def aggicon() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.UpdateAttrParams.aggicon"></a>

#### aggicon

```python
@aggicon.setter
def aggicon(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.UpdateAttrParams.covering"></a>

#### covering

```python
@property
def covering() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.UpdateAttrParams.covering"></a>

#### covering

```python
@covering.setter
def covering(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.StartClusterParams"></a>