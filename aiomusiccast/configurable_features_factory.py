from . import MusicCastDevice
from .configurables import *
from .features import *


def build_zone_features(musiccast_device: MusicCastDevice, zone_id):
    confs = []
    zone_features = musiccast_device.data.zones[zone_id].features
    zone_data = musiccast_device.data.zones[zone_id]

    if ZoneFeature.SLEEP & zone_features:
        confs.append(
            OptionSetter(
                "sleep",
                "Sleep Timer",
                EntityTypes.REGULAR,
                lambda: zone_data.sleep_time,
                lambda val: musiccast_device.set_sleep_timer(zone_id, val),
                {
                    0: "off",
                    30: "30 min",
                    60: "60 min",
                    90: "90 min",
                    120: "120 min"
                }
            )
        )

    return confs
