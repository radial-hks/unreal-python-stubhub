## StripAnimDataOnDedicatedServerSettings Objects

```python
class StripAnimDataOnDedicatedServerSettings(EnumBase)
```

Enum used to decide whether we should strip animation data on dedicated server

**C++ Source:**

- **Module**: Engine
- **File**: AnimSequence.h

<a id="unreal.StripAnimDataOnDedicatedServerSettings.USE_PROJECT_SETTING"></a>

#### USE\_PROJECT\_SETTING

0: Strip track data on dedicated server if 'Strip Animation Data on Dedicated Server' option in Project Settings is true and EnableRootMotion is false

<a id="unreal.StripAnimDataOnDedicatedServerSettings.STRIP_ANIM_DATA_ON_DEDICATED_SERVER"></a>

#### STRIP\_ANIM\_DATA\_ON\_DEDICATED\_SERVER

1: Strip track data on dedicated server regardless of the value of 'Strip Animation Data on Dedicated Server' option in Project Settings as long as EnableRootMotion is false

<a id="unreal.StripAnimDataOnDedicatedServerSettings.DO_NOT_STRIP_ANIM_DATA_ON_DEDICATED_SERVER"></a>

#### DO\_NOT\_STRIP\_ANIM\_DATA\_ON\_DEDICATED\_SERVER

2: Do not strip track data on dedicated server regardless of the value of 'Strip Animation Data on Dedicated Server' option in Project Settings

<a id="unreal.SkyAtmosphereTransformMode"></a>