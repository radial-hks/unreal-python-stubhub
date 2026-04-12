## AesPOISubsystem Objects

```python
class AesPOISubsystem(TickableWorldSubsystem)
```

Aes POISubsystem

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesPOI
- **File**: AesPOISubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_poi_main_ui`` (UserWidget):  [Read-Write]

<a id="unreal.AesPOISubsystem.aes_poi_main_ui"></a>

#### aes\_poi\_main\_ui

```python
@property
def aes_poi_main_ui() -> UserWidget
```

(UserWidget):  [Read-Only]

<a id="unreal.AesPOISubsystem.set_poi_enabled"></a>

#### set\_poi\_enabled

```python
def set_poi_enabled(enabled: bool) -> None
```

x.set_poi_enabled(enabled) -> None
Set POIEnabled

Args:
    enabled (bool):

<a id="unreal.AesPOISubsystem.get_poi_enabled"></a>

#### get\_poi\_enabled

```python
def get_poi_enabled() -> bool
```

x.get_poi_enabled() -> bool
Get POIEnabled

Returns:
    bool:

<a id="unreal.AesPOIUserWidget"></a>