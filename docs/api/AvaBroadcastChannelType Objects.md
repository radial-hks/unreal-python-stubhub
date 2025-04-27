## AvaBroadcastChannelType Objects

```python
class AvaBroadcastChannelType(EnumBase)
```

The channel type defines what it is used for in the broadcast framework.

Primarily, the channel type is intended to resolve channel collisions between
simultaneous "program" and "preview" playbacks on a given system. In other words:
- Channel selection for rundown pages is restricted to "program" channels.
- Channel selection for preview is restricted to "preview" channels.

It is thus not possible for a user to mistakenly select the same channel for both preview and program.

Some additional restrictions are applied according to channel type:
- preview channels must only have outputs local to the process. "Remote" previews are not supported.
- [backend] playback request type (program or preview) must match with the channel type. This is a safety
     net for any other extended code paths that are not in the Motion Design plugin.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaMediaDefines.h

<a id="unreal.AvaBroadcastChannelType.PROGRAM"></a>

#### PROGRAM

0

<a id="unreal.AvaBroadcastChannelType.PREVIEW"></a>

#### PREVIEW

1

<a id="unreal.AvaBroadcastChannelState"></a>