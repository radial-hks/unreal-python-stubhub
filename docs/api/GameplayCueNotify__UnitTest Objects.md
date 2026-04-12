## GameplayCueNotify\_UnitTest Objects

```python
class GameplayCueNotify_UnitTest(GameplayCueNotify_Static)
```

Helper GameplayCueNotify that is used for unit testing.  Note: Since this is a GCN_Static, we're using the CDO during testing

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueTests.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gameplay_cue_tag`` (GameplayTag):  [Read-Write] Tag this notify is activated by
- ``is_override`` (bool):  [Read-Write] Does this Cue override other cues, or is it called in addition to them? E.g., If this is Damage.Physical.Slash, we wont call Damage.Physical afer we run this cue.

<a id="unreal.GameplayEffectComponent"></a>