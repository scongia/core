"""Tests for the SwitchBee Smart Home integration."""

MOCK_GET_CONFIGURATION = {
    "status": "OK",
    "data": {
        "mac": "A8-21-08-E7-67-B6",
        "name": "Residence",
        "version": "1.4.4(4)",
        "lastConfChange": 1661856874511,
        "zones": [
            {
                "name": "Sensor Setting",
                "items": [
                    {
                        "id": 200000,
                        "name": "home",
                        "hw": "VIRTUAL",
                        "type": "ALARM_SYSTEM",
                    },
                    {
                        "id": 200010,
                        "name": "away",
                        "hw": "VIRTUAL",
                        "type": "ALARM_SYSTEM",
                    },
                ],
            },
            {
                "name": "General",
                "items": [
                    {
                        "operations": [113],
                        "id": 100080,
                        "name": "All Lights",
                        "hw": "VIRTUAL",
                        "type": "GROUP_SWITCH",
                    },
                    {
                        "operations": [
                            {"itemId": 21, "value": 100},
                            {"itemId": 333, "value": 100},
                        ],
                        "id": 100160,
                        "name": "Sunrise",
                        "hw": "VIRTUAL",
                        "type": "SCENARIO",
                    },
                ],
            },
            {
                "name": "Entrance",
                "items": [
                    {
                        "id": 113,
                        "name": "Staircase Lights",
                        "hw": "DIMMABLE_SWITCH",
                        "type": "TIMED_SWITCH",
                    },
                    {
                        "id": 222,
                        "name": "Front Door",
                        "hw": "REGULAR_SWITCH",
                        "type": "TIMED_SWITCH",
                    },
                ],
            },
            {
                "name": "Kitchen",
                "items": [
                    {"id": 21, "name": "Shutter ", "hw": "SHUTTER", "type": "SHUTTER"},
                    {
                        "operations": [593, 581, 171],
                        "id": 481,
                        "name": "Leds",
                        "hw": "DIMMABLE_SWITCH",
                        "type": "GROUP_SWITCH",
                    },
                    {
                        "id": 12,
                        "name": "Walls",
                        "hw": "DIMMABLE_SWITCH",
                        "type": "DIMMER",
                    },
                ],
            },
            {
                "name": "Two Way Zone",
                "items": [
                    {
                        "operations": [113],
                        "id": 72,
                        "name": "Staircase Lights",
                        "hw": "DIMMABLE_SWITCH",
                        "type": "TWO_WAY",
                    }
                ],
            },
            {
                "name": "Facilities ",
                "items": [
                    {
                        "id": 321,
                        "name": "Boiler",
                        "hw": "TIMED_POWER_SWITCH",
                        "type": "TIMED_POWER",
                    },
                    {
                        "modes": ["COOL", "HEAT", "FAN"],
                        "temperatureUnits": "CELSIUS",
                        "id": 271,
                        "name": "HVAC",
                        "hw": "THERMOSTAT",
                        "type": "THERMOSTAT",
                    },
                    {
                        "id": 571,
                        "name": "Repeater",
                        "hw": "REPEATER",
                        "type": "REPEATER",
                    },
                ],
            },
            {
                "name": "Alarm",
                "items": [
                    {
                        "operations": [{"itemId": 113, "value": 100}],
                        "id": 81,
                        "name": "Open Home",
                        "hw": "STIKER_SWITCH",
                        "type": "SCENARIO",
                    }
                ],
            },
        ],
    },
}
MOCK_FAILED_TO_LOGIN_MSG = (
    "Central Unit replied with failure: {'status': 'LOGIN_FAILED'}"
)
MOCK_INVALID_TOKEN_MGS = "Error fetching switchbee data: Error communicating with API: data Request failed due to INVALID_TOKEN, trying to re-login"
