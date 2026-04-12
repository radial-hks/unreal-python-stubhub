## QuarztQuantizationReference Objects

```python
class QuarztQuantizationReference(EnumBase)
```

An enumeration for specifying quantization boundary reference frame
display name to hide c++ typo for now

**C++ Source:**

- **Module**: Engine
- **File**: QuartzQuantizationUtilities.h

<a id="unreal.QuarztQuantizationReference.BAR_RELATIVE"></a>

#### BAR\_RELATIVE

0: Will occur on the next occurence of this duration from the start of a bar (i.e. On beat 3)

<a id="unreal.QuarztQuantizationReference.TRANSPORT_RELATIVE"></a>

#### TRANSPORT\_RELATIVE

1: Will occur on the next multiple of this duration since the clock started ticking (i.e. on the next 4 bar boundary)

<a id="unreal.QuarztQuantizationReference.CURRENT_TIME_RELATIVE"></a>

#### CURRENT\_TIME\_RELATIVE

2: Will occur on the next multiple of this duration from the current time (i.e. In three beats)

<a id="unreal.QuartzCommandType"></a>