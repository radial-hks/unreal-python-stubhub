## PossessPawnSettings Objects

```python
class PossessPawnSettings(StructBase)
```

切换Pawn时的配置设置

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_follow`` (bool):  [Read-Write] 切换后原Wdp相机是否自动跟随当前View
- ``return_to_default_pawn_when_destroyed`` (bool):  [Read-Write] 当前控制的Pawn被销毁后是否自动返回到默认Pawn

<a id="unreal.PossessPawnSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(auto_follow: bool = False,
             return_to_default_pawn_when_destroyed: bool = False) -> None
```

<a id="unreal.PossessPawnSettings.auto_follow"></a>

#### auto\_follow

```python
@property
def auto_follow() -> bool
```

(bool):  [Read-Write] 切换后原Wdp相机是否自动跟随当前View

<a id="unreal.PossessPawnSettings.auto_follow"></a>

#### auto\_follow

```python
@auto_follow.setter
def auto_follow(value: bool) -> None
```

<a id="unreal.PossessPawnSettings.return_to_default_pawn_when_destroyed"></a>

#### return\_to\_default\_pawn\_when\_destroyed

```python
@property
def return_to_default_pawn_when_destroyed() -> bool
```

(bool):  [Read-Write] 当前控制的Pawn被销毁后是否自动返回到默认Pawn

<a id="unreal.PossessPawnSettings.return_to_default_pawn_when_destroyed"></a>

#### return\_to\_default\_pawn\_when\_destroyed

```python
@return_to_default_pawn_when_destroyed.setter
def return_to_default_pawn_when_destroyed(value: bool) -> None
```

<a id="unreal.AgentMessage"></a>