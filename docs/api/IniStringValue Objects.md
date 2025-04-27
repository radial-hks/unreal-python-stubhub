## IniStringValue Objects

```python
class IniStringValue(StructBase)
```

Helper struct for setting string console ini values.

**C++ Source:**

- **Module**: UnrealEd
- **File**: AssetGuideline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``branch`` (str):  [Read-Write] Ini branch that Filename belongs to. Ex: if Filename is "/Config/DefaultEngine.ini", Branch should be "Engine".

  If this isn't set, the system will attempt to detect it based on Filename.
- ``filename`` (str):  [Read-Write] From .ini, relative to {PROJECT}. Ex: /Config/DefaultEngine.ini
- ``key`` (str):  [Read-Write] From .ini. Ex: r.GPUSkin.Support16BitBoneIndex
- ``section`` (str):  [Read-Write] From .ini. Ex: /Script/Engine.RendererSettings
- ``value`` (str):  [Read-Write] From .ini. Ex: True

<a id="unreal.IniStringValue.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimSegment"></a>