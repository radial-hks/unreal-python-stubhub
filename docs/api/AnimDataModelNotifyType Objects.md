## AnimDataModelNotifyType Objects

```python
class AnimDataModelNotifyType(EnumBase)
```

EAnim Data Model Notify Type

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataNotifications.h

<a id="unreal.AnimDataModelNotifyType.BRACKET_OPENED"></a>

#### BRACKET_OPENED

0: Indicates a bracket has been opened. Type of payload: FBracketPayload

<a id="unreal.AnimDataModelNotifyType.BRACKET_CLOSED"></a>

#### BRACKET_CLOSED

1: Indicates a bracket has been closed. Type of payload: FEmptyPayload

<a id="unreal.AnimDataModelNotifyType.TRACK_ADDED"></a>

#### TRACK_ADDED

2: Indicates a new bone track has been added. Type of payload: FAnimationTrackAddedPayload

<a id="unreal.AnimDataModelNotifyType.TRACK_CHANGED"></a>

#### TRACK_CHANGED

3: Indicates the keys of a bone track have been changed. Type of payload: FAnimationTrackChangedPayload

<a id="unreal.AnimDataModelNotifyType.TRACK_REMOVED"></a>

#### TRACK_REMOVED

4: Indicates a bone track has been removed. Type of payload: FAnimationTrackRemovedPayload

<a id="unreal.AnimDataModelNotifyType.SEQUENCE_LENGTH_CHANGED"></a>

#### SEQUENCE_LENGTH_CHANGED

5: Indicates the play length of the animated data has changed. Type of payload: FSequenceLengthChangedPayload

<a id="unreal.AnimDataModelNotifyType.FRAME_RATE_CHANGED"></a>

#### FRAME_RATE_CHANGED

6: Indicates the sampling rate of the animated data has changed. Type of payload: FFrameRateChangedPayload

<a id="unreal.AnimDataModelNotifyType.CURVE_ADDED"></a>

#### CURVE_ADDED

7: Indicates a new curve has been added. Type of payload: FCurveAddedPayload

<a id="unreal.AnimDataModelNotifyType.CURVE_CHANGED"></a>

#### CURVE_CHANGED

8: Indicates a curve its data has been changed. Type of payload: FCurveChangedPayload

<a id="unreal.AnimDataModelNotifyType.CURVE_REMOVED"></a>

#### CURVE_REMOVED

9: Indicates a curve has been removed. Type of payload: FCurveRemovedPayload

<a id="unreal.AnimDataModelNotifyType.CURVE_FLAGS_CHANGED"></a>

#### CURVE_FLAGS_CHANGED

10: Indicates a curve its flags have changed. Type of payload: FCurveFlagsChangedPayload

<a id="unreal.AnimDataModelNotifyType.CURVE_RENAMED"></a>

#### CURVE_RENAMED

11: Indicates a curve has been renamed. Type of payload: FCurveRenamedPayload

<a id="unreal.AnimDataModelNotifyType.CURVE_SCALED"></a>

#### CURVE_SCALED

12: Indicates a curve has been scaled. Type of payload: FCurveScaledPayload

<a id="unreal.AnimDataModelNotifyType.CURVE_COLOR_CHANGED"></a>

#### CURVE_COLOR_CHANGED

13: Indicates a curve its color has changed. Type of payload: FCurveChangedPayload

<a id="unreal.AnimDataModelNotifyType.CURVE_COMMENT_CHANGED"></a>

#### CURVE_COMMENT_CHANGED

14: Indicates a curve has been removed. Type of payload: FCurveChangedPayload

<a id="unreal.AnimDataModelNotifyType.ATTRIBUTE_ADDED"></a>

#### ATTRIBUTE_ADDED

15: Indicates a new attribute has been added. Type of payload: FAttributeAddedPayload

<a id="unreal.AnimDataModelNotifyType.ATTRIBUTE_REMOVED"></a>

#### ATTRIBUTE_REMOVED

16: Indicates a new attribute has been removed. Type of payload: FAttributeRemovedPayload

<a id="unreal.AnimDataModelNotifyType.ATTRIBUTE_CHANGED"></a>

#### ATTRIBUTE_CHANGED

17: Indicates an attribute has been changed. Type of payload: FAttributeChangedPayload

<a id="unreal.AnimDataModelNotifyType.POPULATED"></a>

#### POPULATED

18: Indicates the data model has been populated from the source UAnimSequence. Type of payload: FEmptyPayload

<a id="unreal.AnimDataModelNotifyType.RESET"></a>

#### RESET

19: Indicates all data stored on the model has been reset. Type of payload: FEmptyPayload

<a id="unreal.AnimDataModelNotifyType.SKELETON_CHANGED"></a>

#### SKELETON_CHANGED

20: Indicates that the skeleton changed. Type of payload: FEmptyPayload

<a id="unreal.AnimDataModelNotifyType.INVALID"></a>

#### INVALID

21

<a id="unreal.TouchIndex"></a>