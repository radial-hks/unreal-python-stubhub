## AudioParameterType Objects

```python
class AudioParameterType(EnumBase)
```

EAudio Parameter Type

**C++ Source:**

- **Module**: AudioExtensions
- **File**: AudioParameter.h

<a id="unreal.AudioParameterType.NONE"></a>

#### NONE

0: 'Default' results in behavior that is resolved
based on the system interpreting it.  To support
legacy implementation, SoundCues cache all typed values
associated with a given parameter name.
For MetaSounds, use a specific Type instead of this one.

<a id="unreal.AudioParameterType.BOOLEAN"></a>

#### BOOLEAN

1: Boolean value

<a id="unreal.AudioParameterType.INTEGER"></a>

#### INTEGER

2: Integer value

<a id="unreal.AudioParameterType.FLOAT"></a>

#### FLOAT

3: Float value

<a id="unreal.AudioParameterType.STRING"></a>

#### STRING

4: String value (not supported by legacy SoundCue system)

<a id="unreal.AudioParameterType.OBJECT"></a>

#### OBJECT

5: Object value (types other than SoundWave not supported by legacy SoundCue system)

<a id="unreal.AudioParameterType.BOOLEAN_ARRAY"></a>

#### BOOLEAN_ARRAY

7: Array of boolean values (not supported by legacy SoundCue system)

<a id="unreal.AudioParameterType.INTEGER_ARRAY"></a>

#### INTEGER_ARRAY

8: Array of integer values (not supported by legacy SoundCue system)

<a id="unreal.AudioParameterType.FLOAT_ARRAY"></a>

#### FLOAT_ARRAY

9: Array of float values (not supported by legacy SoundCue system)

<a id="unreal.AudioParameterType.STRING_ARRAY"></a>

#### STRING_ARRAY

10: Array of string values (not supported by legacy SoundCue system)

<a id="unreal.AudioParameterType.OBJECT_ARRAY"></a>

#### OBJECT_ARRAY

11: Array of object values (not supported by legacy SoundCue system)

<a id="unreal.AudioParameterType.TRIGGER"></a>

#### TRIGGER

12: Trigger value

<a id="unreal.LiveLinkCameraProjectionMode"></a>