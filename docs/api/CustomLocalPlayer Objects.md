## CustomLocalPlayer Objects

```python
class CustomLocalPlayer(LocalPlayer)
```

Custom Local Player

**C++ Source:**

- **Plugin**: CustomProgram
- **Module**: CustomProgram
- **File**: CustomLocalPlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_multi_views`` (bool):  [Read-Write]
- ``sent_split_join`` (bool):  [Read-Only] set when we've sent a split join request
- ``views_manager`` (ViewportsManager):  [Read-Write]

<a id="unreal.CustomLocalPlayer.enable_multi_views"></a>

#### enable\_multi\_views

```python
@property
def enable_multi_views() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CustomLocalPlayer.enable_multi_views"></a>

#### enable\_multi\_views

```python
@enable_multi_views.setter
def enable_multi_views(value: bool) -> None
```

<a id="unreal.CustomLocalPlayer.views_manager"></a>

#### views\_manager

```python
@property
def views_manager() -> ViewportsManager
```

(ViewportsManager):  [Read-Write]

<a id="unreal.CustomLocalPlayer.views_manager"></a>

#### views\_manager

```python
@views_manager.setter
def views_manager(value: ViewportsManager) -> None
```

<a id="unreal.CustomLocalPlayer.get_max_num_of_views"></a>

#### get\_max\_num\_of\_views

```python
@classmethod
def get_max_num_of_views(cls) -> int
```

X.get_max_num_of_views() -> int32
Get Max Num Of Views

Returns:
    int32:

<a id="unreal.CustomProgramLibrary"></a>