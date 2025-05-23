## AISenseConfig_Touch Objects

```python
class AISenseConfig_Touch(AISenseConfig)
```

AISense Config Touch

**C++ Source:**

- **Module**: AIModule
- **File**: AISenseConfig_Touch.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_color`` (Color):  [Read-Write]
- ``detection_by_affiliation`` (AISenseAffiliationFilter):  [Read-Write]
- ``max_age`` (float):  [Read-Write] specifies age limit after stimuli generated by this sense become forgotten. 0 means "never"
- ``starts_enabled`` (bool):  [Read-Write] determines whether given sense starts in an enabled state

<a id="unreal.AISenseConfig_Touch.detection_by_affiliation"></a>

#### detection_by_affiliation

```python
@property
def detection_by_affiliation() -> AISenseAffiliationFilter
```

(AISenseAffiliationFilter):  [Read-Only]

<a id="unreal.AISenseEvent"></a>