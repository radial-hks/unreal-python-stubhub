## XRSpaceType Objects

```python
class XRSpaceType(EnumBase)
```

Used to get unreal world space or tracking space positions in XR.
Working only with unreal world space coordinates is almost always simpler and should be generally preferred.
There are specific cases where raw XRTrackingSpace coordinates may be useful, particularly in apps where world scale is not 1:1 or where it changes.

**C++ Source:**

- **Module**: HeadMountedDisplay
- **File**: HeadMountedDisplayTypes.h

<a id="unreal.XRSpaceType.UNREAL_WORLD_SPACE"></a>

#### UNREAL_WORLD_SPACE

0: The unreal coordinate system.  Affected by world scaling and the TrackingToWorldTransform.

<a id="unreal.XRSpaceType.XR_TRACKING_SPACE"></a>

#### XR_TRACKING_SPACE

1: The coordinate system the XR Device is tracking itself in.  Should be fixed relative to the real world over short timescales, not affected by world scaling or the TrackingToWorldTransoform.  May change relationship to the physical world through recentering or similar events.

<a id="unreal.XRControllerPoseType"></a>