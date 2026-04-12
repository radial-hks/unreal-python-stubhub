## WdpSceneChangeInfo Objects

```python
class WdpSceneChangeInfo(EventArgsBase)
```

Wdp Scene Change Info

**C++ Source:**

- **Plugin**: WdpAPIFrame
- **Module**: WdpAPIFramework
- **File**: ApiResultBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``added_eids`` (Array[int64]):  [Read-Write]
- ``removed_eids`` (Array[int64]):  [Read-Write]
- ``update_info`` (WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.WdpSceneChangeInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(added_eids: Array[int] = [],
             removed_eids: Array[int] = [],
             update_info: WdpJsonObjectWrapper = []) -> None
```

<a id="unreal.WdpSceneChangeInfo.added_eids"></a>

#### added\_eids

```python
@property
def added_eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.WdpSceneChangeInfo.added_eids"></a>

#### added\_eids

```python
@added_eids.setter
def added_eids(value: Array[int]) -> None
```

<a id="unreal.WdpSceneChangeInfo.removed_eids"></a>

#### removed\_eids

```python
@property
def removed_eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.WdpSceneChangeInfo.removed_eids"></a>

#### removed\_eids

```python
@removed_eids.setter
def removed_eids(value: Array[int]) -> None
```

<a id="unreal.WdpSceneChangeInfo.update_info"></a>

#### update\_info

```python
@property
def update_info() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.WdpSceneChangeInfo.update_info"></a>

#### update\_info

```python
@update_info.setter
def update_info(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.ResultBase"></a>