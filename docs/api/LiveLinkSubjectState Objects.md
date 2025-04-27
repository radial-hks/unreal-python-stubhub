## LiveLinkSubjectState Objects

```python
class LiveLinkSubjectState(EnumBase)
```

Describes the state of a live link subject

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: ILiveLinkClient.h

<a id="unreal.LiveLinkSubjectState.CONNECTED"></a>

#### CONNECTED

0: The input is connected.

<a id="unreal.LiveLinkSubjectState.UNRESPONSIVE"></a>

#### UNRESPONSIVE

1: The input is connected but no data is available.

<a id="unreal.LiveLinkSubjectState.DISCONNECTED"></a>

#### DISCONNECTED

2: The input is not connected.

<a id="unreal.LiveLinkSubjectState.INVALID_OR_DISABLED"></a>

#### INVALID_OR_DISABLED

3: The subject is invalid or disabled

<a id="unreal.LiveLinkSubjectState.UNKNOWN"></a>

#### UNKNOWN

4: The state of the subject is unknown. e.g. It cannot be queried

<a id="unreal.LiveLinkTimecodeProviderEvaluationType"></a>