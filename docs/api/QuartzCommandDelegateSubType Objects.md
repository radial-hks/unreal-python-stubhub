## QuartzCommandDelegateSubType Objects

```python
class QuartzCommandDelegateSubType(EnumBase)
```

An enumeration for specifying different TYPES of delegates

**C++ Source:**

- **Module**: Engine
- **File**: QuartzQuantizationUtilities.h

<a id="unreal.QuartzCommandDelegateSubType.COMMAND_ON_FAILED_TO_QUEUE"></a>

#### COMMAND_ON_FAILED_TO_QUEUE

0: The command will not execute (i.e. Clock doesn't exist or PlayQuantized failed concurrency)

<a id="unreal.QuartzCommandDelegateSubType.COMMAND_ON_QUEUED"></a>

#### COMMAND_ON_QUEUED

1: The command has been passed to the Audio Render Thread

<a id="unreal.QuartzCommandDelegateSubType.COMMAND_ON_CANCELED"></a>

#### COMMAND_ON_CANCELED

2: The command was stopped before it could execute

<a id="unreal.QuartzCommandDelegateSubType.COMMAND_ON_ABOUT_TO_START"></a>

#### COMMAND_ON_ABOUT_TO_START

3: execute off this to be in sync w/ sound starting

<a id="unreal.QuartzCommandDelegateSubType.COMMAND_ON_STARTED"></a>

#### COMMAND_ON_STARTED

4: the command was just executed on the Audio Render Thrtead

<a id="unreal.QuartzCommandQuantization"></a>