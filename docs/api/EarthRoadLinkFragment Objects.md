## EarthRoadLinkFragment Objects

```python
class EarthRoadLinkFragment(EarthPropertyFragment)
```

Earth Road Link Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_link`` (int64):  [Read-Write] 道路末端连接Id
- ``road_id`` (int64):  [Read-Write] 道路ID
- ``start_link`` (int64):  [Read-Write] 道路开端连接Id
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthRoadLinkFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             road_id: int = 0,
             start_link: int = 0,
             end_link: int = 0) -> None
```

<a id="unreal.EarthRoadLinkFragment.road_id"></a>

#### road\_id

```python
@property
def road_id() -> int
```

(int64):  [Read-Write] 道路ID

<a id="unreal.EarthRoadLinkFragment.road_id"></a>

#### road\_id

```python
@road_id.setter
def road_id(value: int) -> None
```

<a id="unreal.EarthRoadLinkFragment.start_link"></a>

#### start\_link

```python
@property
def start_link() -> int
```

(int64):  [Read-Write] 道路开端连接Id

<a id="unreal.EarthRoadLinkFragment.start_link"></a>

#### start\_link

```python
@start_link.setter
def start_link(value: int) -> None
```

<a id="unreal.EarthRoadLinkFragment.end_link"></a>

#### end\_link

```python
@property
def end_link() -> int
```

(int64):  [Read-Write] 道路末端连接Id

<a id="unreal.EarthRoadLinkFragment.end_link"></a>

#### end\_link

```python
@end_link.setter
def end_link(value: int) -> None
```

<a id="unreal.EarthJunctionConnectionFragment"></a>